import csv

def series_score(results, discard_number):
	'''
	A function which takes a set of results from a sailor in the form (bob",[2,4,1,1,2,5]) 
	and returns a score based on the scoring system. (Removing the lowest place and adding the rest togethor

	>>> series_score(("bob",[2,4,1,1,2,5]),1)
	10

	>>> series_score(("Alice",[1,2,1,1,1,1]),1)
	5

	>>> series_score(("bob",[2,4,1,1,2,5]),2)
	6

	'''
	sorted_results=sorted(results[1])
	return sum(sorted_results[0:(len(sorted_results)-discard_number)])
	#This code sorts the list in order from lowest to highest from the 0th value of the list up to the (n - discard_number) value of 
	#the list where n = the length of the list. This essentially creates a new list without the amount of highest values equivalent 
	#to the value of the "discard_number" e.g (if the discard number is 2 a new list without the 2 highest numbers is created)
	#The list is then summed which will give the desired score.


def sort_series(sailors):
	"""
	A function which sorts a list of sailors in ascending order of their series scores, with ties being broken by how the sailors placed
	in their first races.
	
	>>> sort_series([("Alice", [1, 2, 1, 1, 1, 1]), ("Bob", [3, 1, 5, 3, 2, 5]), ("Clare", [2, 3, 2, 2, 4, 2]), ("Dennis", [5, 4, 4, 4, 3, 4]), ("Eva", [4, 5, 3, 5, 5, 3])])
	[('Alice', [1, 2, 1, 1, 1, 1]), ('Clare', [2, 3, 2, 2, 4, 2]), ('Bob', [3, 1, 5, 3, 2, 5]), ('Dennis', [5, 4, 4, 4, 3, 4]), ('Eva', [4, 5, 3, 5, 5, 3])]
	"""
	return sorted(sailors, key=lambda x: (series_score(x,1),x[1][0]))

with open('read_sailor_data.csv') as file:
	reader = csv.reader(file)
	x=[(row[0],(row[1],row[2])) for row in reader]
	del x[0]
	print(dict(x))
