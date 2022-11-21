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
<i><b>Estudiantes:</b><br>Kevin Fabian Chepe<br>David Santiago Zárate<br>
<i><b>Tema:</b></i> Parcial Final
<br>
23/11/22
<br>
</FONT>
</p>

**Resumen**

La siguiente actividad tiene como objetivo aplicar los conceptos de Cython, mediante tres diferentes algoritmos, esto para comprobar que cython puede presentar mejores significativas con respecto a python.

**Introducción**

Cython es un lenguaje de programación que combina Python con el sistema de datos de C, los mismos métodos que se ejecutan en Python pero con definiciones de C.

**Objetivo**

Analizar los resultados que se obtuvieron de la practica mediante graficas dentro de un cuaderno en Google Colaboratory para poder ver la mejora que representa Cython frente a Python.

**Ejecución**

Para cada culquiera de los 3 ejericios, se tendrán en cuenta 5 ficheros los cuales son los siguientes:

**(fichero).py**
Este fichero es el código puro en Python proporcionado.

**(fichero).pyx**
Este fichero es la solución que se encontró en cython, lo mismo que en python pero con definiciones en C.

**setup.py**
El fichero de Setup son las instrucciones para ejecutar el fichero de cython con sus respectivos módulos, esto para evitar confusiones y promover buenas practicas.

**prueba_(fichero).py**
Este fichero es la ejecución de los dos versiones del programa, la de Python y la de Cython, se prueba el algoritmo y mediante módulos para medir el tiempo se obtienen los valores de ejecución de cada versión.

**Makefile**
Este fichero automatiza el proceso de compilación del proyecto.

**Resultados**

>>Ejercicio 1
>>- Algoritmo Factorial
>>* Comparativa de Rendimiento individual por lenguaje
>>![imagen](https://user-images.githubusercontent.com/79543099/202951563-84c5f72a-4f02-49fc-8153-4343a88f9705.png)
>>* Comprativa de rendimiento de Python vs Cython mediantes un grafico de barras para ver el rendimiento que hubo en cada iteracción de la ejecución.
>>![imagen](https://user-images.githubusercontent.com/79543099/202951645-bbab069a-1b99-437a-b9c4-bce023adbffd.png)
>>* Comprativa de rendimiento de Python vs Cython mediantes un grafico de lineas para ver el rendimiento que significativo que demuestra Cython
>>![imagen](https://user-images.githubusercontent.com/79543099/202951694-0378716c-e48e-4d74-871e-f36472325c87.png)


>>Ejercicio 2
>>- Algoritmo Números primos
>>* Comparativa de Rendimiento individual por lenguaje
>>![imagen](https://user-images.githubusercontent.com/79543099/202952036-79d2087a-1b71-47c7-aadc-d4668b5116db.png)
>>* Comprativa de rendimiento de Python vs Cython mediantes un grafico de barras para ver el rendimiento que hubo en cada iteracción de la ejecución.
>>![imagen](https://user-images.githubusercontent.com/79543099/202952095-808a94e7-1253-4b5b-aa0f-b06e19983bd6.png)
>>* Comprativa de rendimiento de Python vs Cython mediantes un grafico de lineas para ver el rendimiento que significativo que demuestra Cython
>>![imagen](https://user-images.githubusercontent.com/79543099/202952122-d58a744e-42ce-4747-9254-e3363f7fc04e.png)


>>Ejercicio 3
>>- Algoritmo Sumatoria de multiplos
>>* Comparativa de Rendimiento individual por lenguaje
>>![imagen](https://user-images.githubusercontent.com/79543099/202952199-c2201a77-3d0e-45e5-9317-f1d4a1d33b13.png)
>>* Comprativa de rendimiento de Python vs Cython mediantes un grafico de barras para ver el rendimiento que hubo en cada iteracción de la ejecución.
>>![imagen](https://user-images.githubusercontent.com/79543099/202952228-37ea18a9-261e-47ca-98b2-7b533e3a223f.png)
>>* Comprativa de rendimiento de Python vs Cython mediantes un grafico de lineas para ver el rendimiento que significativo que demuestra Cython
>>![imagen](https://user-images.githubusercontent.com/79543099/202952260-020c290b-7ddf-43e9-a23d-1f06f2620ae0.png)

**Analisis**

* En el algoritmo de Factorial se evidencia que cython muchos mas rápido ya que es un ejercicio simple que depende de una iteración y cython resuelve todos los problemas de python al momento de definir los tipos de datos y de esta manera se obtiene un rendimiento de casi 500 veces mas rápido la ejecución de cython con números grandes.

* Para el segundo y tercer ejercicio fue aproximadamente 10 veces mas rápido con cython

* Los ejercicios realizados a primera vista pueden parecer algo sencillos, pero son muy prácticos ya que en estos se realizan diferentes operaciones, lo cual hace que se pueda determinar de una mejor manera que tanta es la diferencia entre python y cython

**Conclusiones**

* Como se puede observar en las graficas cuando se ejecuta el programa por medio de python se tiene un tiempo mucho mayor. Los resultados de Cython se reduce en casi un 90% el tiempo. Esto se da ya que al mezclar código de Python y C, Python se puede ajustar a la velocidad de C ajustando tan solo algunos tipos de declaraciones y realizando algunas modificaciones en el código

* Cython es mucho mas rápido al combinar lenguajes de alto nivel como lo es Python como su sintaxis simple y fácil de trabajar y de bajo nivel como lo es C con sus definiciones que proporcionan mayor rendimiento.

* En las ejecuciones individuales de de Cython se puede apreciar lo estable que fue ya que la maquina solo estaba ejecutando el programa en ese momento y se puede evidenciar uno que otro pico de perdida de rendimiento que se puede identificar como un cuello de botella. (Se recomienda el no uso de la maquina mientras ejecuta los programas).

**Referencias**

* M. Huls. "Cython for absolute beginners: 30x faster code in two simple steps". Medium. https://towardsdatascience.com/cython-for-absolute-beginners-30x-faster-code-in-two-simple-steps-bbb6c10d06ad 

* Qué es la función factorial y cómo usarla - Paso a paso. (s. f.). Factorial RH - El Software de Recursos Humanos todo en uno. https://factorial.mx/numero-funcion-factorial

* Cython: C-Extensions for Python. (s. f.). Cython: C-Extensions for Python. https://cython.org/
