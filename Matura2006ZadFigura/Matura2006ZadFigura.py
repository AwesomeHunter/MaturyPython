def f(x: float) -> float:
    return -x*x/50


def g(x: float) -> float:
    return 1+x*x/100-x/200


def area(start: float, end: float, precision: float) -> float:   
    pole = 0
    while(start < end):
        mini_precision = min(precision, end - start)
        pole += abs((g(start) + g(start + mini_precision)) * mini_precision / 2)
        pole += abs((f(start) + f(start + mini_precision)) * mini_precision / 2)
        start += mini_precision
    return pole


def rect(width: int, height: int) -> dict:
    i = 0
    while(int(abs(f(i))) + int(abs(g(i))) < height):
        i += 1
    return {(i, int(g(i)) - height), (i+width, int(g(i)) - height,), (i, int(g(i))), (i+width, int(g(i)))}, i+width


if __name__ == '__main__':
    print(area(0,10,0.001))
    print(rect(100, 26))