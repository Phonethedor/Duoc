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
        }
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
        }
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
        }
    });

    $("#recuperar").validate({
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
        submitHandler: function () { alert("Se ha enviado contraseña al correo") }
    });

    $("#new-product").validate({
        rules: {
            Categoria: {
                required: true
            },
            Proveedor: {
                required: true
            },
            Marca: {
                required: true
            },
            Tipo: {
                required: true
            },
            Nombre: {
                required: true
            },
            Precio: {
                required: true,
                number: true
            },
            Stock: {
                required: true,
                number: true
            }
        },
        messages: {
            Categoria: {
                required: "Ingrese categoria"
            },
            Proveedor: {
                required: "Ingrese proveedor"
            },
            Marca: {
                required: "Ingrese marca"
            },
            Tipo: {
                required: "Ingrese tipo"
            },
            Nombre: {
                required: "Ingrese nombre"
            },
            Precio: {
                required: "Ingrese precio",
                number: "Ingrese precio valido"
            },
            Stock: {
                required: "Ingrese stock",
                number: "Ingrese stock valido"
            }
        }
    });

    $("#edit-product").validate({
        rules: {
            Categoria: {
                required: true
            },
            Proveedor: {
                required: true
            },
            Marca: {
                required: true
            },
            Tipo: {
                required: true
            },
            Nombre: {
                required: true
            },
            Precio: {
                required: true,
                number: true
            },
            Stock: {
                required: true,
                number: true
            }
        },
        messages: {
            Categoria: {
                required: "Ingrese categoria"
            },
            Proveedor: {
                required: "Ingrese proveedor"
            },
            Marca: {
                required: "Ingrese marca"
            },
            Tipo: {
                required: "Ingrese tipo"
            },
            Nombre: {
                required: "Ingrese nombre"
            },
            Precio: {
                required: "Ingrese precio",
                number: "Ingrese precio valido"
            },
            Stock: {
                required: "Ingrese stock",
                number: "Ingrese stock valido"
            }
        }
    });

    $("#btn1").bind("click", function(e) {
        $(e.target).closest("#1").css("display", "none");
    });

    $("#btn2").bind("click", function(e) {
        $(e.target).closest("#2").css("display", "none");
    });

    $("#btn3").bind("click", function(e) {
        $(e.target).closest("#3").css("display", "none");
    });
});
