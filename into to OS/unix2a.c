#include <stdio.h>
#include <stdlib.h>
#include <dirent.h>

int main(int argc, char *argv[]) {
    char buff[100];
    struct dirent *dptr;
    DIR *dirp;

    printf("Enter directory name: ");
    scanf("%s", buff);

    dirp = opendir(buff);
    if (dirp == NULL) {
        printf("Error: Directory '%s' does not exist.\n", buff);
        exit(EXIT_FAILURE);
    }

    while ((dptr = readdir(dirp)) != NULL) {
        printf("%s\n", dptr->d_name);
    }

    closedir(dirp);

    return 0;
}

