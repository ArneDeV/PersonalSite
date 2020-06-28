const modal = document.querySelector(".modal");
const previews = document.querySelectorAll(".galery img");
const original = document.querySelector(".full-img");
const imgText = document.querySelector(".caption");

previews.forEach((preview) => {
    preview.addEventListener("click", () => {
        modal.classList.add("open");
        original.classList.add('open');
        // change image and text
        const originalImg = preview.getAttribute('data-orginal');
        original.src = originalImg;
        console.log(originalImg);
        const altText = preview.alt;
        imgText.textContent = altText
    });
});

modal.addEventListener('click', (event) => {
    if(event.target.classList.contains('modal')) {
        modal.classList.remove('open');
    }
});