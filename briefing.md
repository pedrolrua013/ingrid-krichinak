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

## Inferências a validar com a Ingrid
- Nome e conteúdo dos 3 formatos (Consultoria online, Acompanhamento completo, Plano de manutenção) — baseados nos stories de 2024.
- "Método PR": mantido só como nome (não expandido).
- Etapas do "Como funciona".
- Texto do "Sobre" em primeira pessoa, montado a partir das legendas dela.
- Atendimento em casal: consultas juntas ou separadas.

## Pendências
- CRN (obrigatório pelo CFN). Enquanto vazio, o site sai com noindex. Preencher `CRN` em `_tools/build_pages.py` e rodar o build.
- Endereço do consultório em Santos (NAP, schema, mapa).
- Domínio próprio, GTM/GA4 (`GTM_ID` em `assets/site.js`).
