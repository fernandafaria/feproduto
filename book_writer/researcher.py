"""Researcher Agent — Pesquisa dados atualizados e fontes para o capitulo.

Responsavel por:
- Buscar dados 2025-2026 atualizados (substituir dados 2023)
- Integrar Product Compass insights
- Pesquisar transcripts do feproduto relevantes ao tema
- Fornecer material bruto para o Strategist

NAO escreve conteudo do livro. Apenas coleta e organiza informacao.
"""

import json
from pathlib import Path
from dataclasses import dataclass, field
from book_writer.knowledge_base import DataPoint, CaseStudy, CHAPTER_TOPICS


@dataclass
class ResearchBrief:
    """Brief de pesquisa para um capitulo."""
    chapter: int
    chapter_title: str
    topics: list[str]
    competitors_to_check: list[str] = field(default_factory=list)
    frameworks_needed: list[str] = field(default_factory=list)
    current_year_data: bool = True  # sempre buscar dados recentes


# --- Mapeamento de topicos por capitulo ---
CHAPTER_TOPICS = {
    1: ["AI Trap", "build trap analogia", "metricas tecnicas vs valor", "cases fracasso IA"],
    2: ["AI adoption 2025 2026", "investimento IA global", "regulacao IA Brasil EUA",
        "AI agents mercado", "modelos de negocio IA"],
    3: ["AI PM competencias 2025", "product management IA skills",
        "context depth PM", "agentic workflow thinking"],
    4: ["technical fluency PM 2026", "RAG vs fine-tuning PM", "AI stack product manager",
        "model evaluation PM", "LLM concepts for product managers"],
    5: ["discovery AI probabilistico", "experimentacao produtos IA",
        "AI prototyping tools 2026", "Lovable Supabase AI stack"],
    6: ["AI product metrics", "metricas produtos inteligentes",
        "guardrails metricas IA", "evaluation frameworks LLM"],
    7: ["UX IA design patterns 2026", "intelligent interface design",
        "AI explainability UX", "context depth product design",
        "Claude Design prototyping", "AI design tools 2026"],
    8: ["AI teams estrutura 2026", "AI agents teammates",
        "product operating model IA", "multi-agent systems product"],
    9: ["AI competitive advantage 2026", "defensibilidade IA",
        "product strategy canvas IA", "data moat AI"],
    10: ["AI transformation organizational", "change management IA 2026",
         "lideranca transformacao digital IA"],
    11: ["AI ethics 2026", "EU AI Act implementation", "responsible AI frameworks",
         "AI governance product"],
    12: ["future AI PM 2026 2027", "AI agents future product management",
         "PM brain OS", "product management AI predictions"],
}


def get_topics(chapter: int) -> list[str]:
    """Retorna topicos de pesquisa para o capitulo."""
    return CHAPTER_TOPICS.get(chapter, [])


def build_research_prompt(chapter: int) -> str:
    """Constroi o prompt de pesquisa para o Researcher agent."""
    chapter_info = {}
    for part_num, part_data in __import__("book_writer.knowledge_base", fromlist=["BOOK_OUTLINE"]).BOOK_OUTLINE["parts"].items():
        if chapter in part_data["chapters"]:
            chapter_info = {
                "chapter": chapter,
                "part": part_num,
                "part_title": part_data["title"],
                "chapter_title": part_data["chapters"][chapter],
            }
            break

    topics = get_topics(chapter)
    topic_list = "\n".join(f"- {t}" for t in topics)

    return f"""Voce e o Researcher Agent do sistema de escrita do livro "AI Product Management".

CAPITULO ALVO: {chapter_info.get("chapter_title", f"Capitulo {chapter}")}
PARTE: {chapter_info.get("part_title", "")}

TOPICOS DE PESQUISA:
{topic_list}

INSTRUCOES:
1. Para cada topico, encontre dados atualizados (2025-2026). Substitua dados de 2023.
2. Priorize fontes verificaveis: relatorios, surveys, artigos academicos.
3. Integre insights do Product Compass (7-Layer Framework, Product Strategy Canvas, AI Agents).
4. Busque transcripts relevantes no repositorio feproduto (Lenny's Podcast) nos paths ./transcripts/*.txt
5. Retorne JSON estruturado com: datapoints (valor, fonte, ano), cases (empresa, problema, solucao, resultados), insights_conceituais.

Formato de saida JSON obrigatorio.
"""
