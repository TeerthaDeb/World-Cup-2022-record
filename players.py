import os
import string

class player():
	def __init__(self , name : string = "No Name", jersey_number : int = 0, country : string = "No Country", main_position : string = "default position", club : string = "No Club" , age : int = 0, minutes_played : int = 0, goal_scored : int = 0 , yellow_cards : int = 0 , red_cards : int = 0 , dribbles : int = 0 , shots : int = 0 , shots_on_target : int = 0 , fouls : int = 0 , saves : int = 0 , blocked : int = 0, successfull_tackels : int = 0 , assist : int = 0 , key_passes : int = 0, penalty_goals : int = 0):
		self.name = name
		self.country = country
		self.age = age
		self.club = club
		self.minutes_played = minutes_played
		self.goal_scored = goal_scored
		self.jersey = jersey_number
		self.yellow_cards = yellow_cards
		self.red_cards = red_cards
		self.dribbles = dribbles
		self.shots = shots
		self.shots_on_target = shots_on_target
		self.fouls = fouls
		self.saves = saves
		self.blocked = blocked
		self.successfull_tackels = successfull_tackels
		self.assist = assist
		self.key_passes = key_passes
		self.main_position = main_position
		self.penalty_goals = penalty_goals

	def show_player_details(self):
		print("name =" ,self.name , "\njersey =" , self.jersey , "\ncountry =" , self.country , "\nage= " ,self.age , "\nclub -" ,self.club , "\nminutes+played = " ,self.minutes_played , "\ngoals scored = " + str(self.goal_scored) + "(" + str(self.penalty_goals) + ")", "\nylw crds =" ,self.yellow_cards , "\nrd crds =" ,self.red_cards , "\nDribbles =" ,self.dribbles , "\nshots =" ,self.shots , "\nshots on target =" , self.shots_on_target , "\nfouls =" ,self.fouls , "\nsaves =" ,self.saves , "\nblocked =" , self.blocked , "\nsuccessfull tackles =" ,self.successfull_tackels , "\nassists =" ,self.assist , "\nkey_passes =" ,self.key_passes , "\nhe plays mainly as a" , self.main_position)
	
	def return_for_writting_into_file(self):
		return str( str(self.name) + "\n" + str(self.jersey) + "\n" + str(self.country) + "\n" + str(self.main_position) + "\n" + str(self.club) + "\n" + str(self.age) + "\n" + str(self.minutes_played) + "\n" + str(self.goal_scored) + "\n" + str(self.yellow_cards) + "\n" + str(self.red_cards) + "\n" + str(self.dribbles) + "\n" + str(self.shots) + "\n" + str(self.shots_on_target) + "\n" + str(self.fouls) + "\n" + str(self.saves) + "\n" + str(self.blocked) + "\n" + str(self.successfull_tackels) + "\n" + str(self.assist) + "\n" + str(self.key_passes) + "\n" + str(self.penalty_goals))

def add_player():
	Name = input("Enter the name of the player: ")
	Country = input("Enter his Country: ")
	Age = int(input("Enter his age: "))
	Jersey_Number = int(input("Enter his Jersey Number: "))
	Club = input("Enter his Club: ")
	Main_position = input("Enter his position: ")
	plr = player(Name , Jersey_Number , Country , Main_position , Club , Age)
	plr.show_player_details()
	path = ("C:\\Users\\Teertha\\Desktop\\python\\project\\World Cup 2022 record\\players\\" +str(Country))
	is_exist = os.path.exists(path)
	if(is_exist == False):
		os.makedirs(path)
	player_file_pointer =  open("C:\\Users\\Teertha\\Desktop\\python\\project\\World Cup 2022 record\\players\\" +str(Country)+ "\\" +str(Name)+ ".txt", "a+")
	player_file_pointer.write(str(plr.return_for_writting_into_file()))
	player_file_pointer.close

def read_a_player():
	Country = input("Enter the name of his country: ")
	path = ("C:\\Users\\Teertha\\Desktop\\python\\project\\World Cup 2022 record\\players\\" +str(Country))
	if(os.path.exists(path) == False):
		print("This Country is not listed yet...\n Update will come soon")
	else:
		Name = input("Enter the name of the player: ")
		path = ("C:\\Users\\Teertha\\Desktop\\python\\project\\World Cup 2022 record\\players\\" +str(Country)+ "\\" +str(Name)+ ".txt")
		if(os.path.exists(path) == False):
			print("This player is not listed yet. List will be updated soon...")
		else:
			player_file_pointer = open("C:\\Users\\Teertha\\Desktop\\python\\project\\World Cup 2022 record\\players\\" +str(Country)+ "\\" +str(Name)+ ".txt", "r")
			lst = player_file_pointer.read()
			details = lst.split('\n')
			plr = player(details[0] , details[1] , details[2] , details[3] , details[4] , details[5] , details[6] , details[7] , details[8] , details[9] , details[10] , details[11] , details[12] , details[13] , details[14] , details[15] , details[16] , details[17] , details[18] , details[19])
			os.system('cls')
			plr.show_player_details()
	player_file_pointer.close()
			
