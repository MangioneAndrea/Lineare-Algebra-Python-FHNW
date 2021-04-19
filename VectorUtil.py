
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



