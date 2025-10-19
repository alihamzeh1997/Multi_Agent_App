```markdown
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

## Installation

### Prerequisites
- Python 3.8+
- pip

### Setup

1. **Clone the repository**:
```bash
git clone https://github.com/YOUR_USERNAME/Multi_Agent_App.git
cd Multi_Agent_App
```

2. **Create virtual environment**:
```bash
python3 -m venv .venv
source .venv/bin/activate  # On Windows: .venv\Scripts\activate
```

3. **Install dependencies**:
```bash
python3 -m pip install -r requirements.txt
```

## Usage

1. **Run the app**:
```bash
streamlit run app.py
```

2. **Access in browser**:
```
http://localhost:8501
```

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

## Configuration

### Environment Setup
Create a `.env` file (optional):
```
OPENROUTER_API_KEY=your_api_key_here
```

### Recommended Models (OpenRouter)

**Suggested models for group chat:**
- `meta-llama/llama-2-70b-chat`
- `openrouter/gpt-3.5-turbo`
- `mistralai/mistral-large`
- `openai/gpt-4-turbo`

**Avoid:**
- Models without system message support (e.g., `gemma-3n-e2b-it`)

## Project Structure

```
Multi_Agent_App/
├── app.py                 # Main Streamlit application
├── requirements.txt       # Python dependencies
├── README.md             # This file
└── .venv/                # Virtual environment
```

## Dependencies

- **streamlit**: Web framework for the UI
- **pandas**: Data handling and CSV operations
- **pyautogen**: Multi-agent conversation framework
- **openai**: LLM API integration
- **requests**: HTTP requests

See `requirements.txt` for specific versions.

## Troubleshooting

### Error: `ModuleNotFoundError: No module named 'autogen'`
```bash
python3 -m pip install pyautogen
```

### Error: `API Error 400 - Developer instruction not enabled`
Use a different model that supports system messages. Avoid provider-specific models that don't support system prompts.

### Error: `command not found: streamlit`
Use Python module execution:
```bash
python3 -m streamlit run app.py
```

### Slow responses
- Reduce `Max Rounds` value
- Use faster models
- Check OpenRouter API rate limits

## Deployment

### Deploy to Streamlit Cloud

1. Push code to GitHub
2. Go to [share.streamlit.io](https://share.streamlit.io)
3. Sign in with GitHub
4. Click "New app"
5. Select your repository and `app.py`
6. Add secrets in Streamlit settings:
   - Name: `API_KEY`
   - Value: Your OpenRouter API key
7. Deploy!

### Deploy to other platforms

- **Heroku**: Use `Procfile` with `streamlit run app.py`
- **Docker**: Create Dockerfile with dependencies
- **AWS**: Use EC2 or ECS with Streamlit

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

## Future Enhancements

- [ ] Code execution support
- [ ] Web search integration
- [ ] Conversation history persistence
- [ ] Advanced agent personality templates
- [ ] Real-time visualization
- [ ] Multi-language support

## Contributing

Contributions welcome! Please:
1. Fork the repository
2. Create a feature branch
3. Commit changes
4. Push to branch
5. Create Pull Request

## License

MIT License - see LICENSE file for details

## Support

For issues or questions:
- Open a GitHub issue
- Check existing documentation
- Review troubleshooting section

## Author

Created with ❤️ for AI enthusiasts

## Acknowledgments

- [AutoGen](https://microsoft.github.io/autogen/) by Microsoft
- [Streamlit](https://streamlit.io/) framework
- [OpenRouter](https://openrouter.ai/) API
```