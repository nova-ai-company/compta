/* Bulles d'aide : chaque code (C09, CA3, M+1, E04-03, DAS2…) devient cliquable
   et affiche son explication. Dictionnaire : assets/lexique.js (généré).
   + mise en couleur des encadrés « En clair », « Réflexe senior », « Erreur classique ». */
(function () {
  var LEX = window.LEXIQUE || {};
  var CATS = window.LEXIQUE_CATS || {};
  var SKIP = /^(PRE|CODE|A|SCRIPT|STYLE|H1|BUTTON|KBD|TEXTAREA|INPUT|SVG)$/;
  // Années : un nombre à 4 chiffres précédé de ces mots est une date, pas un formulaire.
  var YEAR_CTX = /(?:^|\s)(en|au|de|du|à|a|depuis|jusqu'en|avant|après|fin|début|exercice|année|millésime|→|–|-)\s*$/i;

  var keys = Object.keys(LEX).sort(function (a, b) { return b.length - a.length; });
  var esc = function (s) { return s.replace(/[.*+?^${}()|[\]\\]/g, "\\$&"); };
  var RE = new RegExp("(^|[^A-Za-z0-9À-ÿ_\\-/.°+'’])(" + keys.map(esc).join("|") + ")(?=$|[^A-Za-z0-9À-ÿ_\\-/+°])", "g");

  function base() {
    try { return new URL(JSON.parse(document.getElementById("__config").textContent).base + "/", location.href).href; }
    catch (e) { return location.origin + "/"; }
  }

  function wrap(root) {
    var walker = document.createTreeWalker(root, NodeFilter.SHOW_TEXT, {
      acceptNode: function (n) {
        if (!n.nodeValue || n.nodeValue.length < 1) return NodeFilter.FILTER_REJECT;
        for (var p = n.parentNode; p && p !== root; p = p.parentNode) {
          if (SKIP.test(p.nodeName) || (p.classList && (p.classList.contains("bulle") || p.classList.contains("headerlink")))) return NodeFilter.FILTER_REJECT;
        }
        return NodeFilter.FILTER_ACCEPT;
      }
    });
    var nodes = [];
    while (walker.nextNode()) nodes.push(walker.currentNode);
    nodes.forEach(function (node) {
      var text = node.nodeValue, last = 0, m, frag = null;
      RE.lastIndex = 0;
      while ((m = RE.exec(text))) {
        var code = m[2], start = m.index + m[1].length;
        if (/^\d{4}$/.test(code) && YEAR_CTX.test(text.slice(Math.max(0, start - 14), start))) continue;
        frag = frag || document.createDocumentFragment();
        frag.appendChild(document.createTextNode(text.slice(last, start)));
        var s = document.createElement("span");
        s.className = "bulle bulle--" + LEX[code].c;
        s.textContent = code;
        s.dataset.k = code;
        s.tabIndex = 0;
        s.setAttribute("role", "button");
        s.setAttribute("aria-label", code + " : afficher l'explication");
        frag.appendChild(s);
        last = start + code.length;
      }
      if (frag) {
        frag.appendChild(document.createTextNode(text.slice(last)));
        node.parentNode.replaceChild(frag, node);
      }
    });
  }

  /* ---------- Popover ---------- */
  var pop, current, hoverTimer;
  function ensurePop() {
    if (pop) return pop;
    pop = document.createElement("div");
    pop.className = "bulle-pop";
    pop.setAttribute("role", "dialog");
    pop.hidden = true;
    document.body.appendChild(pop);
    pop.addEventListener("mouseenter", function () { clearTimeout(hoverTimer); });
    pop.addEventListener("mouseleave", function () { if (!pop.dataset.pinned) hide(); });
    return pop;
  }
  function show(el, pinned) {
    var e = LEX[el.dataset.k]; if (!e) return;
    ensurePop();
    var parts = e.t.split(" — "), head = parts.shift(), sub = parts.join(" — ");
    pop.className = "bulle-pop bulle-pop--" + e.c;
    pop.innerHTML = "";
    var cat = document.createElement("div"); cat.className = "bulle-pop__cat"; cat.textContent = CATS[e.c] || "";
    var h = document.createElement("div"); h.className = "bulle-pop__titre";
    var b = document.createElement("strong"); b.textContent = head; h.appendChild(b);
    if (sub) { var sp = document.createElement("span"); sp.textContent = " — " + sub; h.appendChild(sp); }
    var d = document.createElement("p"); d.textContent = e.d;
    var close = document.createElement("button"); close.className = "bulle-pop__close"; close.type = "button";
    close.setAttribute("aria-label", "Fermer"); close.textContent = "×";
    close.addEventListener("click", hide);
    pop.append(close, cat, h, d);
    if (e.u) {
      var a = document.createElement("a"); a.href = new URL(e.u, base()).href;
      a.className = "bulle-pop__lien";
      a.textContent = e.c === "client" ? "Voir la fiche du client →" : e.c === "exercice" ? "Ouvrir l'exercice →" : "Ouvrir le cours →";
      pop.appendChild(a);
    }
    if (pinned) pop.dataset.pinned = "1"; else delete pop.dataset.pinned;
    if (current && current !== el) current.setAttribute("aria-expanded", "false");
    current = el; el.setAttribute("aria-expanded", "true");
    pop.hidden = false;
    place(el);
  }
  function place(el) {
    if (window.matchMedia("(max-width: 600px)").matches) { pop.style.left = pop.style.top = ""; pop.classList.add("bulle-pop--sheet"); return; }
    pop.classList.remove("bulle-pop--sheet");
    var r = el.getBoundingClientRect(), w = pop.offsetWidth, hgt = pop.offsetHeight;
    var left = Math.min(Math.max(8, r.left + r.width / 2 - w / 2), window.innerWidth - w - 8);
    var top = r.bottom + 8;
    if (top + hgt > window.innerHeight - 8) top = Math.max(8, r.top - hgt - 8);
    pop.style.left = left + "px"; pop.style.top = top + "px";
  }
  function hide() {
    if (!pop) return;
    pop.hidden = true; delete pop.dataset.pinned;
    if (current) current.setAttribute("aria-expanded", "false");
    current = null;
  }

  var finePointer = window.matchMedia("(hover: hover) and (pointer: fine)").matches;
  document.addEventListener("click", function (ev) {
    var el = ev.target.closest && ev.target.closest(".bulle");
    if (el) { ev.preventDefault(); (current === el && pop && pop.dataset.pinned) ? hide() : show(el, true); return; }
    if (pop && !pop.hidden && !pop.contains(ev.target)) hide();
  });
  document.addEventListener("keydown", function (ev) {
    if (ev.key === "Escape") return hide();
    var el = ev.target.closest && ev.target.closest(".bulle");
    if (el && (ev.key === "Enter" || ev.key === " ")) { ev.preventDefault(); show(el, true); }
  });
  if (finePointer) {
    document.addEventListener("mouseover", function (ev) {
      var el = ev.target.closest && ev.target.closest(".bulle");
      if (!el || (pop && pop.dataset.pinned)) return;
      clearTimeout(hoverTimer);
      hoverTimer = setTimeout(function () { show(el, false); }, 220);
    });
    document.addEventListener("mouseout", function (ev) {
      var el = ev.target.closest && ev.target.closest(".bulle");
      if (!el || (pop && pop.dataset.pinned)) return;
      clearTimeout(hoverTimer);
      hoverTimer = setTimeout(function () { if (pop && !pop.dataset.pinned && !pop.matches(":hover")) hide(); }, 200);
    });
  }
  window.addEventListener("resize", hide);
  window.addEventListener("scroll", function () { if (pop && !pop.hidden && !pop.classList.contains("bulle-pop--sheet") && current) place(current); }, { passive: true });

  /* ---------- Lisibilité : encadrés colorés et carte d'exercice ---------- */
  function decorate(article) {
    article.querySelectorAll("blockquote").forEach(function (bq) {
      var t = bq.textContent.trim();
      if (/^🟢/.test(t)) bq.classList.add("bq-clair");
      else if (/^💡/.test(t)) bq.classList.add("bq-senior");
      else if (/^⚠/.test(t)) bq.classList.add("bq-erreur");
      else if (/^(📌|✅|🎯)/.test(t)) bq.classList.add("bq-info");
      else if (/^\*?\*?(Objectif|Pr[ée]requis)/.test(t) || /Objectif du module/.test(t.slice(0, 40))) bq.classList.add("bq-objectif");
    });
    var h1 = article.querySelector("h1");
    var p = h1 && h1.nextElementSibling;
    if (p && p.tagName === "P" && /Client\s*:/.test(p.textContent) && /Difficult/.test(p.textContent)) {
      p.classList.add("fiche-ex");
      var n = p.nextElementSibling;
      if (n && n.tagName === "P" && /^Corner case/.test(n.textContent.trim())) n.classList.add("fiche-ex__corner");
    }
    article.querySelectorAll("table").forEach(function (tb) {
      var hs = Array.prototype.map.call(tb.querySelectorAll("thead th"), function (th) { return th.textContent.trim().toLowerCase(); });
      if (hs.indexOf("débit") >= 0 && hs.indexOf("crédit") >= 0) {
        tb.classList.add("tbl-ecritures");
        hs.forEach(function (h, i) {
          if (h === "débit" || h === "crédit") tb.querySelectorAll("tr > :nth-child(" + (i + 1) + ")").forEach(function (c) { c.classList.add("num", h === "débit" ? "num--d" : "num--c"); });
        });
      }
    });
  }

  function init() {
    var article = document.querySelector(".md-content article");
    if (!article || article.dataset.bulles) return;
    article.dataset.bulles = "1";
    decorate(article);
    wrap(article);
  }
  if (window.document$ && window.document$.subscribe) window.document$.subscribe(init);
  else if (document.readyState !== "loading") init();
  else document.addEventListener("DOMContentLoaded", init);
})();
