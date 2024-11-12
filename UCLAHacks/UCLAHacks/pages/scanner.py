
from UCLAHacks.templates import template
from UCLAHacks import styles
import reflex as rx
import json
import csv
from pathlib import Path

def button_style(selected):
    active_border_color = f"1px solid {rx.color('accent', 6)}"  # Active color
    inactive_border_color = f"1px solid {rx.color('gray', 6)}"  # Inactive (default) color

    return {
        "padding": "1em",
            "width": "100%",
            "border-radius": "5px",
            "border": rx.cond(
                selected,
                active_border_color,  # Use active color if selected
                inactive_border_color,  # Use inactive color if not selected
            ),
            "background-color": rx.cond(
                selected,
                rx.color("accent", 2),  # Active background color
                "transparent",  # Default background
            ),
            "color": rx.cond(
                selected,
                styles.accent_text_color,  # Active text color
                styles.text_color,  # Default text color
            ),
            "font-weight": "bold",
            "text-align": "center",
            "cursor": "pointer",
    }


class InputState(rx.State):
    height: str = ""
    weight: str = ""
    age: str = ""
    image: bool = False
    sex: str = ""
    description: str = ""
    goals = ""
    problems = ""
    experince = ""
    time = ""
    access = ""
    preference = ""
    is_uploaded: bool = False
    upload_text: str = "Upload"

    def update_height(self, value):
        self.height = value

    def update_weight(self, value):
        self.weight = value

    def update_age(self, value):
        self.age = value
    
    def male(self):
        self.sex = "Male"

    def female(self):
        self.sex = "Female"

    def update_image(self, file):
        self.image = file
    
    def updateDescription(self, value):
        self.description=value
    
    def updateCSV(self, value):
        self.csv = value
    
    def updateGoals(self,value):
        self.goals = value
    
    def updateProblems(self, value):
        self.problems = value
        
    def updateExperince(self, value):
        self.experince = value
    
    def updateTime(self, value):
        self.time = value
    
    def updateAccess(self, value):
        self.access = value
    
    def updatePrefrence(self, value):
        self.preference = value
    
    # @rx.event
    async def handle_upload(
        self, files: list[rx.UploadFile]
    ):
        """Handle the upload of file(s).

        Args:
            files: The uploaded files.
        """
        for file in files:
            upload_data = await file.read()
            custom_filename = f"data{Path(file.filename).suffix}"
            outfile = rx.get_upload_dir() / custom_filename

            # Save the file.
            with outfile.open("wb") as file_object:
                file_object.write(upload_data)
        self.is_uploaded = True
        self.upload_text = "Uploaded, Thank you!"
    
    def convertToJson(self):
        self.is_uploaded = False
        self.upload_text = "Upload"
        def csv_to_string(csv_file_path):
            with open(csv_file_path, 'r') as file:
                csv_reader = csv.reader(file)
                csv_string = ""
                for row in csv_reader:
                    csv_string += ','.join(row) + '\n'
            return csv_string
        
        csv_string = csv_to_string('../UCLAHacks/uploaded_files/data.csv')
        
        data = {
            "csv": csv_string,
            "description": self.description,
            "weight": self.weight,
            "height": self.height,
            "age": self.age,
            "sex": self.sex,
            "bmi": float(int(self.weight) / (pow((int(self.height) / 100),2))),
            "goals": self.goals,
            "problems": self.problems,
            "experince": self.experince,
            "time": self.time,
            "access": self.access,
            "preference": self.preference,

        }
        
        # Convert dictionary to JSON string
        json_string = json.dumps(data, indent=4)
        
        # Write JSON string to a file
        with open('../UCLAHacks/UCLAHacks/data.json', 'w') as json_file:
            json_file.write(json_string)
        


