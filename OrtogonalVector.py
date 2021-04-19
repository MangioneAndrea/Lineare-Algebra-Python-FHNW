import VectorUtil


def ortogonal_vector(u, v):
    print(v, " x ", u, ":")

    print("u[y] * v[z] - u[z] * v[y]")
    print("u[z] * v[x] - u[x] * v[z]")
    print("u[x] * v[y] - u[y] * v[x]")

    print()

    print("(", u[1], " * ", v[2], ") - (", u[2], " * ", v[1], ")")
    print("(", u[2], " * ", v[0], ") - (", u[0], " * ", v[2], ")")
    print("(", u[0], " * ", v[1], ") - (", u[1], " * ", v[0], ")")

    print()

    print(u[1]*v[2], "-", u[2]*v[1])
    print(u[2]*v[0], "-", u[0]*v[2])
    print(u[0]*v[1], "-", u[1]*v[0])

    print()
    res = [
        u[1]*v[2] - u[2]*v[1], u[2]*v[0] - u[0]*v[2], u[0]*v[1] - u[1]*v[0]
    ]
    print(res)
    return res


if(__name__ == "__main__"):
    u = VectorUtil.read_vector("Input U:")
    v = VectorUtil.read_vector("Input V:")
    ortogonal_vector(u, v)
