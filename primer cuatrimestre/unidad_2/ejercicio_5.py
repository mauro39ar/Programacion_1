#!/usr/bin/python

a=int(input("ingresa anio:  "))

if((a % 4 == 0) and (a % 100 != 0) or (a % 400 == 0)):
	
	print "ES bisiesto"
else:
    print "no es bisiesto"