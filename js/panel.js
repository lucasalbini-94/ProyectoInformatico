const API = '/api'; // hay que cambiarlo por la url
// lo mismo en cada fetch

async function cargarUsuario() {
  try {
    const respuesta = await fetch(`${API}/`, { credentials: 'include' });
    if (!respuesta.ok) throw new Error('No autenticado');
    const u = await r.json();

    document.getElementById('u-nombre').textContent  = `${u.nombre} ${u.apellido}`;
    document.getElementById('u-usuario').textContent = u.nombre_usuario;
    document.getElementById('u-email').textContent   = u.email;
    document.getElementById('u-fecha').textContent   = new Date(u.fecha_creacion).toLocaleDateString('es-AR');
  } catch (e) {
    const err = document.getElementById('error-usuario');
    err.textContent = 'No se pudieron cargar tus datos. ¿Iniciaste sesión?';
    err.hidden = false;
  }
}

async function cargarHabilidades() {
  try {
    const respuesta = await fetch(`${API}/`, { credentials: 'include' });
    // Si la peticion no fue exitosa da true
    // tiene un not !, lo pasa a false y no sigue
    if (!respuesta.ok) throw new Error();
    // Trae los valores en formato json
    const { lenguajes = [], tecnologias = [] } = await r.json();

    // Busca por ID la lista de lenguajes del html
    const contL = document.getElementById('lista-lenguajes');
    // Los llena con los lenguajes que encontró, pero primero
    // ve si hay lenguajes, sino devuelve lo mismo y no cambia nada
    contL.innerHTML = lenguajes.length
    // Si hay al menos un lenguaje mapea, recorre la lista y va agregando los lenguajes
      ? lenguajes.map(l => `<span class="tag">${l.nombre}<span class="nivel">${l.nivel}</span></span>`).join('')
      : '<span class="vacio">Sin lenguajes cargados.</span>';

    // Lo mismo pero con habilidades
    const contT = document.getElementById('lista-tecnologias');
    contT.innerHTML = tecnologias.length
      ? tecnologias.map(t => `<span class="tag tech">${t.nombre}<span class="nivel">${t.nivel}</span></span>`).join('')
      : '<span class="vacio">Sin tecnologías cargadas.</span>';
  } catch {
      // Agregar despues
  }
}

async function cargarProyectos() {
  try {
    const respuesta = await fetch(`${API}/`, { credentials: 'include' });
    if (!respuesta.ok) throw new Error();
    const proyectos = await r.json();
    const cont = document.getElementById('lista-proyectos');

    if (!proyectos.length) {
      cont.innerHTML = '<p class="vacio">Todavía no cargaste proyectos.</p>';
      return;
    }

    cont.innerHTML = proyectos.map(p => `
      <div class="proyecto">
        <h3>${p.nombre_proyecto}</h3>
        <p>${p.descripcion}</p>
        <p style="margin-top:.4rem;font-size:.75rem;">
          Etapa: <strong>${p.etapa}</strong> ·
          Creado: ${new Date(p.fecha_creacion).toLocaleDateString('es-AR')}
        </p>
      </div>
    `).join('');
  } catch {
    // Agregar despues
  }
}

// Boton para editar usuario
document.getElementById('btn-editar').addEventListener('click', 
 () => {window.alert("Aca se va a poder editar el perfil de usuario")});
// Boton para editar passaword
document.getElementById('btn-password').addEventListener('click', 
 () => {window.alert("Aca se va a poder cambiar la contraseña")});

// Cargo todo
cargarUsuario();
cargarHabilidades();
cargarProyectos();