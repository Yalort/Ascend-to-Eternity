from flask import Flask, jsonify
import os
import sys

sys.path.append(os.path.abspath(os.path.join(os.path.dirname(__file__), "..")))

from core.controller import SimulationController

controller = SimulationController(real_time=True)
controller.start()

app = Flask(__name__)


def agent_to_dict(agent):
    behavior = agent.behavior_stack[0].__name__ if agent.behavior_stack else "idle"
    return {
        "id": agent.unique_id,
        "name": agent.name,
        "behavior": behavior,
        "stats": agent.stats,
    }


@app.route("/agents")
def list_agents():
    agents = [agent_to_dict(a) for a in controller.list_agents()]
    return jsonify(agents)


@app.route("/time")
def get_time():
    return jsonify({"day": controller.get_day()})


@app.post("/debug/spawn-agent")
def spawn_agent():
    agent = controller.spawn_random_agent()
    return jsonify({"message": "spawned", "id": agent.unique_id, "name": agent.name})


if __name__ == "__main__":
    app.run(debug=True, use_reloader=False)
