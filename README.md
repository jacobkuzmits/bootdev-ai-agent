# Boot.dev AI Agent

This is a course project from [Boot.dev](https://boot.dev) that demonstrates how to build an AI coding agent using Google's Gemini API. The agent can interact with code projects, read files, execute Python scripts, and help with coding tasks.

## What It Does

The AI agent acts as a coding assistant that can:

- **List files and directories** in a project
- **Read file contents** to understand code structure
- **Execute Python files** with optional arguments
- **Write or overwrite files** to make changes
- **Analyze and debug code** through natural language interaction

The agent is specifically configured to work with the `calculator` project in this repository, providing a sandboxed environment for the AI to operate safely.

## Features

- **Natural Language Interface**: Ask questions about your code in plain English
- **Function Calling**: Uses Google Gemini's function calling capabilities to perform file operations
- **Iterative Problem Solving**: Can make multiple function calls to solve complex problems
- **Verbose Mode**: Optional detailed output showing API usage and function call results
- **Safety Boundaries**: Restricted to operate only within the specified working directory

## Prerequisites

- Python 3.13 or higher
- Google Gemini API key
- UV package manager (recommended) or pip

## Installation

1. **Clone the repository**:

   ```bash
   git clone <your-repo-url>
   cd bootdev-ai-agent
   ```

2. **Install dependencies**:

   ```bash
   # Using UV (recommended)
   uv sync

   # Or using pip
   pip install -r requirements.txt
   ```

3. **Set up your environment**:
   Create a `.env` file in the project root:
   ```env
   GEMINI_API_KEY=your_gemini_api_key_here
   ```

## Usage

### Basic Usage

Run the AI agent with a natural language prompt:

```bash
python main.py "How do I fix the calculator?"
```

```bash
python main.py "Show me the contents of the main.py file in the calculator"
```

```bash
python main.py "Run the calculator tests and tell me if they pass"
```

### Verbose Mode

For detailed output including token usage and function call results:

```bash
python main.py "Analyze the calculator code" --verbose
```

### Example Prompts

- `"List all files in the calculator directory"`
- `"What does the calculator.py file do?"`
- `"Run the calculator with arguments 5 and 3"`
- `"Fix any bugs you find in the calculator tests"`
- `"Create a new function to multiply two numbers"`

## Project Structure

```
bootdev-ai-agent/
├── main.py              # Main entry point for the AI agent
├── call_function.py     # Function calling logic and available functions
├── prompts.py          # System prompt for the AI agent
├── config.py           # Configuration settings
├── pyproject.toml      # Project dependencies and metadata
├── .env                # Environment variables (create this)
├── functions/          # Available function implementations
│   ├── get_files_info.py    # List files and directories
│   ├── get_file_content.py  # Read file contents
│   ├── run_python_file.py   # Execute Python scripts
│   └── write_file.py        # Write/modify files
└── calculator/         # Sample project for the AI to work with
    ├── main.py
    ├── tests.py
    └── pkg/
        ├── calculator.py
        └── render.py
```

## Configuration

The agent is configured through `config.py`:

- `WORKING_DIR`: The directory the AI agent can operate in (default: `"./calculator"`)
- `MAX_ITERS`: Maximum number of iterations for complex tasks (default: 20)
- `MAX_CHARS`: Maximum characters for file content (default: 10,000)

## How It Works

1. **User Input**: You provide a natural language prompt
2. **AI Processing**: The Gemini model analyzes your request and determines what functions to call
3. **Function Execution**: The agent executes appropriate functions (read files, run code, etc.)
4. **Iterative Refinement**: The agent can make multiple function calls to gather information and solve problems
5. **Response**: You receive a natural language response with the results

## API Integration

This project uses Google's Gemini 2.0 Flash model with function calling capabilities. The agent is configured with:

- **System Prompt**: Defines the agent's role as a helpful coding assistant
- **Available Functions**: File operations and Python execution capabilities
- **Safety Constraints**: Restricted to the designated working directory

## Learning Objectives

This Boot.dev course project teaches:

- How to integrate AI models with function calling
- Building safe, sandboxed AI agents for code assistance
- Working with Google's Gemini API
- Implementing iterative AI problem-solving workflows
- Creating natural language interfaces for developer tools

## Course Context

This project is part of the Boot.dev curriculum.

## Limitations

- The agent operates only within the `calculator` directory for security
- File operations are limited to the configured working directory
- Python execution is restricted to the sandboxed environment
- API usage is subject to Google Gemini rate limits and costs

## License

This project is licensed under the terms specified in the LICENSE file.
