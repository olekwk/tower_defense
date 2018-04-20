

class SlowEffect(object):
	
	def __init__(self):
		self.time=5	

	def add_effect(self, enemy):

		if enemy.sign == 'M':
			for i in enemy.effects:
				if type (i) == type(self):
					enemy.effects.remove(i)
			enemy.effects.append(self)

	def apply_effect (self,enemy):
				
		enemy.frozen=True

		self.time-=1
		if not self.time:
			enemy.effects.remove(self)
			enemy.frozen = False
class PoisonEffect(object):
	def __init__(self):
		self.time=3	
	def add_effect(self, enemy):
		if enemy.sign == 'D':
			enemy.effects.append(self)

	def apply_effect (self,enemy):
		
		if enemy.life>0:		
			enemy.life-=1

		self.time-=1
		if not self.time or enemy.life<=0:
			enemy.effects.remove(self)
		
