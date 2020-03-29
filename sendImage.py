# OpenCV module
import cv2
# Modulo para leer directorios y rutas de archivos
import os
# OpenCV trabaja con arreglos de numpy
import numpy
# Obtener el nombre de la persona que estamos capturando
import sys
import time
import requests
from PIL import Image
from six import StringIO
import io
from matplotlib import pyplot

def start():
    # Tamanio para reducir a miniaturas las fotografias
    size = 4
    # cargamos la plantilla e inicializamos la webcam
    face_cascade = cv2.CascadeClassifier('haarcascade_frontalface_default.xml')
    cap = cv2.VideoCapture(0)
    # Contador
    count = 0

    # Obtenemos las imagenes del feed de videoclo pa
    while count < 3:
        # leemos un frame y lo guardamos
        rval, imgraw = cap.read()
        # print("Read and image, result : " + str(rval))
        img = cv2.flip(imgraw, 1, 0)
        # convertimos la imagen a blanco y negro
        gray = cv2.cvtColor(imgraw, cv2.COLOR_BGR2GRAY)

        # redimensionar la imagen
        mini = cv2.resize(gray, (int(gray.shape[1] / size), int(gray.shape[0] / size)))

        """buscamos las coordenadas de los rostros (si los hay) y
       guardamos su posicion"""
        faces = face_cascade.detectMultiScale(mini)
        faces = sorted(faces, key=lambda x: x[3])

        if faces:
            print("Se detecto una cara")
            #face_i = faces[0]
            #(x, y, w, h) = [v * size for v in face_i]
            #face = gray[y:y + h, x:x + w]
            #face_resize = cv2.resize(face, (img_width, img_height))

            # TODO: invocar backend para determinar la identidad de la persona
            cv2.imwrite("NewCara{}.jpg".format(count), img=img)
            stream = io.BytesIO()
            data = open("NewCara{}.jpg".format(count), 'rb').read()
            stream.seek(0)
            r = requests.post("http://localhost:8085/save", data=data)
            print("status code: " + str(r.status_code))
            count= count + 1

        # Si se presiona la tecla ESC se cierra el programa
        key = cv2.waitKey(10)
        if key == 27:
            cap.release()
            cv2.destroyAllWindows()
            break


if __name__ == '__main__':
    start()