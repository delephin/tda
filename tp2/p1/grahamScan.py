from math import atan2

# para ordenar según su ángulo en radianes
def sort_by_angle(pivot, point):
    return atan2(point[1] - pivot[1], point[0] - pivot[0])

# determinante de P1P2 P1P3, define si el giro es a der o izq
def det(p1, p2, p3):
    return (p2[0] - p1[0]) * (p3[1] - p1[1]) - (p2[1] - p1[1]) * (p3[0] - p1[0])

def convex_hull(points):
    # selecciono el punto con la menor coordenada y, en caso de empate, el de menor coordenada x
    min_point = None
    for _, point in enumerate(points):
        if min_point is None or point.y < min_point.y:
            min_point = point
        if point.y == min_point.y and point.x < min_point.x:
            min_point = point

    # ordeno según su ángulo
    sorted_points = sorted(points, key=lambda x: sort_by_angle(min_point, x))
    sorted_points.remove(min_point)

    # el punto mínimo y el de menor ángulo tienen que pertenecer a la envoltura convexa
    hull = [min_point, sorted_points[0]]

    # por cada uno de los siguientes puntos ordenados, calculo si giro a derecha o izquierda
    # - si giro a izquierda, agrego el nuevo punto a la envoltura convexa
    # - mientras gire a derecha, remuevo el último punto de la envoltura convexa
    for point in sorted_points[1:]:
        while det(hull[-2], hull[-1], point) <= 0:
            if(len(hull) > 2):
                del hull[-1]
            else:
                break
        hull.append(point)
    return hull
