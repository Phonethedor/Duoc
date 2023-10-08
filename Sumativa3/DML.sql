-- ROL
INSERT INTO "ROL"("id_rol", "nombre_rol")
VALUES (1, "admin");
INSERT INTO "ROL"("id_rol", "nombre_rol")
VALUES (2,"cliente");

-- USUARIO
INSERT INTO "USUARIO"("correo_usuario", "nombre_usuario", "pass_usuario", "rol_usuario")
VALUES ("admin@admin.cl", "Administrador_test", "Admin12!", 1);
INSERT INTO "USUARIO"("correo_usuario", "nombre_usuario", "pass_usuario", "rol_usuario")
VALUES ("cliente1@test.cl", "cliente_test1", "Cliente12!", 2);
INSERT INTO "USUARIO"("correo_usuario", "nombre_usuario", "pass_usuario", "rol_usuario")
VALUES ("cliente2@test.cl", "cliente_test2", "Cliente21!", 2);

-- PROVEEDOR
INSERT INTO "Proveedor" ("nombre_proveedor")
VALUES ("LAIKA");

-- MARCA
INSERT INTO "MARCA" ("nombre_marca")
VALUES ("PURINA DOG CHOW");
INSERT INTO "MARCA" ("nombre_marca")
VALUES ("PURINA CAT CHOW");
INSERT INTO "MARCA" ("nombre_marca")
VALUES ("SUNIPET");

-- CATEGORIA
INSERT INTO "CATEGORIA" ("nombre_categoria")
VALUES ("PERRO");
INSERT INTO "CATEGORIA" ("nombre_categoria")
VALUES ("GATO");
INSERT INTO "CATEGORIA" ("nombre_categoria")
VALUES ("MEDICINA");

-- TIPO_PRODUCTO
INSERT INTO "TIPO_PRODUCTO" ("descripcion_tipo_producto")
VALUES ("ALIMENTO");
INSERT INTO "TIPO_PRODUCTO" ("descripcion_tipo_producto")
VALUES ("MEDICINA");

-- PRODUCTO - PERRO
INSERT INTO "PRODUCTO" ("nombre_producto", "descripcion_producto", "valor_producto", "stock_producto", "imagen_producto". "proveedor_producto", "marca_producto", "categoria_producto", "tipo_producto")
VALUES ("Dog Chow - Adultos Todos Los Tamaños Pavo", "ALIMENTO COMPLETO PARA PERROS ADULTOS. Indicación: Alimento balanceado completo húmedo para perros adultos de todos los tamaños.", 800, 10, "imagenes/perro1.jpg", 1, 1, 1, 1);
INSERT INTO "PRODUCTO" ("nombre_producto", "descripcion_producto", "valor_producto", "stock_producto", "imagen_producto". "proveedor_producto", "marca_producto", "categoria_producto", "tipo_producto")
VALUES ("Dog Chow - Galletas Minis y Pequeños Sabor Pollo", "Galletas sabor pollo adultos minis y pequeños es una línea de galletas horneadas con cuidado especial y preparadas con granos integrales. Tu perro hace tu vida mejor. Juntos, hacemos mejor la suya.", 4400, 2, "imagenes/perro2.jpg", 1, 1, 1, 1);
INSERT INTO "PRODUCTO" ("nombre_producto", "descripcion_producto", "valor_producto", "stock_producto", "imagen_producto". "proveedor_producto", "marca_producto", "categoria_producto", "tipo_producto")
VALUES ("Dog Chow - Alimento Adulto Raza Mediana y Grande Carne Pollo", "Dog Chow® Salud Visible Adultos Medianos y Grandes con Carne y Pollo, un producto diseñado para brindarle una nutrición especifica para tu perro adulto mediano o grande que ayuda a mejorar su calidad de vida desde adentro hacia afuera de forma visible. Ahora con Extralife, una mezcla especial de antioxidantes, vitaminas y minerales que ayuda a maximizar la calidad de vida de tu perro día tras día.", 27400, 1, "imagenes/perro3.jpg", 1, 1, 1, 1);

