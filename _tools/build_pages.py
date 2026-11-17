#!/usr/bin/env python3
"""Gera as páginas estáticas do site da Ingrid Krichinak.
Uso: python3 _tools/build_pages.py   (rodar na raiz do projeto)
"""
import json, os, html, datetime
from urllib.parse import quote

ROOT = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))

# ---------------- Configuração ----------------
SITE = "https://ingrid-krichinak.vercel.app"   # trocar ao conectar domínio próprio
NAME = "Ingrid Krichinak"
CRN = ""            # ex.: "CRN-3 12345" — obrigatório pelo CFN em material de divulgação
ADDRESS = {"building": "Edifício Manhattan", "street": "R. São Paulo, 41", "district": "Centro Comercial", "zip": "11075-330"}
WA = "5513997771672"
WA_DISPLAY = "(13) 99777-1672"
IG = "https://www.instagram.com/ingridkrichinak/"
NOINDEX = not CRN   # sem CRN publicado, a página fica fora do Google
TODAY = datetime.date.today().isoformat()

MAPS_Q = "Edifício Manhattan, R. São Paulo, 41, Santos - SP, 11075-330"
MAPS_LINK = "https://www.google.com/maps/search/?api=1&query=" + quote(MAPS_Q)
MAPS_EMBED = "https://www.google.com/maps?q=" + quote(MAPS_Q) + "&output=embed"

def orbs(spec):
    out = "".join(f'<span class="orb {c} float{" slow" if i % 2 else ""}" data-depth="{dp}" style="width:{w}px;height:{w}px;{pos}"></span>' for i, (c, w, pos, dp) in enumerate(spec))
    return f'<div class="orbs" aria-hidden="true">{out}</div>'
ORBS_A = orbs([("rose", 520, "left:-160px;top:10%", "0.6"), ("wine", 380, "right:-80px;bottom:-60px", "-0.5"), ("sand", 420, "right:30%;top:-120px", "0.3")])
ORBS_B = orbs([("rose", 460, "right:-120px;top:-60px", "0.5"), ("sand", 520, "left:-180px;bottom:-140px", "-0.4"), ("wine", 300, "left:42%;top:40%", "0.8")])
ORBS_C = orbs([("milk", 520, "right:-140px;top:-120px", "0.4"), ("rose", 420, "left:-120px;bottom:-100px", "-0.6")])
ORBS_D = orbs([("sand", 460, "left:-140px;top:-80px", "0.5"), ("rose", 400, "right:-100px;bottom:-120px", "-0.5")])

def wa(msg):
    return f"https://wa.me/{WA}?text={quote(msg)}"

ICON_WA = '<svg viewBox="0 0 24 24" fill="currentColor" aria-hidden="true"><path d="M17.47 14.38c-.3-.15-1.75-.86-2.02-.96-.27-.1-.47-.15-.67.15-.2.3-.77.96-.94 1.16-.17.2-.35.22-.64.07-.3-.15-1.25-.46-2.38-1.47-.88-.78-1.47-1.75-1.64-2.05-.17-.3-.02-.46.13-.6.13-.14.3-.35.45-.52.15-.17.2-.3.3-.5.1-.2.05-.37-.03-.52-.07-.15-.67-1.6-.92-2.2-.24-.58-.49-.5-.67-.5h-.57c-.2 0-.52.07-.79.37-.27.3-1.04 1.02-1.04 2.48s1.07 2.88 1.21 3.08c.15.2 2.1 3.2 5.08 4.48.71.31 1.26.49 1.7.63.71.23 1.36.2 1.87.12.57-.08 1.75-.72 2-1.41.25-.7.25-1.29.17-1.41-.07-.13-.27-.2-.57-.35zM12.04 21.5h-.01a9.45 9.45 0 0 1-4.82-1.32l-.35-.2-3.58.94.96-3.49-.23-.36a9.43 9.43 0 0 1-1.45-5.03c0-5.22 4.25-9.46 9.48-9.46a9.4 9.4 0 0 1 6.7 2.78 9.4 9.4 0 0 1 2.77 6.69c0 5.22-4.25 9.46-9.47 9.46zm8.06-17.52A11.33 11.33 0 0 0 12.04.65C5.76.65.65 5.75.65 12.03c0 2 .52 3.96 1.52 5.69L.55 23.35l5.77-1.51a11.37 11.37 0 0 0 5.71 1.46h.01c6.28 0 11.39-5.1 11.39-11.38 0-3.04-1.18-5.9-3.33-8.04z"/></svg>'
ICON_IG = '<svg viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="1.6" aria-hidden="true"><rect x="3" y="3" width="18" height="18" rx="5"/><circle cx="12" cy="12" r="4.2"/><circle cx="17.4" cy="6.6" r="1" fill="currentColor" stroke="none"/></svg>'
ICON_PIN = '<svg viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="1.6" aria-hidden="true"><path d="M12 21s-7-6.2-7-11.5A7 7 0 0 1 19 9.5C19 14.8 12 21 12 21z"/><circle cx="12" cy="9.5" r="2.5"/></svg>'
ICON_GLOBE = '<svg viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="1.6" aria-hidden="true"><circle cx="12" cy="12" r="9"/><path d="M3 12h18M12 3c2.5 2.6 3.8 5.6 3.8 9s-1.3 6.4-3.8 9c-2.5-2.6-3.8-5.6-3.8-9S9.5 5.6 12 3z"/></svg>'

def logo_svg():
    d = open(os.path.join(ROOT, "_tools", "ik_path.txt")).read().strip()
    return (f'<svg viewBox="15 -660 960 790" role="img" aria-label="IK">'
            f'<path fill="currentColor" d="{d}"/><rect x="40" y="70" width="910" height="16" fill="#a8322a"/></svg>')
LOGO = logo_svg()

