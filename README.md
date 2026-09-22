# Error Explainer Bot
A command line bot that explains Python error messages in plain English using a local model through Ollama.

## Setup
You need Ollama with a model pulled .
Eg: ollama pull gemma3:1b

With uv:
    uv sync
    uv run main.py

With pip:
    python -m venv .venv
    .venv/Scripts/activate
    pip install ollama
    python main.py

## Commands
help, exit

## Sample conversation
 NameError: name 'x'is not defined.
 
