"""
Book Writer — Agents
====================
Implementação dos agentes como nós do grafo LangGraph.

Pipeline: Researcher → Strategist → Writer → CopyEditor → EditorChefe

Cada agente é uma função que recebe BookWriterState e retorna BookWriterState.
Agentes com tool access usam _invoke_with_tools para pesquisar antes de responder.
"""

from __future__ import annotations

import json
import os
import sys
from datetime import datetime
from pathlib import Path
from typing import Any

from langchain_core.messages import AIMessage, HumanMessage, SystemMessage

PROJECT_ROOT = Path(__file__).parent.parent
sys.path.insert(0, str(PROJECT_ROOT))

from book_writer.tools import ALL_TOOLS, _invoke_with_tools, _get_model
from book_writer.knowledge_base import get_chapter_info, FRAMEWORKS, BOOK_OUTLINE
from book_writer.curiosity_registry import (
    to_prompt_context, get_gaps_planted_in, get_gaps_to_resolve,
    get_outstanding_gaps, mark_resolved, escalate_gap,
)
from book_writer.style_guide import STYLE_GUIDE


# ── Data freshness anchor ──────────────────────────────────────────────────
CURRENT_YEAR = datetime.now().year
CURRENT_DATE = datetime.now().strftime("%Y-%m-%d")
FRESHNESS_CUTOFF = datetime.now().replace(year=CURRENT_YEAR - 1).strftime("%Y-%m-%d")


# ═══════════════════════════════════════════════════════════════════════════
# SYSTEM PROMPTS
# ═══════════════════════════════════════════════════════════════════════════

BOOK_SYSTEM = f"""Você é parte do sistema multiagente de escrita do livro "AI Product Management"
da autora Fernanda Faria. Ano corrente: {CURRENT_YEAR}.

Suas respostas serão usadas como parte do pipeline de produção do livro.
Seja preciso, direto e orientado à ação.

Regras:
- Sempre escreva em português do Brasil.
- NUNCA use em-dashes (—). Use vírgula, dois-pontos ou ponto.
- NUNCA use ALL CAPS para ênfase.
- Toda afirmação factual precisa de fonte verificável.
- Quando dados forem de anos anteriores a {CURRENT_YEAR}, busque os mais recentes."""


# ═══════════════════════════════════════════════════════════════════════════
# RESEARCHER
# ═══════════════════════════════════════════════════════════════════════════