# ---------------- Serviços ----------------
SERVICES = [
  {
    "slug": "emagrecimento",
    "nav": "Emagrecimento",
    "title": "Nutricionista para emagrecimento em Santos e online",
    "meta": "Emagrecimento com estratégia e sem terrorismo: plano individual, prioridade de proteína e suporte no WhatsApp. Nutricionista em Santos e online.",
    "h1": "Emagrecimento com estratégia, sem viver de restrição",
    "lead": "Emagrecer não é comer pouco. É organizar a rotina, montar um prato que sustenta e ter clareza do que fazer quando a semana sai do roteiro.",
    "card": "Plano para reduzir gordura sem cortar tudo o que você gosta e sem depender de força de vontade o tempo todo.",
    "body": [
      ("Para quem é", [
        "Para quem já tentou dietas restritivas, perdeu peso e recuperou, ou cansou de começar de novo toda segunda-feira. O foco é um plano que cabe na sua rotina de verdade, com trabalho, família, viagens e fins de semana incluídos.",
      ]),
      ("Como o acompanhamento funciona", [
        "Na consulta, a Ingrid entende sua rotina, seu histórico, seus horários, o que você gosta de comer e o que costuma atrapalhar. A partir disso, monta um plano individual, com prioridade de proteína, distribuição das refeições ao longo do dia e estratégias para os momentos mais difíceis.",
        "Entre as consultas, você tem suporte pelo WhatsApp. Com os seus feedbacks, dá para ajustar o plano antes da próxima consulta, sem esperar o problema crescer.",
      ]),
      ("O que muda na prática", [
        "Você aprende a ler a balança com calma: o peso varia ao longo dos dias por água e conteúdo intestinal, e isso não é ganho de gordura. Aprende a lidar com o platô, com a refeição fora de casa e com o fim de semana, sem culpa e sem compensações extremas.",
        "Se você usa algum medicamento prescrito pelo seu médico para perda de peso, a alimentação continua sendo parte do processo, principalmente para preservar massa muscular e manter o que foi conquistado.",
      ]),
    ],
    "faq": [
      ("Vou precisar cortar doces, pão ou bebida?", "Não necessariamente. O plano é construído a partir do que você gosta e da sua rotina. A ideia é aprender a encaixar as escolhas, e não proibir tudo, porque um plano que você não consegue sustentar não funciona."),
      ("Em quanto tempo vejo resultado?", "Cada corpo responde em um ritmo, e a Ingrid não trabalha com promessas de prazo. O que dá para garantir é um plano coerente com o seu objetivo, acompanhamento próximo e ajustes sempre que necessário."),
      ("Preciso treinar para emagrecer?", "É possível emagrecer sem treinar, mas o treino ajuda a preservar massa muscular e melhora a composição corporal. O plano considera a sua realidade atual de atividade física."),
    ],
    "wa": "Olá, Ingrid! Vim pelo site e quero falar sobre acompanhamento para emagrecimento.",
  },
  {
    "slug": "hipertrofia",
    "nav": "Hipertrofia",
    "title": "Nutrição para hipertrofia e ganho de massa | Santos",
    "meta": "Plano alimentar para ganho de massa: proteína bem distribuída, energia para treinar e suplementação quando faz sentido. Santos e online.",
    "h1": "Nutrição para ganhar massa muscular com consistência",
    "lead": "Hipertrofia depende de treino, descanso e alimentação trabalhando juntos. O plano organiza o que você come para o treino render e a recuperação acontecer.",
    "card": "Proteína bem distribuída, energia para treinar e suplementação só quando faz sentido para você.",
    "body": [
      ("Para quem é", [
        "Para quem treina musculação, CrossFit ou outra modalidade e sente que o resultado não acompanha o esforço. Também para quem quer ganhar massa sem acumular gordura além do necessário.",
      ]),
      ("Como o acompanhamento funciona", [
        "A Ingrid avalia a sua rotina de treino, horários, preferências e o quanto você realmente come hoje. O plano define a quantidade e a distribuição de proteína, a energia necessária para sustentar o treino e as refeições antes e depois de treinar.",
        "A suplementação é avaliada caso a caso: o que pode ajudar no seu contexto, o que é dispensável e como usar. Dúvidas sobre produtos e marcas entram no suporte pelo WhatsApp.",
      ]),
      ("Treino de verdade, rotina de verdade", [
        "A Ingrid treina musculação há 10 anos e CrossFit há 3. Ela sabe, na própria rotina, que nunca existe um mês perfeito: tem semana de treino reduzido, viagem, evento. O plano é pensado para continuar funcionando nessas semanas também.",
      ]),
    ],
    "faq": [
      ("Preciso tomar suplemento para ganhar massa?", "Não obrigatoriamente. A base é a alimentação. Suplementos entram quando ajudam a bater uma necessidade que a comida sozinha não cobre com praticidade."),
      ("Ganhar massa é só comer mais calorias?", "Não é só sobre quantas calorias você come. A distribuição de proteína, a qualidade das refeições e a regularidade do treino fazem diferença no resultado."),
      ("Atende quem treina em casa ou está começando?", "Sim. O plano parte do seu nível atual de treino e evolui junto com você."),
    ],
    "wa": "Olá, Ingrid! Vim pelo site e quero falar sobre nutrição para hipertrofia.",
  },
  {
    "slug": "nutricao-esportiva",
    "nav": "Nutrição esportiva",
    "title": "Nutricionista esportiva em Santos | CrossFit e corrida",
    "meta": "Nutrição esportiva para CrossFit, corrida e atletas de competição: estratégia de treino, hidratação e recuperação. Ingrid Krichinak, Santos e online.",
    "h1": "Nutrição esportiva para treinar melhor e se recuperar melhor",
    "lead": "Estratégia alimentar para quem pratica CrossFit, corrida, ginástica ou musculação e quer performance sem abrir mão da saúde.",
    "card": "Estratégia para CrossFit, corrida e competição: antes, durante e depois do treino.",
    "body": [
      ("Para quem é", [
        "Para praticantes e atletas que querem render mais nos treinos, chegar melhor às provas e se recuperar sem sentir que estão sempre no limite.",
        "A Ingrid é nutricionista da equipe de ginástica rítmica de competição da AABB e acompanha praticantes de CrossFit e corrida.",
      ]),
      ("O que entra na estratégia", [
        "Refeições antes e depois do treino ajustadas ao horário e à modalidade. Hidratação e reposição de eletrólitos de acordo com a duração do treino, o ambiente e a sua taxa de sudorese, porque nem todo treino precisa disso.",
        "Atenção a sinais como enjoo, queda de rendimento e cansaço fora do normal, que podem ter relação com a forma como você está se alimentando. Para quem compete, organização das semanas que antecedem a prova.",
      ]),
      ("Atualização constante", [
        "Por trás de cada estratégia existe estudo e decisão baseada em evidência. A Ingrid participa de formações em nutrição esportiva, como a Experiência em Nutrição Esportiva de Excelência, para levar o que há de mais atual para os pacientes.",
      ]),
    ],
    "faq": [
      ("Preciso tomar eletrólitos em todo treino?", "Não. Em treinos curtos, a água geralmente é suficiente. A reposição de eletrólitos faz mais sentido em sessões longas, em ambientes quentes ou com muita perda de suor."),
      ("Sinto enjoo durante o treino. Pode ter relação com a alimentação?", "Pode. O tipo de refeição, a quantidade e o intervalo até o treino influenciam. Esse é um dos pontos avaliados na consulta."),
      ("Atende atletas de outras cidades?", "Sim. O atendimento pode ser online, com o mesmo acompanhamento e suporte pelo WhatsApp."),
    ],
    "wa": "Olá, Ingrid! Vim pelo site e quero falar sobre nutrição esportiva.",
  },
  {
    "slug": "acompanhamento-em-casal",
    "nav": "Acompanhamento em casal",
    "title": "Acompanhamento nutricional em casal | Santos e online",
    "meta": "Acompanhamento nutricional para casais: compras, refeições e refeição livre planejadas a dois para facilitar a adesão. Ingrid Krichinak, nutricionista.",
    "h1": "Acompanhamento nutricional em casal",
    "lead": "Quando o casal caminha junto, a casa vira um ambiente que ajuda, e não que sabota. Cada um com o seu plano, os dois na mesma direção.",
    "card": "Dois planos individuais, uma rotina organizada em conjunto: compras, refeições e refeição livre combinadas a dois.",
    "body": [
      ("Por que fazer em casal", [
        "Muita gente desiste porque está sozinha no processo: a despensa cheia do que atrapalha, refeições diferentes para cada um, a refeição livre que vira motivo de discussão. O acompanhamento em casal resolve isso na raiz.",
      ]),
      ("Como funciona", [
        "Cada pessoa tem avaliação e plano próprios, de acordo com o seu objetivo: um pode querer emagrecer e o outro ganhar massa. A organização da casa é pensada em conjunto: lista de compras planejada, preparo de refeições que funcionam para os dois e a refeição livre combinada a dois, sem culpa e sem um empurrando o outro para fora do plano.",
      ]),
      ("Na prática", [
        "A Ingrid atende casais no consultório e vê a diferença que um ambiente organizado faz na constância. Não é só sobre dieta, é sobre construir uma rotina que sustenta a mudança.",
      ]),
    ],
    "faq": [
      ("Os dois precisam ter o mesmo objetivo?", "Não. Cada um tem o seu plano, com metas próprias. O que é compartilhado é a organização da rotina e da casa."),
      ("As consultas são juntas ou separadas?", "Esse formato é combinado no primeiro contato, de acordo com a preferência do casal. Fale com a Ingrid pelo WhatsApp para entender as opções."),
      ("Dá para fazer online?", "Sim. O acompanhamento em casal também pode ser feito online."),
    ],
    "wa": "Olá, Ingrid! Vim pelo site e quero saber sobre o acompanhamento em casal.",
  },
]

