import csv
import random

def series_score(results, discard_number=1):
	'''
	A function which takes a set of results from a sailor in the form (bob",[2,4,1,1,2,5]) 
	and returns a score based on the scoring system. (Removing the lowest place and adding the rest togethor

	>>> series_score(("bob",[2,4,1,1,2,5]))
	10

	>>> series_score(("bob",[2,4,1,1,2,5]), 2)
	6

	>>> series_score(("Alice",[1,2,1,1,1,1]))
	5

	>>> series_score(("bob",[2,4,1,1,2,5]),2)
	6

	'''
	sorted_results=sorted(results[1])
	#Sorts the positions in the second position of the list from highest to lowest and calls this sorted_results.
	return sum(sorted_results[0:(len(sorted_results)-discard_number)])
	#Slices list of sorted results from the 0th position up to the to the length of "sorted_results" minus the "discard_number" 
	#(This essentially creates a new list without the amount highest numbers in the list equivalent to the value of "discard_number")

def sort_series(sailors):
	"""
	A function which sorts a list of sailors in ascending order of their series scores, with ties being broken by how the sailors placed
	in their first races.
	
	>>> sort_series([("Alice", [1, 2, 1, 1, 1, 1]), ("Bob", [3, 1, 5, 3, 2, 5]), ("Clare", [2, 3, 2, 2, 4, 2]), ("Dennis", [5, 4, 4, 4, 3, 4]), ("Eva", [4, 5, 3, 5, 5, 3])])
	[('Alice', [1, 2, 1, 1, 1, 1]), ('Clare', [2, 3, 2, 2, 4, 2]), ('Bob', [3, 1, 5, 3, 2, 5]), ('Dennis', [5, 4, 4, 4, 3, 4]), ('Eva', [4, 5, 3, 5, 5, 3])]

	"""
	return sorted(sailors, key=lambda x: (series_score(x,1),x[1][0]))
	#Each item in the list will be given the value x e.g (x = ("Alice", [1, 2, 1, 1, 1, 1]), then x= ("Bob", [3, 1, 5, 3, 2, 5]) etc  )
	#The item will be sorted by the value series_score(x,1) from lowest to highest 
	#In the case of a tie it is then sorted by value x[1][0] from lowest to highest


with open('read_sailor_data.csv') as file:
	reader = csv.reader(file)
	x=[(row[0],(row[1],row[2])) for row in reader]
	del x[0]
	Sailor_data = dict(x)


def generate_performances(Sailor_data):
	"""
	A function to generate the performances of the sailors in their races.

	>>> random.seed(57)
	>>> generate_performances({'Alice': ('100', '0'), 'Bob': ('100', '5'), 'Clare': ('100', '10'), 'Dennis': ('90', '0'), 'Eva': ('90', '5')})
	{'Alice': 100.0, 'Bob': 105.76045089520113, 'Clare': 108.36452152548142, 'Dennis': 90.0, 'Eva': 96.10844089749128}
	"""
	return dict([(x, random.normalvariate( int(Sailor_data[x][0]), int( Sailor_data[x][1])))  for x in Sailor_data])

def calculate_finishing_order(sailor_performances):
	"""
	A function to generate the finishing order of the sailors from their performances.

	>>> {'Alice': 100.0, 'Bob': 105.76045089520113, 'Clare': 108.36452152548142, 'Dennis': 90.0, 'Eva': 96.10844089749128}
	['Clare', 'Bob', 'Alice', Eva', 'Dennis']
	"""
	sailor_performances = sorted( list(sailor_performances.items()) , key=lambda x:-x[1])
	return [sailor_name[0] for sailor_name in sailor_performances]


def Final_results(Sailor_data):
	count=0
	Final_Sailor_Results={"Alice": [], "Bob": [], "Clare": [], "Dennis": [], "Eva" : []}
	while count < 6: 
		finishing_order = calculate_finishing_order(generate_performances(Sailor_data))
		for x in range(0,5):
			Final_Sailor_Results[finishing_order[x]].append(int(x+1))
			Final_Sailor_Results
		count+=1
	return sort_series(list(Final_Sailor_Results.items()))
#for x in range()
