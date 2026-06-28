(() => {
  const input = document.querySelector("#garden-search");
  const results = document.querySelector("#garden-search-results");
  if (!input || !results) return;

  let pagesPromise;
  let activeIndex = -1;

  const loadPages = () => {
    if (!pagesPromise) {
      pagesPromise = fetch("/index.json")
        .then((response) => {
          if (!response.ok) throw new Error(`Search index returned ${response.status}`);
          return response.json();
        });
    }
    return pagesPromise;
  };

  const normalize = (value) =>
    String(value || "").toLocaleLowerCase().replace(/\s+/g, " ").trim();

  const excerpt = (content, terms) => {
    const text = String(content || "").replace(/\s+/g, " ").trim();
    const lower = text.toLocaleLowerCase();
    const positions = terms
      .map((term) => lower.indexOf(term))
      .filter((position) => position >= 0);
    const start = Math.max(0, (positions.length ? Math.min(...positions) : 0) - 55);
    const value = text.slice(start, start + 155);
    return `${start ? "…" : ""}${value}${start + 155 < text.length ? "…" : ""}`;
  };

  const hideResults = () => {
    results.hidden = true;
    results.replaceChildren();
    input.setAttribute("aria-expanded", "false");
    activeIndex = -1;
  };

  const showMessage = (message) => {
    const item = document.createElement("span");
    item.className = "site-search__message";
    item.textContent = message;
    results.replaceChildren(item);
    results.hidden = false;
    input.setAttribute("aria-expanded", "true");
  };

  const render = (matches, terms) => {
    results.replaceChildren();
    activeIndex = -1;

    if (!matches.length) {
      showMessage("No matching pages.");
      return;
    }

    matches.slice(0, 10).forEach(({ page }) => {
      const link = document.createElement("a");
      link.className = "site-search__result";
      link.href = page.url;
      link.setAttribute("role", "option");

      const title = document.createElement("span");
      title.className = "site-search__title";
      title.textContent = page.title;

      const summary = document.createElement("span");
      summary.className = "site-search__excerpt";
      summary.textContent = excerpt(page.content, terms);

      link.append(title, summary);
      results.append(link);
    });

    results.hidden = false;
    input.setAttribute("aria-expanded", "true");
  };

  const search = async () => {
    const query = normalize(input.value);
    if (query.length < 2) {
      hideResults();
      return;
    }

    const terms = query.split(" ").filter(Boolean);
    showMessage("Searching…");

    try {
      const pages = await loadPages();
      const matches = pages
        .map((page) => {
          const title = normalize(page.title);
          const tags = normalize((page.tags || []).join(" "));
          const content = normalize(page.content);
          if (!terms.every((term) => title.includes(term) || tags.includes(term) || content.includes(term))) {
            return null;
          }

          let score = 0;
          if (title === query) score += 100;
          if (title.startsWith(query)) score += 60;
          if (title.includes(query)) score += 35;
          terms.forEach((term) => {
            if (title.includes(term)) score += 12;
            if (tags.includes(term)) score += 5;
            if (content.includes(term)) score += 1;
          });
          return { page, score };
        })
        .filter(Boolean)
        .sort((a, b) => b.score - a.score || a.page.title.localeCompare(b.page.title));

      render(matches, terms);
    } catch (error) {
      console.error(error);
      showMessage("Search is temporarily unavailable.");
    }
  };

  const resultLinks = () => [...results.querySelectorAll(".site-search__result")];

  input.addEventListener("input", search);
  input.addEventListener("focus", () => {
    if (normalize(input.value).length >= 2) search();
  });
  input.addEventListener("keydown", (event) => {
    const links = resultLinks();
    if (event.key === "Escape") {
      hideResults();
      input.blur();
      return;
    }
    if (!links.length || !["ArrowDown", "ArrowUp", "Enter"].includes(event.key)) return;

    if (event.key === "Enter") {
      if (activeIndex >= 0) {
        event.preventDefault();
        links[activeIndex].click();
      }
      return;
    }

    event.preventDefault();
    activeIndex =
      event.key === "ArrowDown"
        ? (activeIndex + 1) % links.length
        : (activeIndex - 1 + links.length) % links.length;
    links.forEach((link, index) =>
      link.setAttribute("aria-selected", String(index === activeIndex))
    );
    links[activeIndex].scrollIntoView({ block: "nearest" });
  });

  document.addEventListener("click", (event) => {
    if (!event.target.closest(".site-search")) hideResults();
  });
})();
