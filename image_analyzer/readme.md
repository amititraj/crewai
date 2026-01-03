CrewAI Image Analyzer
=====================

Welcome to the Imageanalyzer Crew project, powered by [crewAI](https://crewai.com). This template is designed to help you set up a multi-agent AI system with ease, leveraging the powerful and flexible framework provided by crewAI. Our goal is to enable your agents to collaborate effectively on complex tasks, maximizing their collective intelligence and capabilities.

Short description
-----------------
CrewAI Image Analyzer is a small Python app to analyze images and run agent-style workflows. The repository contains an application entry point, an image analyzer package, configuration, and a demo video showing the app in action.

What’s in this repo
-------------------
- **Project root**: Entrypoint and project-level files
  - [app.py](app.py) — application entry point / runner
  - [requirements.txt](requirements.txt) — Python dependencies
  - [README.md](README.md) — this file

- **Configuration**:
  - [config/settings.py](config/settings.py) — project settings loader

- **Image analyzer package**:
  - [imageanalyzer/src/imageanalyzer/__init__.py](imageanalyzer/src/imageanalyzer/__init__.py)
  - [imageanalyzer/src/imageanalyzer/crew.py](imageanalyzer/src/imageanalyzer/crew.py) — high-level orchestration of agents
  - [imageanalyzer/src/imageanalyzer/main.py](imageanalyzer/src/imageanalyzer/main.py) — module CLI / application logic
  - [imageanalyzer/src/imageanalyzer/config/agents.yaml](imageanalyzer/src/imageanalyzer/config/agents.yaml) — agents configuration
  - [imageanalyzer/src/imageanalyzer/config/tasks.yaml](imageanalyzer/src/imageanalyzer/config/tasks.yaml) — tasks config
  - [imageanalyzer/src/imageanalyzer/tools/image_tool.py](imageanalyzer/src/imageanalyzer/tools/image_tool.py) — image processing helpers
  - [imageanalyzer/src/imageanalyzer/tools/custom_tool.py](imageanalyzer/src/imageanalyzer/tools/custom_tool.py) — custom utility tools

- **Demo**:  
  - [demo/](demo/) — demo video(s) showing the application

Quick start
-----------
1. Create a Python virtual environment (recommended) and activate it.   
   python -m venv .venv
   

2. Install dependencies:   
   pip install -r requirements.txt
   

3. Create a `.env` (see below) or set environment variables, then run:
   python app.py
   

Environment (.env)
------------------
Create a `.env` file in the project root. Refer .env.example file for reference.

Note: confirm exact variable names from [config/settings.py](config/settings.py) in this repository.

Notes & next steps
------------------
- The `demo/` folder contains a short video demonstrating the app flow.
