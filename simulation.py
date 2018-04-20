from maps import Board, Interface,TimeController
from towers import *
from enemies import *
import time

def cls():
	print ('\n'*10)

class GameBuilder(object):
	@staticmethod
	def build(waves,player_life):
		wav = WaveFactory()
		p=Player(player_life)
		s=Board()
		inter =Interface()
		
		return Game(s,waves,p,inter,wav)


	@staticmethod
	def process_input(game):
		while game.waves:
			planned=game.wav.create_wave(game.waves)[0:]
			game.interface.build_update(game.s,game.player,planned,game.waves,game.slw)
	
			#game.interface.update(game.s,planned)
			inp=input('Ustaw wieze na polu z # np 1 1 T(T,P,S) - nr_wiersza nr_kolumny rodzaj wiezy: ')
			gat=inp.strip().split(' ')
			if len(gat) == 3:
				try :
					x,y,t =int(gat[0]),int(gat[1]),gat[2]
					try:
						game.start_build(x,y,t)
						cls()
				

					except KeyError:
						print('Nie ma takiej wiezy dostępne litery to: ', ['T','P','S'])
				except ValueError:
					print('dwa pierwsze znaki musza byc liczbami')
	
			
			elif len(gat)==1:
		
				if gat[0]=='B':
			
					game.start_battle()
				elif gat[0]=='Q':
					break
				else:
					print('tylko B i Q')
			else:
				print('błedny input')
		


class Player(object):

	def __init__(self,credit,alive=True):
		self.alive=alive
		self.credit=credit
		
	def put_tower(self,x,y,tower,board):
		
		def pos(x,y):
			
			if tower.cost <= self.credit:
			
				if board.struct[x][y].content=='#':
					return True
			else:
				print('Nie Masz wystarczajacych srodkow')
			return False
			
	
		
				
		if pos(x,y):
			board.struct[x][y].content = tower
			for j in (x-1,x+1):
				for i in range(max(0,y-(tower.range-1)),min(y+tower.range-1,board.w-1)):
					board.struct[j][i].tower = tower
			
		
			self.credit-=tower.cost
			#slw.append(tower)
			return tower

class WaveFactory(object):
	
	def __init__(self):
		self.ns = ns={3:[Heli(0,0),Soldier(0,0),Soldier(0,0),Soldier(0,0),Soldier(0,0) ],2:[Heli(0,0),Soldier(0,0),Soldier(0,0),Soldier(0,0),  							Soldier(0,0),Tank(0,0)],1:[Heli(0,0),Heli(0,0),Soldier(0,0),Soldier(0,0),Soldier(0,0),Tank(0,0),Tank(0,0)] }
	def create_wave(self,wave):
		return self.ns[wave]	

class Game(object):
	towers = {'T':BasicTower,'P':PoisonTower,'S':SlowTower}
	def __init__(self,board,waves,player,interface,factory):
		self.slw = []
		self.sln = []
		self.s =board
		self.waves=waves
		self.player = player
		self.interface = interface
		self.wav = factory
	def start_build(self,x,y,tower):
		st = Game.towers[tower](x,y)
		slw = self.player.put_tower(x,y,st,self.s)
		if slw:
			self.slw.append(slw)

	def start_battle(self):
		planned=game.wav.create_wave(self.waves)[0:]

		for i in planned:
			i.update(self.s,self.player)		
		self.interface.war_update(self.s,self.slw,planned)
		for i in self.slw:
			i.attack()
	
		
		
		flag = True
		while flag:
			time.sleep(0.07)
			cls()
			TimeController.proces_task()
			
			pt = 0
			for i in planned:
				i.do_effect()
				if i.x == self.s.height - 1 and i.y == self.s.w - 1:
					flag = False
					self.waves = 0				
					print('Przegrałes !')
				if i.life <=0:
					pt+=1
			if pt == len(planned):
				flag = False 
				self.waves-=1
				if self.waves == 0:
					print ('Wygrałes')
				else:
					self.s = Board()
					self.slw = []
					self.sln = []
					TimeController.reset()
			
									
			
if __name__ =='__main__':					
	game = GameBuilder.build(3,35)
	GameBuilder.process_input(game)
			
		
		

	
	
	
						


		
