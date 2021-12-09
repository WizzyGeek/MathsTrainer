import sys
from time import perf_counter as time
from random import choice

def callibrate(runs, num1=10, num2=10):
    print(f"The input speed callibration utility will now run {runs} times")
    print("Enter the number displayed when prompted")
    print("If a typo occurs simply submit it, that input will be ignored")

    nums = tuple(range(1, num1 + 1))
    nums2 = tuple(range(1, num2 + 1))

    while True:
        k = input("Press enter when ready or enter \"exit\" to quit: ")
        if k.lower() in {"exit", "ex", "et"}:
            sys.exit(0)

        itr = 0
        total = 0
        while itr < runs:
            try:
                print(f"{(ans := (choice(nums) * choice(nums2)))}")
                start = time()
                assert ans == int(input(">>> Callibrate: "))
            except ValueError:
                print("Enter a valid answer, input discarded")
            except AssertionError:
                print("Wrong number, input discarded")
            except KeyboardInterrupt:
                print("Aborting callibration...")
                input("[Press enter to exit] ")
                sys.exit(0)
            else:
                total += time() - start
                itr += 1

        speed = total / itr
        print(f"Your time taken per input was: {speed} seconds")
        c = input("Use this as your callibrated lag point? (Y/n) ")
        if c.lower() in {"y", "ye", "yes"}:
            return speed * 0.8725
        else:
            print("The utility will now run again...")
            input("[Press enter to continue] ")

