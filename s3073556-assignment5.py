import matplotlib.pyplot as plt
import numpy as np

#Adding meals at random intervals
def meal(sugar, start_glu_conc = 1.2):
	dt = 1 #timestep in minutes
	stop_time = 240  #Stop time in minutes
	abs_rate = 0.002 #glucose absorption rate in g/l/min
	c_glu = start_glu_conc #glucose concentration in blood in g/l
	glu_data = []
	total_absorbed_glu = 0

	for t in np.arange(0, stop_time, dt):
		while total_absorbed_glu < sugar:
			c_glu += abs_rate
			total_absorbed_glu += abs_rate
			glu_data += [c_glu]

	return glu_data

#This function simulates the glucose decrease from insulin
def add_insulin(dose, start_ins_conc = 0, start_glu_conc = 1.2):
	dt = 1 #timestep in minutes
	stop_time = 240  #Stop time in minutes
	
	depot = dose #unabsorbed insulin in g/l, starting value is dose
	c_ins = start_ins_conc #insulin concentration in blood in g/l
	c_glu = start_glu_conc #glucose concentration in blood in g/l

	ka = 0.04 #absorption rate constant in /min
	ke = 0.15 #elimination rate constant in /min
	keff = 0.15 #effect rate constant
	ins_data = []
	glu_data = []

	#This pharmacokinetic equation simulates insulin concentrations
	for t in np.arange(0, stop_time, dt):
		d_depot = (-ka*depot)*dt
		d_ins = (ka*depot - ke*c_ins)*dt
		depot += d_depot
		c_ins += d_ins
		ins_data += [c_ins]

	#This pharmacodynamic equation simulates the effect of insulin on glucose concentrations.
	for c in ins_data:
		c_glu += -keff*c
		glu_data += [c_glu]

	return ins_data, glu_data
