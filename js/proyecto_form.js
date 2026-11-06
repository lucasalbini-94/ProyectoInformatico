// ---------- Elementos ----------
// Al apretar este boton se tiene que mandar el nuevo proyecto
const btnGuarda = document.getElementById('btn-submit');

const API = '/api';

// ---------- Cargar categorías ----------
(async function cargarCategorias() {
  const sel = document.getElementById('id_categoria_proyecto');
  try {
    // Intenta traer las categorias de la base de datos
    const r = await fetch(`${API}/categorias`, { credentials: 'include' });
    // Si la respuesta no es correcta se corta
    if (!r.ok) throw new Error();
    // Transforma la respuesta recibida en json
    const cats = await r.json();
    // Va cargando las categorias en los select
    sel.innerHTML = '<option value="">— Elegí una categoría —</option>' +
      cats.map(c => `<option value="${c.id_categoria}">${c.nombre_categoria}</option>`).join('');
  } catch {
    sel.innerHTML = '<option value="">Error al cargar categorías</option>';
  }
})();

// -Cargar habilidades del usuario (para los checks) ----------
(async function cargarHabilidades() {
  const contL = document.getElementById('checks-lenguajes');
  const contT = document.getElementById('checks-tecnologias');
  try {
    const r = await fetch(`${API}/me/habilidades`, { credentials: 'include' });
    if (!r.ok) throw new Error();
    const { lenguajes = [], tecnologias = [] } = await r.json();

    contL.innerHTML = lenguajes.length
      ? lenguajes.map(l => `
          <label><input type="checkbox" name="id_lenguaje" value="${l.id_lenguaje}"> ${l.nombre}</label>
        `).join('')
      : '<span class="hint">No tenés lenguajes cargados. <a href="habilidad_form.html">Agregá uno</a>.</span>';

    contT.innerHTML = tecnologias.length
      ? tecnologias.map(t => `
          <label><input type="checkbox" name="id_tecnologia" value="${t.id_tecnologia}"> ${t.nombre}</label>
        `).join('')
      : '<span class="hint">No tenés tecnologías cargadas. <a href="habilidad_form.html">Agregá una</a>.</span>';
  } catch {
    contL.innerHTML = '<span class="hint">No se pudieron cargar tus lenguajes.</span>';
    contT.innerHTML = '<span class="hint">No se pudieron cargar tus tecnologías.</span>';
  }
})();

cargarHabilidades();
cargarCategorias();
