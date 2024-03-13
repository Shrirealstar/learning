#include <stdio.h>
#include <string.h>

void replacePattern(char *mainStr, const char *pattern, const char *replace) {
    int mainLen = strlen(mainStr);
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
    char mainStr[100], pattern[100], replace[100];
    printf("Enter main string: ");
    scanf(" %[^\n]", mainStr);
    printf("Enter pattern to replace: ");
    scanf(" %[^\n]", pattern);
    printf("Enter replacement string: ");
    scanf(" %[^\n]", replace);

    replacePattern(mainStr, pattern, replace);

    printf("Resulting string after pattern replacement: %s\n", mainStr);

    return 0;
}
