import logging
import random
from mesa import Model
from mesa.time import RandomActivation
from agents.example_agent import ExampleAgent


class World(Model):
    """The game world holding agents and progressing time."""

    def __init__(self, env, num_agents: int = 1):
        super().__init__()
        self.env = env
        self.schedule = RandomActivation(self)
        self.day = 0
        self.next_id = 0
        self.name_pool = [
            "Aiden",
            "Zara",
            "Kai",
            "Luna",
            "Orion",
            "Nova",
        ]
        self.create_agents(num_agents)

    def create_agents(self, num_agents: int) -> None:
        for _ in range(num_agents):
            self.spawn_random_agent()

    def list_agents(self):
        return list(self.schedule.agents)

    def spawn_random_agent(self) -> ExampleAgent:
        name = random.choice(self.name_pool)
        agent = ExampleAgent(self.next_id, self, name=name)
        agent.stats["strength"] = random.randint(1, 10)
        agent.stats["endurance"] = random.randint(1, 10)
        self.schedule.add(agent)
        logging.info(f"Created {agent.name} (id {self.next_id})")
        self.next_id += 1
        return agent

    def step(self) -> None:
        self.day += 1
        logging.info(f"--- Day {self.day} ---")
        self.schedule.step()
