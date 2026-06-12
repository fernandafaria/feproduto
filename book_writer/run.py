"""
Book Writer — CLI Runner
=========================
Ponto de entrada para rodar o pipeline de escrita.

Uso:
  $ cd ~/code/feproduto
  $ python -m book_writer.run --chapter 7
  $ python -m book_writer.run --chapter 7 --max-revisions 2
  $ python -m book_writer.run --chapter 4  # completar cap 4

Requer:
  pip install langgraph langchain-core langchain-openai
  DEEPSEEK_API_KEY no ambiente ou ~/.hermes/.env
"""

from __future__ import annotations

import argparse
import sys
from pathlib import Path

# Garante que o projeto está no path
PROJECT_ROOT = Path(__file__).parent.parent
sys.path.insert(0, str(PROJECT_ROOT))


def main():
    parser = argparse.ArgumentParser(
        description="Book Writer — Pipeline multiagente para escrita de livro"
    )
    parser.add_argument(
        "--chapter", "-c",
        type=int,
        default=7,
        help="Número do capítulo a escrever (1-12). Default: 7 (Designing for AI)",
    )
    parser.add_argument(
        "--max-revisions", "-r",
        type=int,
        default=3,
        help="Máximo de ciclos de revisão. Default: 3",
    )
    parser.add_argument(
        "--list", "-l",
        action="store_true",
        help="Lista os capítulos disponíveis e sai",
    )
    parser.add_argument(
        "--quiet", "-q",
        action="store_true",
        help="Modo silencioso (menos output)",
    )

    args = parser.parse_args()

    if args.list:
        from book_writer.knowledge_base import BOOK_OUTLINE
        print("\nCapítulos disponíveis:\n")
        for part_num in sorted(BOOK_OUTLINE["parts"]):
            part = BOOK_OUTLINE["parts"][part_num]
            print(f"  PARTE {part_num}: {part['title']}")
            print(f"  {part['epigraph']}")
            for ch_num in sorted(part["chapters"]):
                status = "✅" if ch_num <= 3 else "⬜"
                if ch_num == 4:
                    status = "🔄"
                print(f"    {status} Cap {ch_num}: {part['chapters'][ch_num]}")
            print()
        return

    if args.chapter < 0 or args.chapter > 12:
        print(f"Erro: Capítulo {args.chapter} inválido. Use 0-12 (0=Introdução).")
        sys.exit(1)

    from book_writer.engine import run_pipeline

    run_pipeline(
        chapter_num=args.chapter,
        max_revisions=args.max_revisions,
        verbose=not args.quiet,
    )


if __name__ == "__main__":
    main()
