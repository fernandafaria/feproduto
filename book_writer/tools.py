"""
Book Writer — Tools
===================
Ferramentas reais para pesquisa e verificação dos agentes.

Segue o padrão da Post AI Company (langgraph_engine.py):
- search_web: busca na web com múltiplos fallbacks
- extract_urls: extrai conteúdo de páginas
- read_knowledge_base: consulta os frameworks, datapoints e cases locais

Requer: pip install langgraph langchain-core langchain-openai
"""

from __future__ import annotations

import json
import os
import re
from datetime import datetime
from pathlib import Path

from langchain_core.tools import tool

PROJECT_ROOT = Path(__file__).parent.parent  # ~/code/feproduto


# ═══════════════════════════════════════════════════════════════════════════
# WEB SEARCH
# ═══════════════════════════════════════════════════════════════════════════

@tool
def search_web(query: str) -> str:
    """Busca na web informações atuais sobre qualquer tópico.

    Use para pesquisar fatos, estatísticas, cases de empresas, papers,
    notícias, e qualquer informação que precise ser verificada ou atualizada.

    Args:
        query: Termo de busca (ex: 'AI Product Management UX non-deterministic 2025')

    Returns:
        Resultados da busca em JSON com título, URL e descrição.
    """
    import requests

    # Fallback 1: Google search (HTML scraping)
    try:
        url = "https://www.google.com/search"
        headers = {
            "User-Agent": (
                "Mozilla/5.0 (Macintosh; Intel Mac OS X 10_15_7) "
                "AppleWebKit/537.36 (KHTML, like Gecko) Chrome/131.0.0.0 Safari/537.36"
            )
        }
        resp = requests.get(
            url, params={"q": query, "num": 10, "hl": "en"}, headers=headers, timeout=15
        )
        if resp.status_code == 200:
            results = []
            for match in re.finditer(
                r'<a[^>]*href="/url\?q=(https?://[^"&]+)[^"]*"[^>]*>(.*?)</a>',
                resp.text,
                re.DOTALL,
            ):
                href = re.sub(r'&amp;', '&', match.group(1))
                snippet = re.sub(r'<[^>]+>', '', match.group(2) or '')
                if any(skip in href for skip in ['google.com', 'googleadservices', '/search?', '/settings/']):
                    continue
                snippet = snippet[:300]
                results.append({
                    "title": snippet[:120] or href[:120],
                    "url": href,
                    "description": snippet,
                })
                if len(results) >= 5:
                    break
            if results:
                return json.dumps(results, ensure_ascii=False, indent=2)
    except Exception:
        pass

    # Fallback 2: DuckDuckGo Lite
    try:
        url = "https://lite.duckduckgo.com/lite/"
        resp = requests.post(url, data={"q": query}, timeout=15)
        if resp.status_code == 200:
            results = []
            for match in re.finditer(
                r'<a[^>]*href="([^"]+)"[^>]*>(.*?)</a>.*?<span[^>]*>(.*?)</span>',
                resp.text,
                re.DOTALL,
            ):
                href = match.group(1)
                text = re.sub(r'<[^>]+>', '', match.group(2) or match.group(3) or '')
                if href.startswith("http") and "duckduckgo" not in href:
                    results.append({
                        "title": text[:120] or href,
                        "url": href,
                        "description": text[:300] if text else ""
                    })
                if len(results) >= 5:
                    break
            if results:
                return json.dumps(results, ensure_ascii=False, indent=2)
    except Exception:
        pass

    return json.dumps({"error": "Nenhum resultado encontrado", "query": query})


# ═══════════════════════════════════════════════════════════════════════════
# URL EXTRACTION
# ═══════════════════════════════════════════════════════════════════════════

