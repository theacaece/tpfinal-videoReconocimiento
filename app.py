#OpenCV module
import cv2
#Modulo para leer directorios y rutas de archivos
import os
#OpenCV trabaja con arreglos de numpy
import numpy
#Obtener el nombre de la persona que estamos capturando
import sys
import time
import requests
from PIL import Image
from six import StringIO

from matplotlib import pyplot


def start():
    size = 4
    face_cascade = cv2.CascadeClassifier('haarcascade_frontalface_default.xml')
    cap = cv2.VideoCapture(0)

    img_width, img_height = 112, 92
    
    # Obtenemos las imagenes del feed de videoclo pa
    while True:
        #leemos un frame y lo guardamos
        rval, img = cap.read()
        # print("Read and image, result : " + str(rval))
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
    
            # TODO: invocar backend para determinar la identidad de la persona
            r = requests.post("http://localhost:8080/reconocer", data=img.tobytes())
            print("status code: " + str(r.status_code))
            # Determinar el nombre de la persona y etiquetar en el feed
            nombre = "persona"
            cv2.putText(img, nombre, (x - 10, y - 10), cv2.FONT_HERSHEY_PLAIN,1,(0, 255, 0))
    
    
        #Mostramos la imagen
        #cv2.imshow('Thea Molinete', img)
        #cv2.show()
        # print("mostrando imagen, se reconoció a una persona")
        #imgplot = pyplot.imshow(img)
        #pyplot.show()
    
        #Si se presiona la tecla ESC se cierra el programa
        key = cv2.waitKey(10)
        if key == 27:
            cap.release()
            cv2.destroyAllWindows()
            break

if __name__ == '__main__':
    start()