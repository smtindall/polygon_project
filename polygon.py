import math

class Polygon:


    def __init__(self,n,R):
        if n < 3:
            raise ValueError
        self._n = n
        self._R = R
        self._interior_angle = None
        self._side_length = None
        self._apothem = None
        self._peremiter = None
        self._area = None

    def __repr__(self):
        return f'Polygon(n={self._n},R={self._R})'
        #return 'REPR String'

    @property
    def count_vertices(self):
        return self._n

    @property
    def count_edges(self):
        return self._n

    @property
    def circumradius(self):
        return self._R

    @property
    def interior_angle(self):
        if self._interior_angle is None:
            self._interior_angle=(self._n -2) * 180/self._n
        return self._interior_angle

    @property
    def side_length(self):
        if self._side_length is None:
            self._side_length = 2*self._R*math.sin(math.pi/self._n)
        return self._side_length

    @property
    def apothem(self):
        if self._apothem is None:
            self._apothem = self._R*math.cos(math.pi/self._n)
        return self._apothem

    @property
    def area(self):
        if self._area is None:
            self._area = .5 * self._n * self.side_length * self.apothem
        return self._area

    @property
    def perimiter(self):
        if self._peremiter is None:
            self._peremiter = self._n*self.side_length
        return self._peremiter

    def __eq__(self,other):
        if  isinstance(other,Polygon):
            if self._R == other._R and self.count_vertices == other.count_vertices:
                return True
            else:
                return NotImplemented


    def __gt__(self,other):
        if isinstance(other,Polygon):
            if self.count_vertices > other.count_vertices:
                return True
            else:
                return NotImplemented

class PolygonIterator:
    def __init__(self,m,R):
        if m < 3:
            raise ValueError('m must be greater than 3')
        self._m = m
        self._R = R
        self._i = 3

    def __iter__(self):
        return self

    def __next__(self):
        if self._i > self._m:
            raise StopIteration
        else:
            result = Polygon(self._i,self._R)
            self._i += 1
            return result



class Polygons:
    def __init__(self,m,R):
        if m < 3:
            raise ValueError('m must be greater than 3')

        self._m = m
        self._R = R

    def __len__(self):
        return self._m - 2

    def __repr__(self):
        return f'Polygons(m={self._m}, R={self._R})'

    def __iter__(self):
        return PolygonIterator(self._m, self._R)
