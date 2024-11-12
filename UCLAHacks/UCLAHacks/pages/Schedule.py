from UCLAHacks.templates import ThemeState, template
import reflex as rx
import json
import pandas as pd


class ScheduleState(rx.State):
    workout_plan = { "Day 1": { "Focus": "Speed and Strength Building", "Exercises": [ { "Name": "Warm-up", "Sets": 1, "Reps": "5-10 minutes", "Rest": "N/A", "Intensity": "Light jog or dynamic stretching" }, { "Name": "Interval Sprints", "Sets": 6, "Reps": "200m", "Rest": "2 minutes", "Intensity": "Fast, near maximal effort" }, { "Name": "Hamstring Curls", "Sets": 3, "Reps": "10-12", "Rest": "60 seconds", "Intensity": "Moderate weight, focus on controlled movement" }, { "Name": "Cool-down", "Sets": 1, "Reps": "5-10 minutes", "Rest": "N/A", "Intensity": "Light jog or walking" } ] }, "Day 2": { "Focus": "Strength Training", "Exercises": [ { "Name": "Warm-up", "Sets": 1, "Reps": "5-10 minutes", "Rest": "N/A", "Intensity": "Light cardio and dynamic stretches" }, { "Name": "Squats", "Sets": 3, "Reps": "8-10", "Rest": "60 seconds", "Intensity": "Heavy weight, controlled movement" }, { "Name": "Deadlifts", "Sets": 3, "Reps": "6-8", "Rest": "90 seconds", "Intensity": "Heavy weight, controlled movement" }, { "Name": "Bench Press", "Sets": 3, "Reps": "8-10", "Rest": "60 seconds", "Intensity": "Moderate weight" }, { "Name": "Pull-ups", "Sets": 3, "Reps": "As many as possible", "Rest": "60 seconds", "Intensity": "Bodyweight" }, { "Name": "Cool-down", "Sets": 1, "Reps": "5-10 minutes", "Rest": "N/A", "Intensity": "Static stretches, holding each for 30 seconds" } ] }, "Day 3": { "Focus": "Active Recovery and Core", "Exercises": [ { "Name": "Light Cardio", "Sets": 1, "Reps": "30 minutes", "Rest": "N/A", "Intensity": "Easy pace" }, { "Name": "Plank", "Sets": 3, "Reps": "30-60 seconds", "Rest": "30 seconds", "Intensity": "Focus on core engagement" }, { "Name": "Russian Twists", "Sets": 3, "Reps": "15-20", "Rest": "30 seconds", "Intensity": "Moderate weight or bodyweight" }, { "Name": "Leg Raises", "Sets": 3, "Reps": "15-20", "Rest": "30 seconds", "Intensity": "Controlled movement" }, { "Name": "Hamstring Stretches", "Sets": 3, "Reps": "30 seconds hold", "Rest": "15 seconds", "Intensity": "Gentle stretch" } ] }, "Day 4": { "Focus": "Speed and Strength Building", "Exercises": [ { "Name": "Warm-up", "Sets": 1, "Reps": "5-10 minutes", "Rest": "N/A", "Intensity": "Dynamic stretching" }, { "Name": "Hill Sprints", "Sets": 5, "Reps": "100m", "Rest": "3 minutes", "Intensity": "Fast" }, { "Name": "Lunges", "Sets": 3, "Reps": "10-12 per leg", "Rest": "60 seconds", "Intensity": "Bodyweight or light weight" }, { "Name": "Cool-down", "Sets": 1, "Reps": "5-10 minutes", "Rest": "N/A", "Intensity": "Light jog or walking" } ] }, "Day 5": { "Focus": "Strength Training", "Exercises": [ { "Name": "Warm-up", "Sets": 1, "Reps": "5-10 minutes", "Rest": "N/A", "Intensity": "Light cardio and dynamic stretches" }, { "Name": "Overhead Press", "Sets": 3, "Reps": "8-10", "Rest": "60 seconds", "Intensity": "Moderate weight" }, { "Name": "Bent-Over Rows", "Sets": 3, "Reps": "8-10", "Rest": "60 seconds", "Intensity": "Moderate weight" }, { "Name": "Push-ups", "Sets": 3, "Reps": "As many as possible", "Rest": "60 seconds", "Intensity": "Bodyweight" }, { "Name": "Cool-down", "Sets": 1, "Reps": "5-10 minutes", "Rest": "N/A", "Intensity": "Static stretches" } ] }, "Day 6": { "Focus": "Active Recovery and Flexibility", "Exercises": [ { "Name": "Yoga or Pilates", "Sets": 1, "Reps": "60 minutes", "Rest": "N/A", "Intensity": "Focus on flexibility and core strength" }, { "Name": "Hamstring Stretches", "Sets": 3, "Reps": "30 seconds hold", "Rest": "15 seconds", "Intensity": "Gentle stretch" } ] }, "Day 7": { "Focus": "Rest", "Exercises": [ { "Name": "Rest or Light Activity", "Sets": 1, "Reps": "Optional: light walk or stretching", "Rest": "N/A", "Intensity": "Very light" } ] } }  # Initialize workout_plan without rx.Var
    
    # def workout_plan_data(self) -> dict:
    #     # Load JSON data dynamically when accessed
    #     with open('../UCLAHacks/UCLAHacks/output.json', 'r') as file:
    #         return json.load(file)
        
    # def update_schedule(self):
    #     # Dummy function to simulate a state change
    #     self.workout_plan = self.workout_plan
    


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
        

    # Return the constructed components
    return rx.vstack(
        rx.heading("Schedule", size="6", align="center", style={"width": "100%"}),
        *day_components,
        spacing="5",
        style={"width": "100%"},
        align="center",
    )
