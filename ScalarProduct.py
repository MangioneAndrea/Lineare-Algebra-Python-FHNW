import VectorUtil


def scalar_product(u, v):
    print(u, " * ", v)
    print()
    print("u[x] * v[x] + u[y] * v[y] + u[z] * v[z]")
    print()
    print(u[0], " * ", v[0], " + ", u[1],
          " * ", v[1], " + ", u[2], " * ", v[2])
    print()
    print(u[0]*v[0], " + ", u[1]*v[1], " + ", u[2]*v[2])
    print()
    res = u[0]*v[0]+u[1]*v[1] + u[2]*v[2]
    print(res)
    return res


if(__name__ == "__main__"):
    u = VectorUtil.read_vector("Input U:")
    v = VectorUtil.read_vector("Input V:")
    scalar_product(u, v)
