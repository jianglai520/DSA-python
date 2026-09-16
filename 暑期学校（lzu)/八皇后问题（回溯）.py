def main(n):
    if n <= 0:
        return []

    result = []
    pos = [0] * n
    cols = set()
    diag1 = set()
    diag2 = set()

    def is_not_under_attack(row, col):
        return col not in cols and (row - col) not in diag1 and (row + col) not in diag2

    def place_queen(row, col):
        cols.add(col)
        diag1.add(row - col)
        diag2.add(row + col)
        pos[row] = col

    def remove_queen(row, col):
        cols.remove(col)
        diag1.remove(row - col)
        diag2.remove(row + col)

    def backtrack(row):
        if row == n:
            result.append("".join(str(c+1) for c in pos))
            return

        for col in range(n):
            if is_not_under_attack(row, col):
                place_queen(row, col)
                backtrack(row + 1)
                remove_queen(row, col)

    backtrack(0)
    return result

if __name__ == "__main__":
    import sys

    all_solutions = main(8)

    data = sys.stdin.read().split()
    n = int(data[0])
    out = []
    for i in range(1, n+1):
        b = int(data[i])
        out.append(all_solutions[b-1])
    sys.stdout.write("\n".join(out) + "\n")

