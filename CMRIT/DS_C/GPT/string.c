#include <stdio.h>
#include <string.h>

void replacePattern(char *mainsting, const char *pattern, const char *replace) {
    int mainLen = strlen(mainsting);
    int patLen = strlen(pattern);
    int repLen = strlen(replace);

    for (int i = 0; i <= mainLen - patLen; i++) {
        if (strncmp(mainStr + i, pattern, patLen) == 0) {
            memmove(mainStr + i + repLen, mainStr + i + patLen, mainLen - i - patLen + 1);
            memcpy(mainStr + i, replace, repLen);
            mainLen += repLen - patLen;
            i += repLen - 1;
        }
    }
}

int main() {
    char mainsting[100], pattern[100], replace[100];
    printf("Enter main string: ");
    scanf(" %[^\n]", mainsting);
    printf("Enter pattern to replace: ");
    scanf(" %[^\n]", pattern);
    printf("Enter replacement string: ");
    scanf(" %[^\n]", replace);

    replacePattern(mainsting, pattern, replace);

    printf("Resulting string after pattern replacement: %s\n", mainsting);

    return 0;
}