def node_researcher(state: dict) -> dict:
    """Pesquisa fontes, dados, cases e Product Compass para o capítulo alvo.

    Output salvo em state['research_material'].
    """
    model = _get_model(temperature=0.3).bind_tools(ALL_TOOLS)

    chapter_num = state.get("target_chapter", 7)
    chapter_info = get_chapter_info(chapter_num)

    prompt = f"""{BOOK_SYSTEM}

## FUNÇÃO: RESEARCHER — Pesquisa de fontes para o livro

VOCÊ É O PESQUISADOR. Sua missão: coletar material bruto, verificável e ATUALIZADO
(ano {CURRENT_YEAR}, nada anterior a {FRESHNESS_CUTOFF} sem justificativa) para o capítulo:

**Capítulo {chapter_num}: {chapter_info.get('chapter_title', '')}**
**Parte {chapter_info.get('part')}: {chapter_info.get('part_title', '')}**
**Tema:** {chapter_info.get('part_epigraph', '')}

CONTEXTO DO LIVRO:
Este é o guia definitivo para Product Managers na era da IA. A Parte III foca em
construir produtos de IA — do design à estratégia.

CAPÍTULOS ANTERIORES (para contexto):
- Cap 1: A AI Trap (framework ESCAPE)
- Cap 2: O Momento de Inflexão (7 Sinais)
- Cap 3: Anatomia do AI PM (10 Competências)
- Cap 4: Technical Fluency
- Cap 5: O Novo Discovery — Experimentação em Mundo Não-Determinístico
- Cap 6: Data-Driven Decision Making 2.0

CAPÍTULOS POSTERIORES (para plantar gaps):
- Cap 8: Building AI Teams
- Cap 9: AI Product Strategy

PESQUISE USANDO AS FERRAMENTAS:

1. **Product Compass (productcompass.pm):**
   Busque artigos do Pawel Huryn sobre:
   - UX design para produtos de IA
   - Intelligent Interface Sense
   - AI-powered product design patterns
   - Context Depth como power skill
   - Non-deterministic UX

2. **Casos reais de empresas** que implementaram IA com foco em UX:
   - Empresas que erraram (ex: chatbot tecnicamente perfeito mas usuários odiaram)
   - Empresas que acertaram (ex: interface de IA que aumentou adoção drasticamente)

3. **Dados e estatísticas ATUALIZADOS ({CURRENT_YEAR}):**
   - Adoção de AI em produtos de consumo
   - Expectativas de usuários com IA
   - Taxas de abandono de produtos de IA
   - Impacto de UX em métricas de adoção de IA

4. **Frameworks de design para IA:**
   - Princípios de UX para sistemas não-determinísticos
   - Padrões de interação humano-IA
   - Métodos de teste de usabilidade para produtos de IA

5. **Referências acadêmicas e industry reports:**
   - Google PAIR (People + AI Research)
   - Apple Human Interface Guidelines for AI
   - Nielsen Norman Group sobre UX de IA
   - McKinsey/HBR sobre design de produtos de IA

6. **Cases Brasil:**
   - Empresas brasileiras implementando IA com foco em experiência
   - Produtos de IA bem-sucedidos no mercado brasileiro

Use search_web para buscar cada categoria. Extraia URLs promissoras com extract_urls.
Consulte a base de conhecimento local com read_knowledge_base('frameworks') para
entender frameworks já existentes que este capítulo referencia.

ORGANIZE SEU OUTPUT ASSIM:

## 1. PRINCIPAIS FONTES ENCONTRADAS
(tabela com fonte, URL, data, resumo do conteúdo)

## 2. DADOS QUANTITATIVOS ATUALIZADOS
(números, %, estatísticas com fonte e ano)

## 3. CASES REAIS
(3-5 cases com: empresa, problema, solução, resultados)

## 4. FRAMEWORKS DE REFERÊNCIA
(princípios e padrões de design para IA)

## 5. INSIGHTS DO PRODUCT COMPASS
(o que o Pawel Huryn diz sobre design de produtos de IA)

## 6. MATÉRIA-PRIMA PARA O CURIOSITY SCHEDULER
(que perguntas intrigantes este capítulo deveria plantar ou responder?)
"""

    research_msgs = [
        SystemMessage(content=f"{BOOK_SYSTEM}\n\nUse SEMPRE as ferramentas search_web e extract_urls para pesquisar antes de responder."),
        HumanMessage(content=prompt),
    ]

    research_result = _invoke_with_tools(model, research_msgs, max_tool_rounds=5)
    print(f"[Researcher] Pesquisa concluída ({len(research_result)} caracteres)")

    return {
        "research_material": research_result,
        "messages": [AIMessage(content=f"[Researcher] Material de pesquisa coletado para Capítulo {chapter_num}")],
    }


# ═══════════════════════════════════════════════════════════════════════════
# STRATEGIST
# ═══════════════════════════════════════════════════════════════════════════

