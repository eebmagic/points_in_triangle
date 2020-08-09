def x_min_max(verts):
    MIN, MAX = float('inf'), -float('inf')

    for vert in verts:
        if vert[0] < MIN:
            MIN = vert[0]
        if vert[0] > MAX:
            MAX = vert[0]

    return MIN, MAX


def y_min_max(verts):
    MIN, MAX = float('inf'), -float('inf')

    for vert in verts:
        if vert[1] < MIN:
            MIN = vert[1]
        if vert[1] > MAX:
            MAX = vert[1]

    return MIN, MAX


def get_line(a, b):
    '''
    returns A, B, C for standard form equation
    for line from point a to point b
    '''
    if b[0] == a[0]:
        m = 0
    else:
        m = (b[1] - a[1]) / (b[0] - a[0])

    x, y = a
    a = -m
    b = 1.0
    c = -x * m + y

    return (a, b, c)


def get_y(line, x):
    '''
    returns the y value at x on the line
    where line is (A, B, C) for standard form of the line
        (given by get_line())
    '''
    a, b, c = line
    y = (c - (a * x)) / b

    return y


def above_line(point, line, ab):
    '''
    returns if point is above a line
    true if right of vertical line
    true if above horizontal line
    returns null if on the line (useful for comparing two points)
    '''
    # Avoids divide by zero error
    if line[0] == 0:
        a, b = ab
        if a[0] == b[0]:
            x = a[0]
            if point[0] == x:
                return None
            else:
                return point[0] > x
        else:
            y = a[1]
            if point[1] == y:
                return None
            else:
                return point[1] > y
    
    else:
        y_on_line = get_y(line, point[0])
        if point[1] == y_on_line:
            return None
        else:
            return point[1] > y_on_line


def valid_point(point, tri):
    '''
    returns true if a point is inside the lines between
    the three points making the triangle
    '''
    a, b, c = tri
    ab = get_line(a, b)
    ac = get_line(a, c)
    bc = get_line(b, c)

    x_ab = above_line(point, ab, (a, b))
    x_ac = above_line(point, ac, (a, c))
    x_bc = above_line(point, bc, (b, c))

    if x_ab == None or x_ab == above_line(c, ab, (a, b)):
        if x_ac == None or x_ac == above_line(b, ac, (a, c)):
            if x_bc == None or x_bc == above_line(a, bc, (b, c)):
                return True

    return False


def all_valid_points(tri):
    '''
    gets all valid whole number coordinate pairs that are inside triangle
    triangle points must be in ints
    '''
    all_values = list(sum(tri, ()))
    for value in all_values:
        assert type(value) == int, "all triange points should be ints"
    x_min, x_max = x_min_max(tri)
    y_min, y_max = y_min_max(tri)
    ab = get_line(a, b)
    ac = get_line(a, c)
    bc = get_line(b, c)

    valid = []
    for x in range(x_min, x_max+1):
        for y in range(y_min, y_max+1): 
            point = (x, y)
            v = valid_point(point, tri)

            if v or point in tri:
                valid.append(point)

    return valid


if __name__ == "__main__":
    from random import randint
    import matplotlib.pyplot as plt

    # simple test case points
    # a = (5, 3)
    # b = (6, 8)
    # c = (2, 6)
    a = (randint(0, 50), randint(0, 50))
    b = (randint(0, 50), randint(0, 50))
    c = (randint(0, 50), randint(0, 50))
    tri = (a, b, c)
    print(f"tri: {tri}")

    valid = all_valid_points(tri)
    print(f"valid points: {valid}")

    # Chart to check
    x_min, x_max = x_min_max(tri)
    y_min, y_max = y_min_max(tri)
    X = []
    Y = []
    for x in range(x_min, x_max+1):
        for y in range(y_min, y_max+1):
            if x not in X:
                X.append(x)
            if y not in Y:
                Y.append(y)
            point = (x, y)
            if point in valid:
                plt.scatter(*zip(point), color='orange')
            else:
                plt.scatter(*zip(point), color='black')

    plt.plot(*zip(a,b), color='blue')
    plt.plot(*zip(a,c), color='blue')
    plt.plot(*zip(b,c), color='blue')

    print("SHOWING....")
    plt.grid(color='black', linestyle='-', linewidth=0.5)
    plt.show()