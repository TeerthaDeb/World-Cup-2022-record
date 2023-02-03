import string
import players
import os
import shutil

class Contry():
	def __init__(self , name:string , continent:string , match_played : int , match_won : int , goals_scored : int , goals_acheived : int):
		self.name = name
		self.continent = continent
		self.match_played = match_played
		self.match_won = match_won
		self.goals_scored = goals_scored
		self.goals_acheived = goals_acheived
		self.path = ("C:\\Users\\Teertha\\Desktop\\python\\project\\World Cup 2022 record\\players\\" +str(self.name))
		if(os.path.exists(self.path) == False):
			os.makedirs(self.path)
			print("\n===============>>New Contry added")
		else:
			self.plr_lists = os.listdir(self.path)
			del self.plr_lists[self.plr_lists.index(str(name))]
	def show_details(self):
		print("Contry :" ,self.name , " continent =" ,self.continent , " Match_played =" ,self.match_played , " match_won =" ,self.match_won , " match lost =" ,int(self.match_played) - int(self.match_won) , " goal scored =" ,self.goals_scored , " goals acheived =" ,self.goals_acheived)
		if(os.listdir(self.path)):
			print("there are", len(self.plr_lists) , "and they are: ")
			str = [i.replace(".txt" , '') for i in self.plr_lists]
			print(str)
	def show_player_lists(self):
		for i in self.players_lists:
			print("name =" ,self.players_lists[i].name , "Jersey =" ,self.players_lists[i].jersey , "Position =" ,self.players_lists[i].main_position , "\n")
	def return_intfo_to_write_into_files(self):
		return str(str(self.name) + "\n" + str(self.continent) + "\n" + str(self.match_played) + "\n" + str(self.match_won) + "\n" + str(self.goals_scored) + "\n" + str(self.goals_acheived))

def add_country():
	Name_of_country = input("Enter the name of the country: ")
	if(os.path.exists("C:\\Users\\Teertha\\Desktop\\python\\project\\World Cup 2022 record\\players\\" +str(Name_of_country))):
		print("This country already in the system. You can modify the country but can not add another index for it.")
		return
	continent = input("Enter the continent: ")
	match_played = int(input("Enter the number of matches played: "))
	match_won = int(input("Enter the number of matches won: "))
	goal_scored = int(input("Enter the number of goals scored: "))
	goals_acheived = int(input("Enter the number of goals acheived: "))
	new_country = Contry(Name_of_country , continent , match_played , match_won , goal_scored , goals_acheived)
	new_country.show_details()
	contry_file_pointer = open("C:\\Users\\Teertha\\Desktop\\python\\project\\World Cup 2022 record\\players\\" +str(Name_of_country)+ "\\" +str(Name_of_country), "a+")
	contry_file_pointer.write(str(new_country.return_intfo_to_write_into_files()))
	contry_file_pointer.close()

def read_a_country():
	Name_of_country = input("Enter the name of the country: ")
	path = ("C:\\Users\\Teertha\\Desktop\\python\\project\\World Cup 2022 record\\players\\" +str(Name_of_country))
	if(os.path.exists(path) == False):
		print("This Country is not listed yet...\n Update will come soon")
	else:
		contry_file_pointer = open("C:\\Users\\Teertha\\Desktop\\python\\project\\World Cup 2022 record\\players\\" +str(Name_of_country)+ "\\" +str(Name_of_country), "r")
		lst = contry_file_pointer.read()
		lst = lst.split("\n")
		contry = Contry(lst[0] , lst[1] , lst[2] , lst[3] , lst[4] , lst[5])
		os.system('cls')
		contry.show_details()
		contry_file_pointer.close()

def delete_a_country():
	Name_of_country = input("Enter the name of the country: ")
	path = ("C:\\Users\\Teertha\\Desktop\\python\\project\\World Cup 2022 record\\players\\" +str(Name_of_country))
	if(os.path.exists(path) == False):
		print("This Country is not listed yet...\n Update will come soon")
	else:
		contry_file_pointer = open("C:\\Users\\Teertha\\Desktop\\python\\project\\World Cup 2022 record\\players\\" +str(Name_of_country)+ "\\" +str(Name_of_country), "r")
		lst = contry_file_pointer.read()
		lst = lst.split("\n")
		contry = Contry(lst[0] , lst[1] , lst[2] , lst[3] , lst[4] , lst[5])
		os.system('cls')
		contry.show_details()
		contry_file_pointer.close()
		choice = input("Do you want to delete the country?: [Y/N]")
		if(choice[0] == 'Y' or choice[0] == 'y'):
			# files_in_directory = os.listdir(path)
			# for i in files_in_directory:
			# 	os.remove(f'{path}/{i}')
			# os.remove(path)
			shutil.rmtree(path)
			print("Done deleting...")

def modify_a_country():
	Name_of_country = input("Enter the name of the country: ")
	path = ("C:\\Users\\Teertha\\Desktop\\python\\project\\World Cup 2022 record\\players\\" +str(Name_of_country))
	if(os.path.exists(path) == False):
		print("This Country is not listed yet...\n Update will come soon")
	else:
		contry_file_pointer = open("C:\\Users\\Teertha\\Desktop\\python\\project\\World Cup 2022 record\\players\\" +str(Name_of_country)+ "\\" +str(Name_of_country), "r")
		lst = contry_file_pointer.read()
		lst = lst.split("\n")
		contry = Contry(lst[0] , lst[1] , lst[2] , lst[3] , lst[4] , lst[5])
		os.system('cls')
		contry.show_details()
		contry_file_pointer.close()
		choice = input("Do you want to modify the country?: [Y/N]")
		if(choice[0] == 'Y' or choice[0] == 'y'):
			Name_of_country = input("Enter the name of the country(default: " + str(contry.name) + " ): ")
			continent = input("Enter the continent(default: " + str(contry.continent) + " ): ")
			match_played = int(input("Enter the number of matches played(default: " + str(contry.match_played) + " ): "))
			match_won = int(input("Enter the number of matches won(default: " + str(contry.match_won) + " ): "))
			goal_scored = int(input("Enter the number of goals scored(default: " + str(contry.goals_scored) + " ): "))
			goals_acheived = int(input("Enter the number of goals acheived(default: " + str(contry.goals_acheived) + " ): "))
			new_country = Contry(Name_of_country , continent , match_played , match_won , goal_scored , goals_acheived)
			new_country.show_details()
			contry_file_pointer = open("C:\\Users\\Teertha\\Desktop\\python\\project\\World Cup 2022 record\\players\\" +str(Name_of_country)+ "\\" +str(Name_of_country), "a+")
			contry_file_pointer.write(str(new_country.return_intfo_to_write_into_files()))
			contry_file_pointer.close()
		print("Done modifying")


def run_countries():
	print("[1] Add a Country\n[2] Read a country\n[3] Modify a countries info\n[4] Delete a Country\n[5] Run Players Menu \n\n press your selection ...")
	ch = str(input())
	if(ch[0] == '1'):
		os.system('cls')
		add_country()
	elif(ch[0] == '2'):
		os.system('cls')
		read_a_country()
	elif(ch[0] == '3'):
		os.system('cls')
		modify_a_country()
	elif(ch[0] == '4'):
		os.system('cls')
		delete_a_country()
	elif(ch[0] == '5'):
		os.system('cls')
		players.run_player()

#run_countries()