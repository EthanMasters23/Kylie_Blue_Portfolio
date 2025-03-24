document.addEventListener('DOMContentLoaded', () => {
    const sections = document.querySelectorAll('.section');
    let currentSection = 0;

    function animateSection(sectionIndex) {
        sections.forEach((section, index) => {
            if (index === sectionIndex) {
                section.classList.add('active');
                section.classList.remove('inactive');
            } else {
                section.classList.add('inactive');
                section.classList.remove('active');
            }
        });
    }

    animateSection(currentSection);

    window.addEventListener('scroll', () => {
        const scrollY = window.scrollY;
        const viewportHeight = window.innerHeight;

        sections.forEach((section, index) => {
            const sectionTop = section.offsetTop;

            if (scrollY >= sectionTop - viewportHeight / 2 && scrollY < sectionTop + section.offsetHeight) {
                currentSection = index;
                animateSection(currentSection);
            }
        });
    });

    window.addEventListener('resize', () => {
        sections.forEach(section => {
            section.style.height = `${window.innerHeight}px`;
        });
    });

    sections.forEach(section => {
        section.style.height = `${window.innerHeight}px`;
    });
});
