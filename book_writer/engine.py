"""Book Writer — LangGraph Engine.

Pipeline multiagente para escrita de capitulos do livro "AI Product Management".

Arquitetura:
  Researcher → Strategist → Writer → CopyEditor → EditorChefe
                                                   ↑_________|
                                                   REVISE loop

Uso:
  python -m book_writer.run --chapter 7
  python -m book_writer.run --chapter 7 --max-revisions 2
"""

from __future__ import annotations

import operator
from typing import Annotated, Literal

from langgraph.graph import END, START, StateGraph
from langgraph.checkpoint.memory import MemorySaver

from book_writer.agents import (
    node_researcher,
    node_strategist,
    node_writer,
    node_copy_editor,
    node_editor_chefe,
)
from book_writer.knowledge_base import get_chapter_info


def route_after_editor(state: dict) -> Literal["end", "write"]:
    """Decide proximo passo apos EditorChefe."""
    decision = state.get("editor_decision", "APPROVE")
    revision_count = state.get("revision_count", 0)
    max_revisions = state.get("max_revisions", 3)

    if decision in ("APPROVE", "MINOR") or revision_count >= max_revisions:
        return "end"
    else:
        return "write"


def build_graph() -> StateGraph:
    """Constroi o StateGraph do pipeline de escrita.

    Pipeline: research → strategy → write → copyedit → editor → [end|write]
    """
    workflow = StateGraph(dict)

    workflow.add_node("research", node_researcher)
    workflow.add_node("strategy", node_strategist)
    workflow.add_node("write", node_writer)
    workflow.add_node("copyedit", node_copy_editor)
    workflow.add_node("editor", node_editor_chefe)

    workflow.add_edge(START, "research")
    workflow.add_edge("research", "strategy")
    workflow.add_edge("strategy", "write")
    workflow.add_edge("write", "copyedit")
    workflow.add_edge("copyedit", "editor")

    workflow.add_conditional_edges(
        "editor",
        route_after_editor,
        {"end": END, "write": "write"},
    )

    return workflow


def run_pipeline(
    chapter_num: int = 7,
    max_revisions: int = 3,
    verbose: bool = True,
) -> dict:
    """Executa o pipeline completo para um capitulo.

    Args:
        chapter_num: Numero do capitulo (1-12)
        max_revisions: Maximo de ciclos REVISE antes de forcar APPROVE
        verbose: Se True, imprime progresso

    Returns:
        Estado final do grafo com chapter_draft, draft_path, etc.
    """
    info = get_chapter_info(chapter_num)

    if verbose:
        print(f"\n{'='*60}")
        print(f"  BOOK WRITER — AI Product Management")
        print(f"  Capitulo {chapter_num}: {info.get('chapter_title', '')}")
        print(f"  Parte {info.get('part', '')}: {info.get('part_title', '')}")
        print(f"  Max revisoes: {max_revisions}")
        print(f"{'='*60}\n")

    workflow = build_graph()
    graph = workflow.compile(checkpointer=MemorySaver())

    initial_state = {
        "target_chapter": chapter_num,
        "research_material": "",
        "chapter_outline": "",
        "chapter_draft": "",
        "draft_path": "",
        "copy_editor_report": "",
        "editor_decision": "",
        "editor_feedback": "",
        "revision_count": 0,
        "max_revisions": max_revisions,
        "messages": [],
    }

    config = {"configurable": {"thread_id": f"book-chapter-{chapter_num}"}}
    final_state = graph.invoke(initial_state, config)

    if verbose:
        decision = final_state.get("editor_decision", "?")
        path = final_state.get("draft_path", "?")
        revs = final_state.get("revision_count", 0)
        print(f"\n{'='*60}")
        print(f"  PIPELINE CONCLUIDO")
        print(f"  Decisao: {decision}")
        print(f"  Revisoes: {revs}")
        print(f"  Arquivo: {path}")
        print(f"{'='*60}\n")

    return final_state


if __name__ == "__main__":
    import sys
    chapter = int(sys.argv[1]) if len(sys.argv) > 1 else 7
    run_pipeline(chapter_num=chapter)
