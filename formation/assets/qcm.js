/* Examens blancs interactifs : cliquer une réponse, puis « Corriger mon examen ». */
(function () {
  function init() {
    var box = document.querySelector(".qcm-exam");
    if (!box || box.dataset.ready) return;
    box.dataset.ready = "1";
    var answers = box.dataset.answers.split(",");
    var content = box.closest("article") || document.body;
    var qs = [];
    content.querySelectorAll("h3").forEach(function (h) {
      if (!/^Question \d+/.test(h.textContent.trim())) return;
      var el = h.nextElementSibling;
      while (el && el.tagName !== "UL" && el.tagName !== "H3") el = el.nextElementSibling;
      if (el && el.tagName === "UL") qs.push(el);
    });
    qs.forEach(function (ul, i) {
      ul.classList.add("qcm-choices");
      ul.querySelectorAll(":scope > li").forEach(function (li) {
        var m = li.textContent.trim().match(/^([A-D])\)/);
        if (!m) return;
        li.dataset.letter = m[1];
        li.addEventListener("click", function () {
          if (box.dataset.done) return;
          ul.querySelectorAll("li").forEach(function (x) { x.classList.remove("qcm-selected"); });
          li.classList.add("qcm-selected");
          ul.dataset.choice = m[1];
        });
      });
    });
    var btn = document.createElement("button");
    btn.className = "md-button md-button--primary";
    btn.textContent = "Corriger mon examen";
    var reset = document.createElement("button");
    reset.className = "md-button";
    reset.textContent = "Recommencer";
    reset.style.marginLeft = ".5rem";
    var out = document.createElement("div");
    out.className = "qcm-result";
    btn.addEventListener("click", function () {
      var score = 0;
      qs.forEach(function (ul, i) {
        var good = answers[i];
        ul.querySelectorAll("li").forEach(function (li) {
          if (li.dataset.letter === good) li.classList.add("qcm-good");
          else if (li.dataset.letter === ul.dataset.choice) li.classList.add("qcm-bad");
        });
        if (ul.dataset.choice === good) score++;
      });
      box.dataset.done = "1";
      var msg = score >= 14 ? "Excellent : vous êtes prête." : score >= 11 ? "Bon niveau : relisez les questions manquées." :
        score >= 8 ? "Correct mais fragile : retravaillez les thèmes concernés." : "Insuffisant : reprenez le cours avant de réessayer.";
      out.innerHTML = "<strong>Votre score : " + score + " / 15</strong> — " + msg +
        ' <a href="' + box.dataset.corrige + '">Voir le corrigé détaillé →</a>';
      out.scrollIntoView({ behavior: "smooth" });
    });
    reset.addEventListener("click", function () {
      delete box.dataset.done;
      out.innerHTML = "";
      qs.forEach(function (ul) {
        delete ul.dataset.choice;
        ul.querySelectorAll("li").forEach(function (li) { li.classList.remove("qcm-selected", "qcm-good", "qcm-bad"); });
      });
      window.scrollTo({ top: 0, behavior: "smooth" });
    });
    box.appendChild(btn);
    box.appendChild(reset);
    box.appendChild(out);
  }
  if (window.document$) window.document$.subscribe(init); else document.addEventListener("DOMContentLoaded", init);
})();
