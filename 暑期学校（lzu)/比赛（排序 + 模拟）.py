import sys

def main():
    input = sys.stdin.readline
    n = int(input())
    teams = []

    for _ in range(n):
        parts = list(map(int, input().split()))
        tid = parts[0]
        k = parts[1]
        scores = parts[2:2+k]
        total = sum(scores)
        avg = total / k
        max_score = max(scores)
        teams.append((tid, avg, max_score))

    teams.sort(key = lambda x: (-x[1], -x[2], x[0]))

    out = []
    for rank, (tid, avg, _) in enumerate(teams, start = 1):
        out.append(f"{rank} {tid} {avg:.2f}")
    sys.stdout.write("\n".join(out))

if __name__ == "__main__":
    main()