-- PRODUCTO - GATO
INSERT INTO "PRODUCTO" ("nombre_producto", "descripcion_producto", "valor_producto", "stock_producto", "imagen_producto". "proveedor_producto", "marca_producto", "categoria_producto", "tipo_producto")
VALUES ("Cat Chow - Gatitos Pollo", "Purina Cat Chow gatitos sabor a pollo, nuevo alimento húmedo premium para tu gato. Es un alimento 100% completo y balanceado para gatos de 1 a 12 meses de edad de todas las razas.", 1000, 1, "imagenes/gato1.jpg", 1, 2, 2, 1);
INSERT INTO "PRODUCTO" ("nombre_producto", "descripcion_producto", "valor_producto", "stock_producto", "imagen_producto". "proveedor_producto", "marca_producto", "categoria_producto", "tipo_producto")
VALUES ("Cat Chow - Alimento Húmedo Gato Esterilizado Pescado Sobre", "Alimento húmedo 100% completo y balanceado para gatos esterilizados y/o castrados de todos los tamaños a partir de los 6 meses Cat Chow® con Pescado y Sin Colorantes. Con Hydro Defense Plus®, una combinación exclusiva de prebiótico natural, antioxidantes, vitaminas y minerales que ayudan a fortalecer las defensas naturales de tu gato. Contribuye a un tracto urinario saludable.", 900, 20, "imagenes/gato2.jpg", 1, 2, 2, 1);
INSERT INTO "PRODUCTO" ("nombre_producto", "descripcion_producto", "valor_producto", "stock_producto", "imagen_producto". "proveedor_producto", "marca_producto", "categoria_producto", "tipo_producto")
VALUES ("Cat Chow - Alimento Gato Adulto Defense Plus Carne", "Una buena nutrición es fundamental para proteger la salud de los gatos. Es por eso que desarrollamos Purina® Cat Chow® con Defense Plus®, elaborado con una selección de ingredientes naturales y mejorado, con la inclusión de un prebiótico natural. Defense Plus®, una combinación exclusiva de prebiótico natural, antioxidantes, vitaminas, y minerales que ayudan a fortalecer las defensas naturales de tu gato. Esto ayudará a promover un sistema inmune fuerte para proteger su estilo de vida único.", 6800, 32, "imagenes/gato3.jpg", 1, 2, 2, 1);

-- PRODUCTO - MEDICINA
INSERT INTO "PRODUCTO" ("nombre_producto", "descripcion_producto", "valor_producto", "stock_producto", "imagen_producto". "proveedor_producto", "marca_producto", "categoria_producto", "tipo_producto")
VALUES ("Sunipet - Cuidado Articular SuniFlex", "Suplemento alimenticio, desarrollado por veterinarios, que se centra en abordar la raíz del problema articular y de movilidad. Viene en forma de gomita para que sea más fácil de administrar. Apto para mascotas con alergia alimentaria.", 22100, 3, "imagenes/med1.jpg"), 1, 3, 3, 2;
INSERT INTO "PRODUCTO" ("nombre_producto", "descripcion_producto", "valor_producto", "stock_producto", "imagen_producto". "proveedor_producto", "marca_producto", "categoria_producto", "tipo_producto")
VALUES ("Sunipet - Calmante SuniCalm para Mascotas", "SuniCalm® es un tranquilizante 100% natural, desarrollado por veterinarios, que les ayuda a aliviar el estrés y problemas de comportamiento. Puede ser usado diariamente o como SOS. Apto para mascotas con alergia alimentaria. Ideal para calmar en navidad, año nuevo y vacaciones.", 19600, 2, "imagenes/med2.jpg", 1, 3, 3, 2);
INSERT INTO "PRODUCTO" ("nombre_producto", "descripcion_producto", "valor_producto", "stock_producto", "imagen_producto". "proveedor_producto", "marca_producto", "categoria_producto", "tipo_producto")
VALUES ("SuniCoat - Suplemento para piel y pelaje", "Es una poderosa fórmula de Omegas 3-6-9 (EPA y DHA, Vitamina E y Aceite de Salmón) es una combinación de ingredientes que fortalecen el sistema inmune de perros y gatos, su fórmula con OMEGA y Vitamina E, potencian una piel sana y un pelaje suave y brillante", 14990, 6, "imagenes/med3.jpg", 1, 3, 3, 2);