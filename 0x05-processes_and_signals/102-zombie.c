#include <stdlib.h>
#include <sys/types.h>
#include <unistd.h>
#include <stdio.h>

/**
 * infinite_while - Infinite while for manage zombie process
 * Void: No entry parameters
 * Return: exit 0 success
 */
int infinite_while(void)
{
	while (1)
	{
		sleep(1);
	}
	return (0);
}

/**
 * main - Main function zombie process
 * Void: No entry parameters
 * Return: Exit 0 success
 */
int main(void)
{
	pid_t child_pd;
	int num_of_proc;

	for (num_of_proc = 1; num_of_proc < 6; num_of_proc++)
	{
		child_pd = fork();
		if (child_pd > 0)
		{
			printf("Zombie process created, PID: %d\n", child_pd);
			sleep(1);
		}
		else
		{
			exit(0);
		}
	}
	infinite_while();
	return (0);
}
