// static/js/navigation_script.js
document.addEventListener('DOMContentLoaded', function () {
    // Get the current page URL
    var currentUrl = window.location.href;

    // Find and highlight the active link in the navigation menu
    var navLinks = document.querySelectorAll('.navbar a');
    navLinks.forEach(function (link) {
        if (currentUrl.includes(link.getAttribute('href'))) {
            link.classList.add('active');
        }
    });
});
