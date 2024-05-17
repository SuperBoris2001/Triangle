from projectforyadro.triangle import Triangle, triangle

# Равносторонний треугольник
def test_equilateral_triangle():
    assert triangle(5, 5, 5) == Triangle.Equal

# Равнобедренный треугольник
def test_isosceles_triangle():
    assert triangle(5, 5, 3) == Triangle.Isoscale
    assert triangle(5, 3, 5) == Triangle.Isoscale
    assert triangle(3, 5, 5) == Triangle.Isoscale

# Обычный треугольник
def test_regular_triangle():
    assert triangle(3, 4, 5) == Triangle.Regular
    assert triangle(4, 5, 3) == Triangle.Regular
    assert triangle(5, 3, 4) == Triangle.Regular

# Не треугольник
def test_not_a_triangle():
    assert triangle(1, 1, 10) == Triangle.NotATriangle
    assert triangle(1, 10, 1) == Triangle.NotATriangle
    assert triangle(10, 1, 1) == Triangle.NotATriangle

# Граничные случаи
def test_edge_cases():
    assert triangle(0, 0, 0) == Triangle.Equal
    assert triangle(1, 1, 2) == Triangle.NotATriangle
    assert triangle(5, 5, 10) == Triangle.NotATriangle

# Негативные случаи
def test_negative_values():
    assert triangle(-1, 2, 3) == Triangle.NotATriangle
    assert triangle(1, -2, 3) == Triangle.NotATriangle
    assert triangle(1, 2, -3) == Triangle.NotATriangle

# Большие значения
def test_large_values():
    assert triangle(1000000, 1000000, 1000000) == Triangle.Equal
    assert triangle(1000000, 1000000, 1000001) == Triangle.Isoscale
    assert triangle(1000000, 1000001, 1000000) == Triangle.Isoscale
    assert triangle(1000001, 1000000, 1000000) == Triangle.Isoscale
    assert triangle(1000000, 1000001, 1000002) == Triangle.Regular