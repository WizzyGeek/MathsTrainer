# Multiplication Trainer

A simple program, to motivate you to do your times tables

## CLI

```
cli:
    mtrainer [multiplcand: int = 10] [mutiplcand2: int = 10]
    mtrainer help
    mtrainer calibrate [runs: int = 15] [multiplcand: int = 10] [mutiplcand2: int = 10]
```

Using `mtrainer 20 10` will limit first multiplicand to 20 and
second multiplicand to 10.

`mtrainer calibrate` measures the time it takes you to read and
type a number

It is reccommended that you callibrate the average time it takes
you to type an answer, since the real time and real speed will be
provided along with callibrated time and speed.

## Install

```
pip install "mtrainer[calibration] @ git+https://github.com/WizzyGeek/MathsTrainer.git@master#egg=mtrainer"
```

## Why?

During the pandemic, my times tables got noticably rusty, and I could not find any interactive ways to practice, and randomly generated workbooks seemed a bit too much. So in my spare time I wrote this script

## Contribution

**All Contributions are welcome**, feel free to add as many features as you want!
Go Crazy!
