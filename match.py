import string
import Countries
import players
import os


class match():
	def __init__(self, team_a: string, team_b: string, is_KO: string, date: string, formation_for_team_A: string, formation_for_team_B: string, Team_A_Manager: string, Team_B_Manager: string):
		"""
			Everything defined here is before match information...	
		"""
		self.team_a = team_a
		self.team_b = team_b
		self.is_KO = is_KO
		self.date = date
		self.team_A_formation = formation_for_team_A
		self.team_B_formation = formation_for_team_B
		self.Manager_A = Team_A_Manager
		self.Manager_B = Team_B_Manager

	# def players_for_team_A(self ,team_A_goals:int , team_B_goals:int ):
	# 	self.team_A_goals = team_A_goals
	# 	self.team_B_goals = team_B_goals
	# 	self.team_A_players_list = []
	# 	for i in lst_of_players:
	# 		self.team_A_players_list.append(i)
	def show_Preveiw(self):
		if(self.is_KO == "YES" or self.is_KO == "Yes" or self.is_KO=="yes" or self.is_KO[0] == 'y'):
			print("It is a Knock Out match." , end=" ")
		else:
			print("It is not a Knock Out match." , end=" ");
		print("Where Team:", self.team_a , "will play against Team:" ,self.team_b,"on the date:" ,self.date, "The managers are respectively: " ,self.Manager_A , "and" ,self.Manager_B);



def Create_a_match():
	is_KO = input("Is it a knock out match:(Y/N): ")
	team_A = input("Enter the name of the team : ")
	team_B = input("Enter the name of the team : ")
	path_A = ("C:\\Users\\Teertha\\Desktop\\python\\project\\World Cup 2022 record\\players\\" + str(team_A))
	path_B = ("C:\\Users\\Teertha\\Desktop\\python\\project\\World Cup 2022 record\\players\\" + str(team_B))
	if (os.path.exists(path_A) == False or os.path.exists(path_B) == False):
		print("One of the teams Does not exist... Can't start match")
	else:
		date = input("What date the match was played(Y/N)?: ")
		formation_for_A = input("What is the formation for team_A: ")
		formation_for_B = input("What is the formation for team_B: ")
		Manager_A = input("Who is the manager of team A?: ")
		Manager_B = input("Who is the manager of team B?: ")
		new_match = match(team_A , team_B , is_KO , date , formation_for_A , formation_for_B , Manager_A , Manager_B);
		new_match.show_Preveiw()


Create_a_match()
