from display import *
from matrix import *
import math

def add_circle( points, cx, cy, cz, r, step ):
    x = 0
    while x < 1.001:
        add_edge(points, r*math.cos(2*x*math.pi) + cx, r*math.sin(2*x*math.pi) + cy, cz, r*math.cos((x + step)*math.pi*2) + cx, r*math.sin((x + step)*math.pi*2) + cy, cz)
        x += step

def add_curve( points, x0, y0, x1, y1, x2, y2, x3, y3, step, curve_type ):
    if curve_type == "hermite":
        x_coef = generate_curve_coefs(x0, x2, x1, x3, "hermite")
        y_coef = generate_curve_coefs(y0, y2, y1, y3, "hermite")
    elif curve_type == "bezier":
        x_coef = generate_curve_coefs(x0, x1, x2, x3, "bezier")
        y_coef = generate_curve_coefs(y0, y1, y2, y3, "bezier")
    x = 0
    while x < 1:
        x_val_0 = point_calc(x_coef, x)
        y_val_0 = point_calc(y_coef, x)
        x += step
        x_val_1 = point_calc(x_coef, x)
        y_val_1 = point_calc(y_coef, x)
        add_edge(points, x_val_0, y_val_0, 0, x_val_1, y_val_1, 0)

def point_calc( coefficients, step ):
    return pow(step, 3) * coefficients[0][0] + pow(step, 2) * coefficients[0][1] + step * coefficients[0][2] + coefficients[0][3]

def draw_lines( matrix, screen, color ):
    if len( matrix ) < 2:
        print "Need at least 2 points to draw a line"

    p = 0
    while p < len( matrix ) - 1:
        draw_line( screen, matrix[p][0], matrix[p][1],
                   matrix[p+1][0], matrix[p+1][1], color )
        p+= 2

def add_edge( matrix, x0, y0, z0, x1, y1, z1 ):
    add_point( matrix, x0, y0, z0 )
    add_point( matrix, x1, y1, z1 )

def add_point( matrix, x, y, z=0 ):
    matrix.append( [x, y, z, 1] )


def draw_line( screen, x0, y0, x1, y1, color ):
    dx = x1 - x0
    dy = y1 - y0
    if dx + dy < 0:
        dx = 0 - dx
        dy = 0 - dy
        tmp = x0
        x0 = x1
        x1 = tmp
        tmp = y0
        y0 = y1
        y1 = tmp

    if dx == 0:
        y = y0
        while y <= y1:
            plot(screen, color,  x0, y)
            y = y + 1
    elif dy == 0:
        x = x0
        while x <= x1:
            plot(screen, color, x, y0)
            x = x + 1
    elif dy < 0:
        d = 0
        x = x0
        y = y0
        while x <= x1:
            plot(screen, color, x, y)
            if d > 0:
                y = y - 1
                d = d - dx
            x = x + 1
            d = d - dy
    elif dx < 0:
        d = 0
        x = x0
        y = y0
        while y <= y1:
            plot(screen, color, x, y)
            if d > 0:
                x = x - 1
                d = d - dy
            y = y + 1
            d = d - dx
    elif dx > dy:
        d = 0
        x = x0
        y = y0
        while x <= x1:
            plot(screen, color, x, y)
            if d > 0:
                y = y + 1
                d = d - dx
            x = x + 1
            d = d + dy
    else:
        d = 0
        x = x0
        y = y0
        while y <= y1:
            plot(screen, color, x, y)
            if d > 0:
                x = x + 1
                d = d - dy
            y = y + 1
            d = d + dx
