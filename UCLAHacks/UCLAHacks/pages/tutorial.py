"""The settings page."""

from UCLAHacks.templates import ThemeState, template

import reflex as rx


@template(route="/tutorial", title="How to get your CSV")
def tutorial() -> rx.Component:
    """The settings page.

    Returns:
        The UI for the settings page.
    """
    return rx.vstack(
        rx.heading("Tutorial", size="8"),
        rx.hstack(
            rx.text("Navigate to: "),
            rx.link("Garmin Connect", href="https://connect.garmin.com/modern/home"),
        ),
        rx.video(url="/Tutorial.mp4", controls=True, width="100%", height="120%"),
    )