HOME_FAQ = [
  ("Onde fica o consultório?", "No Edifício Manhattan, na R. São Paulo, 41, Centro Comercial, em Santos/SP (CEP 11075-330). Também há atendimento online para qualquer cidade."),
  ("A Ingrid atende online?", "Sim. O atendimento é presencial em Santos e online para qualquer cidade ou país, com o mesmo cuidado e o mesmo suporte pelo WhatsApp."),
  ("Vou ter que cortar tudo o que eu gosto?", "Não. O plano é construído com base na sua rotina e nas suas preferências. A proposta é aprender a fazer escolhas no dia a dia, sem extremismo e sem terrorismo nutricional."),
  ("Como funciona o suporte entre as consultas?", "Você conta com suporte contínuo pelo WhatsApp para dúvidas, imprevistos e ajustes. Com os feedbacks frequentes, é possível ajustar o plano antes mesmo da próxima consulta."),
  ("Preciso levar exames?", "Se você tiver exames recentes, leve. Quando necessário, a Ingrid pode solicitar exames laboratoriais para complementar a avaliação."),
  ("E depois que eu atingir meu objetivo?", "Existe o plano de manutenção, com consultas mais espaçadas e suporte para ajustar estratégias. A ideia é construir autonomia sem perder a direção."),
  ("Como agendo a primeira consulta?", f"Pelo WhatsApp {WA_DISPLAY}. Você recebe as informações sobre formatos, valores e horários disponíveis."),
]

# ---------------- Depoimentos ----------------
# Fonte: destaque "Feedback" do Instagram (avaliações com 5 estrelas, prints enviados pelo Bruno em 16/11/2026).
# Sem nome, sem números de resultado, sem dados de saúde. Trechos com leve ajuste de pontuação.
# Validar com a Ingrid antes de publicar (Código de Ética do CFN). False = seção some do site.
SHOW_DEPOIMENTOS = True
DEPOIMENTOS = [
  "Pela primeira vez, estou conseguindo seguir uma dieta de forma leve, feliz e motivada. O plano alimentar é feito totalmente de acordo com a minha rotina e meus gostos, o que torna tudo muito mais fácil.",
  "Me passou a melhor dieta que já fiz na vida, muito fácil de seguir e muito ajustada ao meu dia a dia. O suporte e acompanhamento do plano fazem toda a diferença para seguir firme nos objetivos.",
  "Mudou minha forma de ver a nutrição! Sempre buscando fazer com que o seu objetivo seja alcançado da forma mais leve possível, sem fazer com que seu relacionamento com a comida seja rígido e monótono.",
  "Muito atenciosa, cuida muito bem do paciente, sempre perguntando como as coisas estão no plano, se tem alguma dúvida, algum problema. Podem ir sem medo.",
  "O plano alimentar é leve, sem aquelas restrições malucas, e adaptado ao que gostamos de comer. No plano temos diversas opções de substituição e também dicas de receitas.",
  "Além dela ser atenciosa, profissional e presente, me sinto muito mais segura e confiante para seguir com meus objetivos, podendo entender melhor sobre alimentação e estilo de vida.",
  "Excelente profissional, muito atenciosa, competente e atualizada. Atendimento personalizado e respeitando sempre as preferências e rotina de vida.",
  "Ela explica tudo de um jeito simples. Os e-books dela são super completos e me ajudam muito, algo que nunca vi em outras nutris.",
]

def depoimentos_section():
    if not SHOW_DEPOIMENTOS:
        return ""
    stars = '<span class="stars" aria-label="5 de 5 estrelas">★★★★★</span>'
    items = "".join(f'<figure class="card testimonial reveal">{stars}<blockquote><p>{html.escape(t)}</p></blockquote><figcaption>Paciente</figcaption></figure>' for t in DEPOIMENTOS)
    return f'''<section class="section has-orbs" id="depoimentos" aria-labelledby="dep-t">
  {ORBS_D}
  <div class="container">
    <div class="section-head center"><span class="eyebrow">Feedbacks</span><h2 id="dep-t">O que dizem sobre o <em>acompanhamento</em></h2>
    <p class="lead">Avaliações deixadas por pacientes, reproduzidas sem identificação.</p></div>
    <div class="carousel" data-carousel>
      <div class="carousel-track" tabindex="0" role="region" aria-roledescription="carrossel" aria-label="Feedbacks de pacientes" data-lenis-prevent>{items}</div>
      <div class="carousel-ui">
        <button class="carousel-btn" type="button" data-dir="-1" aria-label="Feedback anterior"><svg viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="1.6" aria-hidden="true"><path d="M15 5l-7 7 7 7"/></svg></button>
        <div class="carousel-dots" role="tablist" aria-label="Escolher feedback"></div>
        <button class="carousel-btn" type="button" data-dir="1" aria-label="Próximo feedback"><svg viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="1.6" aria-hidden="true"><path d="M9 5l7 7-7 7"/></svg></button>
      </div>
    </div>
    <p class="testimonials-note">Cada pessoa tem um processo individual. Os relatos falam da experiência de atendimento e não representam promessa de resultado.</p>
  </div>
</section>'''

# ---------------- Materiais (plano premium) ----------------
# Fonte: site da Ingrid no Canva (print enviado pelo Bruno em 16/11/2026). Trocar pelos originais em alta quando houver.
EBOOKS = [
  ("trocas-inteligentes-bebidas", "Trocas inteligentes: bebidas alcoólicas"),
  ("receitas-airfryer", "Receitas saudáveis e deliciosas na airfryer"),
  ("reducao-de-danos-fim-de-semana", "Redução de danos no fim de semana"),
  ("marmitas-da-semana", "Passo a passo para preparar as marmitas da semana"),
  ("variar-verduras", "Formas de variar o consumo de verduras"),
  ("guia-produtos-suplementos", "Guia de produtos e suplementos"),
]
PLANNERS = [
  ("planner-cardapio-semanal", "Cardápio semanal", 340, 237),
  ("planner-habitos", "Planner de hábitos", 333, 237),
]

APP_SCREENS = [
  ("app-plano", "Tela inicial do aplicativo com as refeições do plano alimentar"),
  ("app-diario-alimentar", "Diário alimentar do aplicativo com fotos dos pratos registrados"),
  ("app-cupons", "Tela de benefícios do aplicativo com cupons de marcas parceiras"),
]
BASE_BOOKS = [
  ("ebook-receitas", "E-book de receitas"),
  ("manual-organizacao-planejamento", "Manual de organização e planejamento"),
]

def tablet(f, alt, w=188, h=255):
    return f'<div class="tablet"><img src="/assets/img/materiais/{f}.webp" width="{w}" height="{h}" alt="{html.escape(alt)}" loading="lazy" decoding="async"><span class="glare" aria-hidden="true"></span></div>'

