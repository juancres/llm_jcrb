Interfaz de usuario con Ollama y Javascript
0. Introducción
Creación de una aplicaciones web que realizan consultas a modelos de lenguaje largo mediante la API REST de Ollama.

1. Servidor web
Estas aplicaciones estan diseñadas con HTML5, Bootstrap 5) y Javascript, y funciona sobre cualquier servidor web que se tenga disponible, por ejemplo Apache2, nginx, etc. Para este ejemplo se veran 2 opciones:

El servidor web intergrado de python3.
Utilizando twisted.
2. Instalación de los servidores web
2.1 Servidor web de python
En el caso de http.server es un módulo define clases para implementar servidores HTTP y se encuentra presintalada.

$ python3 -m http.server 8080
2.2 Twistted de python
1.2.1 Instalación de twistted

$ python3 -m pip install twisted
1.2.2 Ejecución del servidor

$ python3 -m twisted web --path .