def measurements():
    text_area_style = {
        "padding": "0.5em",  # Reducing padding to make the text area less tall
        "text-align": "left",
    }
    return rx.hstack(
        rx.vstack(
            rx.hstack(
                rx.text("Workout Description : ", align="right", width="100px"),
                rx.text_area(placeholder="e.g., 100m repeats", style=text_area_style, width="200px", on_change=InputState.updateDescription),
                spacing="3"
            ),
            rx.hstack(
                rx.text("Age (years): ", align="right", width="100px"),
                rx.text_area(placeholder="e.g., 30", style=text_area_style, width="200px", on_change=InputState.update_age),
                spacing="3"
            ),
            rx.hstack(
                rx.text("Height (cm): ", align="right", width="100px"),
                rx.text_area(placeholder="e.g., 180", style=text_area_style, width="200px", on_change=InputState.update_height),
                spacing="3"
            ),
            rx.hstack(
                rx.text("Weight (kg): ", align="right", width="100px"),
                rx.text_area(placeholder="e.g., 70", style=text_area_style, width="200px", on_change=InputState.update_weight),
                spacing="3"
            ),
            rx.hstack(
                rx.text("Your Goals:", align="right", width="100px"),
                rx.text_area(placeholder="e.g., lose weight", style=text_area_style, width="200px", on_change=InputState.updateGoals),
                spacing="3"
            ),
        ),
        rx.vstack(
            rx.hstack(
                rx.text("Pain Feedback:", align="right", width="100px"),
                rx.text_area(placeholder="e.g., hamstring pain", style=text_area_style, width="200px", on_change=InputState.updateProblems),
                spacing="3"
            ),
            rx.hstack(
                rx.text("Experince:", align="right", width="100px"),
                rx.text_area(placeholder="e.g., 3 years weightlifting", style=text_area_style, width="200px", on_change=InputState.updateExperince),
                spacing="3"
            ),
            rx.hstack(
                rx.text("Time Availability (days):", align="right", width="100px"),
                rx.text_area(placeholder="e.g., 6 days free to workout", style=text_area_style, width="200px", on_change=InputState.updateTime),
                spacing="3"
            ),
            rx.hstack(
                rx.text("Equipment Access:", align="right", width="100px"),
                rx.text_area(placeholder="e.g., weights only from 15-30lbs", style=text_area_style, width="200px", on_change=InputState.updateAccess),
                spacing="3"
            ),
            rx.hstack(
                rx.text("Preferred Exercise Modalities::", align="right", width="100px"),
                rx.text_area(placeholder="e.g., cardio/weightlifting", style=text_area_style, width="200px", on_change=InputState.updatePrefrence),
                spacing="3"
            ),
        ),
    )

"""
def image_upload():
    return rx.fragment(
        rx.upload(rx.text("Upload files"), rx.icon(tag="upload")),
        rx.button(on_submit=InputState.image),
        spacing="3",
    )
"""
active_border_color = f"1px solid {rx.color('accent', 6)}"  # Active color
inactive_border_color = f"1px solid {rx.color('gray', 6)}"
color = "rgb(128, 128, 128)"

def csv_upload():
    return rx.vstack(
            rx.upload(
                rx.vstack(
                    # rx.button(
                    #     "Select File",
                    #     color=inactive_border_color,
                    #     bg="black",
                    #     border=f"1px solid {inactive_border_color}",
                    #     align="center"
                    # ),
                    rx.text(
                        "Drag and drop files here or click to select files"
                    ),
                ),
                id="upload1",
                border=f"1px dotted {color}",
                padding="5em",
            ),
            rx.hstack(
                rx.foreach(
                    rx.selected_files("upload1"), rx.text
                )
            ),
            rx.button(
                InputState.upload_text,
                on_click=InputState.handle_upload(
                    rx.upload_files(upload_id="upload1"),
                ),
                style=button_style(InputState.is_uploaded)
            ),
            padding="5em",
        )

@template(route="/scanner", title="Upload section")
def scanner() -> rx.Component:
    """The scanner page.

    Returns:
        The UI for the scanner page.
    """

    measurements_section = measurements()
    #upload_section = image_upload()
    camera_button = rx.link("Open Camera", href="/camera", style=button_style(False))
    upload_section = csv_upload()

    return rx.vstack(
        rx.heading("Welcome to the Upload Section", size="6", align="center"),
        rx.text("Please enter your information below:", align="center"),
        upload_section,
        measurements_section,
        rx.hstack(
            rx.button(" Male ", style=button_style(InputState.sex == "Male"), width = "49.5%", on_click=InputState.male),
            rx.button("Female", style=button_style(InputState.sex == "Female"), width = "49.5%", on_click=InputState.female),
            width="100%",
        ),
        rx.button(
            "Submit",
            width="100%",
            style = button_style(False),
            #color_scheme="green",
            on_click=[InputState.convertToJson, rx.window_alert(f"Saving Data: Height - {InputState.height}, Weight - {InputState.weight}, Age - {InputState.age}, Sex - {InputState.sex}"), rx.redirect("/Program")]
        )
    )

