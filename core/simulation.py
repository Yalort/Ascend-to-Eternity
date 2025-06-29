import os
import logging
import simpy

from .world import World


class Simulation:
    """Main simulation controller running the world."""

    SECONDS_PER_DAY = 20

    def __init__(self, days: int | None = None, real_time: bool = True, factor: float = 1):
        self.days = days
        self._setup_logging()
        logging.info("Simulation initialized")
        if real_time:
            self.env = simpy.rt.RealtimeEnvironment(factor=factor, strict=False)
        else:
            self.env = simpy.Environment()
        self.world = World(self.env)

    def _setup_logging(self) -> None:
        os.makedirs("data", exist_ok=True)
        logging.basicConfig(
            filename=os.path.join("data", "simulation.log"),
            level=logging.INFO,
            format="%(asctime)s %(message)s",
        )

    def _day_process(self):
        while True:
            yield self.env.timeout(self.SECONDS_PER_DAY)
            self.world.step()
            if self.days is not None and self.world.day >= self.days:
                break

    def run(self):
        logging.info("Simulation running...")
        self.env.process(self._day_process())
        if self.days is not None:
            self.env.run(until=self.SECONDS_PER_DAY * self.days + 0.1)
        else:
            self.env.run()
