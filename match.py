import string
import Countries
import players
import os


class match():
	def __init__(self, team_a: string, team_b: string, is_KO: string, date: string, Team_A_Manager: string, Team_B_Manager: string):
		"""
			Everything defined here is before match information...	
		"""
		self.team_a = team_a
		self.team_b = team_b
		self.is_KO = is_KO
		self.date = date
		self.Manager_A = Team_A_Manager
		self.Manager_B = Team_B_Manager
	def show_Preveiw(self):
		if(self.is_KO == "YES" or self.is_KO == "Yes" or self.is_KO=="yes" or self.is_KO[0] == 'y'):
			print("It is a Knock Out match." , end=" ")
		else:
			print("It is not a Knock Out match." , end=" ")
		print("Where Team:", self.team_a , "will play against Team:" ,self.team_b,"on the date:" ,self.date, "The managers are respectively: " ,self.Manager_A , "and" ,self.Manager_B);
	def set_stat(self , formation_for_team_A: string, formation_for_team_B: string, goals_A , goals_B , possesion_A , possesion_B):
		self.goals_A = goals_A
		self.goals_B = goals_B
		self.possesion_A = possesion_A
		self.possesion_B = possesion_B
		self.team_A_formation = formation_for_team_A
		self.team_B_formation = formation_for_team_B
	def show_stat(self):
		print(str(self.team_a)+": <" , str(self.goals_A) , "-" , str(self.goals_B) , "> :" ,str(self.team_b) , "In the game, Team:" ,str(self.team_a) + "'s possesion was" , str(self.possesion_A) + "% And Team" , str(self.team_b) + "'s possesion was:" , str(self.possesion_B) + "%")
	def save_unfinished_match_for_a(self):
		return(str(str(self.is_KO) + '\n' + str(self.team_b) + "\n" + str(self.date) + "\n" + str(self.Manager_A) + "\n" + str(self.Manager_B)))
	def save_unfinished_match_for_b(self):
		return(str(str(self.is_KO) + '\n' + str(self.team_a) + "\n" + str(self.date) + "\n" + str(self.Manager_B) + "\n" + str(self.Manager_A)))


def Create_a_match():
	is_KO = input("Is it a knock out match:(Y/N): ")
	team_A = input("Enter the name of the team A: ")
	team_B = input("Enter the name of the team B: ")
	path_A = ("C:\\Users\\Teertha\\Desktop\\python\\project\\World Cup 2022 record\\players\\" + str(team_A))
	path_B = ("C:\\Users\\Teertha\\Desktop\\python\\project\\World Cup 2022 record\\players\\" + str(team_B))
	if (os.path.exists(path_A) == False or os.path.exists(path_B) == False):
		print("One of the teams Does not exist... Can't start match")
	else:
		date = input("What date the match was played: ")
		date = date.replace('/' , '_')
		date = date.replace('\\' , '_')
		Manager_A = input("Who is the manager of team A?: ")
		Manager_B = input("Who is the manager of team B?: ")
		new_match = match(team_A , team_B , is_KO , date , Manager_A , Manager_B);
		new_match.show_Preveiw()
		path = ("C:\\Users\\Teertha\\Desktop\\python\\project\\World Cup 2022 record\\players\\" +str(team_A)+ "\\Unfinished Matches")
		is_exist = os.path.exists(path)
		if(is_exist == False):
			os.makedirs(path)
		match_file_pointer = open("C:\\Users\\Teertha\\Desktop\\python\\project\\World Cup 2022 record\\players\\" +str(team_A)+ "\\Unfinished Matches\\" +str(date)+".txt" , "a+")
		match_file_pointer.write(str(new_match.save_unfinished_match_for_a()))
		match_file_pointer.close()
		path = ("C:\\Users\\Teertha\\Desktop\\python\\project\\World Cup 2022 record\\players\\" +str(team_B)+ "\\Unfinished Matches")
		is_exist = os.path.exists(path)
		if(is_exist == False):
			os.makedirs(path)
		match_file_pointer = open("C:\\Users\\Teertha\\Desktop\\python\\project\\World Cup 2022 record\\players\\" +str(team_B)+ "\\Unfinished Matches\\" +str(date)+".txt" , "a+")
		match_file_pointer.write(str(new_match.save_unfinished_match_for_b()))
		match_file_pointer.close()
		# print("Enter how many goals" , team_A , "Scored:" , end= " ") ; goals_A = int(input())
		# print("Enter how many goals" , team_B , "scored:" , end= " ") ; goals_B = int(input())
		# print("Enter the % of possesion for" , team_A , ":" , end= " ") ; Possesion_A = int(input())
		# print("Enter the % of possesion for" , team_B , ":" , end= " ") ; Possesion_B = int(input())
		# formation_for_A = input("What is the formation for team_A: ")
		# formation_for_B = input("What is the formation for team_B: ")
		# new_match.set_stat(formation_for_A , formation_for_B , goals_A , goals_B , Possesion_A , Possesion_B)
		# new_match.show_stat()
	
	

Create_a_match()
