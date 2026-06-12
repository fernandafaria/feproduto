"""FactChecker Agent — Verifica cada claim do capitulo.

Responsavel por:
- Identificar TODAS as claims verificaveis no texto
- Checar dados numericos, fontes, anos, nomes
- Contrastar com pesquisa atualizada
- Gerar relatorio de fact-check por claim
- Forcar revisao se houver erros graves

NAO edita o texto diretamente. Gera relatorio para o CopyEditor/Editor.
"""

import re
from dataclasses import dataclass, field
from typing import Literal

VerificationStatus = Literal["verified", "unverifiable", "wrong", "outdated", "needs_update"]


@dataclass
class Claim:
    """Uma claim extraida do texto para verificacao."""
    id: str
    text: str
    claim_type: str  # "data", "framework", "case", "quote", "technical"
    verification: VerificationStatus = "unverifiable"
    source: str = ""
    correction: str = ""
    confidence: float = 0.0


def extract_claims(text: str) -> list[dict]:
    """Extrai claims verificaveis do texto.

    Procura por:
    - Numeros com contexto (% ou valores absolutos)
    - Nomes de empresas + acoes
    - Datas e anos
    - Citacoes a frameworks
    - Termos tecnicos com claims factuais
    """
    claims = []

    # Data claims: "X% dos Y" ou "N [unidade]"
    data_patterns = [
        (r"(\d{1,3}(?:\.\d)?%)\s*(?:dos|das|de)\s*(\w[^.,;]+)", "data_percent"),
        (r"(?:R\$\s*)?(\d+(?:\.\d+)?\s*(?:milhoes?|bilhoes?|mil|mi|bi))\s*(\w[^.,;]{10,80})", "data_value"),
        (r"\(([^)]+\d{4})\)", "data_source"),
    ]

    for pattern, claim_type in data_patterns:
        for match in re.finditer(pattern, text, re.IGNORECASE):
            claims.append({
                "text": match.group(0).strip(),
                "claim_type": claim_type,
                "start": match.start(),
            })

    # Framework claims: nomes proprios como ESCAPE, AI Trap, 7 Sinais
    framework_names = ["ESCAPE", "AI Trap", "7 Sinais", "10 Competencias",
                       "Product Strategy Canvas", "7-Layer", "Context Depth"]
    for fw in framework_names:
        if fw in text:
            claims.append({
                "text": fw,
                "claim_type": "framework",
                "start": text.find(fw),
            })

    # Remove duplicates
    seen = set()
    unique = []
    for c in claims:
        key = (c["text"][:50], c["start"])
        if key not in seen:
            seen.add(key)
            unique.append(c)
    return unique


def build_factcheck_prompt(chapter: int, draft: str, research: str) -> str:
    """Constroi prompt para o FactChecker agent."""
    from book_writer.knowledge_base import get_chapter_info
    info = get_chapter_info(chapter)

    # Extract claims for the agent to focus on
    extracted = extract_claims(draft)
    claims_text = "\n".join(f"- [{c['claim_type']}] {c['text'][:120]}" for c in extracted[:30])

    return f"""Voce e o FactChecker Agent do livro "AI Product Management".

CAPITULO: {chapter} — {info.get("chapter_title", "")}

SUA UNICA FUNCAO: Verificar a exatidao factual de CADA claim no texto.
Voce NAO avalia estilo, NAO sugere melhorias de escrita. So fatos.

CLAIMS EXTRAIDAS DO TEXTO:
{claims_text}

PESQUISA ATUALIZADA (referencia):
{research[:2000]}

TEXTO DO CAPITULO (primeiros 3000 caracteres):
{draft[:3000]}

INSTRUCOES:
1. Para cada claim, classifique: verified / unverifiable / wrong / outdated / needs_update
2. Se wrong: forneca a correcao exata com fonte
3. Se outdated: forneca o dado atualizado com fonte e ano
4. Se unverifiable: indique o que seria necessario para verificar
5. Priorize claims com numeros — sao as mais arriscadas

Retorne JSON com array de verdicts.
"""
