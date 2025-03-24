const lightbox = document.getElementById('lightbox');
const lightboxContent = document.querySelector('.lightbox-content');
const lightboxCaption = document.querySelector('.lightbox-caption');
const closeLightbox = document.querySelector('.close');

document.querySelectorAll('.photo-item').forEach(item => {
    item.addEventListener('click', () => {
        lightbox.style.display = 'block';
        lightboxContent.src = item.querySelector('img').src;
        lightboxCaption.innerHTML = item.querySelector('.caption h3').innerText;
    });
});

closeLightbox.addEventListener('click', () => {
    lightbox.style.display = 'none';
});
