document.addEventListener('DOMContentLoaded', function () {
    const menuButton = document.querySelector('.menu-toggle');
    const nav = document.querySelector('.nav-links');
    if (menuButton && nav) {
        menuButton.addEventListener('click', function () {
            const isOpen = nav.classList.toggle('is-open');
            menuButton.setAttribute('aria-expanded', String(isOpen));
            menuButton.textContent = isOpen ? '×' : '☰';
        });
    }

    const revealItems = document.querySelectorAll('.reveal');
    if ('IntersectionObserver' in window) {
        const observer = new IntersectionObserver(function (entries) {
            entries.forEach(function (entry) {
                if (entry.isIntersecting) {
                    entry.target.classList.add('is-visible');
                    observer.unobserve(entry.target);
                }
            });
        }, { threshold: 0.12 });
        revealItems.forEach(function (item, index) {
            item.style.transitionDelay = (index % 3) * 70 + 'ms';
            observer.observe(item);
        });
    } else {
        revealItems.forEach(function (item) { item.classList.add('is-visible'); });
    }
});
