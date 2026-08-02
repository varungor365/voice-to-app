# voice-to-app - AI Agent Guidelines

## Agent Context
If a user asks you to add new features to this tool:
1. Ensure the LLM system prompt mandates JSON output and maintain `response_format={ "type": "json_object" }` in the API call.
2. The core value of this tool is the stream-of-consciousness parsing, so keep the system prompt focused on understanding rambling intent.
