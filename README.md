# Requerimientos
- Python
- Pip
- Token de autenticación a backend

Ejecutar en la carpeta donde se encuentra clonado el repo:

pip3 freeze >> requirements.txt

pip3 install -r requirements.txt

# Molinete - THEA

1 - Ejecutar python3-rest.py "token" para levantar el servicio de captura de imagenes que se invoca desde frontend.

Para invocar directamente a la captura de imagenes, se debe ejecutar app.py, ahi es donde se capturan las imagenes y se envian al backend. 

La cantidad de imagenes a enviar se determinan por el valor que se define en el ciclo While a la variable coun.t.

Unicamente se envian imagenes de cuando se detecta una cara enfrente a la camara.
