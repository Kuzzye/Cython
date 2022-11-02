#cython: language_level=3

cimport cython

'''
Fecha: 2 - Noviembre - 2022
Autor: Kevin Fabian Chepe Astudillo
Tema: Programa en Cython para calcular la orbita de un planeta 
Materia: Parallel and Distributed Computing

'''

cdef extern from "math.h":
	double sqrt(double x) nogil

cdef class Planet(object):
	"""Declaración tipo de datos publica"""
	cdef public double x,y,z,vx,vy,vz,m	
	
	def __init__(self):
		# some initial position and velocity
		self.x = 1.0
		self.y = 0.0
		self.z = 0.0
		self.vx = 0.0
		self.vy = 0.5
		self.vz = 0.0
		
		# some mass
		self.m = 1.0

"""¿Qué pasa si distancia = 0?
Se usara un decorador de cython, para evitar
la división sobre cero, y no sea costo computacional """
@cython.cdivision(True)

cdef void single_step(Planet planet, float dt) nogil:
	"""Make a single time step"""
	cdef double distance,Fx,Fy,Fz
	
	# Compute force: gravity towards origin
	distance = sqrt(planet.x**2 + planet.y**2 + planet.z**2)
	Fx = -planet.x / distance**3
	Fy = -planet.y / distance**3
	Fz = -planet.z / distance**3
	
	# Time step position, according to velocity
	planet.x += dt * planet.vx
	planet.y += dt * planet.vy
	planet.z += dt * planet.vz
	
	# Time step velocity, according to force and mass
	planet.vx += dt * Fx / planet.m
	planet.vy += dt * Fy / planet.m
	planet.vz += dt * Fz / planet.m
	
def step_time(Planet planet, float time_span, int n_steps):
	"""Make a number of time steps forward """
	cdef float dt
	cdef int j
	dt = time_span/n_steps
	"""Habilitar la posibilidad de paralelismo"""
	with nogil:
		for j in range(n_steps):
			single_step(planet, dt)
		
	
