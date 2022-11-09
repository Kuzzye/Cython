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

#**Resumen**
La siguiente actividad tiene como objetivo expandir y aclarar los conceptos de Cython, mediante el ejercicio de la orbita de un planeta, esto para comprobar que cython puede presentar mejores significativas con respecto a python.

#**Introducción**
Cython es un lenguaje de programación que combina Python con el sistema de datos de C, los mismos métodos que se ejecutan en Python pero con definiciones de C.

#**Objetivo**
Analizar los resultados que se obtuvieron de la practica mediante graficas dentro de un cuaderno en Google Colaboratory para poder ver la mejora que representa Cython frente a Python.

#**Ejecución**
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

