from .base import BaseAgent


class ExampleAgent(BaseAgent):
    """A simple agent demonstrating basic behaviors."""

    def __init__(self, unique_id, model, name="Wanderer"):
        super().__init__(unique_id, model, name)
