from mesa import Agent
import logging


class BaseAgent(Agent):
    """Base class for all agents."""

    def __init__(self, unique_id, model, name="Agent"):
        super().__init__(unique_id, model)
        self.name = name
        self.stats = {
            "strength": 5,
            "endurance": 5,
        }
        self.inventory = {
            "food": 3,
            "water": 3,
        }
        self.behavior_stack = []
        self.days_since_wander = 0

    def log(self, message: str) -> None:
        logging.info(f"{self.name}: {message}")

    def consume_resources(self) -> None:
        """Consume daily resources."""
        self.inventory["food"] -= 1
        self.inventory["water"] -= 1
        self.log(
            f"consumes food and water. Food: {self.inventory['food']}, Water: {self.inventory['water']}"
        )

    def evaluate_needs(self) -> None:
        """Push behaviors based on needs or time."""
        self.days_since_wander += 1
        if (
            self.inventory["food"] <= 0
            or self.inventory["water"] <= 0
            or self.days_since_wander >= 3
        ):
            if self.wander not in self.behavior_stack:
                self.behavior_stack.append(self.wander)
                self.days_since_wander = 0

    def idle(self) -> None:
        self.log("is idling.")

    def wander(self) -> None:
        self.log("wanders and finds some resources.")
        self.inventory["food"] += 2
        self.inventory["water"] += 2
        self.log(
            f"now has Food: {self.inventory['food']}, Water: {self.inventory['water']}"
        )

    def step(self) -> None:
        """Perform one day of actions."""
        # Consume resources at start of day
        self.consume_resources()
        # Determine next behaviors
        self.evaluate_needs()

        if not self.behavior_stack:
            self.behavior_stack.append(self.idle)

        behavior = self.behavior_stack.pop(0)
        behavior()
