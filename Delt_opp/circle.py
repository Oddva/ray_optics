import numpy as np
import sympy as sp
import matplotlib.pyplot as plt
import matplotlib.patches as ptc
import functions as f
precision = 20000
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
        print(self.x0)
        print(self.y0)
        normal_vec = np.array([x-self.x0, y-self.y0]) #from origo of circle to the intersection[x,y].
        perp_vec = normal_vec / np.linalg.norm(normal_vec)
        print("(h,k)= ({}, {})".format(self.x0,self.y0), "Perp_vec= ", perp_vec)
        self.perp_vec = perp_vec

    def get_intersection(self, ray_obj):
        """
        This function calculates the intersection putting together the general functions for a line and a circle.
        line:   y = ax + c
        circle: (x-h)^2 - (y-k)^2 = r^2, P(h,k), h = self.x0, k = self.y0
        
        https://stackoverflow.com/questions/1073336/circle-line-segment-collision-detection-algorithm
        En algorytme som kan være verd å prøve.
        """
        ray_d = np.array([ray_obj.x1 - ray_obj.x0, ray_obj.y1 - ray_obj.y0]) 
        cir_ray_f = np.array([ray_obj.x0 - self.x0, ray_obj.y0 - self.y0]) 


        A = ray_d.dot(ray_d)
        B = 2*cir_ray_f.dot(ray_d)
        C = cir_ray_f.dot(cir_ray_f) - self.radius **2      
        root = B**2 - 4*A*C
        if root < 0: #no intersection
            print("root= ", root)
            return None, None, None, None,
        x1 = (-B+np.sqrt(root))/(2*A)
        x2 = (-B-np.sqrt(root))/(2*A)
        y1 = ray_obj.a*x1 + ray_obj.b
        y2 = ray_obj.a*x2 + ray_obj.b                          
        v1 = [x1-ray_obj.x0,y1-ray_obj.y0] 
        v2 = [x2-ray_obj.x0,y2-ray_obj.y0]
        print("x1=",x1,"y1=",y1,"\nx2=", x2,"y2=",y2)
        print("v1=",v1,"\nv2=", v2)
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
            
        # #STØTTER IKKE VEKTORER MEN FUNGERTE TIDLIGERE
        # A = 1+ray_obj.a**2
        # B = 2*ray_obj.a - 2* self.x0 - 2*ray_obj.a*self.y0 
        # C = self.x0**2 + ray_obj.b**2 - 2*ray_obj.b*self.y0 + self.y0**2 - self.radius**2
        # root = B**2 - 4*A*C
        # if root < 0:
        #     print("root= ", root)
        #     return None, None, None, None,
        # x1 = (-B+np.sqrt(root))/(2*A)
        # x2 = (-B-np.sqrt(root))/(2*A)
        # y1 = ray_obj.a*x1 + ray_obj.b
        # y2 = ray_obj.a*x2 + ray_obj.b                           ####SJEKK MATTEN PÅ DENNE DELEN
        # v1 = [x1-ray_obj.x0,y1-ray_obj.y0] 
        # v2 = [x2-ray_obj.x0,y2-ray_obj.y0]
        # print("x1=",x1,"y1=",y1,"\nx2=", x2,"y2=",y2)
        # print("v1=",v1,"\nv2=", v2)
        # if np.sqrt(v1[0]**2 + v1[1]**2) < np.sqrt(v2[0]**2 + v2[1]**2):
        #     x_entering = x1
        #     y_entering = y1
        #     x_exiting = x2
        #     y_exiting = y2
        # else:
        #     x_entering = x2
        #     y_entering = y2
        #     x_exiting = x1
        #     y_exiting = y1
        # return x_entering, y_entering, x_exiting, y_exiting
        

    def check_collision(self,ray_line):
        """
        Checking if a ray is inside of the circle. 
        """
        print(self.x0, self.y0, ray_line.x0, ray_line.y0, ray_line.x1, ray_line.y1)
        x_enter, y_enter, x_exit, y_exit = self.get_intersection(ray_line)
        print("Intersection at x=[{}],y=[{}]".format(x_enter,y_enter))
        print("Intersection at x=[{}],y=[{}]".format(x_exit,y_exit))
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