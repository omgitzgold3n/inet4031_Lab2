import sys


print("Printing out User Data:\n")

for line in sys.stdin:
	split = line.split(":")
	

	if(split[0][0] == "#"):
		print(split[0][1:6], "is skipped because it starts with a hashtag (is commented out)\n")

	else:
		print("The user " +split[0],"has a password of "+split[1]+" and has a userid "+split[2],"and groupid " + split[3])

print("End of User Data")
