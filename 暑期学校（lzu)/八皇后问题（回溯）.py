import sys

def main():
    solutions = []
    pos = [0] * 8
    col = [False] * 8
    diag1 = [False] * 15
    diag2 = [False] * 15

    def dfs(row):
        if row == 8:
            num = 0
            for c in pos:
                num = num * 10 + (c + 1)
            solutions.append(num)
            return

        for c in range(8):
            if col[c] or diag1[row -c + 7] or diag2[row + c]:
                continue
            pos[row] = c
            col[c] = diag1[row -c + 7] = diag2[row + c] = True
            dfs(row + 1)
            col[c] = diag1[row - c + 7] = diag2[row + c] = False

    dfs(0)

    data = sys.stdin.read().split()
    n = int(data[0])
    out = []
    for i in range(1, n+1):
        b = int(data[i])
        out.append(str(solutions[b - 1]))
    sys.stdout.write("\n".join(out) + "\n")

if __name__ == "__main__":
    main()