# Fichero para la creación del objeto Compartido

from distutils.core import setup, Extension
from Cython.Build import cythonize

exts = (cythonize("cy_primo.pyx"))

setup(ext_modules = exts)
