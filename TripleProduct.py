from OrtogonalVector import ortogonal_vector
from ScalarProduct import scalar_product
import VectorUtil


def triple_product(a, b, c):
    print("[a, b, c] = (a×b)·c ")
    ort = ortogonal_vector(a, b)
    vec = scalar_product(ort, c)

    print("[a, b, c] =", vec)
    return vec


if(__name__ == "__main__"):
    a = VectorUtil.read_vector("Input A:")
    b = VectorUtil.read_vector("Input B:")
    c = VectorUtil.read_vector("Input C:")
    triple_product(a, b, c)