def materiais_section():
    books = "".join(f'''<figure class="ebook reveal">{tablet(f, "Capa do e-book " + t)}<figcaption>{html.escape(t)}</figcaption></figure>''' for f, t in EBOOKS)
    planners = "".join(f'''<figure class="planner reveal"><img src="/assets/img/materiais/{f}.webp" width="{w}" height="{h}" alt="{html.escape(t)} para imprimir e preencher na semana" loading="lazy" decoding="async"><figcaption>{html.escape(t)}</figcaption></figure>''' for f, t, w, h in PLANNERS)
    screens = "".join(f'''<figure class="ebook device reveal">{tablet(f, alt, 200, 270)}</figure>''' for f, alt in APP_SCREENS)
    base = "".join(f'''<figure class="ebook reveal">{tablet(f, "Capa do " + t, 190, 256)}<figcaption>{html.escape(t)}</figcaption></figure>''' for f, t in BASE_BOOKS)
    return f'''<section class="section materiais has-orbs" id="materiais" aria-labelledby="materiais-t">
  {ORBS_C}
  <div class="container">
    <div class="center section-head">
      <span class="eyebrow">Benefícios</span>
      <h2 id="materiais-t">Tudo o que acompanha o seu <em>plano</em></h2>
      <p class="lead">Ferramentas e materiais para facilitar as escolhas da semana, das compras ao fim de semana.</p>
    </div>

    <div class="tier-head reveal"><span class="eyebrow">Em todos os acompanhamentos</span></div>
    <div class="benefit">
      <div class="benefit-text reveal">
        <h3>Aplicativo com o seu plano</h3>
        <ul class="benefit-list">
          <li>Plano alimentar sempre à mão, refeição por refeição</li>
          <li>Diário alimentar para registrar os seus pratos</li>
          <li>Cupons de desconto em <a href="/cupons/">marcas parceiras</a></li>
        </ul>
      </div>
      <div class="devices">{screens}</div>
    </div>
    <div class="benefit reverse">
      <div class="benefit-text reveal">
        <h3>Receitas e organização da rotina</h3>
        <p>Um e-book de receitas e um manual de organização e planejamento para ajudar a seguir o plano no dia a dia.</p>
      </div>
      <div class="devices two">{base}</div>
    </div>

    <div class="tier-head premium reveal"><span class="eyebrow">Exclusivos do acompanhamento completo</span><h3>Materiais para ir <em>além</em></h3><p>E-books personalizados de acordo com as suas dúvidas e planners para a organização semanal.</p></div>
    <div class="ebooks" data-lenis-prevent>{books}</div>
    <div class="planners">{planners}</div>
  </div>
</section>'''

# ---------------- Cupons ----------------
# Fonte: destaque "Cupons" do Instagram (prints enviados pelo Bruno em 16/11/2026).
# Validar com a Ingrid: se os códigos seguem ativos e a declaração de parceria.
COUPONS = [
  {"brand": "Liv Up", "url": "https://www.livup.com.br/", "cat": "Marmitas congeladas", "desc": "Refeições prontas para as semanas mais corridas.",
   "codes": [("30% na 1ª compra", "ingrid.krichinak1"), ("10% nas demais compras", "ingrid.krichinak")]},
  {"brand": "Ocean Drop", "url": "https://www.oceandrop.com.br/", "cat": "Eletrólitos e suplementos", "desc": "Hidratação e reposição de eletrólitos.",
   "codes": [("20% de desconto", "INGRIDK")]},
  {"brand": "Dobro", "url": "https://www.soudobro.com.br/", "cat": "Géis de carboidrato", "desc": "Carboidrato para treinos longos, provas e intra-treino.",
   "codes": [("Desconto na loja Dobro", "DOBROINGRIDK")]},
  {"brand": "DUX Nutrition", "url": "https://www.duxnutrition.com/", "cat": "Whey e suplementos", "desc": "Proteína e suplementação esportiva.",
   "codes": [("Desconto na loja DUX", "PACINGRIDFARIA")]},
]

# ---------------- Templates ----------------
NAV_ITEMS = [("/#sobre","Sobre"),("/#atendimento","Atendimento"),("/#metodo","Método"),("/#formatos","Planos"),("/cupons/","Cupons"),("/#contato","Contato")]

def head(title, desc, path, extra_ld=None, preload_img=None):
    url = SITE + path
    robots = '<meta name="robots" content="noindex, follow">' if NOINDEX else '<meta name="robots" content="index, follow, max-image-preview:large">'
    ld = [org_ld(), website_ld()] + (extra_ld or [])
    lds = "\n".join(f'<script type="application/ld+json">{json.dumps(x, ensure_ascii=False)}</script>' for x in ld)
    pre = ""
    if preload_img:
        pre = (f'<link rel="preload" as="image" href="{preload_img[0]}" media="(min-width:601px)" fetchpriority="high">'
               f'<link rel="preload" as="image" href="{preload_img[1]}" media="(max-width:600px)" fetchpriority="high">')
    return f'''<!doctype html>
<html lang="pt-BR">
<head>
<meta charset="utf-8">
<meta name="viewport" content="width=device-width, initial-scale=1, viewport-fit=cover">
<title>{html.escape(title)}</title>
<meta name="description" content="{html.escape(desc)}">
{robots}
<link rel="canonical" href="{url}">
<meta name="theme-color" content="#ebe6df">
<link rel="icon" href="/assets/favicon.svg" type="image/svg+xml">
<link rel="icon" href="/assets/favicon-32.png" sizes="32x32" type="image/png">
<link rel="apple-touch-icon" href="/assets/apple-touch-icon.png">
<meta property="og:type" content="website">
<meta property="og:locale" content="pt_BR">
<meta property="og:site_name" content="{NAME} Nutricionista">
<meta property="og:title" content="{html.escape(title)}">
<meta property="og:description" content="{html.escape(desc)}">
<meta property="og:url" content="{url}">
<meta property="og:image" content="{SITE}/assets/img/og.jpg">
<meta property="og:image:width" content="1200">
<meta property="og:image:height" content="630">
<meta property="og:image:alt" content="Ingrid Krichinak, nutricionista">
<meta name="twitter:card" content="summary_large_image">
<meta name="twitter:title" content="{html.escape(title)}">
<meta name="twitter:description" content="{html.escape(desc)}">
<meta name="twitter:image" content="{SITE}/assets/img/og.jpg">
<link rel="preload" href="/assets/fonts/cormorant-400.woff2" as="font" type="font/woff2" crossorigin>
<link rel="preload" href="/assets/fonts/manrope-400.woff2" as="font" type="font/woff2" crossorigin>
{pre}
<link rel="stylesheet" href="/assets/site.css?v={VER}">
<script src="/assets/vendor/lenis.min.js" defer></script>
<script src="/assets/site.js?v={VER}" defer></script>
{lds}
</head>
<body>
<a class="skip" href="#conteudo">Pular para o conteúdo</a>
'''

def nav():
    links = "".join(f'<li><a href="{h}">{t}</a></li>' for h, t in NAV_ITEMS)
    return f'''<header class="nav">
  <div class="container nav-in">
    <a class="brand" href="/" aria-label="Ingrid Krichinak, página inicial">{LOGO}<span>Ingrid Krichinak<br>Nutricionista</span></a>
    <nav class="nav-panel" id="menu" aria-label="Principal">
      <ul class="nav-links">{links}</ul>
      <a class="btn btn-primary nav-cta" href="{wa('Olá, Ingrid! Vim pelo site e quero agendar uma consulta.')}" target="_blank" rel="noopener" data-cta="nav">Agendar consulta</a>
    </nav>
    <button class="menu-btn" type="button" aria-label="Abrir menu" aria-controls="menu" aria-expanded="false"><span></span><span></span><span></span></button>
  </div>
</header>
'''

