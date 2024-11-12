from UCLAHacks.templates import ThemeState, template
import reflex as rx
import json
import pandas as pd


class ScheduleState(rx.State):
    workout_plan = {}  # Initialize workout_plan without rx.Var

    @classmethod
    def load_workout_plan(cls):
        # Load JSON data into the workout_plan
        with open('../UCLAHacks/UCLAHacks/output.json', 'r') as file:
            cls.workout_plan = json.load(file)

    def update_schedule(self):
        # Load the workout plan when the state is mounted
        self.load_workout_plan()

@template(route="/Schedule", title="Schedule")
def Schedule() -> rx.Component:
    # Load the JSON file
    with open('../UCLAHacks/UCLAHacks/output.json', 'r') as file:
        workout_plan = json.load(file)

    day_components = []

    # Iterate over the dictionary
    for day, details in workout_plan.items():
        exercises = details['Exercises']
        # Create a DataFrame for the exercises
        df = pd.DataFrame(exercises)
        # Create a table for the exercises
        table = rx.data_table(
            data=df,
            pagination=True,
            search=False,
            sort=True
        )
        # Construct the title for the table (day and muscle group)
        title = f"{day}: {details['Focus']}"
        # Construct the component for this day's workout plan
        day_component = rx.vstack(
            rx.heading(title, size="5", align="center"),
            table,
            spacing="5",
            style={"width": "100%"},
            align="center",
        )
        # Append the day component to the list
        day_components.append(day_component)
        
    refresh_button = rx.button(
        "Refresh Schedule",
        on_click=ScheduleState.update_schedule,
        style={"margin": "10px"}
    )

    # Return the constructed components
    return rx.vstack(
        rx.heading("Schedule", size="6", align="center", style={"width": "100%"}),
        refresh_button,
        *day_components,
        spacing="5",
        style={"width": "100%"},
        align="center",
    )
