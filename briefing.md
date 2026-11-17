# Briefing — Ingrid Krichinak Nutricionista

## Dados recebidos (Pedro, 16/11/2026)
- Cliente: Ingrid Krichinak, nutricionista. Sem identidade visual definida.
- Logo: usar somente o "IK" (referência: "EQUIPE IK", serifada clara sobre preto, linha vermelha abaixo).
- WhatsApp: (13) 99777-1672 → 5513997771672.
- Fotos: liberadas as fotos da nutricionista (Instagram @ingridkrichinak).

## Pesquisa (Instagram, 16/11/2026)
- Bio: "Performance que cabe na vida real." · Emagrecimento | Hipertrofia | Praticidade · "Santos e mundo" · "Conheça o método PR".
- Destaque "Método": suporte contínuo no WhatsApp, feedbacks e ajustes antes da consulta; plano premium com materiais (trocas inteligentes em bebidas, receitas na airfryer, redução de danos no fim de semana, passo a passo de marmitas, guia de produtos e suplementos); consultoria online (plano básico + WhatsApp) para quem já segue plano. Stories de ~2 anos atrás.
- Posts: planos de manutenção (consultas espaçadas); acompanhamento em casal; nutricionista da equipe de ginástica rítmica de competição da AABB; 10 anos de musculação e 3 de CrossFit; participação na Experiência em Nutrição Esportiva de Excelência; temas recorrentes: balança, platô, emagrecer sem comer pouco, eletrólitos, enjoo no treino.
- Fotos usadas: ensaio profissional (post "Toda fase de mudança"): blazer (hero/OG), sorrindo (sobre), de óculos no sofá (páginas de serviço).

## Decisões
- Identidade: Cormorant Garamond (títulos, ecoa o "IK" do logo) + Manrope (texto). Paleta: pedra #ebe6df (fundo das fotos), creme #f5f2ed, tinta #1b1816, vermelho #a8322a (linha do logo).
- Logo "IK" vetorizado em SVG a partir da Cormorant Garamond Light, com a linha vermelha.
- Hero: direção editorial (referência 21st.dev "editorial" + gradientes suaves), foto em arco, manchas de cor animadas em CSS puro.
- Páginas por área: emagrecimento, hipertrofia, nutrição esportiva, acompanhamento em casal.
- Formulário envia para o WhatsApp (sem e-mail de destino disponível). Nada é armazenado.
- Depoimentos: seção despublicada (Código de Ética do CFN; validar com a Ingrid).
- Sem preços (enviados pelo WhatsApp). Nenhuma promessa de resultado ou antes/depois.

## Atualização 16/11 (pedido do Pedro)
- Endereço: Edifício Manhattan, R. São Paulo, 41, Centro Comercial, Santos/SP, 11075-330 (contato, rodapé, FAQ, schema, mapa sob demanda).
- Movimento e profundidade: Lenis (scroll suave), parallax por scroll e mouse, entrada animada no hero, reveal escalonado, orbs de cor flutuantes.
- Glassmorphism em cards, planos, fatos, etapas, FAQ, pilares do método e formulário; hover com crescimento, inclinação 3D e brilho seguindo o cursor; botões com escala, brilho e efeito magnético.

## Atualização 16/11 (Bruno): página de cupons
- /cupons/ com os códigos do destaque "Cupons" do Instagram: Liv Up (ingrid.krichinak1 30% 1ª compra; ingrid.krichinak 10% demais), Ocean Drop (INGRIDK 20%), Dobro (DOBROINGRIDK), DUX (PACINGRIDFARIA). Dados em `COUPONS` no build.
- Fica fora do menu e da home (link só no rodapé), com declaração de parceria visível. Novo Código de Ética do CFN (Res. 856/2026) exige declaração ostensiva de conflito de interesses e veda vincular marcas à prescrição individual.

## Inferências a validar com a Ingrid
- Nome e conteúdo dos 3 formatos (Consultoria online, Acompanhamento completo, Plano de manutenção) — baseados nos stories de 2024.
- "Método PR": mantido só como nome (não expandido).
- Etapas do "Como funciona".
- Texto do "Sobre" em primeira pessoa, montado a partir das legendas dela.
- Atendimento em casal: consultas juntas ou separadas.

## Pendências
- CRN (obrigatório pelo CFN). Enquanto vazio, o site sai com noindex. Preencher `CRN` em `_tools/build_pages.py` e rodar o build.
- Cupons: confirmar se os 4 seguem ativos (DUX é de ~87 semanas atrás), os % da Dobro e da DUX, e o texto de transparência.
- Domínio próprio, GTM/GA4 (`GTM_ID` em `assets/site.js`).
