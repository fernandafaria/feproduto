"""Knowledge Base — Fatos, frameworks e fontes compartilhadas entre agentes.

Mantém a fonte única de verdade para dados, definições e referências.
Cada agente consulta esta base antes de escrever ou verificar.
"""

from dataclasses import dataclass, field
from typing import Optional


@dataclass
class Framework:
    """Framework autoral do livro."""
    name: str
    acronym: str
    chapter: int
    components: list[str]
    definition: str
    examples: list[str]


@dataclass
class DataPoint:
    """Dado quantitativo com fonte verificável."""
    value: str
    source: str
    year: int
    context: str
    verified: bool = False


@dataclass
class CaseStudy:
    """Case study de empresa real."""
    company: str
    chapter: int
    sector: str
    problem: str
    solution: str
    results: dict[str, str]
    verified: bool = False


# ── FRAMEWORKS AUTORAIS ──

FRAMEWORKS = {
    "escape": Framework(
        name="ESCAPE",
        acronym="ESCAPE",
        chapter=1,
        components=[
            "Empathy First — Comece com necessidades dos usuários, não capacidades da tecnologia",
            "Simple Metrics — Métricas que conectam com valor para usuário e negócio",
            "Context Awareness — Considere contexto real de uso, não cenários ideais",
            "Augmentation over Automation — IA para augmentar humanos, não substituí-los",
            "Progressive Enhancement — Implemente IA gradualmente, validando valor em cada etapa",
            "Ethical Considerations — Implicações éticas e sociais desde o início",
        ],
        definition="Framework para evitar a AI Trap: organizações obcecadas por implementar IA ao invés de criar valor real.",
        examples=[
            "Banco Digital: chatbot com 92% accuracy e NPS 1.8 → redesign → NPS 4.2",
            "E-commerce: recomendações com CTR 2.3% → contextualização → CTR 12.7%",
            "Startup Mobilidade: algoritmo com 96% accuracy e 12% adoção → redesign → 78% adoção",
        ],
    ),
    "ai_trap": Framework(
        name="AI Trap",
        acronym="AI Trap",
        chapter=1,
        components=[
            "Obsessão por métricas técnicas",
            "Soluções em busca de problemas",
            "Ignorar limitações e contexto",
            "Falta de human-centered design",
            "Ausência de feedback loops",
        ],
        definition="Quando organizações ficam obcecadas por implementar IA ao invés de criar valor real para usuários.",
        examples=[
            "Fintech: modelo com 94% accuracy rejeitava 60% dos clientes bons",
            "Varejo: sistema de recomendações de R$ 2.3M aumentou conversão em 0.3%",
            "Hospital: sistema de diagnóstico com 89% accuracy abandonado por falta de explicabilidade",
        ],
    ),
    "7_sinais": Framework(
        name="7 Sinais do Momento de Inflexão",
        acronym="7 Sinais",
        chapter=2,
        components=[
            "Mudança no Comportamento do Consumidor",
            "Investimento Corporativo Massivo",
            "Transformação do Mercado de Trabalho",
            "Mudança Regulatória Global",
            "Emergência de Novos Modelos de Negócio",
            "Mudança na Educação e Formação",
            "Impacto Geopolítico",
        ],
        definition="Sinais que confirmam que estamos em um momento de inflexão irreversível para IA.",
        examples=[
            "ChatGPT: 100M usuários em 2 meses — mais rápido que qualquer tecnologia na história",
            "89% das Fortune 500 têm projetos ativos de IA",
            "Vagas para AI PM cresceram 1200% em 2023",
        ],
    ),
    "10_competencias": Framework(
        name="10 Competências do AI PM",
        acronym="10 Competências",
        chapter=3,
        components=[
            "Technical Fluency",
            "Data Literacy",
            "Experimentation Mindset",
            "Ethical AI Understanding",
            "Cross-Functional Leadership",
            "AI-Specific Metrics",
            "User Research for AI",
            "AI Strategy & Roadmapping",
            "Regulatory & Compliance Awareness",
            "Change Management",
        ],
        definition="As 10 competências essenciais que diferenciam um AI Product Manager de um PM tradicional.",
        examples=[
            "Technical Fluency: saber perguntar 'Qual é o precision e recall? Testamos em produção?'",
            "Data Literacy: descobrir que 78% dos dados de treino são de homens 25-35 anos",
            "Experimentação: lançar chatbot para 5% dos usuários com múltiplas variações",
        ],
    ),
}


# ── DATAPOINTS (a atualizar com dados 2025-2026 via Researcher) ──

