def find_divisibles(inrange, div_by):
    print("finding nums in range {} divisible by {}".format(inrange, div_by))
    located = []
    for i in range(inrange):
        if i % div_by == 0:
            located.append(i)

    print("Done w/ nums in range {} divisible by {}".format(inrange, div_by))
    return located


if __name__ == '__main__':

    find_divisibles(500000, 23)  # When you run it was blocked here for a long time
    find_divisibles(10000, 19)
    find_divisibles(1000, 17)
