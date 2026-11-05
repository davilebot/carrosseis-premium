---
name: carrosseis-premium
description: Criar, auditar ou revisar carrosséis de conteúdo com copy, retenção e direção de arte tech, minimalista e premium. Usar para roteiros, peças visuais ou ajustes pontuais de slides; preservar versões e escolhas aprovadas.
---

# Carrosséis premium do Davi

Crie uma experiência de leitura que tenha uma ideia clara, progressão entre slides e direção de arte orientada pela função de cada tela. A identidade do Davi é sóbria, contemporânea e visual; o teal Echo funciona como acento, não como um banho de cor. Use esta skill para gerar uma peça nova, auditar uma existente ou corrigir um trecho específico.

## Modos de uso

Interprete estes comandos em linguagem natural, inclusive quando o usuário enviar copy, PDF, imagens ou link:

- **`$carrosseis-premium gerar`**: criar roteiro e, quando solicitado ou viável, os slides. Exemplo: “gere um carrossel de 8 slides sobre X para Y, com fontes Z”.
- **`$carrosseis-premium auditar`**: examinar copy, narrativa, retenção, arte, legibilidade e fidelidade às fontes; apresentar problemas por prioridade e alterações concretas. Não mudar arquivos só para auditar.
- **`$carrosseis-premium revisar slide N`**: alterar apenas o slide indicado e dependências inevitáveis explicitadas. Exemplo: “revise o slide 4 para gerar curiosidade; preserve os slides 1–3 e 5–8”.
- **`$carrosseis-premium comparar`**: confrontar versões, indicar o que foi aprovado, perdido, melhorado ou continua incerto; propor uma versão integrada sem sobrescrever a origem.

Se o pedido for apenas de copy, entregue copy; se for visual, entregue arte ou especificação executável compatível com as ferramentas disponíveis. Não apresente uma descrição de design como se fosse uma peça pronta.

## Contrato de autoria e preservação

1. Separe **texto-fonte**, **versão aprovada**, **proposta** e **hipótese**. Uma imagem gerada, sugestão do assistente ou copy experimental não vira aprovada por existir.
2. Priorize correções explícitas do usuário sobre versões anteriores. Não substitua frase, slide, conceito visual ou estrutura aprovados sem avisar o que mudará e por quê. Guarde a versão anterior quando houver arquivo editável.
3. O designer atua como **diretor de arte**: decide composição, ritmo, imagem, metáfora, hierarquia e distribuição visual do texto; pode sugerir divisão/fusão de slides. Mudança de tese, argumento, promessa, conclusão, dado ou CTA estratégico é proposta editorial identificada, nunca alteração silenciosa.
4. Em revisão pontual, registre o escopo antes de editar. Preserve literalmente os demais slides, salvo reparos mecânicos indispensáveis para exportação; mostre um antes/depois do slide alterado e declare qualquer efeito colateral.
5. Não invente pesquisa, mecanismo interno de empresa, cálculo, metodologia secreta, resultado ou fonte. Marque fatos que precisam de checagem antes de publicar. Uma aplicação do conceito a outro negócio pode ser hipótese ou analogia, desde que assim identificada.
6. Quando produzir arte, entregue **um arquivo individual por slide**, em ordem e com nomes estáveis (`slide-01`, `slide-02` etc.). Uma montagem geral pode ser prévia adicional, nunca o único resultado. Mantenha arquivos-fonte e slides anteriores para ajustes locais; ao revisar um slide, exporte só sua nova versão e confira que os demais arquivos não mudaram.

## Decisão antes de desenhar

1. Identifique público, canal, objetivo, tese, fonte, material aprovado e restrições. Se algo faltar, avance com uma suposição explícita que não mude a tese.
2. Classifique o carrossel: **lista, educacional/tutorial, storytelling, opinião/provocação, case/análise**, ou mistura. O tipo orienta a solução; não impõe template ou número fixo de slides.
3. Para cada slide, anote: **função narrativa**, **ideia única**, **o que o leitor já sabe**, **o que ficará em aberto**, **objetivo visual**, **intensidade de 1 a 5**, **recurso gráfico** e **ligação ao próximo**. A função pode ser capa, contexto, demonstração, tensão, virada, ruptura, ponte, síntese ou CTA, em qualquer posição útil.
4. Faça uma leitura corrida só dos títulos e frases finais. Se a história não avançar, resolva a arquitetura antes de polir frases ou imagens.
5. Distribua impacto. Capa e rupturas podem ter escala exagerada; slides de explicação devem ser rápidos de entender. Uma imagem forte pode atravessar a margem como exceção deliberada. Nem todo slide precisa ser explosivo.

