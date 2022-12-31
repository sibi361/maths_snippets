# Gauss–Seidel iterative method
# Created: 2022-12-29
# ref: https://en.wikipedia.org/wiki/Gauss%E2%80%93Seidel_method

# TODO:
# - make it work for any number of given variables
# - get input from user

PRINT_LEN = 5
COUNT_OF_VARIABLES = 3
N_OF_ITERATIONS = 10

RHS_CONSTANTS = [4, 7, 3]
LHS_MATRIX = [[4, 1, 2],
              [3, 5, 1],
              [1, 1, 3]]

variables = [0, 0, 0]
print("Gauss–Seidel iterative method for",
      N_OF_ITERATIONS, "iterations:\nx\ty\tz")
print(0, 0, 0, sep="\t")

for i in range(N_OF_ITERATIONS):
    for j in range(COUNT_OF_VARIABLES):
        index_list = [0, 1, 2]
        # https://en.wikipedia.org/wiki/Gauss%E2%80%93Seidel_method#Algorithm
        index_list.remove(index_list[j])

        variables[j] = (RHS_CONSTANTS[j] -
                        LHS_MATRIX[j][index_list[0]] * variables[index_list[0]] -
                        LHS_MATRIX[j][index_list[1]] * variables[index_list[1]]) \
                        / LHS_MATRIX[j][j]

        print(str(variables[j])[:PRINT_LEN], end="\t")
    print()


"""
# Sample for testing

x = y = z = 0
print()
for i in range(ITERATIONS):
	x = (4 - y - 2 * z) / b[0][0]
	y = (7 - 3 * x - z) / b[1][1]
	z = (3 - x - y) / b[2][2]
	print(str(x)[:LEN], str(y)[:LEN], str(z)[:LEN])
print()
 """
