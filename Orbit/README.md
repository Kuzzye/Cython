<p align="center">
<FONT FACE="times new roman" SIZE=5>
<br>
<img src="https://res-5.cloudinary.com/crunchbase-production/image/upload/c_lpad,h_256,w_256,f_auto,q_auto:eco/v1455514364/pim02bzqvgz0hibsra41.png"
width="200" height="200">
</img>
<br>
<i><b>Docente:</b></i> John Corredor, PhD.
<br>
<i><b>Asignatura:</b></i> Parallel and Distributed Computing.
<br>
<i><b>Estudiantes:</b><br>Kevin Fabian Chepe<br>
<i><b>Tema:</b></i> Ejercicio Planeta Orbita
<br>
09/11/22
<br>
</FONT>
</p>

**Resumen**

La siguiente actividad tiene como objetivo expandir y aclarar los conceptos de Cython, mediante el ejercicio de la orbita de un planeta, esto para comprobar que cython puede presentar mejores significativas con respecto a python.

**Introducción**

Cython es un lenguaje de programación que combina Python con el sistema de datos de C, los mismos métodos que se ejecutan en Python pero con definiciones de C.

**Objetivo**

Analizar los resultados que se obtuvieron de la practica mediante graficas dentro de un cuaderno en Google Colaboratory para poder ver la mejora que representa Cython frente a Python.

**Ejecución**

Se tendrán en cuenta  5 ficheros los cuales son los siguientes

**py_planet_orbit.py**
Este fichero es el código puro en Python proporcionado.

**cy_planet_orbit.pyx**
Este fichero es la solución que se encontró en cython, lo mismo que en python pero con definiciones en C.

**setup.py**
El fichero de Setup son las instrucciones para ejecutar el fichero de cython con sus respectivos módulos, esto para evitar confusiones y promover buenas practicas.

**prueba_tierra.py**
Este fichero es la ejecución de los dos versiones del programa, la de Python y la de Cython, se le envían valores reales obtenidos de internet y mediante módulos para medir el tiempo se obtienen los valores de ejecución de cada versión.

**Makefile**
Este fichero automatiza el proceso de compilación del proyecto.

**Resultados**

* Comparativa de Rendimiento individual por lenguaje

![imagen](https://user-images.githubusercontent.com/79543099/200901496-964c0462-76e8-4e15-9e49-15cda5058135.png)

* Comprativa de rendimiento de Python vs Cython mediantes un grafico de barras para ver el rendimiento que hubo en cada iteracción de la ejecución.

![imagen](https://user-images.githubusercontent.com/79543099/200901678-7f4fc7d8-f9fa-4b3e-b7a6-e73592cafd8e.png)

* Comprativa de rendimiento de Python vs Cython mediantes un grafico de lineas para ver el rendimiento que significativo que demuestra Cython

![imagen](https://user-images.githubusercontent.com/79543099/200901782-fa6aef47-09ca-4dfa-bf79-718572e4ac4d.png)

**Conclusiones**

* De Cython se puede concluir que es un lenguaje bastante eficiente que combina lo mejor de dos lenguajes como lo son Python y Cython, es la traducción directa de un código de Python.

* Cython es mucho mas rápido al combinar lenguajes de alto nivel como lo es Python como su sintaxis simple y fácil de trabajar y de bajo nivel como lo es C con sus definiciones que proporcionan mayor rendimiento.

* Se logro demostrar que para este caso Cython es casi 18 veces mas rápido que Python.

* En las ejecuciones individuales de de Cython se puede apreciar que hubo variaciones muy pronunciadas debido a que la maquina estaba ejecutando otras aplicaciones en el momento de la ejecución principal.

**Referencias**

* M. Huls. "Cython for absolute beginners: 30x faster code in two simple steps". Medium. https://towardsdatascience.com/cython-for-absolute-beginners-30x-faster-code-in-two-simple-steps-bbb6c10d06ad (accedido el 9 de noviembre de 2022).
