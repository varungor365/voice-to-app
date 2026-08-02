import json
from unittest.mock import MagicMock, patch

from voice2app.generator import generate_app_structure


@patch("voice2app.generator.litellm.completion")
def test_generate_app_structure(mock_completion):
    mock_resp = MagicMock()
    mock_resp.choices = [MagicMock()]
    mock_resp.choices[0].message.content = json.dumps({
        "description": "A simple hello world",
        "filename": "index.html",
        "code": "<h1>Hello</h1>"
    })
    mock_completion.return_value = mock_resp
    
    transcript = "uh yeah make a simple hello world website"
    desc, files = generate_app_structure(transcript)
    
    assert desc == "A simple hello world"
    assert "index.html" in files
    assert files["index.html"] == "<h1>Hello</h1>"
