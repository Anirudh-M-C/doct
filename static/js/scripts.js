document.addEventListener('DOMContentLoaded', function() {
    const navLinks = document.querySelectorAll('.nav-itemss a');
    
    navLinks.forEach(function(link) {
        link.addEventListener('click', function(event) {
            // Remove the 'active' class from all links
            navLinks.forEach(function(link) {
                link.classList.remove('active');
            });

            // Add the 'active' class to the clicked link
            this.classList.add('active');
        });
    });
});




function toggleMode() {
    const body = document.body;
    body.classList.toggle("dark-mode");
    const toggleIcon = document.querySelector(".mode-toggle i");
    toggleIcon.classList.toggle("fa-toggle-on");
    toggleIcon.classList.toggle("fa-toggle-off");
}