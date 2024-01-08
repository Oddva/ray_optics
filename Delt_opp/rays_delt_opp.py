import numpy as np
import matplotlib.pyplot as plt
import circle
import ray 
import functions as f 
import lines

precision = 20000
boarder_height = 1000
boarder_width = 2000



if __name__ == "__main__":
    boarder_height = 1000
    boarder_width = 2000
    amount_of_rays = 1
    start_angle=0
    objects = []
    line1 = lines.Line(700, 200, 701, 800, 1.5, "green")
    line2 = lines.Line(900, 200, 901, 800, 1.5, "green")
    circ = circle.Circle(600,300,1.5,150)
    objects.append(line1)
    # objects.append(line2)
    # objects.append(circ)
    angle = 0.1 #rad
    ray_unit_vec = np.array([np.cos(angle), np.sin(angle)])
    ray1 = ray.Ray(0, 300, ray_unit_vec)
    ray1.Calculated(objects)
    plt.style.use('dark_background')
    fig = plt.figure(figsize=(20,10))
    for obj in objects:
        obj.plot()
    ray1.plot()
    plt.xlim(0,boarder_width)
    plt.ylim(0, boarder_height)
    plt.legend()
    # plt.grid(True)
    plt.show()





    # for ray in rays:    
    #     ray.Caluclate_projection(wall.get_wall())
    #     plt.plot(ray.x_list, ray.y_list, color=ray.color)
    # wall = Wall(400, 600, 400, 600, 1.52, 300)
    # print("starting coords[{},{}], end cooords [{},{}]".format(wall.line2.x0, wall.line2.y0, wall.line2.x1, wall.line2.y1))