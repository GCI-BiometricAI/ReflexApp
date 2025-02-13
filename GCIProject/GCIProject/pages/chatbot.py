import reflex as rx
from typing import List, Dict
from GCIProject.templates import template

class ChatbotState(rx.State):
    user_input: str = ""
    chat_history: List[Dict[str, str]] = []
    error_message: str = ""

    def send_message(self):
        if self.user_input.strip() == "":
            return

        # Add user message to chat history
        self.chat_history.append({"role": "user", "content": self.user_input})

        try:
            # Use DeepSeek-V3 (me) to generate a response
            assistant_message = self.generate_response(self.user_input)

            # Add assistant's response to chat history
            self.chat_history.append({"role": "assistant", "content": assistant_message})
            self.error_message = ""  # Clear any previous error message

        except Exception as e:
            # Handle errors
            self.error_message = f"Error: {str(e)}"
            print(f"Error: {e}")

        # Clear the input field
        self.user_input = ""

    def clear_chat(self):
        """Clear the chat history."""
        self.chat_history = []
        self.error_message = ""

    def generate_response(self, user_input: str) -> str:
        """
        Use DeepSeek-V3 (me) to generate a response to the user's input.
        """
        user_input = user_input.lower()

        # Handle exercise-specific queries
        if "how" in user_input or "proper form" in user_input:
            if "squat" in user_input:
                return (
                    "For squats:\n"
                    "1. Stand with your feet shoulder-width apart.\n"
                    "2. Keep your chest up and back straight.\n"
                    "3. Lower your body by bending your knees and hips.\n"
                    "4. Go down until your thighs are parallel to the ground.\n"
                    "5. Push through your heels to return to the starting position."
                )
            elif "deadlift" in user_input:
                return (
                    "For deadlifts:\n"
                    "1. Stand with your feet hip-width apart and the barbell over your midfoot.\n"
                    "2. Bend at your hips and knees to grip the barbell.\n"
                    "3. Keep your back straight and chest up.\n"
                    "4. Lift the barbell by extending your hips and knees.\n"
                    "5. Lower the barbell back to the ground with control."
                )
            elif "push up" in user_input:
                return (
                    "For push-ups:\n"
                    "1. Start in a plank position with your hands slightly wider than shoulder-width.\n"
                    "2. Lower your body until your chest nearly touches the ground.\n"
                    "3. Keep your core tight and body straight.\n"
                    "4. Push through your hands to return to the starting position."
                )
            elif "lunges" in user_input:
                return (
                    "For lunges:\n"
                    "1. Stand upright with your feet together.\n"
                    "2. Step forward with one leg and lower your hips until both knees are bent at 90 degrees.\n"
                    "3. Keep your front knee above your ankle and your back knee just above the ground.\n"
                    "4. Push through your front heel to return to the starting position.\n"
                    "5. Repeat with the other leg."
                )
            elif "plank" in user_input:
                return (
                    "For planks:\n"
                    "1. Start in a forearm plank position with your elbows directly under your shoulders.\n"
                    "2. Keep your body in a straight line from head to heels.\n"
                    "3. Engage your core and hold the position for as long as possible."
                )
            elif "bench" in user_input:
                return (
                    "For bench press:\n"
                    "1. Lie on a flat bench with your feet flat on the ground.\n"
                    "2. Grip the barbell slightly wider than shoulder-width.\n"
                    "3. Lower the barbell to your chest while keeping your elbows at a 45-degree angle.\n"
                    "4. Press the barbell back up to the starting position."
                )
            elif "pull up" in user_input:
                return (
                    "For pull-ups:\n"
                    "1. Grab a pull-up bar with an overhand grip, hands slightly wider than shoulder-width.\n"
                    "2. Hang with your arms fully extended.\n"
                    "3. Pull yourself up until your chin is above the bar.\n"
                    "4. Lower yourself back down with control."
                )
            elif "rows" in user_input:
                return (
                    "For rows:\n"
                    "1. Stand with your feet hip-width apart and a barbell in front of you.\n"
                    "2. Bend at your hips and knees to grip the barbell.\n"
                    "3. Pull the barbell towards your torso, keeping your elbows close to your body.\n"
                    "4. Lower the barbell back to the starting position."
                )
            elif "overhead press" in user_input:
                return (
                    "For overhead press:\n"
                    "1. Stand with your feet shoulder-width apart and a barbell at shoulder height.\n"
                    "2. Grip the barbell slightly wider than shoulder-width.\n"
                    "3. Press the barbell overhead until your arms are fully extended.\n"
                    "4. Lower the barbell back to shoulder height."
                )
            elif "curls" in user_input:
                return (
                    "For dumbbell curls:\n"
                    "1. Stand with a dumbbell in each hand, palms facing forward.\n"
                    "2. Curl the dumbbells towards your shoulders while keeping your elbows close to your body.\n"
                    "3. Lower the dumbbells back to the starting position."
                )
            elif "dips" in user_input:
                return (
                    "For tricep dips:\n"
                    "1. Place your hands on parallel bars or the edge of a bench.\n"
                    "2. Lower your body by bending your elbows until your upper arms are parallel to the ground.\n"
                    "3. Push yourself back up to the starting position."
                )
            elif "leg press" in user_input:
                return (
                    "For leg press:\n"
                    "1. Sit on a leg press machine with your feet shoulder-width apart on the platform.\n"
                    "2. Push the platform away by extending your legs.\n"
                    "3. Lower the platform back to the starting position by bending your knees."
                )
            elif "calf raises" in user_input:
                return (
                    "For calf raises:\n"
                    "1. Stand with your feet hip-width apart.\n"
                    "2. Raise your heels off the ground by pushing through the balls of your feet.\n"
                    "3. Lower your heels back to the starting position."
                )
            elif "burpees" in user_input:
                return (
                    "For burpees:\n"
                    "1. Start in a standing position.\n"
                    "2. Drop into a squat position and place your hands on the ground.\n"
                    "3. Kick your feet back into a plank position.\n"
                    "4. Perform a push-up.\n"
                    "5. Jump your feet back to the squat position.\n"
                    "6. Jump into the air with your arms overhead."
                )
            elif "mountain climbers" in user_input:
                return (
                    "For mountain climbers:\n"
                    "1. Start in a plank position.\n"
                    "2. Bring one knee towards your chest.\n"
                    "3. Quickly switch legs, as if running in place.\n"
                    "4. Keep your core tight and maintain a steady pace."
                )
            elif "sit up" in user_input:
                return (
                    "For sit-ups:\n"
                    "1. Lie on your back with your knees bent and feet flat on the ground.\n"
                    "2. Place your hands behind your head.\n"
                    "3. Curl your torso towards your knees.\n"
                    "4. Lower your torso back to the starting position."
                )
            elif "russian twists" in user_input:
                return (
                    "For Russian twists:\n"
                    "1. Sit on the ground with your knees bent and feet lifted off the ground.\n"
                    "2. Lean back slightly and hold a weight or medicine ball with both hands.\n"
                    "3. Twist your torso to the right, then to the left, while keeping your core engaged."
                )
            elif "leg raises" in user_input:
                return (
                    "For leg raises:\n"
                    "1. Lie on your back with your legs straight.\n"
                    "2. Lift your legs towards the ceiling while keeping them straight.\n"
                    "3. Lower your legs back to the starting position without letting them touch the ground."
                )
            elif "bicycle" in user_input:
                return (
                    "For bicycle crunches:\n"
                    "1. Lie on your back with your hands behind your head.\n"
                    "2. Lift your legs and bend your knees at a 90-degree angle.\n"
                    "3. Bring your right elbow towards your left knee while extending your right leg.\n"
                    "4. Switch sides, bringing your left elbow towards your right knee."
                )
            elif "side planks" in user_input:
                return (
                    "For side planks:\n"
                    "1. Lie on your side with your legs stacked and your elbow directly under your shoulder.\n"
                    "2. Lift your hips off the ground, forming a straight line from head to feet.\n"
                    "3. Hold the position for as long as possible."
                )
            elif "hip thrust" in user_input:
                return (
                    "For hip thrusts:\n"
                    "1. Sit on the ground with your upper back against a bench and a barbell across your hips.\n"
                    "2. Drive through your heels to lift your hips towards the ceiling.\n"
                    "3. Lower your hips back to the starting position."
                )
            elif "kettlebell swings" in user_input:
                return (
                    "For kettlebell swings:\n"
                    "1. Stand with your feet shoulder-width apart and a kettlebell on the ground in front of you.\n"
                    "2. Hinge at your hips to grip the kettlebell with both hands.\n"
                    "3. Swing the kettlebell up to shoulder height by thrusting your hips forward.\n"
                    "4. Let the kettlebell swing back down between your legs."
                )
            elif "box jumps" in user_input:
                return (
                    "For box jumps:\n"
                    "1. Stand in front of a sturdy box or platform.\n"
                    "2. Jump onto the box, landing softly with your knees slightly bent.\n"
                    "3. Step back down to the starting position."
                )
            elif "jump rope" in user_input:
                return (
                    "For jump rope:\n"
                    "1. Hold the handles of the jump rope with your elbows close to your body.\n"
                    "2. Swing the rope over your head and jump over it as it approaches your feet.\n"
                    "3. Maintain a steady rhythm and keep your jumps low to the ground."
                )
            else:
                return "I can help with exercise instructions! Please specify the exercise (e.g., squats, deadlifts, push-ups)."

        # Handle workout plan queries
        elif "workout" in user_input:
            return "For a personalized workout plan, go to the upload section"

        # Handle general help queries
        elif "help" in user_input:
            return "I'm here to help! What do you need assistance with? You can ask about any exercise"

        # Default response
        else:
            return "I'm here to assist you. Feel free to ask about any exercsie"

