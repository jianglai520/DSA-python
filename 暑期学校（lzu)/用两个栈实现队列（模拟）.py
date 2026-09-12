import sys

def main():
    data = sys.stdin.read().split()
    idx = 0
    n = int(data[idx])
    idx += 1

    s1 = []
    s2 = []
    out = []

    for _ in range(n):
        op = data[idx]
        idx += 1

        if op == 'I':
            val = data[idx]
            idx += 1
            s1.append(val)
        else:
            if s2:
                out.append(f"{s2.pop()} 1")
            elif s1:
                cost = 2 * len(s1) + 1
                while s1:
                    s2.append(s1.pop())
                out.append(f"{s2.pop()} {cost}")
            else:
                out.append("ERROR")
    sys.stdout.write("\n".join(out) + "\n")

if __name__ == "__main__":
    main()