def node_strategist(state: dict) -> dict:
    """Analisa o research, define outline detalhado e Curiosity Schedule.

    Output salvo em state['chapter_outline'] e state['curiosity_plan'].
    """
    model = _get_model(temperature=0.3)

    chapter_num = state.get("target_chapter", 7)
    research = state.get("research_material", "")
    chapter_info = get_chapter_info(chapter_num)

    # Pega contexto de curiosity
    curiosity_ctx = to_prompt_context(chapter_num)
    gaps_to_plant = get_gaps_planted_in(chapter_num)
    gaps_to_resolve = get_gaps_to_resolve(chapter_num)
    outstanding = get_outstanding_gaps(chapter_num - 1)

    prompt = f"""{BOOK_SYSTEM}

## FUNÇÃO: STRATEGIST — Estrategista de Conteúdo e Curiosity Scheduler

VOCÊ É O ESTRATEGISTA. Sua missão: transformar pesquisa bruta em um outline
detalhado com agenda de revelação (Curiosity Schedule) para o capítulo.

**Capítulo {chapter_num}: {chapter_info.get('chapter_title', '')}**
**Parte {chapter_info.get('part')}: {chapter_info.get('part_title', '')}**

MATERIAL DE PESQUISA:
---
{research[:12000]}
---

{curiosity_ctx}

CURIOSITY SCHEDULER:
- Gaps a PLANTAR neste capítulo: {len(gaps_to_plant)} gaps
- Gaps a RESOLVER neste capítulo: {len(gaps_to_resolve)} gaps
- Gaps em aberto (NÃO resolver): {len(outstanding)} gaps

ESTRUTURA DE CAPÍTULO (obrigatória, conforme Style Guide):
1. CENA DE ABERTURA (200-400 palavras) — diálogo real, data, nome, contexto
2. DEFINIÇÃO DO PROBLEMA (300-500 palavras) — nomeia o conceito, conecta com caps anteriores
3. FRAMEWORK / COMPONENTES (800-1200 palavras) — framework autoral com nome próprio
4. CASOS REAIS (600-1000 palavras) — 3 casos: Situação → Problema → Solução → Resultados
5. GUIA PRÁTICO (400-600 palavras) — timeline 30/60/90 dias
6. MÉTRICAS DE SUCESSO (200-400 palavras) — KPIs específicos
7. FECHAMENTO COM GANCHO (200-300 palavras) — resume + planta gap próximo cap

SUA MISSÃO (crie um outline detalhado):

## 1. PREMISSA CENTRAL DO CAPÍTULO
Qual é a tese única deste capítulo que nenhum outro livro de produto aborda?
(1-2 frases)

## 2. CURIOSITY SCHEDULE
a) GAPS A RESOLVER: como cada gap pendente será respondido neste capítulo
b) GAPS A PLANTAR: 2-3 perguntas que este capítulo planta e responde depois
c) ESCALATION: após resolver um gap, qual pergunta MAIOR surge?

## 3. OUTLINE DETALHADO
Para cada uma das 7 seções:
- Gancho/tese da seção
- 3-5 bullet points de conteúdo
- Que dados/cases do research usar
- Onde entra Product Compass
- Onde plantar/resolver gaps

## 4. NOMEAÇÃO DE FRAMEWORKS
- Que framework autoral este capítulo introduz?
- Nome memorável + acrônimo (ex: ESCAPE, 7 Sinais)
- Quantos componentes/elementos?

## 5. PONTES ENTRE CAPÍTULOS
- Conexão com Cap {chapter_num - 1}: o que foi prometido que precisa ser entregue?
- Conexão com Cap {chapter_num + 1}: o que deixar em aberto como gancho?

## 6. GAPS EM ABERTO (NÃO RESOLVER)
Liste os gaps que estão em aberto de capítulos anteriores e que NÃO devem ser
resolvidos aqui (pertencem a capítulos futuros):
{chr(10).join(f'- {g.id}: {g.question}' for g in outstanding) if outstanding else '- Nenhum'}
"""

    result = model.invoke([
        SystemMessage(content=BOOK_SYSTEM),
        HumanMessage(content=prompt),
    ])
    outline = result.content if hasattr(result, "content") else str(result)

    print(f"[Strategist] Outline criado ({len(outline)} caracteres)")

    return {
        "chapter_outline": outline,
        "messages": [AIMessage(content=f"[Strategist] Outline e Curiosity Schedule definidos para Capítulo {chapter_num}")],
    }


# ═══════════════════════════════════════════════════════════════════════════
# WRITER
# ═══════════════════════════════════════════════════════════════════════════

