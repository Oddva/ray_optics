import numpy as np
import matplotlib.pyplot as plt
import functions as f
precision = 2000
boarder_height = 1000
boarder_width = 2000

class Object_Line:
    """
    Is a line which can be used for objects
    """
    def __init__(self, x0, y0, x1, y1, permativity, color):
        self.x0 = x0
        self.x1 = x1
        self.y0 = y0
        self.y1 = y1
        # if x0 > x1: #\Delta x is always positive
        #     self.x0 = x1
        #     self.x1 = x0
        #     self.y0 = y1
        #     self.y1 = y0
        self.type = "line"
        self.name = "x0={},y0={}".format(self.x0,self.y0)
        self.color = color
        self.n = permativity
        self.a = (self.y1-self.y0)/(self.x1-self.x0)
        self.b = self.y0 - self.a * self.x0
        self.angle = np.arctan(self.a)
        self.unit_vec = np.array([np.cos(self.angle), np.sin(self.angle)])
        self.norm = np.linalg.norm(self.unit_vec) #lenght of vector, should always be 1
        self.perp_vec = np.array([-self.unit_vec[1], self.unit_vec[0]]) 
        self.precision = precision
        self.x_list = np.linspace(self.x0,self.x1,int(self.x1-self.x0)) #x-list should be unecesary since enumerate of y_list gives the same
        self.y_list = self.a * self.x_list + self.b 



def Setup_walls(x0,y0,x1,y1,thickness,permativity,color):
    """
    This function will setup up the walls in a way that the lines in it will always go in a positive x-direction.
    Returns: a list of 4 line objects
    """
    line0 = Object_Line(x0,y0,x1,y1,permativity,color)
    perp = line0.perp_vec
    thickness_x = -thickness*perp[0]
    thickness_y = -thickness*perp[1]
    line1 = Object_Line(x0,y0,x0+thickness_x,y0+thickness_y,permativity,"r.")
    line2 = Object_Line(x1,y1,x1+thickness_x,y1+thickness_y,permativity,"g-")
    line3 = Object_Line(x0+thickness_x,y0+thickness_y,x1+thickness_x,y1+thickness_y,permativity,"y-")
    return [line0,line1,line2,line3]


class Wall:
    """
    Creates a wall
    """
    def __init__(self,x0,y0,x1,y1, thickness, permativity):
        self.type = "wall"
        self.color = "blue"
        self.n = permativity
        self.thickness = thickness
        self.x0 = x0
        self.y0 = y0
        self.x1 = x1
        self.y1 = y1
        self.wall = Setup_walls(x0,y0,x1,y1,self.thickness,permativity,self.color)

        
    def plot(self):
        """
        Plots the line-objects of the wall
        """
        for line in self.wall:
            plt.plot(line.x_list, line.y_list, line.color)

    def get_refraction_angle(self, ray_line):
        """
        Should calculate the refraction angle between the ray_line and line of this side of the wall
        """
        incident_angle = f.angleBetweenUnitVectors(-ray_line.unit_vec, self.unit_vec)
        refraction_angle = f.Snells_law(incident_angle, ray_line.n, self.n)
        return refraction_angle

    def line_Intersection(self,x,y,ray_line,object): #fiks denne
        """
        Returns the intersection between two linear lines, inside the limits of the object
        """
        if object.a == ray_line.a:                
            return False, None, None
        if self.last_intersected_wall_line == object:
            return False, None, None
        d = f.Point_line_distance(x,y,object)
        if d < 5:
            print("Collision detected")
            return True, x, y
        else:
            return False, None, None

    def check_collision(self,xn,yn, ray_line):
        """
        Checking if a ray is inside of the circle. Checks if the ray is inside of the object, and which side of the "wall" it entered. 
        """
        for wall_line in self.wall:
            intersection = self.line_Intersection(xn,yn,ray_line,wall_line)  #fiks denne neste.
            if intersection[0] == True:
                return True, wall_line
        return False, None