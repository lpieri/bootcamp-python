if __name__ == "__main__":
    t = (3, 30, 2019, 9, 25)
    toPrint = "{m:0>2}/{d:0>2}/{y:0>4} {h:0>2}:{min:0>2}"
    print(toPrint.format(m=t[3], d=t[4], y=t[2], h=t[0], min=t[1]))
