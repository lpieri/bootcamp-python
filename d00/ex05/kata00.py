if __name__ == "__main__":
    t = (19, 42, 21)
    toPrint = "The {len} numbers are: {}, {}, {}"
    print(toPrint.format(t[0], t[1], t[2], len=len(t)))
