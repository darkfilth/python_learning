student_number = ['1413', '1534', '1354', '3125']
print "What student number do you know?"
number = raw_input('> ')
if number == 0 :
	print "His student number is %s" % student_number[0]
elif number == 1 :
	print "His student number is %s" % student_number[1]
elif number == 2 :
	print "His student number is %s" % student_number[2]
else : 
	print "His student number is %s" % student_number[3]
	
