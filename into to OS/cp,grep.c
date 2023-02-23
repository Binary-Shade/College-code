#include<fcntl.h>
#include<unistd.h>
#include<stdio.h>
int main(int argc,char* argv[])
{
FILE*fp;
char ch;
int sc=0;
fp=fopen("/home/oem/Desktop/new.txt","r");
if(fp==NULL)
printf("unable to open a file %s",argv[1]);
else{
while(!feof(fp))
{ch=fgetc(fp);
sc++;
}
printf("no of space - %d",sc);
printf("\n");
fclose(fp);
} 
}

HELLO WORLD IS MY NEW PROGRAM IS AN INTERNET.