def footer(wa_msg="Olá, Ingrid! Vim pelo site e quero falar com você."):
    serv = "".join(f'<li><a href="/{s["slug"]}/">{s["nav"]}</a></li>' for s in SERVICES)
    crn = f" · {CRN}" if CRN else ""
    addr = (f'{ADDRESS["building"]} · {ADDRESS["street"]}<br>{ADDRESS["district"]}, Santos/SP · {ADDRESS["zip"]}' if ADDRESS else "Santos/SP e atendimento online")
    return f'''<footer class="footer">
  <div class="container">
    <div class="footer-grid">
      <div>
        <a class="brand" href="/" aria-label="Ingrid Krichinak, página inicial">{LOGO}<span>Ingrid Krichinak<br>Nutricionista{crn}</span></a>
        <p>Nutrição para emagrecimento, hipertrofia e performance, com um plano que cabe na vida real.</p>
      </div>
      <div>
        <h3>Atendimento</h3>
        <ul>{serv}</ul>
      </div>
      <div>
        <h3>Contato</h3>
        <ul>
          <li><a href="{wa(wa_msg)}" target="_blank" rel="noopener" data-cta="footer">WhatsApp {WA_DISPLAY}</a></li>
          <li><a href="{IG}" target="_blank" rel="noopener">Instagram @ingridkrichinak</a></li>
          <li>{addr}</li>
          <li><a href="/cupons/">Cupons de parceiros</a></li>
          <li><a href="/politica-de-privacidade/">Política de privacidade</a></li>
        </ul>
      </div>
    </div>
    <div class="footer-bottom">
      <span>© {datetime.date.today().year} {NAME} · Nutricionista{crn}</span>
      <span>Site por <a href="https://www.instagram.com/cproject.dev/" target="_blank" rel="noopener">CProject Lab</a></span>
    </div>
  </div>
</footer>
<a class="wa-float" href="{wa(wa_msg)}" target="_blank" rel="noopener" aria-label="Conversar com a Ingrid no WhatsApp" data-cta="float">{ICON_WA}</a>
<div class="cookie" role="dialog" aria-live="polite" aria-label="Aviso de cookies">
  <p>Cookies de medição só com a sua permissão. <a href="/politica-de-privacidade/">Privacidade</a>.</p>
  <div class="btns"><button class="btn btn-ghost" type="button" data-consent="no">Recusar</button><button class="btn btn-primary" type="button" data-consent="yes">Aceitar</button></div>
</div>
</body>
</html>
'''

def org_ld():
    o = {
      "@context": "https://schema.org",
      "@type": ["MedicalBusiness", "LocalBusiness"],
      "@id": SITE + "/#negocio",
      "name": f"{NAME} Nutricionista",
      "description": "Nutricionista em Santos e online: emagrecimento, hipertrofia, nutrição esportiva e acompanhamento em casal.",
      "url": SITE + "/",
      "image": SITE + "/assets/img/og.jpg",
      "logo": SITE + "/assets/apple-touch-icon.png",
      "telephone": "+55-13-99777-1672",
      "medicalSpecialty": "Nutrition",
      "areaServed": [{"@type": "City", "name": "Santos"}, {"@type": "Country", "name": "Brasil"}],
      "address": {"@type": "PostalAddress", "addressLocality": "Santos", "addressRegion": "SP", "addressCountry": "BR"},
      "sameAs": [IG],
      "founder": {"@type": "Person", "name": NAME, "jobTitle": "Nutricionista"},
    }
    if ADDRESS:
        o["address"].update({"streetAddress": f'{ADDRESS["street"]} - {ADDRESS["building"]}', "postalCode": ADDRESS["zip"]})
        o["hasMap"] = MAPS_LINK
    return o

def website_ld():
    return {"@context": "https://schema.org", "@type": "WebSite", "@id": SITE + "/#site", "url": SITE + "/", "name": f"{NAME} Nutricionista", "inLanguage": "pt-BR"}

def faq_ld(items):
    return {"@context": "https://schema.org", "@type": "FAQPage", "mainEntity": [
        {"@type": "Question", "name": q, "acceptedAnswer": {"@type": "Answer", "text": a}} for q, a in items]}

def faq_html(items):
    return "".join(f'<details><summary>{html.escape(q)}</summary><p>{html.escape(a)}</p></details>' for q, a in items)

