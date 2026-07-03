# FastAPI Quick Start Learning

A quick start learning project for Python FastAPI fundamentals.

## Purpose

This is a foundational project designed to quickly grasp and understand FastAPI basics so we can confidently move into the **agentic programming world** with LangChain and LanGraph.

The goal is to build solid FastAPI and Python knowledge without struggling with framework fundamentals when diving deep into:
- **LangChain** - Building applications with LLMs
- **LanGraph** - State management for agentic workflows
- **Agentic Programming** - Building intelligent agents

## What's Inside

- Basic FastAPI endpoints (`/home`, `/ping`)
- Simple POST endpoint for handling book data
- Pydantic models for request validation
- Foundation patterns for API development

## Java similarities

- Consider pyproject.toml as the pom.xml
- Consider uv lock to have all the exact dependency versions.  

## Getting Started

- Install uv basically do a python -m pip install uv
- Then do a python -m uv sync

```bash
#Set up -> use python 3.13
python -m venv .venv

#activate venv in powershell
.\.venv\Scripts\Activate.ps1 

#activate venv in cmd
.venv\Scripts\activate

#install uv
pip install uv

#check for uv 
uv --version

#sync uv with pyproject.toml and uv lock 
uv sync 

# Run the server
uvicorn main:app --reload
```

Visit `http://localhost:8000` to test the endpoints.

## Next Steps
These are yet to be improved. DB config should not be commited probably picked from .env file. 
Auto creation of tables should be enabled so people using this repo do not have the pain to create tables by themselves.


Once comfortable with FastAPI fundamentals, the next phase is integrating LangChain and LanGraph for building intelligent agentic systems.
