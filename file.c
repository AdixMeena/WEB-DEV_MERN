#include <stdio.h>

int main(void)
{
    FILE *ptr = fopen("doc.txt", "r");
    if (ptr == NULL) {
        perror("fopen");
        return 1;
    }

    char buf[21];                                   // 20 chars + room for '\0'
    size_t n = fread(buf, sizeof(char), 20, ptr);   // n = how many chars were actually read
    buf[n] = '\0';                                  // terminate the string

    printf("read %zu chars: %s\n", n, buf);

    fclose(ptr);\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\
    return 0;
}