# ---------------- Home ----------------
def build_home():
    cards = "".join(f'''<a class="card reveal" href="/{s["slug"]}/"><span class="num">0{i+1}</span><h3>{s["nav"]}</h3><p>{s["card"]}</p><span class="link-arrow">Saiba mais</span></a>''' for i, s in enumerate(SERVICES))
    h = head("Ingrid Krichinak | Nutricionista em Santos e online",
             "Nutricionista em Santos e online para emagrecimento, hipertrofia e nutrição esportiva. Plano que cabe na sua rotina e suporte contínuo no WhatsApp.",
             "/", [faq_ld(HOME_FAQ)], ("/assets/img/ingrid-blazer-960.webp", "/assets/img/ingrid-blazer-600.webp"))
    body = f'''{nav()}
<main id="conteudo">
<section class="hero" aria-labelledby="hero-t">
  <div class="hero-bg" aria-hidden="true"><span class="blob b1" data-depth="1.2"></span><span class="blob b2" data-depth="-0.8"></span><span class="blob b3" data-depth="1.6"></span></div>
  <div class="container hero-grid">
    <div>
      <span class="eyebrow">Nutricionista · Santos e online</span>
      <h1 id="hero-t">Nutricionista em Santos para uma performance que cabe na <em>vida real</em></h1>
      <p class="lead">Emagrecimento, hipertrofia e nutrição esportiva com plano individual e suporte contínuo no WhatsApp.</p>
      <div class="hero-ctas">
        <a class="btn btn-primary" href="{wa('Olá, Ingrid! Vim pelo site e quero agendar uma consulta.')}" target="_blank" rel="noopener" data-cta="hero">{ICON_WA}Agendar pelo WhatsApp</a>
        <a class="btn btn-ghost" href="#metodo">Conhecer o método</a>
      </div>
    </div>
    <div class="hero-photo" data-depth="0.35">
      <span class="ring" aria-hidden="true" data-depth="1.4"></span>
      <div class="frame">
        <picture>
          <source media="(max-width:600px)" srcset="/assets/img/ingrid-blazer-600.webp">
          <img src="/assets/img/ingrid-blazer-960.webp" width="960" height="1200" alt="Retrato da nutricionista Ingrid Krichinak, de blazer preto, com a mão apoiada no queixo" fetchpriority="high" decoding="async">
        </picture>
      </div>
      <div class="badge" data-depth="0.9"><div><strong>Método PR</strong><span>Plano individual, suporte contínuo e ajustes antes da consulta</span></div></div>
    </div>
  </div>
</section>

<section class="proof" aria-label="Destaques">
  <div class="container">
    <ul>
      <li><span class="dot"></span><div><b>Presencial e online</b>Consultório em Santos e atendimento para qualquer lugar.</div></li>
      <li><span class="dot"></span><div><b>Suporte no WhatsApp</b>Dúvidas e ajustes entre as consultas.</div></li>
      <li><span class="dot"></span><div><b>Esporte de competição</b>Nutricionista da equipe de ginástica rítmica da AABB.</div></li>
      <li><span class="dot"></span><div><b>Vive o que orienta</b>10 anos de musculação e 3 de CrossFit na rotina.</div></li>
    </ul>
  </div>
</section>

<section class="section about has-orbs" id="sobre" aria-labelledby="sobre-t">
  {ORBS_C}
  <div class="container about-grid">
    <div class="about-photo reveal" data-depth="0.25">
      <picture>
        <source media="(max-width:600px)" srcset="/assets/img/ingrid-sorriso-520.webp">
        <img src="/assets/img/ingrid-sorriso-800.webp" width="800" height="1000" alt="Ingrid Krichinak sorrindo, de colete preto, em fundo claro" loading="lazy" decoding="async">
      </picture>
    </div>
    <div class="reveal">
      <span class="eyebrow">Sobre</span>
      <h2 id="sobre-t">Ingrid <em>Krichinak</em></h2>
      <p class="lead">Nutricionista com foco em emagrecimento, pós-graduada em Nutrição, Fisiologia e Metabolismo no Esporte. Atendo em Santos e online.</p>
      <p><strong>Minha missão é otimizar a rotina dos meus pacientes.</strong> Com os dias cada vez mais corridos, a gente precisa saber fazer escolhas práticas, gostosas e saudáveis, sem deixar de comer o que gosta. A abordagem respeita o contexto e os hábitos de cada pessoa, porque eu prezo por um estilo de vida sustentável.</p>
      <p>Treino há 10 anos de musculação e 3 de CrossFit, e sei na prática que nunca existiu um mês perfeito. Teve fase de muito resultado, fase de manutenção, semana de treino reduzido e dia em que a alimentação saiu do planejado. É por isso que o meu trabalho não é sobre perfeição, é sobre construir um jeito de comer que você consiga sustentar.</p>
      <p>Hoje também sou nutricionista da equipe de ginástica rítmica de competição da AABB e sigo estudando para levar aos meus pacientes estratégias atualizadas e baseadas em evidência.</p>
      <div class="facts">
        <div class="fact stat reveal"><strong><em>+</em><b data-count="500">500</b></strong><small>pacientes atendidos</small><span>Praticantes de atividade física, corredores, crossfit, musculação, atletas e quem busca mais qualidade de vida.</span></div>
        <div class="fact stat reveal"><strong><em>+</em><b data-count="8">8</b></strong><small>países</small><span>Atendimento online para quem mora fora, adaptado à rotina e à cultura de cada lugar.</span></div>
      </div>
    </div>
  </div>
</section>

<section class="section has-orbs" id="atendimento" aria-labelledby="areas-t">
  {ORBS_A}
  <div class="container">
    <div class="areas-head">
      <div><span class="eyebrow">Áreas de atendimento</span><h2 id="areas-t">Um plano para o seu <em>objetivo</em></h2></div>
      <p class="lead">Cada acompanhamento começa pela sua rotina: horários, preferências, treino e o que costuma tirar você do caminho.</p>
    </div>
    <div class="cards">{cards}</div>
  </div>
</section>

<section class="section method" id="metodo" aria-labelledby="metodo-t">
  <div class="container method-grid">
    <div class="reveal">
      <span class="eyebrow">Método PR</span>
      <h2 id="metodo-t">Não é só uma dieta. É aprender a fazer <em>escolhas</em> no dia a dia.</h2>
      <p class="lead">Sem terrorismo, sem extremismo e sem precisar abrir mão do que você gosta. Um processo construído com estratégia, constância e acompanhamento de perto.</p>
      <p class="quote">“O que faz diferença não é a perfeição. É voltar no dia seguinte.”</p>
    </div>
    <ol class="pillars reveal">
      <li><span class="n">01</span><div><h3>Plano que cabe na rotina</h3><p>Construído a partir dos seus horários, preferências e da sua realidade, inclusive para semanas corridas, viagens e fins de semana.</p></div></li>
      <li><span class="n">02</span><div><h3>Suporte contínuo no WhatsApp</h3><p>Imprevistos, dúvidas sobre suplementos e mudanças de rotina resolvidos na hora. Com os seus feedbacks, os ajustes acontecem antes da consulta.</p></div></li>
      <li><span class="n">03</span><div><h3>Materiais de apoio</h3><p>Conteúdos exclusivos para facilitar a organização da semana.</p>
        <div class="materials"><span>Passo a passo de marmitas</span><span>Receitas na airfryer</span><span>Trocas inteligentes em eventos</span><span>Guia de produtos e suplementos</span></div></div></li>
      <li><span class="n">04</span><div><h3>Ciência e atualização</h3><p>Estratégias baseadas em evidência e formação contínua em nutrição esportiva.</p></div></li>
    </ol>
  </div>
</section>

{depoimentos_section()}

<section class="section has-orbs" aria-labelledby="como-t">
  {ORBS_D}
  <div class="container">
    <span class="eyebrow">Como funciona</span>
    <h2 id="como-t">Do primeiro contato ao <em>acompanhamento</em></h2>
    <ol class="steps">
      <li class="reveal"><h3>Contato</h3><p>Você chama no WhatsApp e recebe as informações sobre formatos, valores e horários.</p></li>
      <li class="reveal"><h3>Consulta</h3><p>Avaliação da sua rotina, histórico, objetivo, treino e preferências alimentares.</p></li>
      <li class="reveal"><h3>Plano</h3><p>Plano alimentar individual e materiais de apoio para organizar a semana.</p></li>
      <li class="reveal"><h3>Ajustes</h3><p>Suporte pelo WhatsApp e retornos para ajustar a estratégia sempre que for preciso.</p></li>
    </ol>
  </div>
</section>

<section class="section has-orbs" id="formatos" aria-labelledby="formatos-t">
  {ORBS_B}
  <div class="container">
    <div class="center">
      <span class="eyebrow">Formatos de acompanhamento</span>
      <h2 id="formatos-t">Escolha como você quer ser <em>acompanhado</em></h2>
      <p class="lead">Valores e horários são enviados no primeiro contato pelo WhatsApp.</p>
    </div>
    <div class="plans">
      <div class="plan reveal">
        <span class="tag">Online</span>
        <h3>Consultoria online</h3>
        <p>Para quem já segue um plano, não precisa de consulta mensal e quer ajustes e respostas pontuais.</p>
        <ul><li>Plano alimentar individual</li><li>Suporte contínuo no WhatsApp</li><li>Dúvidas sobre suplementos e alterações</li><li><a class="plan-link" href="#materiais">App com plano, diário e cupons</a></li></ul>
        <a class="btn btn-ghost" href="{wa('Olá, Ingrid! Vim pelo site e quero saber sobre a consultoria online.')}" target="_blank" rel="noopener" data-cta="plano-online">Quero saber mais</a>
      </div>
      <div class="plan feature reveal">
        <span class="tag">Mais completo</span>
        <h3>Acompanhamento completo</h3>
        <p>Consultas, plano individual e todo o suporte para mudar a rotina com segurança. Presencial em Santos ou online.</p>
        <ul><li>Consultas de avaliação e retorno</li><li>Plano alimentar individual</li><li>Suporte contínuo no WhatsApp</li><li><a class="plan-link" href="#materiais">Materiais exclusivos de apoio</a></li></ul>
        <a class="btn btn-light" href="{wa('Olá, Ingrid! Vim pelo site e quero saber sobre o acompanhamento completo.')}" target="_blank" rel="noopener" data-cta="plano-completo">Quero saber mais</a>
      </div>
      <div class="plan reveal">
        <span class="tag">Depois do objetivo</span>
        <h3>Plano de manutenção</h3>
        <p>Para quem já chegou lá e quer manter o resultado com mais flexibilidade e autonomia.</p>
        <ul><li>Consultas mais espaçadas</li><li>Ajustes de estratégia e suplementação</li><li>Suporte para realinhar a rota</li></ul>
        <a class="btn btn-ghost" href="{wa('Olá, Ingrid! Vim pelo site e quero saber sobre o plano de manutenção.')}" target="_blank" rel="noopener" data-cta="plano-manutencao">Quero saber mais</a>
      </div>
    </div>
  </div>
</section>

{materiais_section()}

<section class="section faq has-orbs" id="duvidas" aria-labelledby="faq-t">
  {ORBS_A}
  <div class="container faq-grid">
    <div><span class="eyebrow">Dúvidas frequentes</span><h2 id="faq-t">Antes de <em>agendar</em></h2><p class="lead">Não encontrou o que procura? Fale direto com a Ingrid pelo WhatsApp.</p></div>
    <div class="faq-panel reveal">{faq_html(HOME_FAQ)}</div>
  </div>
</section>

{contact_section()}
</main>
'''
    write("index.html", h + body + footer())

