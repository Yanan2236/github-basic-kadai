const backBtn = document.querySelector('#back-btn')

window.addEventListener('scroll', () => {
    const y = window.scrollY;

    if (y >= 300) {
        backBtn.classList.add("is-visible")
    } else {
        backBtn.classList.remove("is-visible")
    }
});