def node_writer(state: dict) -> dict:
    """Escreve o capítulo completo seguindo outline, style guide e curiosity registry.

    Output salvo em state['chapter_draft'] e state['draft_path'].
    """
    model = _get_model(temperature=0.8)
    research_model = _get_model(temperature=0.4).bind_tools(ALL_TOOLS)

    chapter_num = state.get("target_chapter", 7)
    research = state.get("research_material", "")
    outline = state.get("chapter_outline", "")
    revision_count = state.get("revision_count", 0)
    chapter_info = get_chapter_info(chapter_num)

    # ── REVISION MODE ───────────────────────────────────────────────────
    if revision_count > 0:
        existing_draft = state.get("chapter_draft", "")
        editor_feedback = state.get("editor_feedback", "")

        print(f"[Writer] Modo REVISÃO (ciclo {revision_count})")

        # Fase 1: Pesquisa adicional para corrigir problemas
        research_prompt = f"""{BOOK_SYSTEM}

MODO: PESQUISA PARA REVISÃO.

FEEDBACK DO EDITOR-CHEFE:
{editor_feedback}

CAPÍTULO ATUAL (problemático):
{existing_draft[:4000]}

Busque fontes e dados que corrijam os problemas apontados pelo Editor-Chefe.
Use search_web para cada ponto específico. Seja cirúrgico."""

        research_msgs = [
            SystemMessage(content=f"{BOOK_SYSTEM}\n\nUse SEMPRE as ferramentas para pesquisar."),
            HumanMessage(content=research_prompt),
        ]
        research_result = _invoke_with_tools(research_model, research_msgs, max_tool_rounds=3)

        # Fase 2: Reescrever corrigindo
        write_prompt = f"""{BOOK_SYSTEM}

## FUNÇÃO: WRITER — Modo REVISÃO (ciclo {revision_count})

{STYLE_GUIDE[:2000]}

CAPÍTULO ATUAL:
---
{existing_draft[:8000]}
---

PESQUISA ADICIONAL (dados corrigidos):
{research_result[:3000]}

FEEDBACK DO EDITOR-CHEFE:
{editor_feedback}

INSTRUÇÕES:
1. Corrija TODOS os problemas apontados pelo Editor-Chefe
2. Use os dados da pesquisa adicional onde necessário
3. Mantenha o que está bom — reescreva apenas o que precisa ser corrigido
4. Preserve estrutura, voz, frameworks e seções intactas
5. NÃO encurte — o capítulo deve continuar completo (~3000-4000 palavras)

Retorne o capítulo COMPLETO corrigido em Markdown."""

        result = model.invoke([
            SystemMessage(content=BOOK_SYSTEM),
            HumanMessage(content=write_prompt),
        ])

        draft = result.content if hasattr(result, "content") else str(result)
        timestamp = datetime.now().strftime("%Y%m%d-%H%M")
        draft_path = f"output/capitulo-{chapter_num:02d}-r{revision_count}-{timestamp}.md"
        Path(f"{PROJECT_ROOT}/{draft_path}").parent.mkdir(parents=True, exist_ok=True)
        Path(f"{PROJECT_ROOT}/{draft_path}").write_text(draft, encoding="utf-8")

        print(f"[Writer] Revisão (ciclo {revision_count}) salva em {draft_path}")

        return {
            "chapter_draft": draft,
            "draft_path": draft_path,
            "messages": [AIMessage(content=f"[Writer] Capítulo {chapter_num} revisado (ciclo {revision_count}): {draft_path}")],
        }

    # ── FIRST DRAFT MODE ────────────────────────────────────────────────
    print(f"[Writer] Modo PRIMEIRA VERSÃO — Capítulo {chapter_num}")

    # Fase 1: Pesquisa rápida adicional para preencher lacunas
    research_prompt = f"""{BOOK_SYSTEM}

MODO: PESQUISA PRÉ-ESCRITA.

Capítulo {chapter_num}: {chapter_info.get('chapter_title', '')}

OUTLINE:
{outline[:3000]}

Pesquise dados e fatos adicionais para preencher lacunas no outline.
Use search_web para buscar estatísticas recentes e casos de UX/design para IA.
Seja rápido: 2-3 buscas no máximo."""

    research_msgs = [
        SystemMessage(content=f"{BOOK_SYSTEM}\n\nUse SEMPRE as ferramentas para pesquisar."),
        HumanMessage(content=research_prompt),
    ]
    extra_research = _invoke_with_tools(research_model, research_msgs, max_tool_rounds=2)

    # Fase 2: Escrever o capítulo
    write_prompt = f"""{BOOK_SYSTEM}

## FUNÇÃO: WRITER — Primeira versão do capítulo

{STYLE_GUIDE}

**Capítulo {chapter_num}: {chapter_info.get('chapter_title', '')}**
**Parte {chapter_info.get('part')}: {chapter_info.get('part_title', '')}**

MATERIAL DE PESQUISA:
{research[:8000]}

PESQUISA ADICIONAL:
{extra_research[:3000]}

OUTLINE DETALHADO:
{outline[:6000]}

CONTEXTO DE CURIOSITY:
{to_prompt_context(chapter_num)}

INSTRUÇÕES CRÍTICAS:

1. **Siga EXATAMENTE a estrutura de 7 seções do Style Guide.**
   Não pule nenhuma. Não invente seções novas.

2. **Voz:** A cena de abertura DEVE seguir o padrão:
   "Era uma [dia] de [mês] de [ano], e [nome], [cargo], ..."
   Cena real, nome real, contexto concreto. NUNCA comece com definição.

3. **Frameworks:** Se o capítulo introduz um framework novo, dê um NOME
   memorável + acrônimo. Siga o padrão ESCAPE (6 componentes) ou 7 Sinais.

4. **Dados:** Use os dados MAIS RECENTES disponíveis ({CURRENT_YEAR}).
   Se um dado de 2023 aparecer e houver versão mais recente, use a mais recente.
   SEMPRE cite fonte + ano entre parênteses.

5. **Product Compass:** Integre naturalmente os insights do Pawel Huryn onde
   forem relevantes (especialmente: Intelligent Interface Sense, Context Depth,
   AI prototyping stack).

6. **Curiosity:** Plante os gaps designados. Resolva os gaps pendentes.
   Após resolver um gap, crie um NOVO gap (escalate).

7. **Português brasileiro:** Zero em-dashes (—). Zero ALL CAPS. Tom direto,
   executivo, sem autoajuda.

8. **Extensão:** 3000-4000 palavras. Capítulo completo, não resumo.

ESCREVA O CAPÍTULO COMPLETO EM MARKDOWN:"""

    result = model.invoke([
        SystemMessage(content=BOOK_SYSTEM),
        HumanMessage(content=write_prompt),
    ])

    draft = result.content if hasattr(result, "content") else str(result)
    timestamp = datetime.now().strftime("%Y%m%d-%H%M")
    draft_path = f"output/capitulo-{chapter_num:02d}-v1-{timestamp}.md"
    Path(f"{PROJECT_ROOT}/{draft_path}").parent.mkdir(parents=True, exist_ok=True)
    Path(f"{PROJECT_ROOT}/{draft_path}").write_text(draft, encoding="utf-8")

    print(f"[Writer] Primeira versão salva em {draft_path} ({len(draft)} caracteres)")

    return {
        "chapter_draft": draft,
        "draft_path": draft_path,
        "messages": [AIMessage(content=f"[Writer] Capítulo {chapter_num} escrito: {draft_path}")],
    }


