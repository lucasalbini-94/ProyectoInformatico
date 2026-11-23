import Ajv from 'ajv';
import addFormats from 'https://cdn.jsdelivr.net/npm/ajv-formats@3.0.1/dist/ajv-formats.min.js';

// js/registro.js
(function () {
    'use strict';

    // --- 1. Captura de elementos del DOM ---
    const form = document.getElementById('form-registro');
    const mensajeGlobal = document.getElementById('mensaje');

    // Inputs por nombre (usaremos el atributo name que coincide con el schema)
    const inputs = {
        nombre: document.getElementById('nombre'),
        apellido: document.getElementById('apellido'),
        nombreUsuario: document.getElementById('nombreUsuario'),
        email: document.getElementById('email'),
        password: document.getElementById('password'),
        password2: document.getElementById('password2')
    };

    // Spans de error (usando data-error-for)
    const errorSpans = {};
    document.querySelectorAll('[data-error-for]').forEach(span => {
        errorSpans[span.dataset.errorFor] = span;
    });

    // Botones de mostrar/ocultar contraseña
    const botonesVer = document.querySelectorAll('[data-ver]');

    const ajv = new Ajv({ allErrors: true });
    addFormats(ajv);

})();
