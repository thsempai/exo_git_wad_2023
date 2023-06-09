class Cube:

    def __init__(self, side):
        self.side = side

    @property
    def volume(self):
        return self.side ** 3

    def __eq__(self, other):
        if isinstance(other, Cube):
            return self.side == other.side
        else:
            return super().__eq__(other)

    def __mod__(self, other):
        n_side = self.side * other.side
        return Cube(n_side)


if __name__ == "__main__":
    c = Cube(3)
    d = Cube(3)
    e = Cube(5)

    f = c % 3

    print(c == d)
    print(c == e)

    print(f.side)