#include <stdio.h>
#include <stdlib.h>
//The C program of the corresponding python program//
int main(void)
{
	int year;
	
	printf("What year do you want to check? : \n");
	scanf("%d", &year);
	
	if (year % 4 == 0)
		if (year % 100 == 0)
			if (year % 400 == 0)
				printf("Leap: Satisfied. It is a leap year.\n");
			else
				printf("Leap: Not satisfied. It is not a leap year.\n");
			else
				printf("Leap: Satisfied. It is a leap year.\n");
			else
				printf("Leap: Satisfied. It is not a leap year.\n");
			
			return(0);
}