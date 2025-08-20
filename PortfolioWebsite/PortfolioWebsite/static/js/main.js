document.addEventListener("DOMContentLoaded", () => {
    const themeToggle = document.getElementById("theme-toggle");
    const htmlEl = document.documentElement;

    // Load saved theme from localStorage
    const savedTheme = localStorage.getItem("theme");
    if (savedTheme === "dark") {
        htmlEl.classList.add("dark");
    } else {
        htmlEl.classList.remove("dark");
    }

    // Toggle dark/light theme
    themeToggle.addEventListener("click", () => {
        htmlEl.classList.toggle("dark");
        localStorage.setItem("theme", htmlEl.classList.contains("dark") ? "dark" : "light");
    });

    // Intersection Observer for scroll animations
    const observer = new IntersectionObserver(
      (entries) => {
        entries.forEach(entry => {
          if (entry.isIntersecting) {
            entry.target.classList.add('fade-in');
            observer.unobserve(entry.target);
          }
        });
      },
      { threshold: 0.1 }
    );

    document.querySelectorAll('.animate-on-scroll').forEach(el => observer.observe(el));
});




