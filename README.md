# Dj-Car-Services
Dj-Car-Services es una aplicación de ejemplo desarrollada en Django que ofrece servicios de mantenimiento de vehículos. Este proyecto está diseñado para ser simple y servir como un ejemplo en la charla "Django Turbo Cargado". La aplicación incluye características básicas de gestión de servicios de mantenimiento de vehículos.

## Funcionalidades
* Registro y autenticación de usuarios.
* Gestión de vehículos (agregar, editar, eliminar).
* Programación de servicios de mantenimiento.
* Registro de servicios realizados.
* Visualización de historial de mantenimiento.

## Requisitos de Instalación
Antes de ejecutar la aplicación, asegúrate de tener Python y Django instalados en tu sistema. Puedes instalar Django utilizando pip:

```bash
pip install Django
```

A continuación, sigue estos pasos para ejecutar el proyecto:

1. Clona este repositorio:

```bash
git clone https://github.com/emilioferreyra/dj-car-services.git
```

2. Navega al directorio del proyecto:

```bash
cd dj-car-services
```

3. Crea un entorno virtual (opcional pero recomendado):

```bash
python -m venv venv
```

4. Activa el entorno virtual:

* En Windows:

```bash
venv\Scripts\activate
```

* En macOS y Linux:

```bash
source venv/bin/activate
```

5. Instala las dependencias del proyecto:

```bash
pip install -r requirements.txt
```

6. Inicia el servidor de desarrollo de Django:

```bash
python manage.py runserver
```

La aplicación estará disponible en http://127.0.0.1:8000/. Puedes acceder al panel de administración en http://127.0.0.1:8000/admin/.

## Uso

Accede al panel de administración para gestionar vehículos, servicios programados y servicios realizados.

**Usuario**: admin

**Contreseña**: demolition

## Capturas de pantalla:

Sitio de administración de django usando Django Jazzmin:

<img src="docs/images/Django-Jazzmin.png" width="800" height="500" />

Sitio de administración de Django por defecto:

<img src="docs/images/Django-Admin.png" width="800" height="500" />

Los usuarios pueden registrar sus vehículos, programar servicios de mantenimiento y ver su historial de mantenimiento.

## Recursos y fuentes de documentación:

Para acceder a la página del proyecto Django, Django-Jazzmin, Django-Packages favor hacer clic [aquí](https://bit.ly/3FUfrEb) 
o escanear el siguiente **código QR**:

<img src="docs/images/bit.ly_3FUfrEb.png" width="400" height="400" />

## Contribuciones
¡Las contribuciones son bienvenidas! Si deseas mejorar esta aplicación de ejemplo, siéntete libre de bifurcar el 
repositorio y enviar tus solicitudes de extracción.

## Licencia
Este proyecto se distribuye bajo la Licencia MIT. Para más detalles, consulta el archivo LICENSE.