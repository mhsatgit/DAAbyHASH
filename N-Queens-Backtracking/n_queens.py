def is_safe(board, row, col):
    for prev_row in range(row):
        placed_col = board[prev_row]

        # Same column
        if placed_col == col:
            return False

        # Same diagonal
        if abs(prev_row - row) == abs(placed_col - col):
            return False

    return True


def solve_n_queens(n):
    board = [-1] * n
    solutions = []
    backtrack_count = [0]

    def backtrack(row):
        if row == n:
            solutions.append(board[:])
            return

        for col in range(n):

            if is_safe(board, row, col):

                board[row] = col

                backtrack(row + 1)

                # Undo placement
                board[row] = -1

                backtrack_count[0] += 1

    backtrack(0)

    return solutions, backtrack_count[0]


def display_board(solution, n):
    print(" +" + "---+" * n)

    for row in range(n):

        print(" |", end="")

        for col in range(n):

            if solution[row] == col:
                print(" Q |", end="")
            else:
                print(" . |", end="")

        print()

        print(" +" + "---+" * n)


def main():

    print("========== N-QUEENS PROBLEM ==========")

    print("\nSolving N-Queens using Backtracking")

    # Solve for N = 4, 6 and 8
    for n in [4, 6, 8]:

        solutions, backtracks = solve_n_queens(n)

        print(f"\n========== N = {n} ==========")

        print(f"Number of Solutions : {len(solutions)}")
        print(f"Number of Backtracks: {backtracks}")

        # Display all solutions only for N = 4
        if n == 4:

            print(f"\nAll Solutions for {n}-Queens:")

            for i, solution in enumerate(solutions, 1):

                print(f"\nSolution {i}: {solution}")

                display_board(solution, n)

    print("\n========== COMPLEXITY ANALYSIS ==========")

    print("Time Complexity  : O(N!)")
    print("Space Complexity : O(N)")

    print("\n========== RESULT ==========")

    print(
        "The Backtracking algorithm successfully solved "
        "the N-Queens problem \nand found all valid solutions "
        "for the given board sizes."
    )


if __name__ == "__main__":
    main()