"""Book Writer — Sistema multiagente para escrita de livros com LangGraph.

Pipeline: Researcher → Strategist → Writer → CopyEditor → EditorChefe

Uso:
  from book_writer.engine import run_pipeline
  run_pipeline(chapter_num=7)

Ou via CLI:
  python -m book_writer.run --chapter 7

Autor: Theo (assistente da Fernanda Faria)
Livro: AI Product Management
"""

from book_writer.engine import run_pipeline, build_graph
from book_writer.knowledge_base import (
    FRAMEWORKS, DATAPOINTS, CASE_STUDIES, BOOK_OUTLINE, get_chapter_info
)
from book_writer.curiosity_registry import (
    CURIOSITY_REGISTRY, get_gaps_planted_in, get_gaps_to_resolve,
    get_outstanding_gaps, mark_resolved, escalate_gap, to_prompt_context,
)
from book_writer.style_guide import STYLE_GUIDE, CHAPTER_OPENING_EXAMPLES

__all__ = [
    "run_pipeline",
    "build_graph",
    "FRAMEWORKS",
    "DATAPOINTS",
    "CASE_STUDIES",
    "BOOK_OUTLINE",
    "get_chapter_info",
    "CURIOSITY_REGISTRY",
    "get_gaps_planted_in",
    "get_gaps_to_resolve",
    "get_outstanding_gaps",
    "mark_resolved",
    "escalate_gap",
    "to_prompt_context",
    "STYLE_GUIDE",
    "CHAPTER_OPENING_EXAMPLES",
]