def chatbot() -> rx.Component:
    return rx.vstack(
        rx.heading("AI Chatbot", size="6", align="center", style={"width": "100%"}),
        rx.box(
            rx.foreach(
                ChatbotState.chat_history,
                lambda message: rx.text(
                    f"{message['role']}: {message['content']}",
                    style={"margin": "10px", "padding": "10px", "border": "1px solid #ddd", "border-radius": "5px"},
                ),
            ),
            style={"width": "100%", "height": "400px", "overflow-y": "scroll", "border": "1px solid #ccc", "padding": "10px"},
        ),
        rx.hstack(
            rx.input(
                value=ChatbotState.user_input,
                on_change=ChatbotState.set_user_input,
                placeholder="Type your message here...",
                style={"width": "60%", "padding": "10px"},
            ),
            rx.button(
                "Send",
                on_click=ChatbotState.send_message,
                style={"width": "20%", "padding": "10px"},
            ),
            rx.button(
                "Clear Chat",
                on_click=ChatbotState.clear_chat,
                style={"width": "20%", "padding": "10px", "background-color": "red", "color": "white"},
            ),
            style={"width": "100%"},
        ),
        rx.cond(
            ChatbotState.error_message,
            rx.text(ChatbotState.error_message, color="red"),
        ),
        spacing="5",
        style={"width": "100%", "max-width": "800px", "margin": "auto"},
        align="center",
    )

# Add the route to your app
@template(route="/chatbot", title="Chatbot")
def chatbot_page() -> rx.Component:
    return chatbot()