"""
Configuracao central do sistema multiagente.

Modelos, prompts-base, e paths consolidados aqui.
"""

import os
from pathlib import Path

# Paths
PROJECT_ROOT = Path(__file__).parent.parent
OUTPUT_DIR = PROJECT_ROOT / "output"
FEPRODUTO_TRANSCRIPTS = PROJECT_ROOT / "transcripts"
BOOK_DIR = PROJECT_ROOT / "book"

# Model
DEEPSEEK_API_KEY = os.environ.get("DEEPSEEK_API_KEY", "")
MODEL_NAME = "deepseek-chat"
BASE_URL = "https://api.deepseek.com/v1"
MAX_TOKENS_WRITER = 8192
MAX_TOKENS_DEFAULT = 4096

# Temperatures por agente
TEMPERATURES = {
    "researcher": 0.3,
    "strategist": 0.7,
    "writer": 0.8,
    "factchecker": 0.2,
    "copyeditor": 0.4,
    "editor": 0.6,
}

# Pipeline stages
STAGES = ["research", "strategy", "write", "factcheck", "copyedit", "editorial"]


def get_model(temperature: float = 0.7, max_tokens: int = MAX_TOKENS_DEFAULT):
    """Cria modelo DeepSeek via langchain-openai."""
    from langchain_openai import ChatOpenAI
    return ChatOpenAI(
        model=MODEL_NAME,
        api_key=DEEPSEEK_API_KEY,
        base_url=BASE_URL,
        temperature=temperature,
        max_tokens=max_tokens,
    )
