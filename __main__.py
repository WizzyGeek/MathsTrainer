import sys
from random import choice

def parse_args(argv=sys.argv):
    try:
        return argv[2]
    except Exception:
        return 10

def main(argv=None):
    if not argv:
        argv = parse_args()
    print("Multiplication Trainer")

    nums = tuple(range(argv))

    score = 0

    while True:
        num1 = choice(nums)
        num2 = choice(nums)

        print(f"{num1}x{num2}")

        try:
            ans = int(input(">>> Answer: "))
        except Exception:
            break

        if ans == (num1 * num2):
            score += 1
        else:
            score -= 1

    print(f"Your score was {score}")
    input()
    return 0

if __name__ == "__main__":
    main()
