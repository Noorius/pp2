from typing import List
Vector = List

def add_vector(v: Vector, w: Vector) -> Vector:
    assert len(v)==len(w)

    return [v_i+w_i for v_i,w_i in zip(v,w)]

print(add_vector([1,2,3],[4,5,6]))