from maps import TimeController

#planned=[Soldier(0,0),Soldier(0,0),Soldier(0,0),Soldier(0,0)]
from Effects import SlowEffect,PoisonEffect


class Tower(object):
	def __init__(self,x,y):
		self.range = 5
		self.cost = 10
		self.x=x
		self.y=y
		self.time = 11
		self.pt = 11
		self.fly = 0
		self.enemy_to_attack = []
	
	def attack (self):



		for enemy in self.enemy_to_attack:
			if enemy.life>0:
				if not self.fly and enemy.can_fly:
					pass
				else:
					enemy.life-=1
		
		
		if len(self.enemy_to_attack):
			TimeController.add_task(self.attack,TimeController.t+self.time)
		else:
			TimeController.add_task(self.attack,TimeController.t+1)
			
	
			
			
				
			
	
class BasicTower(Tower):
	def __init__(self,x,y):
		Tower.__init__(self,x,y)
	def attack(self):
		Tower.attack(self)
	
	def display(self):
		return 'Basic'+'( '+str(self.x) + ' , ' + str(self.y)+' )'
	def __str__(self):
		return 'T'

class SlowTower(Tower):
	def __init__(self,x,y):
		Tower.__init__(self,x,y)
		self.special = 5
		self.fly = 1
		self.range = 5
		self.time = 11
		self.k=self.time
		self.cost = 15

	def attack(self):
		Tower.attack(self)
		for enemy in self.enemy_to_attack:
			
			SlowEffect().add_effect(enemy)
		
	def display(self):
		return 'Slow'+'( '+str(self.x) + ' , ' + str(self.y)+' )'
	def __str__(self):
		return 'S'
		

class PoisonTower(Tower):
	def __init__(self,x,y):
		Tower.__init__(self,x,y)
		self.special = 2
		self.fly = 0
		self.range = 10
		self.time = 4
		self.k=self.time
		self.cost = 30

	def attack(self):
		Tower.attack(self)

		for enemy in self.enemy_to_attack:
			PoisonEffect().add_effect(enemy)
		
	def display(self):
		return 'Poison'+'( '+str(self.x) + ' , ' + str(self.y)+' )'
	def __str__(self):
		return 'P'
