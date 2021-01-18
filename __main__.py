import sys
from random import choice
from time import time

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
    start = time()

    ques = 0

    while True:
        num1 = choice(nums)
        num2 = choice(nums)

        print(f"{num1} x {num2}")

        try:
            ans = int(input(">>> Answer: "))
        except Exception:
            break
        else:
            ques += 1

        if ans == (num1 * num2):
            score += 1

    end = time()

    print(f"Your score was {score}")
    print(f"You took {(end - start):2f} seconds for {ques} questions")
    print(f"Your avg. speed was, {(ques / (end - start)):2f} questions per second or {((end - start) / ques)} seconds per question")
    print(f"Accuracy {(score/ques):%} :)")
    print("*You Can Do Better!*")
    input()
    return 0

if __name__ == "__main__":
    main()
