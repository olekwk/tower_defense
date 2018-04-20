

#planned=[Soldier(0,0),Soldier(0,0),Soldier(0,0),Soldier(0,0)]


from maps import TimeController

class Enemy (object):

	def __init__(self,x,y):
		self.x = x
		self.y = y
		self.award = 10
		self.can_fly = False
		self.time = 3
		self.st = self.time
		self.ds = 3
		self.life = 3
		self.speed = 1/self.time
		self.sign = 'E'
		self.effects=[]
		self.player_awarded = False
		self.dead = False
		self.frozen =False
	def do_effect(self):
		for effect in self.effects:
			effect.apply_effect(self)
			
	

	def update(self,board,player):
	
		if self.life >0:
			
			if not self.frozen:
				
				if self.x%4==0:
					if self.y+1>board.w-1:
						if board.struct[self.x+1][self.y].content=='.':
							self.x+=1
							board.struct[self.x][self.y].content=self
							board.struct[self.x-1][self.y].content='.'
			
					else:
						if board.struct[self.x][self.y+1].content=='.':
							self.y+=1
							board.struct[self.x][self.y].content=self
							board.struct[self.x][self.y-1].content='.'
			
				elif self.x%4 ==2:
					if self.y-1<0:
						if board.struct[self.x+1][self.y].content=='.':
							self.x+=1
							board.struct[self.x][self.y].content=self
							board.struct[self.x-1][self.y].content='.'
		
					else:
						if board.struct[self.x][self.y-1].content=='.':
							self.y-=1
							board.struct[self.x][self.y].content=self
							board.struct[self.x][self.y+1].content='.'
			
				else:
					if board.struct[self.x+1][self.y].content=='.':
						self.x+=1
						board.struct[self.x][self.y].content=self
						board.struct[self.x-1][self.y].content='.'
					
			TimeController.add_task(self.update,TimeController.t+self.time,board,player)
					
		else:
			board.struct[self.x][self.y].content='.'
			if not self.player_awarded:
				player.credit+=self.award
				self.player_awarded = True
				self.dead = True
	

		
			
			
class Heli(Enemy):

	def __init__(self,x,y):
		Enemy.__init__(self,x,y)
		self.time = 1
		self.sign = 'H'
		self.speed=1/self.time
		self.can_fly = True
		self.life = 3
	def display(self):
		return 'Heli'+'( '+str(self.life)+' )'
	def __str__(self):
		return 'H'

class Tank(Enemy):

	def __init__(self,x,y):
		Enemy.__init__(self,x,y)
		self.time = 5
		self.sign = 'D'
		self.speed=1/self.time
		self.can_fly = False
		self.life =11
	def display(self):
		return 'Tank'+'( '+str(self.life)+' )'
	def __str__(self):
		return 'D'

class Soldier(Enemy):

	def __init__(self,x,y):
		Enemy.__init__(self,x,y)
		self.time = 2
		self.sign = 'M'
		self.speed=1/self.time
		self.can_fly = False
		self.life = 5
	def display(self):
		return 'Soldier'+'( '+str(self.life)+' )'
	def __str__(self):
		return 'M'

