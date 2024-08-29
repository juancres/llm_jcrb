# llm_jcrb
Repositorio para creacion de lenguajes de programacion

# **1. Instalacion** #

1. Como primer paso descargar en Ollama en https://ollama.com/download/linux

```` bash
 Ejecutar curl -fsSL https://ollama.com/install.sh | sh

````
# **2. Ejecutar el servidor** #


Ejecutar el servidor de API REST de cliente con el siguiente comando:

```` bash

Ollama SERVE


````

# **3. Descargar un modelo** #


descargar el modelo con el siguiente comando:

```` bash

ollama pull tinyllama


````

# **4. Listar un modelo** #


Para lista los modelos descargado usar el siguiente comando:

```` bash

Ollama list


````


# **5. Correr el modelo** #


para ejecutar algun modelo descargado usar el siguiente comando:

```` bash

ollama run  tinyllama


````

# **6. Crear la API rest local** #

Enviar peticiones al servidor local formato streaming

```` bash
curl http://localhost:11434/api/generate -d '{
  "model": "tinyllama",
  "prompt": "Why is the sky blue?"
}
````


# **7. Crear la API rest local** #

Enviar peticiones al servidor local formato normal

```` bash
curl http://localhost:11434/api/generate -d '{
  "model": "tinyllama",
  "prompt": "Why is the sky blue?",
  "stream": false
}'
````


# **8. Comandos GITHUB** #

Enviar peticiones al servidor local formato normal

```` bash

git add .

git commit -m UPDATE README.md"

git push -u origin main

````


# ** wiki** #

sobre los temas de ia

```` bash
https://github.com/salvadorhm/introduccion_ia_generativa/wiki
````