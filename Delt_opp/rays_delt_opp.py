import numpy as np
import matplotlib.pyplot as plt
import circle
import ray
import functions as f 
import lines

precision = 2000
boarder_height = 1000
boarder_width = 2000



if __name__ == "__main__":
    boarder_height = 1000
    boarder_width = 2000
    amount_of_rays = 1
    start_angle=0
    objects = []
    circ = circle.Circle(1000,500,1.5,300)
    objects.append(circ)
    ray1 = ray.Ray(0, 500, 0.1)
    ray1.Calculated(objects)
    fig = plt.figure(figsize=(20,10))
    plt.style.use('dark_background')
    circ.plot()
    ray1.plot()
    plt.xlim(0,boarder_width)
    plt.ylim(0, boarder_height)
    plt.legend()
    plt.grid(True)
    plt.show()





    # for ray in rays:    
    #     ray.Caluclate_projection(wall.get_wall())
    #     plt.plot(ray.x_list, ray.y_list, color=ray.color)
    # wall = Wall(400, 600, 400, 600, 1.52, 300)
    # print("starting coords[{},{}], end cooords [{},{}]".format(wall.line2.x0, wall.line2.y0, wall.line2.x1, wall.line2.y1))