def modify_a_player():
	Country = input("Enter the name of his country: ")
	path = ("C:\\Users\\Teertha\\Desktop\\python\\project\\World Cup 2022 record\\players\\" +str(Country))
	if(os.path.exists(path) == False):
		print("This Country is not listed yet...\n Update will come soon")
	else:
		Name = input("Enter the name of the player: ")
		path = ("C:\\Users\\Teertha\\Desktop\\python\\project\\World Cup 2022 record\\players\\" +str(Country)+ "\\" +str(Name)+ ".txt")
		if(os.path.exists(path) == False):
			print("This player is not listed yet. List will be updated soon...")
		else:
			player_file_pointer = open("C:\\Users\\Teertha\\Desktop\\python\\project\\World Cup 2022 record\\players\\" +str(Country)+ "\\" +str(Name)+ ".txt", "r")
			lst = player_file_pointer.read()
			details = lst.split('\n')
			plr = player(details[0] , details[1] , details[2] , details[3] , details[4] , details[5] , details[6] , details[7] , details[8] , details[9] , details[10] , details[11] , details[12] , details[13] , details[14] , details[15] , details[16] , details[17] , details[18] , details[19])
			os.system('cls')
			plr.show_player_details()
			mod = int(input("What do you want to modify?\n[1] name\n[2] jersey_number\n[3] country\n[4] main_position\n[5] club\n[6] age\n[7] minutes played\n[8] goal_scored\n[9] yellow_cards\n[10] red_cards\n[11] dribbles\n[12] shots\n[13] shots_on_target\n[14] fouls\n[15] saves\n[16] blocked \n[17] successfull_tackels\n[18] assists\n[19] Key_Passes\n[20] Penalty Goals\nSelect your option: "))
			print(plr.name+"'s current is: "+details[mod -1])
			entry = input("Enter the new entry: ")
			details[mod -1] = entry
			if(mod == 3):
				player_file_pointer.close()
				os.remove("C:\\Users\\Teertha\\Desktop\\python\\project\\World Cup 2022 record\\players\\" +str(Country)+ "\\" +str(Name)+ ".txt")
				Country = details[2]
				path = ("C:\\Users\\Teertha\\Desktop\\python\\project\\World Cup 2022 record\\players\\" +str(Country))
				if(os.path.exists(path) == False):
					print("This Country is not listed yet...\n Update will come soon")
					return
			plr = player(details[0] , details[1] , details[2] , details[3] , details[4] , details[5] , details[6] , details[7] , details[8] , details[9] , details[10] , details[11] , details[12] , details[13] , details[14] , details[15] , details[16] , details[17] , details[18] , details[19])
			player_file_pointer =  open("C:\\Users\\Teertha\\Desktop\\python\\project\\World Cup 2022 record\\players\\" +str(Country)+ "\\" +str(Name)+ ".txt", "w+")
			player_file_pointer.write(str(plr.return_for_writting_into_file()))
	player_file_pointer.close()

def delete_a_player():
	Country = input("Enter the name of his country: ")
	path = ("C:\\Users\\Teertha\\Desktop\\python\\project\\World Cup 2022 record\\players\\" +str(Country))
	if(os.path.exists(path) == False):
		print("This Country is not listed yet...\n Update will come soon")
	else:
		Name = input("Enter the name of the player: ")
		path = ("C:\\Users\\Teertha\\Desktop\\python\\project\\World Cup 2022 record\\players\\" +str(Country)+ "\\" +str(Name)+ ".txt")
		if(os.path.exists(path) == False):
			print("This player is not listed yet. List will be updated soon...")
		else:
			player_file_pointer = open("C:\\Users\\Teertha\\Desktop\\python\\project\\World Cup 2022 record\\players\\" +str(Country)+ "\\" +str(Name)+ ".txt", "r")
			lst = player_file_pointer.read()
			details = lst.split('\n')
			plr = player(details[0] , details[1] , details[2] , details[3] , details[4] , details[5] , details[6] , details[7] , details[8] , details[9] , details[10] , details[11] , details[12] , details[13] , details[14] , details[15] , details[16] , details[17] , details[18] , details[19])
			os.system('cls')
			decision = input("are you sure that you want to delete "+plr.name+"'s profile [Y/N]? : ")
			if(decision[0] == 'Y' or decision[0] == 'y'):
				player_file_pointer.close()
				os.remove("C:\\Users\\Teertha\\Desktop\\python\\project\\World Cup 2022 record\\players\\" +str(Country)+ "\\" +str(Name)+ ".txt")
	player_file_pointer.close()

def run_player():
	print("[1] Add a Player\n[2] Read a player info\n[3] Modify a player info\n[4] Delete a player \n\n press your selection ...")
	ch = str(input())
	if(ch[0] == '1'):
		os.system('cls')
		add_player()
	elif(ch[0] == '2'):
		os.system('cls')
		read_a_player()
	elif(ch[0] == '3'):
		os.system('cls')
		modify_a_player()
	elif(ch[0] == '4'):
		os.system('cls')
		delete_a_player()
	ch = input("Want to run again?[Y/N]: ")
	if(ch == 'y' or ch == 'Y'):
		run_player()

#run_player()