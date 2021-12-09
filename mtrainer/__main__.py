import sys
from random import choice
from time import perf_counter as time
from math import log1p, ceil
import pathlib

from . import calibrate

try:
    from appdirs import AppDirs
except (ModuleNotFoundError, ImportError):
    appdir = None
else:
    appdir = AppDirs(appname="mtrainer")

def parse_args(argv=sys.argv):
    argv = argv[1:]
    if not argv:
        return 10, 10, True
    else:
        if argv[0].lower() == "calibrate":
            if appdir is None:
                print("Calibration dependency not installed")
                sys.exit(0)

            try:
                runs = int(argv[1], base=10)
            except Exception:
                runs = 15

            t = calibrate(runs)
            data = pathlib.Path(appdir.user_data_dir)
            data.mkdir(exist_ok=True, parents=True)
            with (data / "lag.txt").open("w") as wr:
                wr.write(str(t))
            sys.exit(0)

        elif len(argv) == 1:
            if argv[0].lower() == "help":
                print("Trainer", "=" * 6, sep="\n")
                print(
                    "cli:",
                    "mtrainer [multiplcand: int = 10] [mutiplcand2: int = 10]",
                    "mtrainer help",
                    "mtrainer calibrate [runs: int = 15] [multiplca nd: int = 10] [mutiplcand2: int = 10]",
                    sep="\n" + " " * 4
                )
                sys.exit(0)

            ret = [int(argv[0]), 10]
        else:
            ret = list(int(i) for i in argv[:2])
        return ret + [(("--no-zeroes" in argv) or ("--zeroes" not in argv))]

def main(argv=sys.argv):
    argv = parse_args(argv)

    print("Multiplication Trainer")
    print("Instructions")
    print("The questions will appear sequentially, you must type the answer an press enter to move to the next question")
    print("To end the test simply press enter without typing the answer.")
    k = input("Press enter when ready or enter \"exit\" to quit: ")
    if k.lower() in {"exit", "ex", "et"}:
        return 0

    cal = pathlib.Path(appdir.user_data_dir) / "lag.txt"
    if cal.exists():
        with cal.open("r") as r:
            lag = float(r.read())
    else:
        lag = 0

    nums = sorted(argv[:2])
    nums = tuple(range(argv[2], argv[1] + 1))
    nums2 = tuple(range(1, argv[0] + 1))

    score = 0

    start = time()

    degradant = ceil(log1p(argv[0] * argv[1]))

    ques = 0
    quality = 0

    while True:
        num1 = choice(nums)
        num2 = choice(nums2)

        print(f"{ques + 1} | {num1} x {num2}")

        try:
            ans = int(input(">>> Answer: "), base=10)
        except Exception:
            break
        else:
            ques += 1

        real = (num1 * num2)

        if ans == real:
            score += 1
        else:
            quality += log1p(abs(ans - real)) / degradant
            print(f"=== That was not the answer, it was {real}")

    end = time()
    r_delta = (end - start) - 0.0009 * ques # calculation overhead estimate
    delta = r_delta - lag * ques

    if delta < 0:
        print("\n")
        print("=" * 10)
        print("!" * 6,"The time taken was negative you need to recallibrate", "!" * 6)
        print("=" * 10)

    if ques:
        tp = ((delta) / ques)
        acc =  score / ques

        print(f"Your score was {score}")
        print(f"User input compenstion: {lag} seconds per question")
        print(f"You took {delta:2f} seconds for {ques} questions. Real time: {r_delta}")
        print(f"Your avg. speed was, {(ques / delta):2f} questions per second or {tp} seconds per question. Real speed: {(ques / r_delta)}")
        print(f"Accuracy {acc:%} :)")
        print(f"Adjusted Accuracy {(1 - 2 * quality / ques):%}")

        if score == 0:
            print("You got a zero :O that is very probabilistically unlikely, quit joking around :)")
        elif acc <= 0.5:
            if acc == 0.5 and (tp >= 1 or tp <= 2):
                print("*Is that you Ayanokoji Kiyotaka?*")
            print("Your accuracy is very bad, work on accuracy before speed")
        elif acc <= 0.75:
            if tp <= 2:
                print("You had a pretty good score, increase your accuracy!")
            elif tp <= 3:
                print("You should work on your speed while focusing on accuracy")
        else:
            if acc < 0.9:
                if tp <= 1:
                    print("You are probably on the limits of your speed, increase your accuracy.")
                elif tp <= 2:
                    print("Try to improve your accuracy")
                elif tp <= 3:
                    print("You should improve your speed more")
                elif tp <= 5:
                    print("You should focus majorly on speed.")
                else:
                    print("You severly lack speed, accuracy is meaningless")
            elif acc < 1:
                if tp <= 1:
                    print("Good work, you can still improve accuracy!!")
                elif tp <= 2:
                    print("You can still improve, callibrate the input speed to get more truthfull results")
                elif tp <= 5:
                    print("Work o you speed! callibration may help!")
                else:
                    print("Accuracy without speed is meaningless")
            else:
                if tp <= 0.5:
                    print("Insane!! Are you a robot. Increase the multplicands, and recallibrate")
                elif tp <= 1:
                    print("Awesome! You are blazing fast while being correct. Increase the mutplicands to practice more!")
                elif tp <= 3:
                    print("Good work! work on speed!")
                else:
                    print("Good Work, but speed is important!")

    else:
        print("No questions attempted! :(")

    input("[Press enter to exit] ")
    return 0

if __name__ == "__main__":
    sys.exit(main())
