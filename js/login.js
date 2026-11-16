document.addEventListener("DOMContentLoaded", () => {
    const formulario = document.getElementById("form-login");

    formulario.addEventListener("submit", (evento) => {
        evento.preventDefault();

        const email = document.getElementById("email").value;
        const password = document.getElementById("password").value;

        const datosLogin = {
            email: email,
            password: password
        };

        fetch("http://localhost:5000/api/login", {
            method: "POST",
            headers: {
                "Content-Type": "application/json"
            },
            body: JSON.stringify(datosLogin)
        })
        .then(respuesta => {
            console.log("Código de estado:", respuesta.status);
            return respuesta.json().then(datos => {
                if (!respuesta.ok) {
                    console.error("Respuesta del servidor:", datos);
                    throw new Error(datos.mensaje || "Error del servidor");
                }
                return datos;
            });
            
        })
        .then(datos => {
            console.log("Login exitoso. Token recibido:", datos.token);
            localStorage.setItem("token", datos.token);
        })
        .catch(error => {
            console.error("Error en el login:", error.message);
            alert("No se pudo iniciar sesión. Verificá tus datos.");
        });
    });
});