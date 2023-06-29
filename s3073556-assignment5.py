import matplotlib.pyplot as plt
import numpy as np

#Adding meals at random intervals
def meal(sugar):
	abs_rate = 0.002 #glucose absorption rate in g/l/min
	c_glu = 0 #glucose concentration in blood in g/l
	glu_up_data = []
	total_absorbed_glu = 0
	abs_time = 0 #time it takes to absorb the sugar in min
	
	while total_absorbed_glu < sugar:
		c_glu += abs_rate
		total_absorbed_glu += abs_rate
		glu_up_data += [c_glu]
		abs_time += 1

	return glu_up_data, abs_time

#This function simulates the glucose decrease from insulin
def add_insulin(dose, start_glu_conc):
	dt = 1 #timestep in minutes
	ins_time = 0 #time it takes for the insulin to return to the baseline
	
	depot = dose #unabsorbed insulin in g/l, starting value is dose
	c_ins = 0 #insulin concentration in blood in g/l
	c_glu = start_glu_conc #glucose concentration in blood in g/l

	ka = 0.04 #absorption rate constant in /min
	ke = 0.15 #elimination rate constant in /min
	keff = 0.15 #effect rate constant
	ins_data = []
	glu_down_data = []

	#This pharmacokinetic equation simulates insulin concentrations
	while c_ins > 0.01 or depot > 0.01:
		d_depot = (-ka*depot)*dt
		d_ins = (ka*depot - ke*c_ins)*dt
		depot += d_depot
		c_ins += d_ins
		ins_data += [c_ins]
		ins_time += 1

	#This pharmacodynamic equation simulates the effect of insulin on glucose concentrations.
	for c in ins_data:
		c_glu += -keff*c
		glu_down_data += [c_glu]

	return ins_data, glu_down_data, ins_time

repeat = True
while repeat:
	sugar_input = float(input("How much sugar does your meal contain in grams?"))
	#SUGAR INPUT NAAR G/L???
	glu_up_data, abs_time = meal(sugar_input)
	#DOSIS BEREKENEN

	ins_data, glu_down_data, ins_time = add_insulin(0.5, glu_up_data[-1])

	total_time = abs_time + ins_time
	glu_data = glu_up_data + glu_down_data

	plt.plot(np.arange(abs_time, total_time, 1), ins_data, label="Insulin concentration in blood (g/l), change from baseline")
	plt.plot(np.arange(0, total_time, 1), glu_data, label="Glucose concentration in blood (g/l), change from baseline")
	plt.legend()
	plt.show()

	again_input = input("Calculate again? (y/n)")
	if x == "y":
		repeat = True
	else:
		repeat = False
