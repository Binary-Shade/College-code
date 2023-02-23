#include<stdio.h>
#include<stdlib.h>
#include<string.h>
#define max 1000
void usage()
{
printf("usage at ./a.out and filename word\n");
}
int main(int argc,char *argv[])
{
FILE *fp;
char fline[max];
char *newline;
int count=0;
int occurence=0;
if(argc!=3)
{
usage();
}
fp=fopen(argv[1],"r");
if(!fp)
{
printf("grep could not open file :%s\n",argv[1]);
}
while(fgets(fline,max,fp)!=NULL)
{
count++;
if(newline=strchr(fline,'\n'))
newline=NULL;
if(strstr(fline,argv[2])!=NULL){
printf("%s:%d %s \n",argv[1],count,fline);
occurence++;

}
}
}

