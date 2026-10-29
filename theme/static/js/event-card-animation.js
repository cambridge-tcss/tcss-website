const mobileViewport = window.matchMedia("(max-width: 768px)");
let eventCardObserver;

function updateEventCardObserver() {
  if (eventCardObserver) {
    eventCardObserver.disconnect();
    eventCardObserver = undefined;
  }

  const eventCards = document.querySelectorAll(".event-card");
  if (!mobileViewport.matches || !("IntersectionObserver" in window)) {
    eventCards.forEach((card) => card.classList.remove("animated"));
    return;
  }

  eventCardObserver = new IntersectionObserver(
    (entries) => {
      entries.forEach((entry) => {
        entry.target.classList.toggle("animated", entry.intersectionRatio >= 0.90);
      });
    },
    { threshold: 0.90 }
  );

  eventCards.forEach((card) => eventCardObserver.observe(card));
}

let observerReady = false;

mobileViewport.addEventListener("change", () => {
  if (observerReady) {
    updateEventCardObserver();
  }
});

window.addEventListener(
  "load",
  () => {
    window.setTimeout(() => {
      observerReady = true;
      updateEventCardObserver();
    }, 200);
  },
  { once: true }
);