"""Curiosity Registry — Rastreia gaps de curiosidade entre capítulos.

Adaptado do controle epistêmico do Book-Agent para não-ficção:
em vez de esconder plot twists, criamos tensão intelectual com gaps
que são plantados em um capítulo e resolvidos em outro.
"""

from dataclasses import dataclass, field
from typing import Literal, Optional
import json
from pathlib import Path

GapStatus = Literal["planted", "in_flight", "resolved", "escalated"]
GapType = Literal["short", "medium", "long", "full_arc"]


@dataclass
class CuriosityGap:
    """Uma pergunta plantada em um capítulo para ser respondida depois."""
    id: str                     # e.g. "gap-why-ai-trap"
    question: str               # A pergunta plantada
    planted_in: int             # Número do capítulo onde é plantada
    resolved_in: int            # Número do capítulo onde é respondida
    gap_type: GapType           # short(1 cap), medium(2-3), long(4+), full_arc
    status: GapStatus = "planted"
    resolution: Optional[str] = None  # Como foi resolvida (preenchido após resolução)
    escalated_to: Optional[str] = None  # Se escalated, ID do novo gap


# ── Curiosity Registry para AI Product Management ──

CURIOSITY_REGISTRY: list[CuriosityGap] = [
    CuriosityGap(
        id="gap-ai-trap-root-cause",
        question="Por que tanta empresa cai na AI Trap mesmo tendo dinheiro, talento e dados?",
        planted_in=1,
        resolved_in=8,
        gap_type="medium",
        status="planted",
    ),
    CuriosityGap(
        id="gap-hype-vs-reality",
        question="Isso não é só mais um hype que vai passar? Como distinguir entre tendência passageira e transformação fundamental?",
        planted_in=0,  # Introdução
        resolved_in=12,
        gap_type="full_arc",
        status="planted",
    ),
    CuriosityGap(
        id="gap-pm-transition",
        question="Como um PM tradicional vira AI PM sem começar do zero? Quais competências realmente importam?",
        planted_in=3,
        resolved_in=4,  # Começa no 4, constrói até o 9
        gap_type="medium",
        status="planted",
    ),
    CuriosityGap(
        id="gap-model-perfect-user-hates",
        question="O que fazer quando o modelo é tecnicamente perfeito mas o usuário odeia?",
        planted_in=1,
        resolved_in=7,
        gap_type="long",
        status="planted",
    ),
    CuriosityGap(
        id="gap-competitive-moat",
        question="Como criar vantagem competitiva com IA que não pode ser copiada amanhã?",
        planted_in=2,
        resolved_in=9,
        gap_type="long",
        status="planted",
    ),
    CuriosityGap(
        id="gap-ai-replace-pm",
        question="IA vai substituir o Product Manager?",
        planted_in=3,
        resolved_in=12,
        gap_type="full_arc",
        status="planted",
    ),
    CuriosityGap(
        id="gap-discovery-non-deterministic",
        question="Como fazer discovery quando o comportamento do produto é probabilístico e não determinístico?",
        planted_in=4,
        resolved_in=5,
        gap_type="short",
        status="planted",
    ),
    CuriosityGap(
        id="gap-metrics-ai-vs-traditional",
        question="Se métricas tradicionais não funcionam para IA, o que colocar no lugar?",
        planted_in=5,
        resolved_in=6,
        gap_type="short",
        status="planted",
    ),
    CuriosityGap(
        id="gap-building-ai-teams",
        question="Como montar times de IA quando os melhores data scientists querem startups, não corporações?",
        planted_in=6,
        resolved_in=8,
        gap_type="medium",
        status="planted",
    ),
    CuriosityGap(
        id="gap-ethics-practical",
        question="Ética em IA é bonito no papel. Como implementar na prática quando o board quer resultado?",
        planted_in=8,
        resolved_in=11,
        gap_type="medium",
        status="planted",
    ),
    CuriosityGap(
        id="gap-transformation-real",
        question="Como liderar transformação de IA quando metade da empresa está resistindo e a outra metade está com medo?",
        planted_in=9,
        resolved_in=10,
        gap_type="short",
        status="planted",
    ),
]


