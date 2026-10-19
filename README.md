# LangChain Daily

Daily practice and learning notes for [LangChain](https://langchain.com/) and related libraries (LangGraph, LangChain Community, etc.).

## Project structure

```
langchain-daily/
├── 01_langchain_intro/          # Introductory LangChain notebooks
│   ├── 01_langchain_basics.ipynb
│   ├── 02_model_integration.ipynb
│   ├── 03_tools.ipynb
│   ├── 04_structured_output.ipynb
│   └── 05_middleware.ipynb
├── pyproject.toml               # Project metadata & dependencies (uv)
├── requirements.txt             # Pip-compatible dependency list
├── uv.lock                      # Locked dependency versions
├── .env                         # Environment variables (API keys, etc.)
└── README.md
```

## Getting started

### Prerequisites

- Python >= 3.14
- [uv](https://github.com/astral-sh/uv) (recommended)

### Install dependencies

```bash
uv sync
```

Or with pip:

```bash
pip install -r requirements.txt
```

### Environment variables

Create a `.env` file in the project root and add the API keys you need, for example:

```ini
GOOGLE_API_KEY=your-google-ai-api-key
GROQ_API_KEY=your-groq-api-key
OPENAI_API_KEY=your-openai-api-key
```

The notebooks load variables with `python-dotenv`, so `.env` is picked up automatically.

## Notebooks

Open any notebook in Jupyter:

```bash
uv run jupyter notebook 01_langchain_intro/01_langchain_basics.ipynb
```

| Notebook | Topics |
|---|---|
| `01_langchain_basics.ipynb` | LangChain version check, environment setup |
| `02_model_integration.ipynb` | Chat model integration |
| `03_tools.ipynb` | Tool calling / agent tools |
| `04_structured_output.ipynb` | Structured output / Pydantic schemas |
| `05_middleware.ipynb` | Middleware / callbacks |

## Dependencies

Key packages (see `pyproject.toml` for the full list):

- `langchain`, `langchain-community`
- `langchain-google-genai`, `langchain-groq`, `langchain-openai`, `langchain-ollama`
- `langgraph`
- `ipykernel`

## License

This project is for personal learning and practice.
