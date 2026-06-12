"""Style Guide extraído dos capítulos 1-3 do AI Product Management.

Define voz, tom, estrutura de parágrafo, e padrões autorais da Fernanda Faria.
"""

STYLE_GUIDE = """
# STYLE GUIDE — AI Product Management
## Autora: Fernanda Faria

## VOZ E TOM

### Três traços da voz autoral:

1. **Gancho autobiográfico**: Todo capítulo abre com cena real.
   Formato: "Era uma [dia da semana] de [mês] de [ano], e [nome], [cargo] de [empresa], estava..."
   Sempre inclui: dia da semana, mês, ano, nome da pessoa, cargo, contexto concreto.
   NUNCA começar com teoria abstrata ou definição.

2. **Frameworks autorais com acrônimos**: Cada conceito importante ganha nome próprio.
   Exemplos: ESCAPE (6 princípios), AI Trap (5 sintomas), 7 Sinais, 10 Competências.
   Frameworks têm: nome memorável + componentes numerados + exemplos reais para cada.
   NUNCA usar frameworks genéricos de outros autores sem adaptação.

3. **Tom antipático com hype**: Direto, executivo, sem autoajuda.
   - "Isso não é teoria abstrata. É conhecimento prático baseado em implementações reais."
   - Corta bullshit: "IA é ferramenta poderosa, mas não é solução universal."
   - Fala de dentro: "Meu data scientist...", "O CEO me perguntou..."
   NUNCA usar: "espero que esteja bem", "é um prazer compartilhar", "nessa jornada".

### Padrões de linguagem:

- Português brasileiro formal mas acessível
- Zero em-dashes (—). Usar vírgula, dois-pontos ou ponto.
- Zero ALL CAPS para ênfase
- Números em português: "R$ 12 milhões", "78% dos consumidores"
- NUNCA: "very", "really", "quite" ou equivalentes em PT ("muito importante" → "crucial")
- NUNCA: jargão de consultoria ("alavancar", "sinergia", "disruptivo")

## ESTRUTURA DE CAPÍTULO

Cada capítulo segue esta sequência:

1. **CENA DE ABERTURA** (200-400 palavras)
   - Diálogo ou cena real com nome, data, contexto
   - Planta a pergunta central do capítulo
   - Termina com tensão não resolvida

2. **DEFINIÇÃO DO PROBLEMA** (300-500 palavras)
   - Nomeia o conceito/framework
   - Explica por que é diferente/novo
   - Conecta com capítulos anteriores (cross-reference)

3. **FRAMEWORK / COMPONENTES** (800-1200 palavras)
   - Framework com nome próprio + número de componentes
   - Cada componente: definição → exemplo real → "Por que é problemático/importante"
   - Dados quantitativos sempre com fonte

4. **CASOS REAIS** (600-1000 palavras)
   - 3 casos de empresas reais
   - Estrutura: Situação Inicial → O que estava errado → Como resolveu → Resultados
   - Resultados sempre com números e timeframe

5. **GUIA PRÁTICO** (400-600 palavras)
   - Timeline de implementação (30/60/90 dias)
   - Ações concretas, não conselhos vagos
   - "Esta semana:", "Próximos 30 dias:", "Próximos 90 dias:"

6. **MÉTRICAS DE SUCESSO** (200-400 palavras)
   - KPIs específicos e mensuráveis
   - 3 categorias: Valor para Usuário, Valor para Negócio, Qualidade de Implementação

7. **FECHAMENTO COM GANCHO** (200-300 palavras)
   - Resume o que foi aprendido
   - Planta gap para o próximo capítulo
   - "No próximo capítulo, vamos explorar..."

## ELEMENTOS RECORRENTES

### Abertura de seção (dentro do capítulo):
- Sempre com pergunta real entre aspas
- Ex: `"Fernanda, como garantimos que nossa estratégia de IA não seja apenas mais uma iniciativa de tecnologia?"`

### Caixas de ❌ vs ✅:
- Usar para contrastes
- ❌ O que NÃO é
- ✅ O que É

### Dados quantitativos:
- Sempre com fonte e ano
- Ex: "89% das empresas Fortune 500 têm projetos ativos de IA (McKinsey Global AI Survey 2023)"
- Quando dados forem de 2023, usar os mais recentes disponíveis (2025-2026)

## TERMINOLOGIA PADRÃO

| Termo | Uso |
|-------|-----|
| AI Product Manager | Sempre por extenso na primeira menção |
| Inteligência Artificial | "IA" após primeira menção |
| Product Manager | "PM" após primeira menção |
| Machine Learning | "ML" após primeira menção |
| Framework ESCAPE | Sempre com link para capítulo 1 |
| AI Trap | Sempre com maiúsculas |

## PROIBIÇÕES

- ❌ Começar capítulo com definição teórica
- ❌ Citar frameworks de outros autores sem contexto
- ❌ "Espero que este capítulo ajude você..."
- ❌ "Nesta jornada de aprendizado..."
- ❌ Adjetivos vazios: "importante", "interessante", "incrível"
- ❌ Perguntas retóricas no final do capítulo
- ❌ Conselhos sem ação concreta
"""

# Exemplos de abertura de capítulo para referência do Writer
CHAPTER_OPENING_EXAMPLES = [
    # Cap 1
    '''"Por que nosso chatbot tem 95% de accuracy mas os usuários o odeiam?"

Era uma segunda-feira de janeiro de 2023, e Marina Santos, Head of Product de uma empresa de logística brasileira, estava me mostrando métricas que não faziam sentido.''',

    # Cap 2
    '''"Fernanda, todo mundo está falando de IA, mas como sabemos se isso não é apenas mais um hype que vai passar?"

Era uma quarta-feira de abril de 2023, e estava conversando com Carlos, CPO de uma das maiores empresas de telecomunicações do Brasil.''',

    # Cap 3
    '''"Fernanda, sei que preciso me adaptar para IA, mas por onde começar? Quais competências são realmente essenciais vs. nice-to-have?"

Era uma sexta-feira de maio de 2023, e estava conversando com Ana, uma Product Manager sênior com 8 anos de experiência em produtos digitais.''',
]
