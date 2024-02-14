document.addEventListener('DOMContentLoaded', function () {
    // Toggle header button and menu
    document.getElementById('menu-btn').addEventListener('click', function () {
        this.classList.toggle('fa-times');
        document.querySelector('.navbar.nav-2 .menu').classList.toggle('active');
    });

    // Smooth scrolling for anchor links
    document.querySelectorAll('a[href^="#"]').forEach(anchor => {
        anchor.addEventListener('click', function (e) {
            e.preventDefault();

            const targetId = this.getAttribute('href').substring(1);
            const targetElement = document.getElementById(targetId);

            if (targetElement) {
                window.scrollTo({
                    top: targetElement.offsetTop,
                    behavior: 'smooth'
                });
            }
        });
    });

    // Show/hide header on scroll
    window.addEventListener('scroll', function () {
        const header = document.querySelector('.header');
        const menuBtn = document.getElementById('menu-btn');

        menuBtn.classList.remove('fa-times');
        document.querySelector('.navbar.nav-2 .menu').classList.remove('active');

        if (window.scrollY > 0) {
            header.classList.add('scroll');
        } else {
            header.classList.remove('scroll');
        }
    });
});
