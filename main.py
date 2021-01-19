total_points = 0

for race in range (1,22):
	print ("Race Number", race)
	
	race_place = int(input('What posistion did you finsih in?:'))
	 
	if race_place == 1:
	 	points = 25
	elif race_place == 2:
	 	point = 18
	elif race_place == 3:
	 	points = 15
	elif race_place == 4:
	 	points = 12
	elif race_place == 5:
	 	points = 10
	elif race_place == 6:
	 	points = 8
	elif race_place == 7:
	 	points = 6
	elif race_place == 8:
	 	points = 4
	elif race_place == 9:
	 	points = 2
	elif race_place == 10:
	 	points = 1
	else:
		points = 0
	
	total_points = total_points + 25
	average = total_points / race
	print ("you have", total_points, "after race", race)
	print ("Your race average so far is", average)
	
print ("You have scored", total_points, "this season")
print ("and you had an average of", average, "this season")