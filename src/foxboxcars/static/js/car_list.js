// car_list.js

// Obtener referencia al botón de "Start Updating"
const startUpdatingBtn = document.getElementById('start-updating-btn');

// Obtener referencia a los botones "Cancel" y "Save"
const cancelBtn = document.querySelector('a.btn.btn-secondary');
const saveBtn = document.querySelector('button[type="submit"]');

// Ocultar los botones "Cancel" y "Save" inicialmente
cancelBtn.style.display = 'none';
saveBtn.style.display = 'none';

// Agregar evento
