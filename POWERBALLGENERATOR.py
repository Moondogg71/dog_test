import random
import time

print "\n"
print "Powerball Winning Numbers:\n"

print "How many sets to play? "
i = raw_input(">")
i = int(i)
counter = 1

while i > 0:
	print "\nPlay " + str(counter)
	win_numbers = sorted(random.sample(range(1,60), 5))
	powerball = sorted(random.sample(range(1,36), 1))
	print "Winning Numbers", win_numbers, "Powerball Number", powerball
	#print "Powerball Number", powerball
	print "\n"
	time.sleep(4)
	counter += 1  
	i -= 1


print "Good Luck!!!!!"	

print "\n"











