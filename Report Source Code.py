from Question_1 import *
import matplotlib.pyplot as plt

def Multiple_tests(Number_of_tests):
	Count_2=0
	All_positions = {"Alice" : {1: 0 , 2: 0 , 3: 0 , 4: 0, 5: 0 }, "Bob" : {1: 0 , 2: 0 , 3: 0 , 4: 0, 5: 0 }, "Clare" : {1: 0 , 2: 0 , 3: 0 , 4: 0, 5: 0 }, "Dennis" : {1: 0 , 2: 0 , 3: 0 , 4: 0, 5: 0 }, "Eva" : {1: 0 , 2: 0 , 3: 0 , 4: 0, 5: 0 }}
	while Number_of_tests > Count_2:
		position=1
		for y in Final_results(Sailor_data):
			All_positions[y[0]][position]=(int(All_positions[y[0]][position]) + 1)
			position+=1
		Count_2+=1
	return All_positions


def Position_Percentage(Number_of_tests):
	All_positions = Multiple_tests(Number_of_tests)
	for y in All_positions:
		for x in range (1,6):
			print( str(y) + " " + str(x) + ": " + str( ( int( All_positions[y][x]) * 100 / int(Number_of_tests) ) ))

