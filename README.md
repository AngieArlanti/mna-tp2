# Determinación de frecuencia cardíaca a partir de videos tomados con un teléfono celular

## Descripción
Determinación de la frecuencia cardíaca a partir de videos de 20-30 segundos tomados con un teléfono, tablet u otro dispositivo móvil a través de la Transformada Rápida de Fourier.

## Consideraciones sobre los videos 

### Formato de Nombre de Videos

Las pruebas que responden a los resultados se encuentran en el package “tests”. Las mismas leen automáticamente los videos del directorio “res/videos”. Pero sólo leerá aquellos videos cuyos nombres posean el formato “A-B-C.mp4”, donde:

- A: es un número entero de 2 o 3 dígitos, el cual representa el valor de frecuencia cardíaca tomado con otro medio, (en nuestro caso con la pulsera FitBit).
- B: sólo acepta las cadenas “led” o “sinled”. Es decir, indica si el video fue tomado con o sin led.
- C: Valor alfanumérico. Nombre o etiqueta del sujeto del que fue tomada la muestra.

#### Ejemplo de cadenas correctas: 

- 59-led-mujer1.mp4
- 59-sinled-mujer1.mp4
- 85-led-hombre1.mp4
- 85-sinled-hombre1.mp4
- etc.

### Descargar Videos
Como hemos tomado 18 muestras de videos y los mismos tienen un tamaño lo suficientemente grande como para dificultar la subida a Campus, decidimos dejar un link de descarga de los mismos. Recordar que para el correcto funcionamiento deben ser ubicados en la carpeta “res/videos”.

[Link de descarga](https://drive.google.com/open?id=0B3LIS_uzcS5ZSmF6bkRISlpMTUE)



