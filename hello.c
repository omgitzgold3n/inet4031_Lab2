#include <stdio.h>

 int main() {

	int a = 2;
	int b = 2;
	int c = a + b;
	char listOfUsers[3][6] = {"User1","User2","User3"};
	printf("List of Users:\n");
	for(int i=0; i<3; i++){
		printf("%s\n", listOfUsers[i]);
	}
	printf("C says: Hello, World!\n");
	printf("%d + %d = %d\n", a,b,c);

	return 0;
}
