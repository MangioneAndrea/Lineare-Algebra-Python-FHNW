import math


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

    
if(__name__ == "__main__"):
    v = VectorUtil.read_vector("Input V:")
    vector_length(v)