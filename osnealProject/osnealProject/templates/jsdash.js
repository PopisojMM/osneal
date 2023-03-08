let btn = document.querySelector("#btn");
let sidebar = document.querySelector(".sidebar");
let searchBtn = document.querySelector(".bx-search");
const dropdownButton = document.querySelector(".dropdown-button");
const dropdownContent = document.querySelector(".dropdown-content");


btn.onclick = function(){
    sidebar.classList.toggle("active");
}
searchBtn.onclick = function(){
    sidebar.classList.toggle("active");
}



//////////////////////////////////////////////////////// QUERY BUSCADOR DNI
// Obtener el formulario y el campo de entrada de texto
const form = document.querySelector('#search-form');
const input = document.querySelector('#search-dni');

// Manejar el evento de envío del formulario
form.addEventListener('submit', (event) => {
  // Prevenir la acción predeterminada del envío del formulario
  event.preventDefault();
  
  // Obtener el valor del campo de entrada de texto
  const searchQuery = input.value.trim();
  
  // Realizar la búsqueda si el campo de entrada de texto no está vacío
  if (searchQuery !== '') {
    // Aquí puedes agregar tu código para realizar la búsqueda con el DNI ingresado
    console.log(`Buscando DNI ${searchQuery}...`);
  }
});


const animalTableBody = document.getElementById('animalTableBody');
const agregarAnimalForm = document.querySelector('form');

agregarAnimalForm.addEventListener('submit', (event) => {
  event.preventDefault();

  const nombre = document.getElementById('nombre').value;
  const especie = document.getElementById('especie').value;
  const fechaAplicacion = document.getElementById('fechaAplicacion').value;
  const proximaVacunacion = document.getElementById('proximaVacunacion').value;

  const newRow = document.createElement('tr');
  newRow.innerHTML = `
    <td>${nombre}</td>
    <td>${especie}</td>
    <td>${fechaAplicacion}</td>
    <td>${proximaVacunacion}</td>