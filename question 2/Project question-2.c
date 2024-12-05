#include <stdio.h> //Includes standard input/output

//Function to add two integer variables
void add(int var1, int var2) {
    int result = var1 + var2; //Creates variable called 'result' to store the sum of var1 and var2
    printf("%d added to %d is equal to: %d\n",var1,var2,result); //Outputs a sentence explaining the sum of the numbers
}

//Program Entry Point
int main() {
    int var1, var2; //Creates two integer type variables
    printf("Enter two numbers: ");
    scanf("%d %d",&var1,&var2); //Takes input, and stores in var1 and var2
    add(var1,var2); //Calls add function, using var1 and var2
    
    return 0;
}
