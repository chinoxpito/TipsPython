#import cv2

"""
#imagenes
# cargar el archivo PNG indicado
img = cv2.imread('C:/Git/TipsPython/camara_web/Imagenes/43_spherespirals.jpg', cv2.IMREAD_GRAYSCALE)

# guardar la imagen en formato JPG
#cv2.imwrite('save.jpg', img)

# mostrar la imagen en una ventana
cv2.imshow('IMAGEN', img)


# esperar hasta que se presiona una tecla
cv2.waitKey(0)
#print("hola Mundo")

#VIDEOS

cap = cv2.VideoCapture(0)

while (True):
    ret, frame = cap.read()

    if ret:
        cv2.imshow('video', frame)

    if cv2.waitKey(1) & 0xFF == 27:
        break

cap.release()
cv2.destroyAllWindows()
"""
"""
cap = cv2.VideoCapture('C:/Git/TipsPython/camara_web/Videos/Pro.mp4')

# Definir el codec y crear el objeto VideoWriter
fourcc = cv2.VideoWriter_fourcc('M','S','V','C')
out = cv2.VideoWriter('output.mp4', fourcc, 25.0, (720, 528))

while(True):
    # capturar el cuadro
    ret, frame = cap.read()

    if ret:
        # procesar la captura, convertir a grises
        gray = cv2.cvtColor(frame, cv2.COLOR_BGR2GRAY)

        # escribir el cuadro procesado
        out.write(gray)

        # mostar la captura actual
        cv2.imshow('video', gray)

    # esperar, si se presiona la tecla ESC salir
    if cv2.waitKey(1) & 0xFF == 27:
        break

cap.release()
out.release()

cv2.destroyAllWindows()
"""
from cv2 import *

namedWindow("webcam")
vc = VideoCapture(0);
"""
while True:
    next, frame = vc.read()
    imshow("webcam", frame)
    if waitKey(50) >= 0:
        break;
"""
while True:
    next, frame = vc.read()

    gray = cvtColor(frame, COLOR_BGR2GRAY)
    gauss = GaussianBlur(gray, (7,7), 1.5, 1.5)
    can = Canny(gauss, 0, 30, 3)

    imshow("webcam", can)

    if waitKey(50) >= 0:

        break;
#http://acodigo.blogspot.com/2013/06/acceso-la-webcam.html



