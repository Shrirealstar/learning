#include<stdio.h>
#include<fcntl.h>
#include<sys/stat.h>
#include<sys/types.h>
#include<unistd.h>

int main() 
{
	int fd;
	char buf[1024];
	char *myfifo = "/tmp/myfifo";
    mkfifo(myfifo, 0666);
    printf("Run the reader file to read the FIFO\n");
	fd = open(myfifo, O_WRONLY);
	write(fd, "Hi", sizeof("Hi"));
	close(fd);
	unlink(myfifo);
	return 0;

}
