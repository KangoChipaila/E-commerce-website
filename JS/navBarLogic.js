document.addEventListener("DOMContentLoaded", navControl());

function navControl(){

    const menu = document.getElementsByClassName("menu")[0];
    const menuOverlay = document.getElementsByClassName("menu-overlay")[0];

    if (!menu || !menuOverlay){
        console.log("Error");
        return;
    }

    menu.addEventListener('mouseenter', () => {
        menuOverlay.style.display = "block";
    });

    menu.addEventListener('mouseleave', () => {
        menuOverlay.style.display = "none";
    });

    menuOverlay.addEventListener('mouseenter', () => {
        menuOverlay.style.display = "block";
    });

    menuOverlay.addEventListener('mouseleave', () => {
        menuOverlay.style.display = "none";
    });
}    