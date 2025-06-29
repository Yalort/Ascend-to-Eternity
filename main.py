from core.simulation import Simulation


def main() -> None:
    sim = Simulation(days=10, real_time=False)
    sim.run()


if __name__ == "__main__":
    main()
