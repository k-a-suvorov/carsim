try:
	
	
	#Block of input of user values
	speed = float(input("Какова средняя скорость вашего автомобиля? "))
	distance = float(input("Какова дистанция, которую надо проехать? "))
	expenses = float(input("Каков расход топлива на 100 километров? "))
	container = float(input("Каков объем бака машины? "))
	
	
	#Block of calculating the results of program
	time = round(distance / speed, 2)
	hours_expenses = round(container / expenses, 2)
	
	
	#Block of outputs of the results of program
	print(F'Часов в дороге {time} и топливо закончится через {hours_expenses} часов.')
		 	
	if (hours_expenses < time):
		print("Запасов топлива в дорогу вам не хватит, дозаправте бак машины!.")
	elif (hours_expenses > time):
		print("Все в порядке, топлива хватит, можете ехать.")


except ValueError:
    print("You have some mistake of userinput current float Value")	
except TypeError:
    print("You have some mistake of userinput float Value!")
except SystemError:
	print("This is system mistake! Please don't panic! Relax!" )