# ═══════════════════════════════════════════════════════════════════════════
# COPY EDITOR
# ═══════════════════════════════════════════════════════════════════════════

def node_copy_editor(state: dict) -> dict:
    """Revisa gramática, clareza, voz, flow e terminologia (5 passes).

    Output salvo em state['chapter_draft'] (atualizado) e
    state['copy_editor_report'].
    """
    model = _get_model(temperature=0.2)

    chapter_num = state.get("target_chapter", 7)
    draft = state.get("chapter_draft", "")

    print(f"[CopyEditor] Iniciando 5 passes de revisão...")

    # Passes do Copy Editor (seguindo Post AI pattern: 5 passes)
    passes = [
        ("PASSE 1: GRAMÁTICA", """
Revise APENAS gramática e ortografia:
- Concordância verbal e nominal
- Pontuação (vírgula, ponto, dois-pontos)
- Ortografia e acentuação
- Crase
NÃO mude estrutura ou conteúdo. Corrija apenas erros gramaticais."""),

        ("PASSE 2: CLAREZA", """
Revise APENAS clareza e legibilidade:
- Frases com mais de 30 palavras → quebre em 2
- Termos ambíguos → substitua por específicos
- Parágrafos longos (>6 frases) → quebre
- Jargão sem explicação → adicione definição
NÃO mude o conteúdo, apenas torne-o mais claro."""),

        ("PASSE 3: VOZ", """
Revise APENAS voz e tom, comparando com o Style Guide:
- A cena de abertura tem gancho autobiográfico?
- O tom é direto, executivo, sem autoajuda?
- Cortou bullshit e hype?
- As pessoas falam de dentro ("meu data scientist", "o CEO me perguntou")?
- Removeu: "espero que esteja bem", "jornada", "importante", "interessante"?
- Substituiu frases fracas por afirmações fortes?
CORRIJA APENAS problemas de voz. Não reescreva."""),

        ("PASSE 4: FLOW", """
Revise APENAS fluxo e transições:
- Cada seção conecta naturalmente com a próxima?
- As pontes entre seções são explícitas?
- O capítulo flui como narrativa, não como lista?
- O gancho final planta curiosidade para o próximo capítulo?
- Removeu transições fracas ("além disso", "outro ponto importante")?
CORRIJA APENAS transições. Não reescreva seções."""),

        ("PASSE 5: TERMINOLOGIA", """
Revise APENAS consistência terminológica:
- AI Product Manager → "AI PM" após primeira menção
- Machine Learning → "ML" após primeira menção
- AI Trap → sempre com maiúsculas
- Framework ESCAPE → sempre com link para Capítulo 1
- 10 Competências → sempre numerado corretamente
- Termos em inglês: itálico na primeira menção, normal depois
CORRIJA APENAS terminologia. Não reescreva."""),
    ]

    current_draft = draft
    for pass_name, pass_instructions in passes:
        prompt = f"""{BOOK_SYSTEM}

## FUNÇÃO: COPY EDITOR — {pass_name}

{STYLE_GUIDE[:1500]}

TEXTO ATUAL:
---
{current_draft[:10000]}
---

INSTRUÇÕES:
{pass_instructions}

Retorne o texto COMPLETO revisado (apenas as correções deste passe):"""

        result = model.invoke([
            SystemMessage(content=BOOK_SYSTEM),
            HumanMessage(content=prompt),
        ])
        current_draft = result.content if hasattr(result, "content") else str(result)
        print(f"[CopyEditor] {pass_name} concluído ({len(current_draft)} caracteres)")

    # Atualiza o draft
    draft_path = state.get("draft_path", "")
    if draft_path:
        Path(f"{PROJECT_ROOT}/{draft_path}").write_text(current_draft, encoding="utf-8")

    report = f"""Copy Editor Report — Capítulo {chapter_num}
Data: {CURRENT_DATE}
5 passes executados: Gramática → Clareza → Voz → Flow → Terminologia
Original: {len(draft)} caracteres → Final: {len(current_draft)} caracteres
"""

    print(f"[CopyEditor] Revisão completa. {len(draft)} → {len(current_draft)} caracteres")

    return {
        "chapter_draft": current_draft,
        "copy_editor_report": report,
        "messages": [AIMessage(content=f"[CopyEditor] 5 passes concluídos para Capítulo {chapter_num}")],
    }


