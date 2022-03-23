def diagonal_RL_traversal(matrix, N):
    for slice in range(0, 2 * N - 1):
        z = -1
        if slice < N:
            z = 0
        else:
            z = slice - N + 1

        for j in range(z, slice - z + 1):
            print(matrix[j][slice - j], end=" ")


def boundary_traversal(mat, N):
    # Print the first row
    for i in range(N):
        print(mat[0][i], end=" ")

    # Print the last column except the first row
    for i in range(1, N):
        print(mat[i][N - 1], end=" ")

    # Print the last row except the last column
    if (N > 1):

        # Print the last row
        for i in range(N - 2, -1, -1):
            print(mat[N - 1][i], end=" ")

    # Print the first column except the first and last row
    if (N > 1):

        # Print the first column
        for i in range(N - 2, 0, -1):
            print(mat[i][0], end=" ")


def spiral_traversal(mat, N):

    # base case
    if not mat or not N:
        return

    top = left = 0
    bottom = N - 1
    right = N - 1

    while True:
        if left > right:
            break

        # print top row
        for i in range(left, right + 1):
            print(mat[top][i], end=' ')
        top = top + 1

        if top > bottom:
            break

        # print right column
        for i in range(top, bottom + 1):
            print(mat[i][right], end=' ')
        right = right - 1

        if left > right:
            break

        # print bottom row
        for i in range(right, left - 1, -1):
            print(mat[bottom][i], end=' ')
        bottom = bottom - 1

        if top > bottom:
            break

        # print left column
        for i in range(bottom, top - 1, -1):
            print(mat[i][left], end=' ')
        left = left + 1


def alternate_traversal(matrix, N):
    leftToRight = True
    for i in range(N):
        if (leftToRight):
            for j in range(N):
                print(matrix[i][j], end=" ")

        else:
            for j in range(N - 1, -1, -1):
                print(matrix[i][j], end=" ")

        leftToRight = not leftToRight


def normal_traversal(matrix, N):

    for i in range(N):
        for j in range(N):
            print(matrix[i][j], end=" ")


def print_menu():
    print("\nSelect from below menu:")
    print("1.Normal Traversal")
    print("2.Alternate Traversal")
    print("3.Spiral Traversal")
    print("4.Boundary Traversal")
    print("5.Diagonal Traversal [right to left]")
    print("6.Exit")

    choice = int(input("\nEnter your choice: "))
    return choice


def main():

    N = int(input("Enter matrix size: "))

    print("\nEnter elements of {0}X{1} matrix".format(N, N))

    matrix = []
    for i in range(0, N):
        matrix.append([int(j) for j in input().split()])

    print("\nGiven matrix")
    for i in range(N):
        for j in range(N):
            print("{:<5}".format(matrix[i][j]), end="")
        print()

    while True:
        choice = print_menu()

        if choice == 1:
            print("\nNormal Traversal")
            normal_traversal(matrix, N)
            print()

        elif choice == 2:
            print("\nAlternate Traversal")
            alternate_traversal(matrix, N)
            print()

        elif choice == 3:
            print("\nSpiral Traversal")
            spiral_traversal(matrix, N)
            print()

        elif choice == 4:
            print("\nBoundary Traversal")
            boundary_traversal(matrix, N)
            print()

        elif choice == 5:
            print("\nDiagonal Traversal [right to left]")
            diagonal_RL_traversal(matrix, N)
            print()

        elif choice == 6:
            print("\nThank you!")
            break
        else:
            print("Invalid choice!")


main()
