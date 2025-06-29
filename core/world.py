import logging
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
        self.create_agents(num_agents)

    def create_agents(self, num_agents: int) -> None:
        for i in range(num_agents):
            agent = ExampleAgent(i, self, name=f"Agent_{i}")
            self.schedule.add(agent)
            logging.info(f"Created {agent.name}")

    def step(self) -> None:
        self.day += 1
        logging.info(f"--- Day {self.day} ---")
        self.schedule.step()
