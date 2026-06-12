"""Editor Agent — Julgamento editorial final.

Responsavel por:
- Avaliar qualidade do capitulo contra criterios editoriais
- Decidir: APPROVE, REVISE (volta para Writer), ou KILL (reinicia)
- Verificar arco narrativo e plantio de curiosity gaps
- Garantir que o capitulo entrega valor unico (nao generico)
- Validar cross-references com outros capitulos

Este agente NAO edita. Decide.
"""

from dataclasses import dataclass
from typing import Literal

EditorialDecision = Literal["APPROVE", "REVISE", "KILL"]


@dataclass
class EditorVerdict:
    """Decisao editorial sobre um capitulo."""
    decision: EditorialDecision
    score: float                # 0.0 a 10.0
    strengths: list[str]
    weaknesses: list[str]
    revision_notes: str         # se REVISE, instrucoes para o Writer
    kill_reason: str            # se KILL, por que reiniciar


QUALITY_CRITERIA = [
    ("Abertura autobiografica", "Capitulo abre com cena real com data/nome/contexto?"),
    ("Frameworks autorais", "Usa frameworks com nome proprio e componentes numerados?"),
    ("Dados verificados", "Todos os dados tem fonte e ano? Nao ha dados 2023 sem atualizacao?"),
    ("Voz autoral", "Tom direto, antipatico com hype, sem jargao de consultoria?"),
    ("Casos concretos", "3 casos reais com resultados quantitativos?"),
    ("Guia pratico", "Acoes concretas 30/60/90 dias?"),
    ("Curiosity gaps", "Plantou os gaps pendentes? Resolveu os devidos?"),
    ("Valor unico", "O capitulo diz algo que nao esta em nenhum outro livro de AI PM?"),
    ("Cross-references", "Conecta com capitulos anteriores e posteriores?"),
    ("Gancho final", "Fecha com resumo + ponte para proximo capitulo?"),
]


def build_editor_prompt(chapter: int, final_text: str, blueprint: str) -> str:
    """Constroi prompt para o Editor agent."""
    from book_writer.knowledge_base import get_chapter_info
    from book_writer.curiosity_registry import get_gaps_to_resolve, get_gaps_planted_in
    info = get_chapter_info(chapter)

    gaps_resolve = get_gaps_to_resolve(chapter)
    gaps_plant = get_gaps_planted_in(chapter)

    criteria_text = "\n".join(f"{i+1}. {name}: {desc}" for i, (name, desc) in enumerate(QUALITY_CRITERIA))

    return f"""Voce e o Editor Agent do livro "AI Product Management".

CAPITULO: {chapter} — {info.get("chapter_title", "")}
PARTE: {info.get("part", "")} — {info.get("part_title", "")}

CRITERIOS DE QUALIDADE:
{criteria_text}

GAPS A RESOLVER NESTE CAPITULO:
{chr(10).join(f"- [{g.id}] {g.question}" for g in gaps_resolve) if gaps_resolve else "Nenhum"}

GAPS A PLANTAR NESTE CAPITULO:
{chr(10).join(f"- [{g.id}] {g.question}" for g in gaps_plant) if gaps_plant else "Nenhum"}

BLUEPRINT:
{blueprint[:1000]}

TEXTO FINAL:
{final_text[:5000]}

DECISAO:
- APPROVE: capitulo pronto. Qualidade >= 8.0.
- REVISE: precisa ajustes. Forneca notas especificas para o Writer.
- KILL: refazer do zero. Problema estrutural.

Retorne JSON com: decision, score, strengths, weaknesses, revision_notes (se REVISE).
"""
