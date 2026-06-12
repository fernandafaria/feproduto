"""Writer Agent — Escreve o capitulo seguindo Style Guide e Blueprint.

Responsavel por:
- Escrever prosa completa seguindo a voz autoral da Fernanda
- Respeitar estrutura de 7 secoes por capitulo
- Usar frameworks autorais com nome proprio
- Incluir dados com fonte e ano
- Manter tom antipatico com hype

Este e o agente que produz o texto final do capitulo.
"""

from book_writer.style_guide import STYLE_GUIDE
from book_writer.curiosity_registry import to_prompt_context
from book_writer.knowledge_base import get_chapter_info


def build_writer_prompt(chapter: int, blueprint: str, research: str) -> str:
    """Constroi o prompt para o Writer agent."""
    info = get_chapter_info(chapter)

    return f"""Voce e o Writer Agent do livro "AI Product Management" da Fernanda Faria.

Voce INCORPORA a voz da Fernanda. Voce NAO descreve o que escreveria — voce ESCREVE.

CAPITULO: {chapter} — {info.get("chapter_title", "")}

STYLE GUIDE COMPLETO:
{STYLE_GUIDE}

BLUEPRINT DO CAPITULO:
{blueprint[:3000]}

RESUMO DA PESQUISA:
{research[:2000]}

REGRAS ABSOLUTAS:
1. ABERTURA: Sempre com cena real — "Era uma [dia] de [mes] de [ano], e [Nome], [cargo]..."
2. TOM: Direto, executivo, antipatico com hype. Palavras da Fernanda, nao de consultoria.
3. FRAMEWORKS: Nome proprio, componentes numerados, exemplos reais para cada componente.
4. DADOS: Sempre com fonte e ano. Atualizar dados 2023 para 2025-2026 quando disponivel.
5. PROIBIDO: "espero que esteja bem", "nesta jornada", "importante/interessante/incrivel", jargao de consultoria.
6. ESTRUTURA: 7 secoes. Cada secao comeca com pergunta real entre aspas.
7. FECHAMENTO: Resume + ponte para proximo capitulo + planta gap de curiosidade.

Escreva o capitulo COMPLETO. Nao deixe placeholder. Nao use "[...]". Texto final, pronto para revisao.
"""