def contact_section():
    opts = "".join(f"<option>{s['nav']}</option>" for s in SERVICES)
    return f'''<section class="section contact" id="contato" aria-labelledby="contato-t">
  <div class="container contact-grid">
    <div>
      <span class="eyebrow">Contato</span>
      <h2 id="contato-t">Vamos montar um plano que cabe na <em>sua rotina</em>?</h2>
      <p class="lead">Preencha o formulário e a mensagem abre pronta no WhatsApp. Se preferir, chame direto.</p>
      <ul class="contact-list">
        <li><a href="{wa('Olá, Ingrid! Vim pelo site e quero agendar uma consulta.')}" target="_blank" rel="noopener" data-cta="contato">{ICON_WA}WhatsApp {WA_DISPLAY}</a></li>
        <li><a href="{IG}" target="_blank" rel="noopener">{ICON_IG}@ingridkrichinak</a></li>
        <li><a href="{MAPS_LINK}" target="_blank" rel="noopener">{ICON_PIN}<span class="addr">{ADDRESS["building"]} · {ADDRESS["street"]}<br>{ADDRESS["district"]}, Santos/SP · {ADDRESS["zip"]}</span></a></li>
        <li><div>{ICON_GLOBE}Atendimento online para qualquer cidade</div></li>
      </ul>
      <div class="map">
        <div class="map-facade"><div><p>Edifício Manhattan · R. São Paulo, 41 · Santos/SP</p><button class="btn btn-light" type="button" data-map="{MAPS_EMBED}">Ver no mapa</button></div></div>
      </div>
    </div>
    <form class="form" id="form-contato" novalidate>
      <div class="row">
        <div class="field"><label for="f-nome">Nome</label><input id="f-nome" name="nome" type="text" autocomplete="name" required><span class="err" aria-live="polite"></span></div>
        <div class="field"><label for="f-tel">WhatsApp com DDD</label><input id="f-tel" name="telefone" type="tel" inputmode="tel" autocomplete="tel" required><span class="err" aria-live="polite"></span></div>
      </div>
      <div class="row">
        <div class="field"><label for="f-obj">Objetivo</label><select id="f-obj" name="objetivo" required><option value="">Selecione</option>{opts}<option>Manutenção</option><option>Outro</option></select><span class="err" aria-live="polite"></span></div>
        <div class="field"><label for="f-mod">Atendimento</label><select id="f-mod" name="modalidade"><option>Presencial em Santos</option><option>Online</option><option>Ainda não sei</option></select></div>
      </div>
      <div class="field"><label for="f-msg">Mensagem (opcional)</label><textarea id="f-msg" name="mensagem" rows="3"></textarea></div>
      <div class="hp" aria-hidden="true"><label for="f-emp">Empresa</label><input id="f-emp" name="empresa" type="text" tabindex="-1" autocomplete="off"></div>
      <button class="btn btn-light" type="submit">{ICON_WA}Enviar pelo WhatsApp</button>
      <p class="form-status" role="status"></p>
      <p class="form-note">Seus dados vão direto para o WhatsApp da Ingrid e não ficam armazenados no site. Veja a <a href="/politica-de-privacidade/">política de privacidade</a>.</p>
    </form>
  </div>
</section>'''

# ---------------- Serviços ----------------
def build_service(s):
    path = f"/{s['slug']}/"
    crumbs_ld = {"@context": "https://schema.org", "@type": "BreadcrumbList", "itemListElement": [
        {"@type": "ListItem", "position": 1, "name": "Início", "item": SITE + "/"},
        {"@type": "ListItem", "position": 2, "name": s["nav"], "item": SITE + path}]}
    svc_ld = {"@context": "https://schema.org", "@type": "Service", "name": s["h1"], "serviceType": s["nav"],
              "description": s["meta"], "url": SITE + path, "provider": {"@id": SITE + "/#negocio"},
              "areaServed": [{"@type": "City", "name": "Santos"}, {"@type": "Country", "name": "Brasil"}]}
    h = head(s["title"], s["meta"], path, [svc_ld, crumbs_ld, faq_ld(s["faq"])])
    sections = ""
    for t, ps in s["body"]:
        sections += f"<h2>{t}</h2>" + "".join(f"<p>{p}</p>" for p in ps)
    related = "".join(f'''<a class="card reveal" href="/{o["slug"]}/"><h3>{o["nav"]}</h3><p>{o["card"]}</p><span class="link-arrow">Saiba mais</span></a>''' for o in SERVICES if o is not s)
    body = f'''{nav()}
<main id="conteudo">
<section class="page-hero">
  <div class="container">
    <nav class="crumbs" aria-label="Você está em"><a href="/">Início</a><span>/</span>{s["nav"]}</nav>
    <span class="eyebrow">Nutricionista · Santos e online</span>
    <h1>{s["h1"]}</h1>
    <p class="lead">{s["lead"]}</p>
  </div>
</section>
<section class="section has-orbs">
  {ORBS_B}
  <div class="container split">
    <article class="prose">{sections}
      <h2>Perguntas frequentes</h2>
      <div class="faq" style="background:none"><div class="faq-panel">{faq_html(s["faq"])}</div></div>
    </article>
    <aside class="aside">
      <img src="/assets/img/ingrid-oculos-520.webp" width="520" height="650" alt="Ingrid Krichinak de óculos, sentada em um sofá claro com livros de nutrição ao lado" loading="lazy" decoding="async">
      <h2>Fale com a Ingrid</h2>
      <p>Atendimento presencial em Santos e online, com suporte contínuo pelo WhatsApp entre as consultas.</p>
      <a class="btn btn-primary" href="{wa(s["wa"])}" target="_blank" rel="noopener" data-cta="servico">{ICON_WA}Conversar no WhatsApp</a>
      <p style="margin:18px 0 0;font-size:.88rem"><a class="link-arrow" href="/#metodo">Conheça o Método PR</a></p>
    </aside>
  </div>
</section>
<section class="section has-orbs" style="background:var(--stone)">
  {ORBS_C}
  <div class="container">
    <span class="eyebrow">Outras áreas</span>
    <h2>Veja também</h2>
    <div class="related">{related}</div>
  </div>
</section>
{contact_section()}
</main>
'''
    write(f"{s['slug']}/index.html", h + body + footer(s["wa"]))

ICON_COPY = '<svg viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="1.6" aria-hidden="true"><rect x="9" y="9" width="11" height="11" rx="2.5"/><path d="M15 9V6.5A2.5 2.5 0 0 0 12.5 4h-6A2.5 2.5 0 0 0 4 6.5v6A2.5 2.5 0 0 0 6.5 15H9"/></svg>'

