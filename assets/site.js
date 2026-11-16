(function(){
  "use strict";
  var WA = "5513997771672";
  var d = document, b = d.body;
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

  // Reveal on scroll
  var rv = d.querySelectorAll(".reveal");
  if("IntersectionObserver" in window){
    var io = new IntersectionObserver(function(es){
      es.forEach(function(en){ if(en.isIntersecting){ en.target.classList.add("in"); io.unobserve(en.target); } });
    }, {rootMargin:"0px 0px -8% 0px"});
    rv.forEach(function(el){ io.observe(el); });
    // Pause hero animation off-screen
    var hero = d.querySelector(".hero");
    if(hero){
      new IntersectionObserver(function(es){ hero.classList.toggle("paused", !es[0].isIntersecting); }).observe(hero);
    }
  } else { rv.forEach(function(el){ el.classList.add("in"); }); }

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
})();
