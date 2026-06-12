"""Strategist Agent — Planeja a estrutura do capitulo.

Responsavel por:
- Definir arco narrativo do capitulo
- Selecionar frameworks autorais a usar
- Estruturar secoes e subsecoes
- Garantir que gaps do Curiosity Registry sao plantados/resolvidos
- Definir tom e abordagem para o Writer

NAO escreve o capitulo. Define o blueprint.
"""

from dataclasses import dataclass, field
from book_writer.knowledge_base import FRAMEWORKS, BOOK_OUTLINE
from book_writer.curiosity_registry import get_gaps_planted_in, get_gaps_to_resolve, get_outstanding_gaps


@dataclass
class ChapterBlueprint:
    """Blueprint estrutural de um capitulo."""
    chapter: int
    title: str
    opening_scene: str          # descricao da cena de abertura
    frameworks: list[str]       # frameworks autorais a usar
    sections: list[dict]        # [{title, word_count, key_points}]
    data_points: list[str]      # dados-chave a incluir
    cases: list[str]            # cases a desenvolver
    gaps_to_plant: list[str]    # curiosity gaps a plantar
    gaps_to_resolve: list[str]  # curiosity gaps a resolver
    cross_refs: list[str]       # referencias a outros capitulos
    tone_notes: str             # notas de tom especificas


CHAPTER_TEMPLATES = {
    # Template padrao (todos os capitulos)
    "default": {
        "sections": [
            {"name": "Cena de Abertura", "words": 300, "key": "hook real com data/nome/contexto"},
            {"name": "Definicao do Problema", "words": 400, "key": "nomeia conceito, conecta com capitulos anteriores"},
            {"name": "Framework", "words": 1000, "key": "componentes numerados, exemplos reais para cada"},
            {"name": "Casos Reais", "words": 800, "key": "3 empresas, Situacao > Problema > Solucao > Resultados"},
            {"name": "Guia Pratico", "words": 500, "key": "acoes 30/60/90 dias"},
            {"name": "Metricas de Sucesso", "words": 300, "key": "KPIs Valor Usuario / Negocio / Implementacao"},
            {"name": "Fechamento com Gancho", "words": 250, "key": "resumo + ponte para proximo capitulo"},
        ],
        "total_words": 3550,
    },
}

# Frameworks por capitulo
CHAPTER_FRAMEWORKS = {
    1: ["escape", "ai_trap"],
    2: ["7_sinais"],
    3: ["10_competencias"],
    4: [],
    5: [],
    6: [],
    7: [],
    8: [],
    9: [],
    10: [],
    11: [],
    12: [],
}


def build_strategy_prompt(chapter: int, research_summary: str) -> str:
    """Constroi o prompt para o Strategist agent."""
    from book_writer.curiosity_registry import to_prompt_context
    from book_writer.knowledge_base import get_chapter_info

    info = get_chapter_info(chapter)
    frameworks = [FRAMEWORKS[f].name for f in CHAPTER_FRAMEWORKS.get(chapter, [])]
    curiosity_ctx = to_prompt_context(chapter)

    return f"""Voce e o Strategist Agent do sistema de escrita do livro "AI Product Management".

CAPITULO: {chapter} — {info.get("chapter_title", "")}
PARTE: {info.get("part", "")} — {info.get("part_title", "")}

FRAMEWORKS AUTORAIS DISPONIVEIS PARA ESTE CAPITULO: {frameworks}

RESUMO DA PESQUISA:
{research_summary[:3000]}

{curiosity_ctx}

INSTRUCOES:
1. Defina a cena de abertura: contexto real, pessoa, data. Gancho autobiografico.
2. Estruture o capitulo em 7 secoes (template default).
3. Selecione frameworks autorais a desenvolver e exemplos a usar.
4. Plante os gaps de curiosidade indicados. Resolva os que estao pendentes.
5. Inclua cross-references a outros capitulos.
6. Defina o tom: direto, antipatico com hype, voz de dentro.

Retorne um JSON com o blueprint completo do capitulo.
"""
