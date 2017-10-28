import matplotlib.pyplot as plt

def plotRGB(R, G, B, f):
    plt.xlabel("frecuencia [1/minuto]")
    plt.plot(60 * f, R, "r")
    plt.xlim(0, 200)

    plt.plot(60 * f, G, "g")
    plt.xlim(0, 200)

    plt.plot(60 * f, B, "b")
    plt.xlim(0, 200)

    plt.show()