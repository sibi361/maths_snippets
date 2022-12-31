// Gauss–Seidel iterative method
// Created: 2022-12-31
// ref: https://en.wikipedia.org/wiki/Gauss%E2%80%93Seidel_method

// TODO:
// - make it work for any number of given variables
// - get input from user

#define PRINT_LEN 5
#define COUNT_OF_VARIABLES 3
#define N_OF_ITERATIONS 10

#include <iostream>

int main(void)
{
    using namespace std;

    float RHS_CONSTANTS[] = {4, 7, 3};
    float LHS_MATRIX[][3] = {{4, 1, 2},
                             {3, 5, 1},
                             {1, 1, 3}};

    float variables[] = {0, 0, 0};
    int index_list[2], l;

    printf("Gauss–Seidel iterative method for %d iterations:\nx\ty\tz\n",
           N_OF_ITERATIONS);
    printf("0\t0\t0\n");

    for (int i = 0; i < N_OF_ITERATIONS; i++)
    {
        for (int j = 0; j < COUNT_OF_VARIABLES; j++)
        {
            // https://en.wikipedia.org/wiki/Gauss%E2%80%93Seidel_method#Algorithm
            l = 0;
            for (int k = 0; k < 3; k++)
                if (k != j)
                    index_list[l++] = k;

            variables[j] = (float)(RHS_CONSTANTS[j] -
                                   LHS_MATRIX[j][index_list[0]] * variables[index_list[0]] -
                                   LHS_MATRIX[j][index_list[1]] * variables[index_list[1]]) /
                           LHS_MATRIX[j][j];

            // cout << variables[j] << "\t";
            printf("%.3f\t", variables[j]);
        }
        cout << "\n";
    }
    cout << "\n\n";
    return 0;
}