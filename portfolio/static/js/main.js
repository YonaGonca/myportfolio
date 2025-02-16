/*=============== SHOW MENU ===============*/
const navMenu = document.getElementById('nav-menu'),
      navToggle = document.getElementById('nav-toggle')
      navClose = document.getElementById('nav-close')

/* Menu show */
navToggle.addEventListener('click', () =>{
   navMenu.classList.add('show-menu')
})

/* Menu hidden */
navClose.addEventListener('click', () =>{
  navMenu.classList.remove('show-menu')
})

/*=============== DARK MODE ===============*/
const navDarkMode = document.getElementById('darkmode-btn');

// Función para aplicar modo oscuro o claro
function applyDarkMode(enabled) {
  if (enabled) {

    document.cookie = "darkMode=enabled; path=/; max-age=" + 60 * 60 * 24 * 365;
    localStorage.setItem('darkMode', 'enabled');
    document.documentElement.style.setProperty('--title-color', 'hsl(230, 100%, 98%)');
    document.documentElement.style.setProperty('--header-color', 'hsla(228, 97%, 12%, 0.651)');
    document.documentElement.style.setProperty('--text-color', 'hsl(230, 100%, 98%)');
    document.documentElement.style.setProperty('--body-color', 'hsl(230, 75%, 15%)');
    document.documentElement.style.setProperty('--animation-color1', 'rgb(0, 0, 24)');
    document.documentElement.style.setProperty('--animation-color2', 'rgb(5, 1, 43)');

    // Cambiar imágenes a dark mode
    document.querySelectorAll('.project_image_change').forEach(img => {
      if (img.dataset.dark) img.src = img.dataset.dark;
    });

  } else {
    document.cookie = "darkMode=disabled; path=/; max-age=" + 60 * 60 * 24 * 365;  // Expira en un año

    localStorage.setItem('darkMode', 'disabled');
    document.documentElement.style.setProperty('--title-color', 'hsl(230, 75%, 15%)');
    document.documentElement.style.setProperty('--text-color', 'hsl(230, 75%, 15%)');
    document.documentElement.style.setProperty('--body-color', 'hsl(230, 100%, 98%)');
    document.documentElement.style.setProperty('--header-color', 'hsla(228, 100%, 98%, 0.651)');
    document.documentElement.style.setProperty('--animation-color1', 'rgb(244, 247, 244)');
    document.documentElement.style.setProperty('--animation-color2', 'rgb(185, 248, 248)');

    // Cambiar imágenes a light mode
    document.querySelectorAll('.project_image_change').forEach(img => {
      if (img.dataset.light) img.src = img.dataset.light;
    });
  }
}

// Evento para cambiar el modo oscuro cuando se haga clic en el botón
navDarkMode.addEventListener('click', () => {
  const darkModeEnabled = localStorage.getItem('darkMode') === 'enabled';
  applyDarkMode(!darkModeEnabled); // Invierte el estado actual
});



/*animation contactme*/

const inputs = document.querySelectorAll(".input")

function focusFunc() {
  let parent = this.parentNode;
  parent.classList.add("focus")
}

function blurFunc() {
  let parent = this.parentNode;
  if (this.value == "") {
    parent.classList.remove("focus")
  }
}

inputs.forEach(input => {
  input.addEventListener("focus", focusFunc)
  input.addEventListener("blur", blurFunc)
})

/*Copy Email*/

function copyEmail() {
  const emailText = document.getElementById('email').textContent; // Obtiene el texto del email
  navigator.clipboard.writeText(emailText).then(() => {
      const check = document.getElementById('copy_icon');
      check.classList.remove('ri-checkbox-multiple-blank-line')
      check.classList.add('ri-checkbox-multiple-line')
      check.classList.add('copy_click')
      setTimeout(() => {
        check.classList.remove('ri-checkbox-multiple-line')
        check.classList.add('ri-checkbox-multiple-blank-line')
        check.classList.remove('copy_click')
      }, 5000);
  }).catch(err => {
      console.error('Error al copiar: ', err);
  });
}

/*Select Lenguage*/

const languageBtn = document.getElementById('language-btn');
const languageOptions = document.getElementById('language-options');
const languageOptionItems = document.querySelectorAll('.language-option');

// Mostrar/ocultar las opciones de idioma al hacer clic en el botón
languageBtn.addEventListener('click', () => {
    if (languageOptions.classList.contains('show')) {
        // Si el menú está visible, lo ocultamos
        languageOptions.classList.remove('show');
    } else {
        // Si está oculto, lo mostramos con animación
        languageOptions.classList.add('show');
    }
});


// Cerrar el menú de opciones si se hace clic fuera de él
document.addEventListener('click', (e) => {
    if (!languageBtn.contains(e.target) && !languageOptions.contains(e.target)) {
        languageOptions.classList.remove('show');
    }
});