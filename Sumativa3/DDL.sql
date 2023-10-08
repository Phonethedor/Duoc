CREATE TABLE "ROL" (
	"id_rol" INT NOT NULL,
	"nombre_rol" NVARCHAR2(10) NOT NULL,
	constraint ROL_PK PRIMARY KEY ("id_rol"));

/
CREATE TABLE "USUARIO" (
	"id_usuario" INT ,
	"correo_usuario" NVARCHAR2(50) NOT NULL,
	"nombre_usuario" NVARCHAR2(50) NOT NULL,
	"pass_usuario" NVARCHAR2(50) NOT NULL,
	"rol_usuario" INT NOT NULL,
	constraint USUARIO_PK PRIMARY KEY ("id_usuario"));

CREATE sequence "USUARIO_ID_USUARIO_SEQ";

CREATE trigger "BI_USUARIO_ID_USUARIO"
  before insert on "USUARIO"
  for each row
begin
  select "USUARIO_ID_USUARIO_SEQ".nextval into :NEW."id_usuario" from dual;
end;

/
CREATE TABLE "Proveedor" (
	"id_proveedor" INT,
	"nombre_proveedor" NVARCHAR2(100) NOT NULL,
	constraint PROVEEDOR_PK PRIMARY KEY ("id_proveedor"));

CREATE sequence "PROVEEDOR_ID_PROVEEDOR_SEQ";

CREATE trigger "BI_PROVEEDOR_ID_PROVEEDOR"
  before insert on "Proveedor"
  for each row
begin
  select "PROVEEDOR_ID_PROVEEDOR_SEQ".nextval into :NEW."id_proveedor" from dual;
end;

/
CREATE TABLE "MARCA" (
	"id_marca" INT,
	"nombre_marca" NVARCHAR2(100) NOT NULL,
	constraint MARCA_PK PRIMARY KEY ("id_marca"));

CREATE sequence "MARCA_ID_MARCA_SEQ";

CREATE trigger "BI_MARCA_ID_MARCA"
  before insert on "MARCA"
  for each row
begin
  select "MARCA_ID_MARCA_SEQ".nextval into :NEW."id_marca" from dual;
end;

/
CREATE TABLE "CATEGORIA" (
	"id_categoria",
	"nombre_categoria" NVARCHAR2(100) NOT NULL,
	constraint CATEGORIA_PK PRIMARY KEY ("id_categoria"));

CREATE sequence "CATEGORIA_ID_CATEGORIA_SEQ";

CREATE trigger "BI_CATEGORIA_ID_CATEGORIA"
  before insert on "CATEGORIA"
  for each row
begin
  select "CATEGORIA_ID_CATEGORIA_SEQ".nextval into :NEW."id_categoria" from dual;
end;

/
CREATE TABLE "TIPO_PRODUCTO" (
	"id_tipo_producto" INT,
	"descripcion_tipo_producto" NVARCHAR2(100) NOT NULL,
	constraint TIPO_PRODUCTO_PK PRIMARY KEY ("id_tipo_producto"));

CREATE sequence "TIPO_PRODUCTO_ID_TIPO_PRODUCTO_SEQ";

CREATE trigger "BI_TIPO_PRODUCTO_ID_TIPO_PRODUCTO"
  before insert on "TIPO_PRODUCTO"
  for each row
begin
  select "TIPO_PRODUCTO_ID_TIPO_PRODUCTO_SEQ".nextval into :NEW."id_tipo_producto" from dual;
end;

/
CREATE TABLE "PRODUCTO" (
	"id_producto" INT,
	"nombre_producto" NVARCHAR2(50) NOT NULL,
	"descripcion_producto" NVARCHAR2(200) NOT NULL,
	"valor_producto" INT NOT NULL,
	"stock_producto" INT NOT NULL,
	"imagen_producto" NVARCHAR2(255) NOT NULL,
	"proveedor_producto" INT NOT NULL,
	"marca_producto" INT NOT NULL,
	"categoria_producto" INT NOT NULL,
	"tipo_producto" INT NOT NULL,
	constraint PRODUCTO_PK PRIMARY KEY ("id_producto"));

CREATE sequence "PRODUCTO_ID_PRODUCTO_SEQ";

CREATE trigger "BI_PRODUCTO_ID_PRODUCTO"
  before insert on "PRODUCTO"
  for each row
begin
  select "PRODUCTO_ID_PRODUCTO_SEQ".nextval into :NEW."id_producto" from dual;
end;

/
CREATE TABLE "VENTA" (
	"id_venta" INT,
	"producto" INT NOT NULL,
	"cantidad" INT NOT NULL,
	"total" INT NOT NULL,
	constraint VENTA_PK PRIMARY KEY ("id_venta"));

CREATE sequence "VENTA_ID_VENTA_SEQ";

CREATE trigger "BI_VENTA_ID_VENTA"
  before insert on "VENTA"
  for each row
begin
  select "VENTA_ID_VENTA_SEQ".nextval into :NEW."id_venta" from dual;
end;

/
CREATE TABLE "DETALLE_VENTA" (
	"id_detalle" INT,
	"usuario" INT NOT NULL,
	"ventas" INT NOT NULL,
	"created_at" TIMESTAMP NOT NULL,
	constraint DETALLE_VENTA_PK PRIMARY KEY ("id_detalle"));

CREATE sequence "DETALLE_VENTA_ID_DETALLE_SEQ";

CREATE trigger "BI_DETALLE_VENTA_ID_DETALLE"
  before insert on "DETALLE_VENTA"
  for each row
begin
  select "DETALLE_VENTA_ID_DETALLE_SEQ".nextval into :NEW."id_detalle" from dual;
end;

/

ALTER TABLE "USUARIO" ADD CONSTRAINT "USUARIO_fk0" FOREIGN KEY ("rol_usuario") REFERENCES "ROL"("id_rol");





ALTER TABLE "PRODUCTO" ADD CONSTRAINT "PRODUCTO_fk0" FOREIGN KEY ("proveedor_producto") REFERENCES "Proveedor"("id_proveedor");
ALTER TABLE "PRODUCTO" ADD CONSTRAINT "PRODUCTO_fk1" FOREIGN KEY ("marca_producto") REFERENCES "MARCA"("id_marca");
ALTER TABLE "PRODUCTO" ADD CONSTRAINT "PRODUCTO_fk2" FOREIGN KEY ("categoria_producto") REFERENCES "CATEGORIA"("id_categoria");
ALTER TABLE "PRODUCTO" ADD CONSTRAINT "PRODUCTO_fk3" FOREIGN KEY ("tipo_producto") REFERENCES "TIPO_PRODUCTO"("id_tipo_producto");

ALTER TABLE "VENTA" ADD CONSTRAINT "VENTA_fk0" FOREIGN KEY ("producto") REFERENCES "PRODUCTO"("id_producto");

ALTER TABLE "DETALLE_VENTA" ADD CONSTRAINT "DETALLE_VENTA_fk0" FOREIGN KEY ("usuario") REFERENCES "USUARIO"("id_usuario");
ALTER TABLE "DETALLE_VENTA" ADD CONSTRAINT "DETALLE_VENTA_fk1" FOREIGN KEY ("ventas") REFERENCES "VENTA"("id_venta");

