from display import *
from matrix import *
from draw import *

def parse_file( fname, points, transform, screen, color ):
    with open(fname, "r") as f:
        data = f.read()
    data = data.splitlines()
    x = 0
    while x < len(data):
        if data[x] == "line":
            params = data[x+1].split(" ")
            params = [int(i) for i in params]
            add_edge( points, params[0], params[1], params[2], params[3], params[4], params[5])
            x+=1
        elif data[x] == "circle":
            params = data[x+1].split(" ")
            params = [int(i) for i in params]
            add_circle(points, params[0], params[1], 0, params[2], 0.0001)
            x+=1
        elif data[x] == "hermite":
            params = data[x+1].split(" ")
            params = [int(i) for i in params]
            add_curve(points, params[0], params[1], params[2], params[3], params[4], params[5], params[6], params[7], 0.0001, "hermite")
            x+=1
        elif data[x] == "bezier":
            params = data[x+1].split(" ")
            params = [int(i) for i in params]
            add_curve(points, params[0], params[1], params[2], params[3], params[4], params[5], params[6], params[7], 0.0001, "bezier")
            x+=1
        elif data[x] == "ident":
            ident(transform)
        elif data[x] == "scale":
            params = data[x+1].split(" ")
            params = [float(i) for i in params]
            s = make_scale(params[0], params[1], params[2])
            matrix_mult(s, transform)
            x+=1
        elif data[x] == "translate":
            params = data[x+1].split(" ")
            params = [int(i) for i in params]
            s = make_translate(params[0], params[1], params[2])
            matrix_mult(s, transform)
            x+=1
        elif data[x] == "xrotate":
            s = make_rotX(float(data[x+1]))
            matrix_mult(s, transform)
            x+=1
        elif data[x] == "yrotate":
            s = make_rotY(float(data[x+1]))
            matrix_mult(s, transform)
            x+=1
        elif data[x] == "zrotate":
            s = make_rotZ(float(data[x+1]))
            matrix_mult(s, transform)
            x+=1
        elif data[x] == "apply":
            matrix_mult(transform, points)
        elif data[x] == "display":
            draw_lines(points, screen, color)
            display(screen)
        elif data[x] == "save":
            draw_lines(points, screen, color)
            save_extension(screen, data[x+1])
            x+=1
        x+=1
