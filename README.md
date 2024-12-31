# Note Evaluation

Welcome to the NoteEval Crew project, powered by [crewAI](https://crewai.com). This template is designed to help you set up a multi-agent AI system easily, leveraging the powerful and flexible framework provided by crewAI. Our goal is to enable your agents to collaborate effectively on complex tasks, maximizing their collective intelligence and capabilities.

## Installation

Ensure you have Python >=3.10 <=3.13 installed on your system. This project uses [UV](https://docs.astral.sh/uv/) for dependency management and package handling, offering a seamless setup and execution experience.

First, if you haven't already, install uv:

```bash
pip install uv
```

Next, navigate to your project directory and install the dependencies:

(Optional) Lock the dependencies and install them by using the CLI command:
```bash
crewai install
```

### Customizing

**Add your `OPENAI_API_KEY` and other required variables into the `.env` file**

The `.env` file should contain the following environment variables:

```
OPENAI_API_KEY=your_openai_api_key_here
OTHER_API_KEY=your_other_api_key_here
MODEL_NAME=your_model_name_here
```

- `OPENAI_API_KEY`: This key is essential for enabling the AI agents to access OpenAI's services and perform their tasks effectively.
- `OTHER_API_KEY`: Replace this with any other API keys required for your specific agents or tasks.
- `MODEL_NAME`: The name of the model your agents will use for processing tasks.

- Modify `src/note_eval/config/agents.yaml` to define your agents
- Modify `src/note_eval/config/tasks.yaml` to define your tasks
- Modify `src/note_eval/crew.py` to add your own logic, tools, and specific arguments
- Modify `src/note_eval/main.py` to add custom inputs for your agents and tasks

## Running the Project

To start your crew of AI agents and begin task execution, run this from the root folder of your project:

```bash
$ crewai run
```

This command initializes the NoteEval Crew, assembling the agents and assigning them tasks as defined in your configuration.

This example, unmodified, will create `note_summary.md`, `note_comparison.md`, and `note_next_steps.md` files with the output of the tasks in the root folder.

## Understanding Your Crew

The NoteEval Crew is composed of multiple AI agents, each with unique roles, goals, and tools. These agents collaborate on a series of tasks, defined in `config/tasks.yaml`, leveraging their collective skills to achieve complex objectives. The `config/agents.yaml` file outlines the capabilities and configurations of each agent in your crew.

## Support

For support, questions, or feedback regarding the NoteEval Crew or crewAI:
- Visit our [documentation](https://docs.crewai.com)
- Reach out to us through our [GitHub repository](https://github.com/joaomdmoura/crewai)
- [Join our Discord](https://discord.com/invite/X4JWnZnxPb)
- [Chat with our docs](https://chatg.pt/DWjSBZn)

Let's create wonders together with the power and simplicity of crewAI.
