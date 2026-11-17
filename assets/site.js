(function(){
  "use strict";
  var WA = "5513997771672";
  var d = document, b = d.body;
  d.documentElement.classList.add("js");
  var REDUCED = window.matchMedia("(prefers-reduced-motion: reduce)").matches;
  var FINE = window.matchMedia("(hover: hover) and (pointer: fine)").matches;
  window.dataLayer = window.dataLayer || [];
  window.gtag = window.gtag || function(){ window.dataLayer.push(arguments); };
  window.gtag("consent","default",{analytics_storage:"denied",ad_storage:"denied",ad_user_data:"denied",ad_personalization:"denied",wait_for_update:500});
  // Medição: preencher GTM_ID para ativar (carrega somente após consentimento)
  var GTM_ID = "";
  window.IK_LOAD_TAGS = function(){
    if(!GTM_ID || window.__ikTags) return; window.__ikTags = true;
    window.dataLayer.push({"gtm.start":Date.now(),event:"gtm.js"});
    var s = d.createElement("script"); s.async = true; s.src = "https://www.googletagmanager.com/gtm.js?id=" + GTM_ID; d.head.appendChild(s);
  };

  // Nav scrolled + mobile menu
  var nav = d.querySelector(".nav");
  var onScroll = function(){ if(nav) nav.classList.toggle("scrolled", window.scrollY > 8); };
  onScroll(); window.addEventListener("scroll", onScroll, {passive:true});
  var mb = d.querySelector(".menu-btn");
  if(mb){
    mb.addEventListener("click", function(){
      var open = b.classList.toggle("menu-open");
      mb.setAttribute("aria-expanded", open ? "true" : "false");
    });
    d.querySelectorAll(".nav-panel a").forEach(function(a){
      a.addEventListener("click", function(){ b.classList.remove("menu-open"); mb.setAttribute("aria-expanded","false"); });
    });
  }

  // WhatsApp click tracking
  d.addEventListener("click", function(e){
    var a = e.target.closest && e.target.closest("a[href*='wa.me']");
    if(a){ window.dataLayer.push({event:"whatsapp_click", page:location.pathname, cta:a.getAttribute("data-cta")||"link"}); }
  });

  // Smooth scroll (Lenis)
  var lenis = null;
  if(!REDUCED && window.Lenis){
    lenis = new window.Lenis({duration:1.15, easing:function(t){return Math.min(1, 1.001 - Math.pow(2, -10 * t));}, anchors:{offset:-80}, smoothWheel:true});
  }

  // Reveal on scroll, com escalonamento entre irmãos
  var rv = d.querySelectorAll(".reveal");
  rv.forEach(function(el){
    var sib = Array.prototype.filter.call(el.parentNode.children, function(c){ return c.classList.contains("reveal"); });
    var i = sib.indexOf(el);
    if(i > 0) el.style.setProperty("--d", (i * 0.09) + "s");
    el.addEventListener("transitionend", function te(e){ if(e.propertyName === "opacity"){ el.classList.add("done"); el.removeEventListener("transitionend", te); } });
  });
  if("IntersectionObserver" in window && !REDUCED){
    var io = new IntersectionObserver(function(es){
      es.forEach(function(en){ if(en.isIntersecting){ en.target.classList.add("in"); io.unobserve(en.target); } });
    }, {rootMargin:"0px 0px -8% 0px"});
    rv.forEach(function(el){ io.observe(el); });
  } else { rv.forEach(function(el){ el.classList.add("in","done"); }); }

  // Profundidade: parallax por scroll e por mouse
  var depthEls = Array.prototype.slice.call(d.querySelectorAll("[data-depth]"));
  var hero = d.querySelector(".hero");
  var mx = 0, my = 0, cmx = 0, cmy = 0, heroVisible = true;
  if(hero && "IntersectionObserver" in window){
    new IntersectionObserver(function(es){ heroVisible = es[0].isIntersecting; hero.classList.toggle("paused", !heroVisible); }).observe(hero);
  }
  if(FINE && hero){
    hero.addEventListener("pointermove", function(e){
      var r = hero.getBoundingClientRect();
      mx = (e.clientX - r.left) / r.width - .5; my = (e.clientY - r.top) / r.height - .5;
    });
    hero.addEventListener("pointerleave", function(){ mx = 0; my = 0; });
  }
  var vh = window.innerHeight;
  window.addEventListener("resize", function(){ vh = window.innerHeight; });
  function frame(t){
    if(lenis) lenis.raf(t);
    if(!REDUCED){
      cmx += (mx - cmx) * .07; cmy += (my - cmy) * .07;
      for(var i = 0; i < depthEls.length; i++){
        var el = depthEls[i], k = parseFloat(el.getAttribute("data-depth")) || 0;
        var r = el.getBoundingClientRect();
        if(r.bottom < -200 || r.top > vh + 200) continue;
        var center = r.top + r.height / 2 - vh / 2;
        var y = -center * k * .25;
        var inHero = el.closest(".hero");
        var x = inHero ? cmx * k * 60 : 0;
        if(inHero) y += cmy * k * 40;
        el.style.translate = x.toFixed(1) + "px " + y.toFixed(1) + "px";
      }
    }
    requestAnimationFrame(frame);
  }
  requestAnimationFrame(frame);

  // Cards: inclinação 3D + brilho seguindo o cursor
  d.querySelectorAll(".card, .plan, .fact, .steps li").forEach(function(c){
    var g = d.createElement("span"); g.className = "glare"; g.setAttribute("aria-hidden","true"); c.appendChild(g);
    if(!FINE || REDUCED) return;
    c.addEventListener("pointermove", function(e){
      var r = c.getBoundingClientRect();
      var px = (e.clientX - r.left) / r.width, py = (e.clientY - r.top) / r.height;
      c.style.setProperty("--mx", (px * 100) + "%"); c.style.setProperty("--my", (py * 100) + "%");
      c.style.setProperty("--ry", ((px - .5) * 5).toFixed(2) + "deg");
      c.style.setProperty("--rx", ((.5 - py) * 5).toFixed(2) + "deg");
    });
    c.addEventListener("pointerleave", function(){ c.style.setProperty("--rx","0deg"); c.style.setProperty("--ry","0deg"); });
  });

  // Botões magnéticos
  if(FINE && !REDUCED){
    d.querySelectorAll(".btn, .wa-float").forEach(function(btn){
      btn.addEventListener("pointermove", function(e){
        var r = btn.getBoundingClientRect();
        btn.style.translate = ((e.clientX - r.left - r.width/2) * .18).toFixed(1) + "px " + ((e.clientY - r.top - r.height/2) * .25).toFixed(1) + "px";
      });
      btn.addEventListener("pointerleave", function(){ btn.style.translate = "0 0"; });
    });
  }

  // Mapa sob demanda (não pesa no carregamento)
  var mapBtn = d.querySelector("[data-map]");
  if(mapBtn){
    mapBtn.addEventListener("click", function(){
      var box = mapBtn.closest(".map");
      var f = d.createElement("iframe");
      f.src = mapBtn.getAttribute("data-map"); f.title = "Mapa do consultório"; f.loading = "lazy"; f.referrerPolicy = "no-referrer-when-downgrade";
      box.appendChild(f); box.querySelector(".map-facade").remove();
    });
  }

  // Form -> WhatsApp
  var f = d.getElementById("form-contato");
  if(f){
    f.addEventListener("submit", function(e){
      e.preventDefault();
      var st = f.querySelector(".form-status");
      if(f.querySelector("[name=empresa]").value){ return; } // honeypot
      var ok = true;
      f.querySelectorAll("[required]").forEach(function(el){
        var err = el.parentNode.querySelector(".err");
        var bad = !el.value.trim() || (el.type === "tel" && el.value.replace(/\D/g,"").length < 10);
        if(err) err.textContent = bad ? (el.type === "tel" ? "Informe um WhatsApp com DDD." : "Campo obrigatório.") : "";
        el.setAttribute("aria-invalid", bad ? "true" : "false");
        if(bad && ok){ el.focus(); ok = false; }
      });
      if(!ok){ st.className = "form-status bad"; st.textContent = "Confira os campos destacados."; return; }
      var v = function(n){ return (f.querySelector("[name="+n+"]").value || "").trim(); };
      var msg = "Olá, Ingrid! Vim pelo site.\n\n" +
        "Nome: " + v("nome") + "\n" +
        "WhatsApp: " + v("telefone") + "\n" +
        "Objetivo: " + v("objetivo") + "\n" +
        "Atendimento: " + v("modalidade") +
        (v("mensagem") ? "\n\n" + v("mensagem") : "");
      var url = "https://wa.me/" + WA + "?text=" + encodeURIComponent(msg);
      window.dataLayer.push({event:"form_submit", page:location.pathname, objetivo:v("objetivo")});
      var w = window.open(url, "_blank");
      if(w){ try { w.opener = null; } catch(err){} }
      st.className = "form-status ok";
      st.innerHTML = w ? "Pronto! Sua mensagem foi aberta no WhatsApp. É só enviar." :
        'Não conseguimos abrir o WhatsApp automaticamente. <a href="' + url + '" target="_blank" rel="noopener">Toque aqui para enviar</a>.';
    });
  }

  // Cookie consent (Consent Mode v2: default denied set inline in <head>)
  var ck = d.querySelector(".cookie");
  var KEY = "ik_consent";
  var get = function(){ try { return localStorage.getItem(KEY); } catch(e){ return null; } };
  var set = function(v){ try { localStorage.setItem(KEY, v); } catch(e){} };
  var apply = function(v){
    if(typeof window.gtag === "function"){
      window.gtag("consent","update",{analytics_storage:v==="granted"?"granted":"denied",ad_storage:v==="granted"?"granted":"denied",ad_user_data:v==="granted"?"granted":"denied",ad_personalization:v==="granted"?"granted":"denied"});
    }
    if(v === "granted" && window.IK_LOAD_TAGS) window.IK_LOAD_TAGS();
  };
  var hide = function(){ ck.classList.remove("show"); b.classList.remove("cookie-on"); };
  if(ck){
    var cur = get();
    if(cur){ apply(cur); }
    else {
      ck.classList.add("show"); b.classList.add("cookie-on");
      var setH = function(){ d.documentElement.style.setProperty("--cookie-h", ck.offsetHeight + 16 + "px"); };
      setH(); window.addEventListener("resize", setH);
    }
    ck.querySelector("[data-consent=yes]").addEventListener("click", function(){ set("granted"); apply("granted"); hide(); });
    ck.querySelector("[data-consent=no]").addEventListener("click", function(){ set("denied"); apply("denied"); hide(); });
  }

  // Cupons: copiar código
  d.querySelectorAll("[data-copy]").forEach(function(btn){
    btn.addEventListener("click", function(){
      var code = btn.getAttribute("data-copy");
      var done = function(){ btn.classList.add("copied"); setTimeout(function(){ btn.classList.remove("copied"); }, 1600); window.dataLayer.push({event:"cupom_copiado", cupom: code}); };
      if(navigator.clipboard && window.isSecureContext){ navigator.clipboard.writeText(code).then(done, function(){ fallback(); }); } else { fallback(); }
      function fallback(){ var t = d.createElement("textarea"); t.value = code; t.setAttribute("readonly",""); t.style.position = "fixed"; t.style.opacity = "0"; b.appendChild(t); t.select(); try{ d.execCommand("copy"); done(); }catch(e){} b.removeChild(t); }
    });
  });

  // FAQ: animação de expansão (sanfona)
  d.querySelectorAll(".faq details").forEach(function(det){
    var sum = det.querySelector("summary"), anim = null, closing = false;
    if(!sum || !det.animate) return;
    function finish(open){ det.open = open; anim = null; closing = false; det.style.height = det.style.overflow = ""; }
    function shrink(){
      closing = true; det.style.overflow = "hidden";
      var from = det.offsetHeight + "px", to = sum.offsetHeight + "px";
      if(anim) anim.cancel();
      anim = det.animate({height:[from,to]},{duration:REDUCED ? 0 : 380, easing:"cubic-bezier(.22,1,.36,1)"});
      anim.onfinish = function(){ finish(false); }; anim.oncancel = function(){ closing = false; };
    }
    function expand(){
      det.style.overflow = "hidden";
      var from = det.offsetHeight + "px"; det.open = true;
      var to = det.scrollHeight + "px";
      if(anim) anim.cancel();
      anim = det.animate({height:[from,to]},{duration:REDUCED ? 0 : 480, easing:"cubic-bezier(.22,1,.36,1)"});
      anim.onfinish = function(){ finish(true); };
      var c = det.querySelector("p");
      if(c && !REDUCED) c.animate({opacity:[0,1],transform:["translateY(-8px)","none"]},{duration:420, delay:80, easing:"ease-out", fill:"backwards"});
    }
    sum.addEventListener("click", function(e){
      e.preventDefault();
      if(closing || !det.open){
        det.parentNode.querySelectorAll("details[open]").forEach(function(o){ if(o !== det) o.querySelector("summary").click(); });
        expand();
      } else { shrink(); }
    });
  });

  // Carrossel de feedbacks
  d.querySelectorAll("[data-carousel]").forEach(function(car){
    var track = car.querySelector(".carousel-track"), items = Array.prototype.slice.call(track.children);
    items.forEach(function(it, i){ it.style.setProperty("--d", ((i % 3) * 0.09) + "s"); });
    var dotsBox = car.querySelector(".carousel-dots"), btns = car.querySelectorAll(".carousel-btn"), timer = null, hold = false;
    function step(){ return items.length > 1 ? items[1].offsetLeft - items[0].offsetLeft : track.clientWidth; }
    function perView(){ return Math.max(1, Math.round(track.clientWidth / step())); }
    function pages(){ return Math.max(1, items.length - perView() + 1); }
    function current(){ return Math.min(pages() - 1, Math.round(track.scrollLeft / step())); }
    function go(i){ track.scrollTo({left: Math.max(0, Math.min(pages() - 1, i)) * step(), behavior: REDUCED ? "auto" : "smooth"}); }
    function buildDots(){
      dotsBox.innerHTML = "";
      for(var i = 0; i < pages(); i++){ (function(i){
        var b2 = d.createElement("button"); b2.type = "button"; b2.setAttribute("role","tab"); b2.setAttribute("aria-label","Ir para o feedback " + (i + 1));
        b2.addEventListener("click", function(){ go(i); restart(); }); dotsBox.appendChild(b2);
      })(i); }
      sync();
    }
    function sync(){
      var c = current();
      Array.prototype.forEach.call(dotsBox.children, function(x, i){ x.setAttribute("aria-selected", i === c ? "true" : "false"); });
      btns[0].disabled = c <= 0; btns[1].disabled = c >= pages() - 1;
    }
    btns.forEach(function(b2){ b2.addEventListener("click", function(){ go(current() + parseInt(b2.getAttribute("data-dir"), 10)); restart(); }); });
    track.addEventListener("keydown", function(e){ if(e.key === "ArrowRight"){ e.preventDefault(); go(current() + 1); } if(e.key === "ArrowLeft"){ e.preventDefault(); go(current() - 1); } });
    var raf = 0; track.addEventListener("scroll", function(){ cancelAnimationFrame(raf); raf = requestAnimationFrame(sync); }, {passive:true});
    function tick(){ if(hold) return; var c = current(); go(c >= pages() - 1 ? 0 : c + 1); }
    function restart(){ if(REDUCED) return; clearInterval(timer); timer = setInterval(tick, 6000); }
    ["pointerenter","focusin","touchstart"].forEach(function(ev){ car.addEventListener(ev, function(){ hold = true; }, {passive:true}); });
    ["pointerleave","focusout"].forEach(function(ev){ car.addEventListener(ev, function(){ hold = false; }); });
    var rt; window.addEventListener("resize", function(){ clearTimeout(rt); rt = setTimeout(buildDots, 150); });
    buildDots();
    if("IntersectionObserver" in window){ new IntersectionObserver(function(es){ if(es[0].isIntersecting) restart(); else clearInterval(timer); }).observe(car); } else restart();
  });
})();
