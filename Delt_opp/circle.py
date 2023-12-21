import numpy as np
import sympy as sp
import matplotlib.pyplot as plt
import matplotlib.patches as ptc
import functions as f
precision = 2000
boarder_height = 1000
boarder_width = 2000


class Circle:
    """
    Is a object which interacts with rays
    """
    def __init__(self, x0,y0, permativity, radius):
        self.type = "Circle"
        self.x0 = x0
        self.y0 = y0
        self.n = permativity
        self.radius = radius

    def plot(self):
        plt.gca().add_patch(plt.Circle((self.x0,self.y0),self.radius, color="slategrey"))

    def get_perp_vec(self, x, y):
        """
        The perp vector will change depending on where the ray collides with the circle. 
        This will first give you the normal vector at that point. This will after be used as to calculate the perp vector
        """
        normal_vec = np.array([x-self.x0, y-self.y0]) #from origo of circle to the intersection[x,y].
        perp_vec = normal_vec / np.linalg.norm(normal_vec)
        return perp_vec

    def get_intersection(self, ray_obj):
        """
        This function calculates the intersection putting together the general functions for a line and a circle.
        line:   y = ax + c
        circle: (x-h)^2 - (y-k)^2 = r^2, P(h,k), h = self.x0, k = self.y0

        """
        A = 1+ray_obj.a**2
        B = 2*ray_obj.a - 2* self.x0 - 2*ray_obj.a*self.y0 
        C = self.x0**2 + ray_obj.b**2 - 2*ray_obj.b*self.y0 + self.y0**2 - self.radius**2
        x1 = (-B+np.sqrt(B**2 - 4*A*C))/(2*A)
        x2 = (-B-np.sqrt(B**2 - 4*A*C))/(2*A)
        y1 = ray_obj.a*x1 + ray_obj.b
        y2 = ray_obj.a*x2 + ray_obj.b                           ####SJEKK MATTEN PÅ DENNE DELEN
        v1 = [x1-ray_obj.x0,y1-ray_obj.y0] 
        v2 = [x2-ray_obj.x0,y2-ray_obj.y0]
        print("x1=",x1,"y1=",y1,"\nx2=", x2,"y2=",y2)
        print("v1=",v1,"\nv2=", v2)
        if np.sqrt(v1[0]**2 + v1[1]**2) < np.sqrt(v1[0]**2 + v1[1]**2):
            x = v1[0]
            y = v1[1]
        else:
            x = v2[0]
            y = v2[1]
        return x,y
        

    def check_collision(self,ray):
        """
        Checking if a ray is inside of the circle. 
        """
        # print(self.x0, self.y0, ray.x0, ray.y0, ray.x1, ray.y1)
        s = sp.Line(sp.Point(ray.x0, ray.y0), sp.Point(ray.x1, ray.y1))
        d = int(s.distance(sp.Point(self.x0, self.y0)))
        print("shortest distance:",d)
        if d < self.radius:
            x,y = self.get_intersection(ray)
            print("Intersection at x=[{}],y=[{}]".format(x,y))
            return True, x,y,self
        else:
            return False, None, None, self


class Ellipse:
    """
    Creates a ellipse object
    """
    def check_collision(self,ray):
        """
        Checking if a ray is inside of the circle. 
        """
        pass