Leia [copy e retenção](references/copy-retencao.md) para redigir ou auditar a narrativa. Leia [direção de arte](references/direcao-arte.md) para desenhar ou julgar o visual. Leia o [caso Mercado Livre](references/mercado-livre.md) quando o pedido usar esse caso ou precisar de exemplos concretos de escolhas aceitas e rejeitadas.

Ao modificar esta skill, rode os [cenários de teste](references/testes.md) com pedidos realistas e refine apenas regras que falharem de forma observável.

## Fluxo por modo

### Gerar

1. Inventarie fontes e decisões aprovadas; confira fatos, datas e direitos de uso quando a peça for para publicação.
2. Monte o mapa de slides com tipo, função, progressão e intensidade. Escolha a quantidade pelo conteúdo; “5 a 7” é uma referência do PDF de origem, não uma regra universal. O caso Mercado Livre tem 8 slides.
3. Escreva a copy em linguagem natural e específica. Transforme afirmações óbvias em uma consequência, contradição ou aplicação ainda não percebida, e entregue a resposta depois. Evite prometer mais informação sem motivo para virar a tela.
4. Defina hierarquia, paleta, tipografia, margens e recursos visuais a partir da função de cada slide. Faça imagens trabalharem a favor da ideia, inclusive por sombra, perspectiva e integração ao fundo.
5. Produza e revise a sequência inteira. Se houver arte, entregue cada slide em arquivo separado, na mesma proporção e área segura; uma prévia conjunta é opcional. Entregue também um mapa curto de função por slide e as fontes/pendências relevantes.

### Auditar

Examine a peça em três passadas: (a) promessa, progressão e retenção; (b) clareza, evidência e fidelidade à copy aprovada; (c) ritmo, legibilidade, margens e identidade visual. Relate **slide / problema observável / efeito / correção proposta / prioridade**. Cite o texto ou elemento visual exato. Não recomende trocar tudo quando um ajuste local resolver.

### Revisar pontualmente

Trave os slides fora do escopo. Faça um diagnóstico do papel do slide alvo e das expectativas criadas pelos vizinhos. Gere no máximo algumas opções quando a escolha de copy for material; indique uma recomendação. Aplique só a opção selecionada ou, se o usuário já escolheu, aplique-a diretamente. Compare antes/depois e verifique se o slide seguinte entrega a pergunta aberta sem antecipação nem quebra de fluxo.

## Testes de aceitação

Use estes testes no resultado real, não apenas como perguntas retóricas:

- **Teste do “já sei”**: o leitor que conhece o fato superficial encontra uma razão específica para continuar? A frase final cria uma lacuna legítima e o slide seguinte a resolve?
- **Teste de slide isolado**: título, visual e texto permitem entender sua ideia principal em poucos segundos? Se a imagem for retirada, perde-se uma explicação relevante ou apenas enfeite?
- **Teste de sequência**: cada tela tem função e mudança perceptível de ritmo? A passagem entre telas é causal, sem listas genéricas ou promessas vazias?
- **Teste de fidelidade**: compare texto-fonte, escolhas aprovadas e resultado. Toda mudança editorial substancial está identificada? Números, aspas, fontes e atribuições foram verificados?
- **Teste visual**: veja em tamanho de celular e na proporção de publicação atual. Confira corte, margens, contraste, hierarquia, leitura e consistência. A proporção deve ser confirmada para a plataforma no momento da exportação.
- **Teste de revisão localizada**: compare hashes ou lado a lado dos slides fora do escopo quando houver arquivos; devem permanecer iguais. Se não for possível comparar, declare o limite da verificação.
- **Teste de entrega individual**: há exatamente um arquivo visual identificável para cada slide, na ordem correta? É possível substituir apenas o slide pedido sem reconstruir a sequência?

## Checklist de entrega

- [ ] Tese e público identificados; fonte e status de aprovação registrados.
- [ ] Cada slide tem uma função e uma ideia central.
- [ ] Capa cria atenção sem promessa enganosa; slides intermediários entregam o que foi prometido.
- [ ] Há um motivo concreto para passar ao próximo slide, especialmente após uma explicação aparentemente óbvia.
- [ ] A copy não antecipa a resposta, não injeta tópicos desconectados e não inventa dados.
- [ ] Ritmo alterna ênfase, explicação e respiro conforme a história.
- [ ] Margens e área segura estão preservadas; invasões são exceções intencionais.
- [ ] Teal Echo é acento pontual e suficientemente vivo; cores da marca analisada não substituem a identidade do Davi.
- [ ] Tipografia, imagens e metáforas servem ao conteúdo e seguem legíveis no celular.
- [ ] Slides aprovados fora do escopo continuam intactos; mudanças e limites foram declarados.
- [ ] A arte foi entregue em arquivos individuais, numerados e consistentes; a montagem geral, se existir, é apenas uma prévia.

