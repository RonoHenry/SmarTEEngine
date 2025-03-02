# SmarTEEngine
An Agentic AI post generator for Teespring marketing. Automates content creation and posting with Mistral (Ollama), Playwright, and Canva.

## Features
- Generates Teespring posts with Mistral
- Posts text to X, text + images to Instagram via browser automation
- Uses Canva for placeholder designs

## Setup
1. `pip install -r requirements.txt`
2. `playwright install`
3. Add your credentials to `config/credentials.yaml` (don’t commit!)
4. Run `python src/main.py`
