cdef extern from "math.h":
	double sqrt(double x)

cdef class Planet(object):
	cdef public double x, y, z, vx, vy, vz, m	
	
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
		
cdef void single_step(Planet planet, double dt):
	"""Make a single time step"""
	cdef double distance, Fx, Fy, Fz, x, y ,z
	
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
	
cdef void step_time(Planet planet, double time_span, int n_steps):
	"""Make a number of time steps forward """
	cdef double dt
	cdef int j
	
	dt = time_span / n_steps
	
	for j in range(n_steps):
		single_step(planet, dt)
		
def main():
	planeta=Planet()
	step_time(planeta,1000,3000) 
	
