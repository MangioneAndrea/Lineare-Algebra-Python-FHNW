import VectorUtil
import math
from ScalarProduct import scalar_product


def angle_in_between(u, v):
    product = scalar_product(u, v)
    print()
    ulen = VectorUtil.vector_length(u)
    print()
    vlen = VectorUtil.vector_length(v)
    print()
    print("cos(γ) = u*v / |u|*|v|")
    print(product, " / (", ulen, " * ", vlen, ")")
    print(product, " / (", ulen * vlen, ")")
    cos = product/(ulen * vlen)
    print("cos(γ) = ", cos)
    print("γ = arccos(cos(γ))")
    print("γ = ", math.acos(cos),"rad ~", math.degrees(math.acos(cos)),"°")


if(__name__ == "__main__"):
    u = VectorUtil.read_vector("Input U:")
    v = VectorUtil.read_vector("Input V:")
    angle_in_between(u, v)
