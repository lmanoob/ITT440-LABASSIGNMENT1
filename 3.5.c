#include <stdio.h>
#include <stdlib.h>
#include <sys/types.h>
#include <sys/wait.h>
#include <unistd.h>
 
#define PIN_LENGTH 1
#define PIN_WAIT_INTERVAL 2

void getPIN(char pin[PIN_LENGTH + 1]) {
  srand(getpid() + getppid());
 
  pin[0] = 49 + rand() % 7;
 
  for(int i = 1; i < PIN_LENGTH; i++) {
    pin[i] = 48 + rand() % 7;
  }
 
  pin[PIN_LENGTH] = '\0';
}

 
int main(void) {
  int fd[2];
  pipe(fd);
  pid_t pid = fork();
 
  if(pid > 0) {
    close(0);
    close(fd[1]);
    dup(fd[0]);
 
    int secretNumber;
    size_t readBytes = read(fd[0], &secretNumber, sizeof(secretNumber));
 
    printf("Waiting for PIN...\n");
    wait(NULL);
 
    printf("PIN: %d\n", secretNumber);
  }
  else if(pid == 0) {
    close(1);
    close(fd[0]);
    dup(fd[1]);
 
    int secret = getPIN();
    write(fd[1], &secret, sizeof(secret));
    exit(EXIT_SUCCESS);
  }
 
  return EXIT_SUCCESS;
}
