import os


def main():
    __location__ = os.path.realpath(os.path.join(os.getcwd(), os.path.dirname(__file__)))
    calorie_list = []

    file = open(os.path.join(__location__, "input.in"), "r")
    for line in file:
        line = line.split("\n")[0]
        if line == "":
            calorie_list.append(0)
        else:
            calorie_list.append(int(line))

    for number in calorie_list:
        print(number)

main()

