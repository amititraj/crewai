

# CrewAI — Trip Planner

A lightweight trip planning Python package that helps generate itineraries and day plans.

This repository contains the trip-planner code, configuration for agents, helper tools, and a demo video showing the app in action.

**Quick links**
- **Source:** src/trip_planner/
- **Demo video:** demo/
- **Tests:** tests/

**How to use**
1. Create a Python virtualenv and install dependencies:

```bash
python -m venv .venv
.
# Windows PowerShell
.\.venv\Scripts\Activate.ps1
# or CMD
\.venv\Scripts\activate.bat
pip install -r requirements.txt
```

2. Copy the `.env.example` to `.env` and fill in values.

3. Run the application (example):

```bash
cd src/trip_planner
python main.py
```

Repository layout

- [src/trip_planner](src/trip_planner)
	- `__init__.py`: package marker.
	- `main.py`: application entry point / runner.
	- `crew.py`: core orchestration / high-level workflow (crew-level logic).
	- [classes](src/trip_planner/classes)
		- `activity.py`: Activity model and helpers.
		- `dayplan.py`: Day-level planning logic, scheduling helpers.
		- `itinerary.py`: Itinerary composition, serialization, and helpers.
	- [config](src/trip_planner/config)
		- `agents.yaml`: YAML config for agent settings and behavior.
		- `tasks.yaml`: Task definitions used by agents.
		- `settings.py`: Runtime config helpers and defaults.
	- [tools](src/trip_planner/tools)
		- `custom_tool.py`: Example custom utility used by agents or pipelines.

- [demo](demo)
	- Contains a short video demonstration showing the application in use.

- `requirements.txt` / `pyproject.toml`: dependency manifests.

What each top-level file/folder does

- `src/trip_planner/main.py`: Starts the application; loads configuration, environment, and kicks off the planning flow.
- `src/trip_planner/crew.py`: Implements the main high-level orchestration for generating a trip (combines classes, tools, configs).
- `src/trip_planner/classes/*.py`: Domain models and business logic for activities, day plans, and itineraries.
- `src/trip_planner/config/*`: Configuration files for agents and runtime settings.
- `src/trip_planner/tools/*`: Small helper utilities and custom connectors.
- `demo/`: The video demonstrates the typical user flow and output.
- `tests/`: Unit and integration tests for the project.

Environment variables (.env)

Create a `.env` in the repository root using `.env.example` as a template. 


