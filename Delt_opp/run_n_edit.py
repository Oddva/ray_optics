import numpy as np
import matplotlib.pyplot as plt
import circle
import ray 
import functions as f 
import lines
import time

precision = 2000
boarder_height = 1000
boarder_width = 2000



if __name__ == "__main__":
    start = time.time()
    
    #object examples
    objects = []
    line1 = lines.Line(300, 100, 1300, 300, 1.5, "green", "transparent")



    objects.append(line1)
  


    #ray examples
    angle = 0.0  #rad
    ray_unit_vec = np.array([np.cos(angle), np.sin(angle)])
    ray1 = ray.Ray(0, 700, ray_unit_vec)
    rays = ray.Rays(100, 100, ray_unit_vec, 20, 100)
    #kalkulerer strålebaner
    # ray1.calculated(objects)
    rays.calculated(objects)

    #makes a display and plots
    plt.style.use('dark_background')
    fig = plt.figure(figsize=(20 ,10))
    for obj in objects:
        obj.plot()
    ray1.plot()
    rays.plot()
    plt.xlim(0,boarder_width)
    plt.ylim(0, boarder_height)
    # plt.legend()
    # plt.grid(True)
    stop = time.time()
    print("Runtime: ", stop-start)
    plt.show()