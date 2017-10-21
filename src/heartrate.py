import numpy as np
import matplotlib.pyplot as plt
import cv2

from src import comparationMethods
from math import pow, floor,log2

cap = cv2.VideoCapture('../res/videos/71.mp4')
#cap = cv2.VideoCapture('../res/videos/alonso.MOV')

length = int(cap.get(cv2.CAP_PROP_FRAME_COUNT))
width = int(cap.get(cv2.CAP_PROP_FRAME_WIDTH))
height = int(cap.get(cv2.CAP_PROP_FRAME_HEIGHT))
fps = cap.get(cv2.CAP_PROP_FPS)

r = np.zeros((1, length))
g = np.zeros((1, length))
b = np.zeros((1, length))

k = 0
while (cap.isOpened()):
    ret, frame = cap.read()

    if ret == True:
        r[0, k] = np.mean(frame[330:360, 610:640, 0])
        g[0, k] = np.mean(frame[330:360, 610:640, 1])
        b[0, k] = np.mean(frame[330:360, 610:640, 2])
    # print(k)
    else:
        break
    k = k + 1

cap.release()
cv2.destroyAllWindows()

n = int(pow(2,floor(log2(length))))
#Estudiar bien como se justifica ésto. Se calculaba así en la teoria.
f = np.linspace(-n / 2, n / 2 - 1, n) * fps / n

r = r[0, 0:n] - np.mean(r[0, 0:n])
g = g[0, 0:n] - np.mean(g[0, 0:n])
b = b[0, 0:n] - np.mean(b[0, 0:n])
R = np.abs(np.fft.fftshift(np.fft.fft(r))) ** 2
G = np.abs(np.fft.fftshift(np.fft.fft(g))) ** 2
B = np.abs(np.fft.fftshift(np.fft.fft(b))) ** 2

# plt.plot(60 * f, R)
# plt.xlim(0, 200)
# plt.savefig("plots/fR.png")
#
# plt.plot(60 * f, G)
# plt.xlim(0, 200)
# plt.xlabel("frecuencia [1/minuto]")
# plt.savefig("plots/fG.png")

plt.plot(60 * f, B)
plt.xlim(0, 200)
plt.savefig("../out/fB.png")

frecR = abs(f[np.argmax(R)]) * 60
frecB = abs(f[np.argmax(B)]) * 60
frecG = abs(f[np.argmax(G)]) * 60

x = np.array([frecR,frecR,frecG, frecG, frecB,frecB])
y = x#np.array([frecG,frecB, frecB, frecR,frecR,frecG])

comparationMethods.get_coefficient_of_determination(x, y)

print("Frecuencia cardíaca R: ", frecR, " pulsaciones por minuto")
print("Frecuencia cardíaca G: ", frecG, " pulsaciones por minuto")
print("Frecuencia cardíaca B: ", frecB, " pulsaciones por minuto")