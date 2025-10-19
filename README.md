# AutoGen Multi-Agent Group Chat

A Streamlit web application that enables dynamic multi-agent conversations using AutoGen and OpenRouter API. Create custom AI agents with different personalities and system prompts, then watch them collaborate in real-time group discussions.

## Features

- **Agent Configuration**: Create and customize multiple AI agents with:
  - Custom names and descriptions
  - Personalized system messages
  - Model selection (via OpenRouter)
  - Temperature control for creativity levels

- **Group Chat Management**: 
  - Manage conversations between 2+ agents
  - Group chat with a centralized manager
  - Admin oversight via UserProxyAgent
  - Configurable conversation rounds

- **Data Export**:
  - Save agent configurations to CSV
  - Download conversation transcripts
  - Session state management

- **OpenRouter Integration**:
  - Support for multiple LLM providers
  - Easy API key management
  - Model flexibility



### Workflow

#### Step 1: Configure Agents
- Go to "Configure Agents" tab
- Enter agent details:
  - **Name**: Agent identifier
  - **Model**: OpenRouter model (e.g., `meta-llama/llama-2-70b-chat`)
  - **System Message**: Agent's personality/instructions
  - **Temperature**: Creativity level (0-2, default 0.7)
  - **Description**: Agent purpose
- Click "Add Agent"
- Edit agents in the data editor
- Download configuration as CSV

#### Step 2: Run Group Chat
- Go to "Run Group Chat" tab
- Enter:
  - **Initial Message**: Topic for discussion
  - **Max Rounds**: Number of conversation turns
- Click "Start Group Chat"
- View conversation in real-time
- Download transcript as CSV


### Recommended Models (OpenRouter)

**Suggested models for group chat:**
- `meta-llama/llama-2-70b-chat`
- `openrouter/gpt-3.5-turbo`
- `mistralai/mistral-large`
- `openai/gpt-4-turbo`

**Avoid:**
- Models without system message support (e.g., `gemma-3n-e2b-it`)


## Dependencies

- **streamlit**: Web framework for the UI
- **pandas**: Data handling and CSV operations
- **pyautogen**: Multi-agent conversation framework
- **openai**: LLM API integration
- **requests**: HTTP requests

See `requirements.txt` for specific versions.


### Slow responses
- Reduce `Max Rounds` value
- Use faster models
- Check OpenRouter API rate limits


## Example Use Cases

1. **Debate Simulation**: Two agents with opposing viewpoints
2. **Research Discussion**: Scientist and engineer collaboration
3. **Content Creation**: Creative agents generating ideas
4. **Problem Solving**: Multiple experts discussing solutions

## API Rate Limits

OpenRouter has rate limits. For production use:
- Monitor API usage
- Implement request throttling
- Consider subscription tier upgrades

## Author

Created with ❤️ for AI enthusiasts, Ask me any question via LinkedIn. https://www.linkedin.com/in/alihamzeh/

## Acknowledgments

- [AutoGen](https://microsoft.github.io/autogen/) by Microsoft
- [Streamlit](https://streamlit.io/) framework
- [OpenRouter](https://openrouter.ai/) API
```