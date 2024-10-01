#include <stdio.h>
#include <stdlib.h>
#include <time.h>

char* generateRandomPassword(int length) {
    char charset[] = "abcdefghijklmnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ0123456789!@#$%^&*";
    char* password = (char*)malloc((length + 1) * sizeof(char));

    if (password == NULL) {
        return NULL;
    }

    srand(time(NULL));

    for (int i = 0; i < length; i++) {
        password[i] = charset[rand() % (sizeof(charset) - 1)];
    }
    password[length] = '\0';

    return password;
}

int main() {
    int passwordLength;
    
    printf("Welcome to the Random Password Generator!\n");
    printf("Please enter the desired password length: ");
    if (scanf("%d", &passwordLength) != 1) {
        printf("Invalid input. Please enter a valid number.\n");
        return 1;
    }

    if (passwordLength <= 0) {
        printf("Password length must be a positive integer.\n");
        return 1;
    }

    char* password = generateRandomPassword(passwordLength);

    if (password != NULL) {
        printf("Your Random Password: %s\n", password);
        free(password);
    } else {
        printf("Memory allocation failed. Unable to generate the password.\n");
        return 1;
    }

    return 0;
}
