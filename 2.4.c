#include <stdio.h>
#include <stdlib.h>
#include <sys/types.h>
#include <sys/wait.h>
#include <unistd.h>
 
int main(void) {
  for(int i = 1; i < 13; i++) {
    pid_t pid = fork();
    char str1[20];
    if(pid == 0) {
      printf("Enter Child Name \n");
      scanf("%19s",str1);
      printf("%s \n",str1);
      exit(0);
    }
    else  {
      wait(NULL);
      printf("Job is done.\n");
    }
  }
 
  return EXIT_SUCCESS;
}