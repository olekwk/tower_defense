


import time
class Field(object):
	def __init__(self,content):
		self.content = content
		self.tower = None

	def inform(self):
		if self.tower and self.content != '.':
			self.tower.enemy_to_attack.append(self.content)
	def __str__(self):
		return str(self.content)	
	def disp(self):
		print(self.content,end='')

class Board(object):
	w,height=30,13
	def __init__(self):
		self.w=Board.w
		self.h=Board.height
		l1,l2,l3 =['.']*self.w,['#']*self.w+['.'],['.']*self.w+['#']
		self.struct=[]
		#f1,f2 = Field('.'),Field('#')
		for i in range(self.h):
			if i%4==0 or i%4==2:
				self.struct.append([Field('.') for i in range(self.w)])
			elif  i%4==1:
				self.struct.append([Field('#') for i in range(self.w-1)]+[Field('.')])
			else:
				self.struct.append([Field('.')]+[Field('#') for i in range(self.w-1)])


class Interface(object):
	def __init__(self):
		self.time=1

	def build_update(self,board,player,planned,waves,slw):
		self.info_right=[['|'] for i in range(Board.height)]
		self.info_right[0].append('$  ')
		self.info_right[0].append(str(player.credit))
		kc=1
		for i in range(len(slw)):
			self.info_right[i+1].append(slw[i].display())
			kc+=1
		self.info_right[kc].append('Waves remaining: ' +str(waves))
		tp = {}
		for j in planned:
			if j.display() in tp:
				tp[j.display()]+=1
			else:
				tp[j.display()]=1
		ks=-1
		for j in tp:
			ks+=1
			self.info_right[kc+1+ks].append(j + ': '+ str(tp[j]))
		self.info_bottom ='B -- start battle, Q -- quit battle'
		kcp = [i+j for i,j in zip(board.struct,self.info_right)]
		for i in kcp:
			for j in i:
				try:
					
					j.inform()	
					
				except:
					pass
				print(j,end='')
			print('\n')
		
		print(self.info_bottom)	

	def war_update(self, board,towers,sln):
		
		self.info_right=[['|'] for i in range(Board.height)]		
		for i in range(len(sln)):
			if i<Board.height:
				self.info_right[i].append(sln[i].display())
		kcp = [i+j for i,j in zip(board.struct,self.info_right)]
		
		for i in towers:
			i.enemy_to_attack = []
		
		for i in kcp:
			for j in i:
				try:
					
					j.inform()	
					
				except:
					pass
				print(j,end='')
			print('\n')
		
		print(self.info_bottom)	
		TimeController.add_task(self.war_update,TimeController.t+self.time,board,towers,sln)
	
		
		
	
		
		
class TimeController(object):
	queue = []
	t = 0
	@staticmethod
	def add_task(task,time_b,*args,**kwargs):
		TimeController.queue.append((task,time_b,args,kwargs))
	
	@staticmethod
	def proces_task():
		
		kc=[]

		wit = TimeController.queue[:]
		git = []
		TimeController.queue = []
		for j,i in enumerate(wit):
			
		
			
			if i[1] == TimeController.t:
				f,t,args,kwargs = i
				f(*args,**kwargs)
					
			else:
				git.append(i)
		TimeController.queue = git[:]+TimeController.queue[:]	
	
		TimeController.t+=1
	@staticmethod
	def reset():
		TimeController.t=0
		TimeController.queue = []
	

