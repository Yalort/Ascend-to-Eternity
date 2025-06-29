import threading
from typing import List

from .simulation import Simulation


class SimulationController:
    """Controller to manage the simulation instance."""

    def __init__(self, days: int | None = None, real_time: bool = False):
        self.sim = Simulation(days=days, real_time=real_time)
        self.thread: threading.Thread | None = None
        self.lock = threading.Lock()

    def start(self) -> None:
        """Start the simulation in a background thread."""
        if self.thread and self.thread.is_alive():
            return
        self.thread = threading.Thread(target=self.sim.run, daemon=True)
        self.thread.start()

    def list_agents(self):
        with self.lock:
            return self.sim.list_agents()

    def spawn_random_agent(self):
        with self.lock:
            return self.sim.spawn_random_agent()

    def get_day(self) -> int:
        return self.sim.get_day()