def get_gaps_planted_in(chapter: int) -> list[CuriosityGap]:
    """Gaps que devem ser plantados neste capítulo."""
    return [g for g in CURIOSITY_REGISTRY if g.planted_in == chapter]


def get_gaps_to_resolve(chapter: int) -> list[CuriosityGap]:
    """Gaps que devem ser resolvidos neste capítulo."""
    return [g for g in CURIOSITY_REGISTRY if g.resolved_in == chapter]


def get_outstanding_gaps(up_to_chapter: int) -> list[CuriosityGap]:
    """Gaps plantados mas ainda não resolvidos até este capítulo."""
    return [
        g for g in CURIOSITY_REGISTRY
        if g.planted_in <= up_to_chapter
        and g.resolved_in > up_to_chapter
        and g.status != "resolved"
    ]


def mark_resolved(gap_id: str, resolution: str) -> None:
    """Marca um gap como resolvido."""
    for g in CURIOSITY_REGISTRY:
        if g.id == gap_id:
            g.status = "resolved"
            g.resolution = resolution
            return


def escalate_gap(gap_id: str, new_question: str, new_gap_id: str, resolve_in: int) -> CuriosityGap:
    """Uma resposta gera uma pergunta maior. Cria gap novo."""
    for g in CURIOSITY_REGISTRY:
        if g.id == gap_id:
            g.status = "escalated"
            g.escalated_to = new_gap_id
    
    new_gap = CuriosityGap(
        id=new_gap_id,
        question=new_question,
        planted_in=g.resolved_in if g else 0,
        resolved_in=resolve_in,
        gap_type="short",
        status="planted",
    )
    CURIOSITY_REGISTRY.append(new_gap)
    return new_gap


def to_prompt_context(chapter: int) -> str:
    """Gera contexto para o prompt do Writer."""
    to_plant = get_gaps_planted_in(chapter)
    to_resolve = get_gaps_to_resolve(chapter)
    outstanding = get_outstanding_gaps(chapter - 1)
    
    lines = ["## CURIOSITY REGISTRY — Gaps de tensão narrativa\n"]
    
    if to_resolve:
        lines.append("### GAPS A RESOLVER NESTE CAPÍTULO:")
        for g in to_resolve:
            lines.append(f"- [{g.id}] Plantado no Cap {g.planted_in}: \"{g.question}\"")
            lines.append(f"  → RESOLVER neste capítulo com resposta concreta. Após responder, gerar nova pergunta (escalate).")
        lines.append("")
    
    if to_plant:
        lines.append("### GAPS A PLANTAR NESTE CAPÍTULO:")
        for g in to_plant:
            lines.append(f"- [{g.id}] \"{g.question}\" → Resolver no Cap {g.resolved_in} (tipo: {g.gap_type})")
            lines.append(f"  → Plantar com tensão. O leitor deve QUERER a resposta. Não revelar ainda.")
        lines.append("")
    
    if outstanding:
        lines.append("### GAPS AINDA EM ABERTO (já plantados, ainda não resolvidos):")
        for g in outstanding:
            lines.append(f"- [{g.id}] \"{g.question}\" → Resolver no Cap {g.resolved_in}")
        lines.append("  → NÃO resolver estes gaps neste capítulo. Eles pertencem a capítulos futuros.")
        lines.append("")
    
    return "\n".join(lines)


def registry_summary() -> str:
    """Resumo do estado atual do registry."""
    total = len(CURIOSITY_REGISTRY)
    resolved = sum(1 for g in CURIOSITY_REGISTRY if g.status == "resolved")
    planted = sum(1 for g in CURIOSITY_REGISTRY if g.status == "planted")
    escalated = sum(1 for g in CURIOSITY_REGISTRY if g.status == "escalated")
    
    return (
        f"Curiosity Registry: {total} gaps | "
        f"{resolved} resolvidos | {planted} plantados | {escalated} escalados"
    )
