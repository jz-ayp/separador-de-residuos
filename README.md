# Separador de residuos
 
## Descripción 
En una ciudad X, de la que no te contaré su nombre, existen 51 rellenos sanitarios y vertederos para arrojar los desechos de la población, pero 15 de ellos están a punto de colapsar. Esta ciudad, a pesar de ser la tercera más grande de su país, no cuenta con un sistema moderno y tecnológico para la separación de residuos y deja todo el trabajo a recolectores y pepenadores, los cuales, claramente, no se dan abasto. 

Por la falta de legislación y normas, así como de la falta de conciencia  ciudadana para reducir la cantidad de desechos y hacer separación de residuos desde el hogar, te das cuenta de lo crítico de la situación, y desde tu carrera de ingeniería, decides poner manos a la obra para prevenir un desastre ecológico. 

Junto con un equipo multidisciplinario de ingenieros, has realizado el diseño de una máquina que reciba y separe de manera eficiente y rápida los residuos; sólo falta el software; este claro, es tu trabajo desde tu asignatura de programación. 

Este reto consiste en que realices el programa que separará los residuos. Cada bloque de residuos es una cadena de caracteres (llamémosle *S*) y los residuos serán etiquetados con números del `1` al `4`, para identificar principalmente cuatro residuos en una primera etapa. Cualquier otro tipo de 
residuo que recibas en la cadena *S* será de otra categoría y pasará a otro proceso de separación. 

Separarás y darás un resumen al final de cuántos residuos se separaron de cada tipo; así como cuántos residuos pasaron a la siguiente etapa de separación. 

Los caracteres en la cadena tendrán el siguiente significado:

1 – Plástico

2 – Papel y cartón 

3 – Vidrio 

4 – Metales 

Cualquier otro – Otro tipo de residuos 

## Restricciones
La longitud de la cadena *S* será de entre 1 y 1024 caracteres.

## Entradas 
Una única entrada con la cadena *S*, donde encontrarás números del 1 al 4, además de otros caracteres. 

## Salidas 
Cinco números enteros separados por un único espacio, que serán la cantidad de residuos de cada tipo que se separaron por bloque, iniciando por los residuos tipo 1, luego los de tipo 2, y así sucesivamente, y al final los de otro tipo. 

## Ejemplos de entradas y salidas
 
### Ejemplo 1
Entrada | Salida
--------|-------
`A2\131444411(124` | `5 2 1 5 3`
 
### Ejemplo 2
Entrada | Salida
--------|-------
`3H1/41432e22613i223414131!12Y1m` | `8 6 5 4 8`
 
### Ejemplo 3
Entrada | Salida
--------|-------
`d302131` | `2 1 2 0 2`

***Fuente***: Problema propuesto por la maestra Tere Loza para el concurso interno de programación del ITESO en otoño de 2019.