@tool
def extract_urls(urls: list[str]) -> str:
    """Extrai o conteúdo completo de páginas web.

    Use para ler artigos, papers, reportagens referenciadas
    em resultados de busca. Permite verificar informações específicas.

    Args:
        urls: Lista de URLs para extrair (máximo 3)

    Returns:
        Conteúdo extraído em formato texto.
    """
    import requests

    results = {}
    for url in urls[:3]:
        try:
            resp = requests.get(url, timeout=20, headers={
                "User-Agent": "Mozilla/5.0 (compatible; BookWriter/1.0)"
            })
            if resp.status_code == 200:
                text = resp.text[:12000]
                # Remove HTML
                text = re.sub(r'<script[^>]*>.*?</script>', '', text, flags=re.DOTALL | re.IGNORECASE)
                text = re.sub(r'<style[^>]*>.*?</style>', '', text, flags=re.DOTALL | re.IGNORECASE)
                text = re.sub(r'<[^>]+>', ' ', text)
                text = re.sub(r'\s+', ' ', text).strip()
                results[url] = text[:5000]
            else:
                results[url] = f"HTTP {resp.status_code}: não foi possível acessar"
        except Exception as e:
            results[url] = f"Erro: {str(e)}"

    return json.dumps(results, ensure_ascii=False, indent=2)


# ═══════════════════════════════════════════════════════════════════════════
# KNOWLEDGE BASE ACCESS
# ═══════════════════════════════════════════════════════════════════════════

@tool
def read_knowledge_base(query: str) -> str:
    """Consulta a base de conhecimento do livro (frameworks, datapoints, cases).

    Use para acessar frameworks autorais (ESCAPE, AI Trap, 7 Sinais,
    10 Competências), dados quantitativos com fonte, cases de empresas,
    outline do livro, e style guide.

    Args:
        query: Tipo de informação desejada. Opções:
               'frameworks' - Todos os frameworks autorais
               'datapoints' - Dados quantitativos com fontes
               'cases' - Case studies de empresas
               'outline' - Estrutura completa do livro
               'curiosity_chapter_N' - Gaps de curiosidade para capítulo N
               'style_guide' - Guia de voz e tom da autora

    Returns:
        Conteúdo solicitado em formato JSON ou texto.
    """
    import sys
    sys.path.insert(0, str(PROJECT_ROOT))

    from book_writer.knowledge_base import (
        FRAMEWORKS, DATAPOINTS, CASE_STUDIES, BOOK_OUTLINE,
        get_chapter_info, knowledge_summary,
    )
    from book_writer.curiosity_registry import to_prompt_context, registry_summary
    from book_writer.style_guide import STYLE_GUIDE

    if query == "frameworks":
        result = {}
        for key, fw in FRAMEWORKS.items():
            result[key] = {
                "name": fw.name,
                "acronym": fw.acronym,
                "chapter": fw.chapter,
                "definition": fw.definition,
                "components": fw.components,
                "examples": fw.examples,
            }
        return json.dumps(result, ensure_ascii=False, indent=2)

    elif query == "datapoints":
        dps = []
        for dp in DATAPOINTS:
            dps.append({
                "value": dp.value,
                "source": dp.source,
                "year": dp.year,
                "context": dp.context,
            })
        return json.dumps(dps, ensure_ascii=False, indent=2)

    elif query == "cases":
        cases = []
        for cs in CASE_STUDIES:
            cases.append({
                "company": cs.company,
                "chapter": cs.chapter,
                "sector": cs.sector,
                "problem": cs.problem,
                "solution": cs.solution,
                "results": cs.results,
            })
        return json.dumps(cases, ensure_ascii=False, indent=2)

    elif query == "outline":
        return json.dumps(BOOK_OUTLINE, ensure_ascii=False, indent=2)

    elif query == "style_guide":
        return STYLE_GUIDE

    elif query.startswith("curiosity_chapter_"):
        chapter = int(query.split("_")[-1])
        ctx = to_prompt_context(chapter)
        summary = registry_summary()
        return f"{summary}\n\n{ctx}"

    elif query == "summary":
        return knowledge_summary()

    else:
        return json.dumps({
            "error": f"Query '{query}' não reconhecida",
            "valid_options": [
                "frameworks", "datapoints", "cases", "outline",
                "curiosity_chapter_N", "style_guide", "summary"
            ]
        }, ensure_ascii=False, indent=2)