# ═══════════════════════════════════════════════════════════════════════════
# EDITOR-CHEFE
# ═══════════════════════════════════════════════════════════════════════════

def node_editor_chefe(state: dict) -> dict:
    """Gatekeeper final. Decide: APPROVE, MINOR, ou REVISE.

    Output: state['editor_decision'], state['editor_feedback'].
    """
    model = _get_model(temperature=0.2)

    chapter_num = state.get("target_chapter", 7)
    draft = state.get("chapter_draft", "")
    copy_report = state.get("copy_editor_report", "")
    revision_count = state.get("revision_count", 0)

    prompt = f"""{BOOK_SYSTEM}

## FUNÇÃO: EDITOR-CHEFE — Gatekeeper de Qualidade

{STYLE_GUIDE[:2000]}

Você é o Editor-Chefe do livro "AI Product Management". Sua função é aprovar
ou rejeitar capítulos baseado em critérios objetivos de qualidade.

CAPÍTULO {chapter_num} PARA AVALIAÇÃO:
---
{draft[:10000]}
---

COPY EDITOR REPORT:
{copy_report}

CRITÉRIOS DE AVALIAÇÃO (cada item: APROVADO ou REPROVADO):

1. ESTRUTURA (as 7 seções estão presentes?)
   - [ ] Cena de abertura com gancho autobiográfico
   - [ ] Definição do problema
   - [ ] Framework autoral com componentes
   - [ ] Casos reais (≥3)
   - [ ] Guia prático (30/60/90 dias)
   - [ ] Métricas de sucesso
   - [ ] Fechamento com gancho para próximo capítulo

2. VOZ (consistente com Style Guide?)
   - [ ] Tom direto, executivo, sem autoajuda
   - [ ] Zero em-dashes (—)
   - [ ] Zero ALL CAPS
   - [ ] Português brasileiro correto

3. CONTEÚDO
   - [ ] Framework autoral nomeado (com acrônimo)?
   - [ ] Dados atualizados ({CURRENT_YEAR}) com fontes?
   - [ ] Product Compass integrado onde relevante?
   - [ ] Curiosity gaps plantados/resolvidos corretamente?

4. EXTENSÃO E PROFUNDIDADE
   - [ ] 3000-4000 palavras?
   - [ ] Profundidade suficiente (não é resumo)?

DECISÃO FINAL:

Escolha UMA:

**APPROVE** — Capítulo está pronto. Todos os critérios atendidos.
**MINOR** — Pequenos ajustes. Listar correções pontuais (máx 3).
**REVISE** — Problemas estruturais. Devolver ao Writer com feedback detalhado.

Se REVISE (ciclo {revision_count + 1}/3):
- Descreva EXATAMENTE o que está errado (não "melhorar o tom" — diga qual frase, por que)
- Priorize: o que corrigir PRIMEIRO
- Se este é o ciclo 3, considere APPROVE com ressalvas (limite de revisões)

Se APPROVE:
- Destaque 1-2 pontos fortes do capítulo

FORMATO DA RESPOSTA:

DECISÃO: [APPROVE|MINOR|REVISE]
JUSTIFICATIVA: [1 parágrafo]
FEEDBACK: [específico e acionável]"""

    result = model.invoke([
        SystemMessage(content=BOOK_SYSTEM),
        HumanMessage(content=prompt),
    ])

    feedback = result.content if hasattr(result, "content") else str(result)

    # Extrai decisão
    decision = "APPROVE"
    if "REVISE" in feedback.upper():
        decision = "REVISE"
    elif "MINOR" in feedback.upper():
        decision = "MINOR"

    # Se já revisou 3 vezes, força APPROVE
    if revision_count >= 3:
        decision = "APPROVE"
        feedback = f"[APROVADO AUTOMATICAMENTE após {revision_count} revisões]\n\n{feedback}"

    print(f"[EditorChefe] Decisão: {decision} (ciclo {revision_count})")

    return {
        "editor_decision": decision,
        "editor_feedback": feedback,
        "messages": [AIMessage(content=f"[EditorChefe] Decisão: {decision} para Capítulo {chapter_num}")],
    }
