#!/usr/bin/env python3
"""Confere a estrutura da edição pública; não avalia qualidade criativa."""
from pathlib import Path
import sys

root = Path(__file__).resolve().parents[1]
required = [
    'SKILL.md', 'profiles/davi.md', 'playbooks/01-arquitetura.md',
    'playbooks/02-ganchos-identificacao.md', 'playbooks/03-ganchos-curiosidade.md',
    'playbooks/04-retencao-e-frameworks.md', 'playbooks/05-direcao-de-arte.md',
    'playbooks/06-producao-e-revisao-local.md', 'playbooks/07-escopo-editorial.md',
    'examples/banco-80-ganchos.md', 'examples/transicoes-antes-depois.md',
    'examples/receitas-visuais.md', 'examples/casos/01-mercado-livre.md',
    'references/mercado-livre-evolucao.md', 'assets/mercado-livre/slide-04-final.png',
]
errors = [f'Falta: {path}' for path in required if not (root / path).is_file()]
for n in range(1, 9):
    path = f'assets/mercado-livre/slide-{n:02}.png'
    if not (root / path).is_file():
        errors.append(f'Falta: {path}')
if (root / 'assets/mercado-livre/slide-04.png').read_bytes() != (root / 'assets/mercado-livre/slide-04-final.png').read_bytes():
    errors.append('slide-04.png deixou de ser a versão final aprovada')
for folder in ['assets/pinterest', 'assets/sam-gaudet', 'assets/backlog', 'assets/diagnostico', 'assets/concorrente-barato']:
    if (root / folder).exists():
        errors.append(f'Imagem de terceiro no pacote público: {folder}')
print('Estrutura pública:', 'OK' if not errors else 'FALHOU')
for error in errors:
    print(' -', error)
sys.exit(bool(errors))
