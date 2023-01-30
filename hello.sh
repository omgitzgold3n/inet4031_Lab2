#!/bin/bash

a=2
b=2
c=$((a + b))

echo "List of Users:"
UserStringArray=( User1 User2 User3 )
for i in "${UserStringArray[@]}"
do
	echo "$i"
done
echo "Bash says: Hello, World!"
echo "$a + $b = $c"

