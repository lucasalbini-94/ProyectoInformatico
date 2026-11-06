// ---------- Elementos ----------
const tabL = document.getElementById('tab-lenguaje');
const tabT = document.getElementById('tab-tecnologia');
const tipoInput = document.getElementById('tipo');
const labelItem = document.getElementById('label-item');
const hintItem = document.getElementById('hint-item');
const selItem = document.getElementById('id_item');

//  Función que cambia según el tipo -
function cambiarTipo(tipo) {
  // busca cual es el valor de tipo, si habilidad o tecnologia
  tipoInput.value = tipo;

  // Aca los cambia a el otro o los deja asi
  if (tipo === 'tecnologia') {
    labelItem.textContent = 'Tecnología *';
  } else {
    labelItem.textContent = 'Lenguaje *';
  }
  // Remarca el boton que este activo
  tabL.classList.toggle('activo', tipo === 'lenguaje');
  tabT.classList.toggle('activo', tipo === 'tecnologia');
}

// Aca se agrega el evento a los click de cada boton
tabL.addEventListener('click', () => cambiarTipo('lenguaje'));
tabT.addEventListener('click', () => cambiarTipo('tecnologia'));

// Estado inicial
cambiarTipo("lenguaje");

// FALTA CARGAR LOS CATALOGOS DESDE LA BASE DE DATOS