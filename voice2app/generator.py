import openai
import litellm
import os
import json
from typing import Dict, Any, Tuple

def transcribe_audio(audio_path: str) -> str:
    """Transcribes an audio file using OpenAI Whisper API."""
    if not os.path.exists(audio_path):
        raise FileNotFoundError(f"Audio file not found: {audio_path}")
        
    client = openai.OpenAI()
    
    with open(audio_path, "rb") as audio_file:
        transcript = client.audio.transcriptions.create(
            model="whisper-1", 
            file=audio_file
        )
        
    return transcript.text

def generate_app_structure(transcript: str, model: str = "gpt-4o-mini") -> Tuple[str, Dict[str, str]]:
    """Generates application code from a stream-of-consciousness transcript."""
    
    system_prompt = """You are an expert AI Developer. 
The user is speaking in a stream-of-consciousness manner about an app they want to build.
Parse their intent and generate a working, single-file HTML/JS/CSS application (or python script if requested).

You must respond with a JSON object containing:
1. "description": A brief explanation of what you built based on their rambling.
2. "filename": The suggested filename (e.g., 'index.html' or 'app.py').
3. "code": The full, complete code for the application.
"""

    messages = [
        {"role": "system", "content": system_prompt},
        {"role": "user", "content": f"Here is the voice transcript:\n\n{transcript}"}
    ]
    
    response = litellm.completion(
        model=model,
        messages=messages,
        response_format={ "type": "json_object" }
    )
    
    try:
        content = response.choices[0].message.content
        parsed = json.loads(content)
        
        description = parsed.get("description", "Generated App")
        filename = parsed.get("filename", "app.txt")
        code = parsed.get("code", "")
        
        return description, {filename: code}
    except Exception as e:
        raise ValueError(f"Failed to parse LLM response: {e}")
