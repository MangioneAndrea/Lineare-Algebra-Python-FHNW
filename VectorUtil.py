import math


def is_digit(question):
    try:
        int(question)
        return True
    except ValueError:
        return False


def read_vector(msg):
    vec = None
    while vec is None:
        try:
            out = input(msg).split(" ")
            if len(out) == 3 and all(is_digit(n) for n in out):
                vec = list(map(int, out))
            else:
                print(out, " is not a vector")
        except e:
            vec = None
    return vec


def vector_length(v):
    print(v, " length:")
    print()
    print("sqrt(v[x]² + v[y]² + v[z]²)")
    print("sqrt(", v[0], "² + ", v[1], "² + v", v[2], "²)")
    print("sqrt(", v[0]**2, " + ", v[1]**2, " + ", v[2]**2, ")")
    print("sqrt(", v[0]**2 + v[1]**2 + v[2]**2, ")")
    res = (math.sqrt(v[0]**2 + v[1]**2 + v[2]**2))
    print(res)
    return res