DATAPOINTS = [
    DataPoint(
        value="100 milhões de usuários em 2 meses",
        source="Reuters, fevereiro 2023",
        year=2023,
        context="Velocidade de adoção do ChatGPT comparada a outras tecnologias",
    ),
    DataPoint(
        value="67% dos profissionais de tecnologia usam IA regularmente",
        source="Stack Overflow Survey 2023",
        year=2023,
        context="Adoção de IA entre desenvolvedores",
    ),
    DataPoint(
        value="89% das empresas Fortune 500 têm projetos ativos de IA",
        source="McKinsey Global AI Survey 2023",
        year=2023,
        context="Adoção corporativa de IA",
    ),
    DataPoint(
        value="$93.5 bilhões em 2023",
        source="IDC Worldwide AI Spending Guide",
        year=2023,
        context="Investimento global em IA",
    ),
    DataPoint(
        value="Vagas para AI PM cresceram 1200% em 2023",
        source="LinkedIn Workforce Report 2023",
        year=2023,
        context="Demanda por AI Product Managers",
    ),
    DataPoint(
        value="78% dos consumidores brasileiros usaram IA nos últimos 6 meses",
        source="Pesquisa Datafolha/Bain 2023",
        year=2023,
        context="Adoção de IA no Brasil",
    ),
    DataPoint(
        value="Mercado global de IA: $207.9 bilhões (2023), projeção $1.8 trilhões (2030)",
        source="Grand View Research, 2023",
        year=2023,
        context="Tamanho e crescimento do mercado de IA",
    ),
    DataPoint(
        value="CAGR 38.1% (vs internet 28%, mobile 31%)",
        source="Análise comparativa da autora, 2023",
        year=2023,
        context="Comparação de velocidade de adoção entre revoluções tecnológicas",
    ),
]


# ── CASE STUDIES ──

CASE_STUDIES = [
    CaseStudy(
        company="Banco Digital (Brasil)",
        chapter=1,
        sector="Financeiro",
        problem="Chatbot com 92% accuracy técnica e NPS 1.8. 89% dos usuários pediam humano.",
        solution="Redesenharam experiência com foco no usuário, implementaram escalação inteligente, explicações simples, feedback loops.",
        results={
            "NPS": "1.8 → 4.2",
            "Adoção": "67% preferem chatbot para tarefas simples",
            "ROI": "Positivo em 8 meses",
            "Custo": "Redução de 34% em custos de atendimento",
        },
    ),
    CaseStudy(
        company="E-commerce (Brasil)",
        chapter=1,
        sector="Varejo",
        problem="Sistema de recomendações com métricas técnicas excelentes (precision 0.89) mas CTR de 2.3%.",
        solution="Mudaram métricas para revenue, implementaram contextualização, adicionaram explicações, A/B tests focados em outcomes.",
        results={
            "CTR": "2.3% → 12.7%",
            "Conversão": "0.8% → 8.4%",
            "Ticket médio": "+23%",
            "Revenue": "34% do revenue total via recomendações",
        },
    ),
    CaseStudy(
        company="Startup de Mobilidade (Brasil)",
        chapter=1,
        sector="Transporte",
        problem="Algoritmo de otimização de rotas com 96% accuracy mas 12% adoção dos motoristas.",
        solution="Incluíram motoristas no design, simplificaram interface, adicionaram explicações, implementaram override manual.",
        results={
            "Adoção": "12% → 78%",
            "Satisfação": "4.1/5",
            "Tempo": "Redução real de 22%",
            "Combustível": "-15% em custos",
        },
    ),
]


# ── BOOK OUTLINE ──

BOOK_OUTLINE = {
    "title": "AI Product Management",
    "subtitle": "O guia para Product Managers na era da inteligência artificial",
    "author": "Fernanda Faria",
    "parts": {
        1: {
            "title": "Fundamentos",
            "epigraph": "Entendendo o momento de inflexão e construindo bases sólidas",
            "chapters": {
                0: "Introdução: O Momento de Inflexão",
                1: "A AI Trap — O Novo Build Trap",
                2: "O Momento de Inflexão — Sinais de Mudança",
                3: "Anatomia do AI Product Manager — As 10 Competências",
            },
        },
        2: {
            "title": "Competências Técnicas",
            "epigraph": "Desenvolvendo fluência para liderar produtos de IA",
            "chapters": {
                4: "Technical Fluency — Falando a Língua da IA",
                5: "O Novo Discovery — Experimentação em Mundo Não-Determinístico",
                6: "Data-Driven Decision Making 2.0 — Métricas para IA",
            },
        },
        3: {
            "title": "Construindo Produtos de IA",
            "epigraph": "Do design à estratégia, como construir produtos de IA excepcionais",
            "chapters": {
                7: "Designing for AI — UX em Mundo Não-Determinístico",
                8: "Building AI Teams — Orquestrando Talentos Multidisciplinares",
                9: "AI Product Strategy — Vantagem Competitiva Sustentável",
            },
        },
        4: {
            "title": "Liderança e Futuro",
            "epigraph": "Liderando a transformação e se preparando para o que vem depois",
            "chapters": {
                10: "Leading AI Transformation — Mudança Organizacional",
                11: "Ethics and Responsibility — IA Responsável na Prática",
                12: "The Future of AI PM — Tendências e Preparação",
            },
        },
    },
}


def get_chapter_info(chapter_num: int) -> dict:
    """Retorna informações do capítulo: parte, título, epígrafe."""
    for part_num, part_data in BOOK_OUTLINE["parts"].items():
        if chapter_num in part_data["chapters"]:
            return {
                "chapter": chapter_num,
                "part": part_num,
                "part_title": part_data["title"],
                "part_epigraph": part_data["epigraph"],
                "chapter_title": part_data["chapters"][chapter_num],
            }
    return {}


def get_style_guide_prompt() -> str:
    """Retorna o style guide como prompt para o Writer."""
    from book_writer.style_guide import STYLE_GUIDE
    return STYLE_GUIDE


def knowledge_summary() -> str:
    """Resumo para logging."""
    return (
        f"Knowledge Base: {len(FRAMEWORKS)} frameworks | "
        f"{len(DATAPOINTS)} datapoints | "
        f"{len(CASE_STUDIES)} case studies"
    )
