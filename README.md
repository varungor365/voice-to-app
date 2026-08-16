<div align="center">

# 🎙️ voice-to-app

**Stream-of-consciousness voice-to-app generator.**

[![PyPI version](https://badge.fury.io/py/voice-to-app.svg)](https://badge.fury.io/py/voice-to-app)
[![Python 3.9+](https://img.shields.io/badge/python-3.9+-blue.svg)](https://www.python.org/downloads/)
[![License: MIT](https://img.shields.io/badge/License-MIT-yellow.svg)](https://opensource.org/licenses/MIT)

<br/>

</div>

---

## ✨ Why this exists

Have a great idea for a web app while on a walk? Record a voice memo of you rambling about how it should look and work.

**voice-to-app** uses OpenAI Whisper to transcribe your raw thoughts and pipes them directly into an LLM (using `litellm`) configured to spit out a fully functional, single-file HTML/JS/CSS application.

### Features
- 🗣️ **Raw Audio to Code:** Transcribes rambling audio directly into working code.
- ⚙️ **JSON Structured Output:** Forces the LLM to output clean JSON with the code so it is saved locally immediately.
- 🌐 **Model Agnostic:** Powered by `litellm`, so you can use Claude, GPT-4, or even local models for the generation phase.

---

## Security and output safety

Voice-to-App sends audio to the configured transcription provider and sends the resulting transcript to the selected LLM provider. Keep API keys in environment variables, review generated code before running it, and avoid placing sensitive recordings or transcripts in shared directories.

Generated filenames are restricted to a single path component before writing to the requested output directory. The project is a developer-tool prototype, not an autonomous deployment system; generated applications should be treated as untrusted code until reviewed.

## 🚀 Quickstart

### Install
```bash
pip install voice-to-app
```

### Usage

Set your API key (if using a cloud provider):
```bash
export OPENAI_API_KEY="sk-..."
```

Pass your voice memo to the CLI:
```bash
voice2app my_app_idea.m4a
```

Use a specific model and save to a specific directory:
```bash
voice2app my_app_idea.m4a --model claude-3-5-sonnet-20240620 --outdir ./my_new_app
```

---

## 🤖 AI Agent Context

See [CLAUDE.md](CLAUDE.md) for contribution guidelines.

---

## 📄 License

MIT © Varun Ruhella. See [LICENSE](LICENSE) for details.

## Why star this repository

Star Voice-to-App if voice-driven prototyping, transcription-to-code workflows, or safe local generation of application prototypes is useful in your developer workflow.