# Todos os tools disponíveis para os agentes
ALL_TOOLS = [search_web, extract_urls, read_knowledge_base]


# ═══════════════════════════════════════════════════════════════════════════
# MODEL FACTORY
# ═══════════════════════════════════════════════════════════════════════════

def _get_model(temperature: float = 0.7, max_tokens: int = 8192):
    """Cria modelo DeepSeek via langchain-openai (compatível com OpenAI API).

    Usa DeepSeek como padrão (custo baixo, qualidade alta para PT-BR).
    """
    from langchain_openai import ChatOpenAI

    api_key = os.environ.get("DEEPSEEK_API_KEY", "")
    if not api_key:
        # Tenta carregar do .env do Hermes
        hermes_env = Path.home() / ".hermes" / ".env"
        if hermes_env.exists():
            for line in hermes_env.read_text().split("\n"):
                if line.startswith("DEEPSEEK_API_KEY="):
                    api_key = line.split("=", 1)[1].strip().strip('"').strip("'")
                    break

    return ChatOpenAI(
        model="deepseek-chat",
        api_key=api_key,
        base_url="https://api.deepseek.com/v1",
        temperature=temperature,
        max_tokens=max_tokens,
    )


# ═══════════════════════════════════════════════════════════════════════════
# TOOL-CALLING HELPER
# ═══════════════════════════════════════════════════════════════════════════

def _invoke_with_tools(
    model,
    messages: list,
    max_tool_rounds: int = 3,
    verbose: bool = True,
) -> str:
    """Invoca o modelo com tool calling loop.

    O modelo pode chamar tools múltiplas vezes. Cada tool call é executada
    e o resultado é injetado como ToolMessage. O loop continua até o modelo
    responder sem tool calls ou atingir max_tool_rounds.

    Args:
        model: Modelo com tools bindadas (model.bind_tools(ALL_TOOLS))
        messages: Lista de mensagens (HumanMessage, SystemMessage, etc.)
        max_tool_rounds: Máximo de rounds de tool calling
        verbose: Se True, imprime tool calls no console

    Returns:
        Resposta final do modelo (string).
    """
    from langchain_core.messages import ToolMessage, HumanMessage

    current_messages = list(messages)

    for round_num in range(max_tool_rounds):
        response = model.invoke(current_messages)

        # Se não há tool calls, é a resposta final
        if not hasattr(response, "tool_calls") or not response.tool_calls:
            return response.content if hasattr(response, "content") else str(response)

        # Adiciona AIMessage com tool_calls
        current_messages.append(response)

        # Executa cada tool call
        for tc in response.tool_calls:
            tool_name = tc.get("name", "")
            tool_args = tc.get("args", {})
            tool_id = tc.get("id", "")

            if verbose:
                arg_preview = str(tool_args)[:120]
                print(f"  🔧 {tool_name}({arg_preview})")

            # Encontra e executa a tool
            tool_fn = {t.name: t for t in ALL_TOOLS}.get(tool_name)
            if tool_fn:
                try:
                    result = tool_fn.invoke(tool_args)
                except Exception as e:
                    result = f"Erro ao executar tool: {e}"
            else:
                result = f"Tool '{tool_name}' não encontrada"

            # Adiciona ToolMessage
            current_messages.append(ToolMessage(
                content=str(result),
                tool_call_id=tool_id,
                name=tool_name,
            ))

    # Se atingiu max_tool_rounds, força resposta final
    current_messages.append(HumanMessage(
        content="Agora responda com sua análise final, sem chamar mais ferramentas."
    ))
    final = model.invoke(current_messages)
    return final.content if hasattr(final, "content") else str(final)
