#OpenCV module
import cv2
#Modulo para leer directorios y rutas de archivos
import os
#OpenCV trabaja con arreglos de numpy
import numpy
import sys

#Tamanio para reducir a miniaturas las fotografias
size = 4

#cargamos la plantilla e inicializamos la webcam
cap = cv2.VideoCapture(0)

img_width, img_height = 112, 92

#Ciclo para tomar fotografias
count = 0
while True:
    #leemos un frame y lo guardamos
    rval, img = cap.read()
    img = cv2.flip(img, 1, 0)

    #convertimos la imagen a blanco y negro
    gray = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)

    #redimensionar la imagen
    mini = cv2.resize(gray, (int(gray.shape[1] / size), int(gray.shape[0] / size)))

    """buscamos las coordenadas de los rostros (si los hay) y
   guardamos su posicion"""
    faces = face_cascade.detectMultiScale(mini)    
    faces = sorted(faces, key=lambda x: x[3])
    
    if faces:
        face_i = faces[0]
        (x, y, w, h) = [v * size for v in face_i]
        face = gray[y:y + h, x:x + w]
        face_resize = cv2.resize(face, (img_width, img_height))
        
        #Dibujamos un rectangulo en las coordenadas del rostro
        cv2.rectangle(img, (x, y), (x + w, y + h), (0, 255, 0), 3)
        #Ponemos el nombre en el rectagulo
        cv2.putText(img, "CARA", (x - 10, y - 10), cv2.FONT_HERSHEY_PLAIN,1,(0, 255, 0))        
        # invocar servicio con la cara
        sleep(1000)

    sleep(250)

    #Mostramos la imagen
    cv2.imshow('OpenCV Entrenamiento de '+nombre, img)
