filename = 'fileprocessor.input'
infile = open(filename, 'r')
list = []
print("Printing out User Data:\n")
for line in infile:
	if(line[0] == '#'):
		print("The user "+line[1:6]+" is skipped because it starts with a hashtag (is commented out)")
	else:
		var = line.split(':')
		print("The user " + var[0],"has a password of "+var[1]+" and has a userid "+var[2],"and groupid " + var[3])

print('\n')
print("End of User Data")
