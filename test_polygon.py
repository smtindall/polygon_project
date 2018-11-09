from polygon import *
import math
import pytest

def test_polygon():
    rel_tol = 0.0001
    abs_tol = 0.0001

    try:
        p=Polygon(2,1)
        assert False
    except ValueError:
        pass
    n=3
    R=1
    p=Polygon(n,R)
    assert str(p) == f'Polygon(n=3,R=1)',f'actual; {str(p)}'
    assert p.count_edges == n
    assert p.circumradius==R
    assert p.interior_angle == 60
    n=4
    R=1
    p=Polygon(n,R)
    assert p.interior_angle == 90
    assert math.isclose(p.area,2,rel_tol=rel_tol, abs_tol=abs_tol), (f'actual {p.area},'
                                                                    f'expected {2.0}')


    assert math.isclose(p.side_length,math.sqrt(2),rel_tol=rel_tol, abs_tol=abs_tol)

    assert math.isclose(p.perimiter,4*math.sqrt(2),rel_tol=rel_tol, abs_tol=abs_tol)

p1=Polygon(3,100)
p2=Polygon(10,10)
p3=Polygon(15,10)
p4=Polygon(15,100)
p5=Polygon(15,100)

assert (p2 > p1)
assert (p2 < p3)
assert (p3 != p4)
assert (p1 != p4)
assert (p4 == p5)


def test_PolygonIterator():
    p_iter = PolygonIterator(5,3)
    next(p_iter)
    next(p_iter)
    next(p_iter)

@pytest.mark.xfail
def test_PolygonIterator2():
    p_iter = PolygonIterator(5,3)
    next(p_iter)
    next(p_iter)
    next(p_iter)
    next(p_iter)


polygons = Polygons(5,3)
for p in polygons:
    print(p)
