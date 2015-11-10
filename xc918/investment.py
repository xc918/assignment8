#Author: Xing Cui
#NetID: xc918
#Data: 11/08


import numpy as np

class investment():
	"""
	This class takes an input calls initial_investment. It also gives a daily_investment according to
	num_trails and position.
	"""
	#test initial investment
	def __init__(self,initial_investment):
		if initial_investment > 0:
			self.initial_investment = initial_investment
		else: 
			raise ValueError
			print "position value should be positive."

	#get daily investment
	def daily_investment(self, position, num_trails):
		position_val = self.initial_investment/position
		cumu_ret = []
		daily_ret = []
		for i in range(num_trails):
			cumu_ret.append((np.random.choice([2,0], size = position, p = [0.51,0.49]).sum())*position_val)
		for ret in cumu_ret:
			daily_ret.append((ret/float(self.initial_investment))-1)
		return daily_ret

		

