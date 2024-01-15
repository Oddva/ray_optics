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
    Is a circular object which interacts with rays\n
    -------------------------------------
    For it to run you need to input:
    - Center of the circle x0, y0 
    - Refractive index
    - Radius 
    - Type, this should be either "glass", "mirror" or "dark"\n

    This objects has some problems where it needs a new algorythm for checking for intersections.
    After changing the code so that it handles vectors, this code has some problems
    """
    def __init__(self, x0,y0, refractive_index, radius, type):
        self.type = type
        self.x0 = x0
        self.y0 = y0
        self.n = refractive_index
        self.radius = radius
        self.perp_vec = None

    def plot(self):
        plt.gca().add_patch(plt.Circle((self.x0,self.y0),self.radius, color="slategrey"))

    def get_perp_vec(self):
        """
        The perp vector will change depending on where the ray collides with the circle. 
        This will first give you the normal vector at that point. This will after be used as to calculate the perp vector
        """
        return self.perp_vec

    def set_perp_vec(self, x, y):
        """
        The perp vector will change depending on where the ray collides with the circle. 
        This will first give you the normal vector at that point. This will after be used as to calculate the perp vector
        """
        normal_vec = np.array([x-self.x0, y-self.y0]) #from origo of circle to the intersection[x,y].
        perp_vec = normal_vec / np.linalg.norm(normal_vec)
        self.perp_vec = perp_vec

    def get_intersection(self, ray_obj):
        """
        This function calculates the intersection putting together the general functions for a line and a circle.
        line:   y = ax + c
        circle: (x-h)^2 - (y-k)^2 = r^2, P(h,k), h = self.x0, k = self.y0
        
        https://stackoverflow.com/questions/1073336/circle-line-segment-collision-detection-algorithm
        En algoritme som kan være verd å prøve.
        """
        A = 1+ray_obj.a**2
        B = 2*ray_obj.a - 2* self.x0 - 2*ray_obj.a*self.y0 
        C = self.x0**2 + ray_obj.b**2 - 2*ray_obj.b*self.y0 + self.y0**2 - self.radius**2
        root = B**2 - 4*A*C
        if root < 0:
            print("root= ", root)
            return None, None, None, None,
        x1 = (-B+np.sqrt(root))/(2*A)
        x2 = (-B-np.sqrt(root))/(2*A)
        y1 = ray_obj.a*x1 + ray_obj.b
        y2 = ray_obj.a*x2 + ray_obj.b                       
        v1 = [x1-ray_obj.x0,y1-ray_obj.y0] 
        v2 = [x2-ray_obj.x0,y2-ray_obj.y0]
        if np.sqrt(v1[0]**2 + v1[1]**2) < np.sqrt(v2[0]**2 + v2[1]**2):
            x_entering = x1
            y_entering = y1
            x_exiting = x2
            y_exiting = y2
        else:
            x_entering = x2
            y_entering = y2
            x_exiting = x1
            y_exiting = y1
        return x_entering, y_entering, x_exiting, y_exiting
        

    def check_collision(self,ray_line):
        """
        Checking if a ray is inside of the circle. 
        """
        x_enter, y_enter, x_exit, y_exit = self.get_intersection(ray_line)
        if x_enter is None:
            return False, None, None, None, None, self
        else:
            return True, x_enter, y_enter, x_exit, y_exit, self


class Ellipse:
    """
    Creates a ellipse object
    """
    def check_collision(self,ray):
        """
        Checking if a ray is inside of the circle. 
        """
        pass