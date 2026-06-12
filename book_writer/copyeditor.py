"""CopyEditor Agent — Revisa gramatica, voz e consistencia.

Responsavel por:
- Corrigir gramatica e ortografia (PT-BR)
- Garantir aderencia ao Style Guide
- Verificar consistencia de terminologia
- Remover proibicoes (jargao de consultoria, adjetivos vazios)
- Aplicar correcoes do FactChecker

Este agente FAZ edicoes diretas no texto.
"""

from book_writer.style_guide import STYLE_GUIDE


def build_copyedit_prompt(chapter: int, draft: str, factcheck_report: str) -> str:
    """Constroi prompt para o CopyEditor agent."""
    from book_writer.knowledge_base import get_chapter_info
    info = get_chapter_info(chapter)

    return f"""Voce e o CopyEditor Agent do livro "AI Product Management".

CAPITULO: {chapter} — {info.get("chapter_title", "")}

STYLE GUIDE:
{STYLE_GUIDE}

RELATORIO DE FACT-CHECK:
{factcheck_report[:1500]}

TEXTO PARA REVISAR:
{draft}

INSTRUCOES:
1. Aplique TODAS as correcoes factuais do FactChecker.
2. Corrija gramatica e ortografia PT-BR.
3. Remova proibicoes: "espero que esteja bem", "nesta jornada", "importante", "interessante", "incrivel".
4. Remova jargao de consultoria: "alavancar", "sinergia", "disruptivo", "empoderar".
5. Verifique consistencia de terminologia (AI Product Manager → AI PM apos primeira mencao).
6. Garanta que aberturas de secao tem pergunta real entre aspas.
7. Numeros em formato brasileiro: "R$ 12 milhoes", "78%".
8. Zero ALL CAPS para enfase.

Retorne o texto COMPLETO e REVISADO.
NAO adicione comentarios. Retorne APENAS o texto final.
"""