def build_coupons():
    path = "/cupons/"
    crumbs_ld = {"@context": "https://schema.org", "@type": "BreadcrumbList", "itemListElement": [
        {"@type": "ListItem", "position": 1, "name": "Início", "item": SITE + "/"},
        {"@type": "ListItem", "position": 2, "name": "Cupons", "item": SITE + path}]}
    h = head("Cupons de parceiros | Ingrid Krichinak Nutricionista",
             "Cupons de desconto de marcas parceiras da nutricionista Ingrid Krichinak: marmitas, eletrólitos, géis de carboidrato e suplementos.",
             path, [crumbs_ld])
    cards = ""
    for i, c in enumerate(COUPONS):
        codes = "".join(f'''<div class="code-row"><span class="code-label">{html.escape(lbl)}</span>
          <button class="code" type="button" data-copy="{html.escape(code)}" aria-label="Copiar cupom {html.escape(code)}"><span>{html.escape(code)}</span>{ICON_COPY}<em aria-hidden="true">Copiado</em></button></div>''' for lbl, code in c["codes"])
        cards += f'''<article class="card coupon reveal"><span class="num">0{i+1}</span><span class="coupon-cat">{html.escape(c["cat"])}</span>
        <h3>{html.escape(c["brand"])}</h3><p>{html.escape(c["desc"])}</p>{codes}
        <a class="link-arrow coupon-link" href="{c["url"]}" target="_blank" rel="noopener sponsored" data-cta="cupom-loja">Ir para a loja {html.escape(c["brand"])}</a></article>'''
    body = f'''{nav()}
<main id="conteudo">
<section class="page-hero coupons-hero">
  <div class="container">
    <span class="eyebrow">Parcerias</span>
    <h1>Cupons de <em>parceiros</em></h1>
    <p class="lead">Marcas que fazem parte da rotina da Ingrid. Toque no código para copiar.</p>
    <ul class="coupon-brands" aria-label="Marcas parceiras">{"".join(f"<li>{html.escape(c['brand'])}</li>" for c in COUPONS)}</ul>
  </div>
</section>
<section class="section has-orbs coupons-section">
  {ORBS_B}
  <div class="container">
    <div class="coupons">{cards}</div>
    <p class="coupons-cta reveal"><a class="link-arrow" href="{wa("Olá, Ingrid! Vim pela página de cupons e quero saber mais sobre o acompanhamento.")}" target="_blank" rel="noopener" data-cta="cupons">Quero um plano feito para mim</a></p>
  </div>
</section>
</main>
'''
    write("cupons/index.html", h + body + footer("Olá, Ingrid! Vim pela página de cupons do site."))

def build_privacy():
    path = "/politica-de-privacidade/"
    h = head("Política de privacidade | Ingrid Krichinak", "Como o site da nutricionista Ingrid Krichinak trata dados pessoais, cookies e contatos pelo WhatsApp, conforme a LGPD.", path)
    body = f'''{nav()}
<main id="conteudo">
<section class="page-hero"><div class="container"><nav class="crumbs" aria-label="Você está em"><a href="/">Início</a><span>/</span>Política de privacidade</nav><h1>Política de privacidade</h1><p class="lead">Atualizada em {datetime.date.today().strftime("%d/%m/%Y")}.</p></div></section>
<section class="section"><div class="container prose legal">
<p>Este site pertence a {NAME}, nutricionista{(" (" + CRN + ")") if CRN else ""}, com atendimento em Santos/SP e online. Esta política explica quais dados são tratados quando você navega por aqui e como você pode exercer seus direitos previstos na Lei Geral de Proteção de Dados (Lei 13.709/2018).</p>
<h2>Dados que você envia</h2>
<p>O formulário de contato não armazena informações no site. Ao clicar em enviar, o seu navegador abre o WhatsApp com uma mensagem montada a partir do que você preencheu (nome, telefone, objetivo, formato de atendimento e mensagem). Os dados só são compartilhados se você enviar essa mensagem. A partir daí, a conversa segue as regras do WhatsApp (Meta).</p>
<p>Essas informações são usadas apenas para responder ao seu contato e, se você seguir com o atendimento, para a prestação do serviço de nutrição, com sigilo profissional.</p>
<h2>Cookies e medição de acesso</h2>
<p>O site pode usar ferramentas de medição de audiência, como o Google Analytics e o Google Tag Manager, somente se você aceitar no aviso de cookies. Se você recusar, nenhuma ferramenta de medição é carregada. Sua escolha fica salva no seu navegador e pode ser alterada limpando os dados do site.</p>
<h2>Serviços de terceiros</h2>
<ul>
<li>Vercel: hospedagem do site, que pode registrar dados técnicos de acesso (como endereço IP) para segurança e funcionamento.</li>
<li>WhatsApp (Meta): canal de atendimento, quando você opta por enviar uma mensagem.</li>
<li>Instagram (Meta): quando você acessa o perfil pelo link do site.</li>
<li>Google (Analytics/Tag Manager): somente após o seu consentimento.</li>
</ul>
<h2>Seus direitos</h2>
<p>Você pode pedir a confirmação, o acesso, a correção ou a exclusão dos seus dados, além de revogar consentimentos, pelo WhatsApp {WA_DISPLAY}.</p>
<h2>Alterações</h2>
<p>Esta política pode ser atualizada. A data no topo da página indica a versão mais recente.</p>
</div></section>
</main>
'''
    write("politica-de-privacidade/index.html", h + body + footer())

def build_404():
    h = head("Página não encontrada | Ingrid Krichinak", "A página que você procurou não existe.", "/404")
    h = h.replace('<meta name="robots" content="index, follow, max-image-preview:large">', '<meta name="robots" content="noindex">')
    body = f'''{nav()}
<main id="conteudo">
<section class="page-hero" style="min-height:70vh;display:flex;align-items:center"><div class="container">
<span class="eyebrow">Erro 404</span><h1>Essa página não está no <em>cardápio</em></h1>
<p class="lead">O endereço pode ter mudado. Volte para o início ou fale com a Ingrid pelo WhatsApp.</p>
<div class="hero-ctas" style="display:flex;gap:14px;flex-wrap:wrap;margin-top:28px"><a class="btn btn-primary" href="/">Ir para o início</a><a class="btn btn-ghost" href="{wa('Olá, Ingrid! Vim pelo site.')}" target="_blank" rel="noopener">Falar no WhatsApp</a></div>
</div></section>
</main>
'''
    write("404.html", h + body + footer())

def build_meta_files():
    pages = ["/"] + [f"/{s['slug']}/" for s in SERVICES] + ["/cupons/", "/politica-de-privacidade/"]
    sm = '<?xml version="1.0" encoding="UTF-8"?>\n<urlset xmlns="http://www.sitemaps.org/schemas/sitemap/0.9">\n'
    for p in pages:
        sm += f"  <url><loc>{SITE}{p}</loc><lastmod>{TODAY}</lastmod></url>\n"
    sm += "</urlset>\n"
    write("sitemap.xml", sm)
    write("robots.txt", f"User-agent: *\nAllow: /\n\nSitemap: {SITE}/sitemap.xml\n")

def write(rel, content):
    p = os.path.join(ROOT, rel)
    os.makedirs(os.path.dirname(p), exist_ok=True)
    with open(p, "w", encoding="utf-8") as f:
        f.write(content)

VER = datetime.datetime.now().strftime("%Y%m%d%H%M")

if __name__ == "__main__":
    build_home()
    for s in SERVICES:
        build_service(s)
    build_coupons()
    build_privacy()
    build_404()
    build_meta_files()
    print("ok", "noindex" if NOINDEX else "index")
