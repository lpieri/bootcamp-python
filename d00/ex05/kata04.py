if __name__ == "__main__":
    t = (0, 4, 132.42222, 10000, 12345.67)
    toPrint = "day_{n:0>2}, ex_{e:0>2} : {nb1:.2f}, {nb2:0.2e}, {nb3:0.2e}"
    print(toPrint.format(n=t[0], e=t[1], nb1=t[2], nb2=t[3], nb3=t[4]))
