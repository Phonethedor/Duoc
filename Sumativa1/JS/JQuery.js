$(document).ready(function () {
    $("#register").validate({
        rules: {
            email: {
                required: true,
                email: true
            },
            nombre: {
                required: true,
                minlength: 3
            },
            pass1: {
                required: true,
                minlength: 10
            },
            pass2: {
                required: true,
                minlength: 10,
                equalTo: "#pass1"
            }
        },
        messages: {
            email: {
                required: "Ingrese un correo",
                email: "Ingrese un correo valido"
            },
            nombre: {
                requeired: "Ingrese un nombre",
                minlength: "El nombre debe contener minimo 3 caracteres"
            },
            pass1: {
                required: "Ingrese una contraseña",
                minlength: "La contraseña debe contener minimo 10 caracteres"
            },
            pass2: {
                required: "Ingrese nuevamente la contraseña",
                minlength: "La contraseña debe contener minimo 10 caracteres",
                equalTo: "La contraseña no es igual"
            }
        },
        success: "valido",
        submitHandler: function() { alert("Registrado con exito") }
    });

    $("#login").validate({
        rules: {
            email: {
                required: true,
                email: true
            },
            password: {
                required: true,
                minlength: 10
            }
        },
        messages: {
            email: {
                required: "Ingrese un correo",
                email: "Ingrese un correo valido"
            },
            password: {
                required: "Ingrese contraseña",
                minlength: "Ingrese una contraseña valida"
            }
        },
        success: "valido",
        submitHandler: function() { alert("Ha ingresado con exito!") }
    });

    $("#edit").validate({
        rules: {
            email: {
                required: true,
                email: true
            },
            nombre: {
                required: true,
                minlength: 3
            },
            pass1: {
                required: true,
                minlength: 10
            },
            pass2: {
                required: true,
                minlength: 10,
                equalTo: "#pass1"
            }
        },
        messages: {
            email: {
                required: "Ingrese un correo",
                email: "Ingrese un correo valido"
            },
            nombre: {
                requeired: "Ingrese un nombre",
                minlength: "El nombre debe contener minimo 3 caracteres"
            },
            pass1: {
                required: "Ingrese una contraseña",
                minlength: "La contraseña debe contener minimo 10 caracteres"
            },
            pass2: {
                required: "Ingrese nuevamente la contraseña",
                minlength: "La contraseña debe contener minimo 10 caracteres",
                equalTo: "La contraseña no es igual"
            }
        },
        success: "valido",
        submitHandler: function() { alert("Datos editados con exito") }
    });

    $("#edit").validate({
        rules: {
            email: {
                required: true,
                email: true
            }
        },
        messages: {
            email: {
                required: "Ingrese un correo",
                email: "Ingrese un correo valido"
            }
        },
        success: "valido",
        submitHandler: function() { alert("Se ha enviado contraseña al correo") }
    });
});
