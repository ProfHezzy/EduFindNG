// main.js
document.addEventListener('DOMContentLoaded', function() {
    // Mobile Menu Toggle (keep this as is)
    const mobileMenuToggle = document.querySelector('.mobile-menu-toggle');
    const mobileMenu = document.querySelector('.mobile-menu');
    
    if (mobileMenuToggle && mobileMenu) {
        mobileMenuToggle.addEventListener('click', function() {
            this.classList.toggle('active');
            mobileMenu.classList.toggle('active');
            document.body.classList.toggle('no-scroll');
        });
    }
    
    // Close mobile menu when clicking on a link (keep this as is)
    const mobileNavLinks = document.querySelectorAll('.mobile-nav-link');
    mobileNavLinks.forEach(link => {
        link.addEventListener('click', function() {
            mobileMenuToggle.classList.remove('active');
            mobileMenu.classList.remove('active');
            document.body.classList.remove('no-scroll');
        });
    });

    // Carousel Initialization
    function initHeroCarousel() {
        const carousel = document.querySelector('.hero-carousel');
        if (!carousel) return; // Exit if carousel element isn't found

        const items = carousel.querySelectorAll('.carousel-item');
        let currentIndex = 0;
        const intervalTime = 5000; // 5 seconds
        
        function showNextItem() {
            // Remove active class from current item
            items[currentIndex].classList.remove('active');
            
            // Move to next item
            currentIndex = (currentIndex + 1) % items.length;
            
            // Add active class to new item
            items[currentIndex].classList.add('active');
        }
        
        // Start the carousel
        let carouselInterval = setInterval(showNextItem, intervalTime);
        
        // Pause on hover
        carousel.addEventListener('mouseenter', () => {
            clearInterval(carouselInterval);
        });
        
        // Resume when mouse leaves
        carousel.addEventListener('mouseleave', () => {
            carouselInterval = setInterval(showNextItem, intervalTime);
        });
        
        // Initialize first item
        // Ensure there's at least one item before trying to add 'active' class
        if (items.length > 0) {
            items[0].classList.add('active');
        }
    }

    // CALL THE CAROUSEL INITIALIZATION FUNCTION DIRECTLY HERE
    initHeroCarousel(); // <-- CHANGE: Call it directly, remove the nested addEventListener

    // Back to Top Button (keep as is)
    const backToTopButton = document.querySelector('.back-to-top');
    
    if (backToTopButton) {
        window.addEventListener('scroll', function() {
            if (window.pageYOffset > 300) {
                backToTopButton.classList.add('visible');
            } else {
                backToTopButton.classList.remove('visible');
            }
        });
        
        backToTopButton.addEventListener('click', function(e) {
            e.preventDefault();
            window.scrollTo({
                top: 0,
                behavior: 'smooth'
            });
        });
    }
    
    // Preloader (keep as is)
    const preloader = document.querySelector('.preloader');
    
    if (preloader) {
        window.addEventListener('load', function() { // Note: 'load' event, not DOMContentLoaded
            setTimeout(function() {
                preloader.classList.add('loaded');
                setTimeout(function() {
                    preloader.style.display = 'none';
                }, 500);
            }, 1000);
        });
    }
    
    // Scroll Reveal Animation (keep as is)
    const animateElements = document.querySelectorAll('.animate-on-scroll');
    
    function checkAnimation() {
        animateElements.forEach(element => {
            const elementPosition = element.getBoundingClientRect().top;
            const windowHeight = window.innerHeight;
            
            if (elementPosition < windowHeight - 100) {
                const animation = element.getAttribute('data-animation');
                const delay = element.getAttribute('data-delay') || 0;
                
                element.style.animationDelay = delay + 's';
                element.classList.add(animation);
                element.classList.add('animated');
            }
        });
    }
    
    // Initial check
    checkAnimation();
    
    // Check on scroll
    window.addEventListener('scroll', checkAnimation);
    
    // Favorite Button Toggle (keep as is)
    const favoriteButtons = document.querySelectorAll('.favorite-btn');
    
    favoriteButtons.forEach(button => {
        button.addEventListener('click', function() {
            const icon = this.querySelector('i');
            
            if (icon.classList.contains('far')) {
                icon.classList.remove('far');
                icon.classList.add('fas');
                this.classList.add('active');
                
                // Show temporary feedback
                const feedback = document.createElement('span');
                feedback.textContent = 'Added to favorites';
                feedback.classList.add('favorite-feedback');
                this.appendChild(feedback);
                
                setTimeout(() => {
                    feedback.remove();
                }, 2000);
            } else {
                icon.classList.remove('fas');
                icon.classList.add('far');
                this.classList.remove('active');
            }
        });
    });
    
    // Location Select Dropdown Enhancement (keep as is)
    const locationSelects = document.querySelectorAll('.location-select');
    
    locationSelects.forEach(select => {
        select.addEventListener('focus', function() {
            this.size = 5;
        });
        
        select.addEventListener('blur', function() {
            this.size = 1;
        });
        
        select.addEventListener('change', function() {
            this.size = 1;
            this.blur();
        });
    });
    
    // School Card Hover Effect (keep as is)
    const schoolCards = document.querySelectorAll('.school-card');
    
    schoolCards.forEach(card => {
        card.addEventListener('mouseenter', function() {
            this.querySelector('.school-card-inner').style.transform = 'translateY(-5px)';
            this.querySelector('.school-card-inner').style.boxShadow = '0 10px 20px rgba(0, 0, 0, 0.1)';
        });
        
        card.addEventListener('mouseleave', function() {
            this.querySelector('.school-card-inner').style.transform = '';
            this.querySelector('.school-card-inner').style.boxShadow = '';
        });
    });
    
    // Ripple Effect for Buttons (keep as is)
    const buttons = document.querySelectorAll('.btn:not(.btn-icon)');
    
    buttons.forEach(button => {
        button.addEventListener('click', function(e) {
            const x = e.clientX - e.target.getBoundingClientRect().left;
            const y = e.clientY - e.target.getBoundingClientRect().top;
            
            const ripple = document.createElement('span');
            ripple.classList.add('ripple-effect');
            ripple.style.left = `${x}px`;
            ripple.style.top = `${y}px`;
            
            this.appendChild(ripple);
            
            setTimeout(() => {
                ripple.remove();
            }, 600);
        });
    });
    
    // Current Year in Footer (keep as is)
    document.getElementById('current-year').textContent = new Date().getFullYear();
});