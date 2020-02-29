import io
import cv2
from PIL import Image
from six import StringIO
import requests


cap = cv2.VideoCapture(0)
while True:
    ret, frame = cap.read()

    cv2.imshow('frame', frame)
    frame_im = cv2.cvtColor(frame, cv2.COLOR_BGR2RGB)
    pil_im = Image.fromarray(frame_im)
    stream = io.BytesIO()
    pil_im.save(stream, format="JPEG")
    stream.seek(0)
    img_for_post = stream.read()    
    headers = {'Content-type': 'image/jpeg'} 
    files = {'image': img_for_post}
    response = requests.get(
         url='http://localhost:8080/reconocer', headers = headers, files=files)

cap.release()
cv2.destroyAllWindows()
