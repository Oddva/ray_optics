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
    def __init__(self, x0, y0, x1, y1, refractive_index, color):
        self.x0 = x0
        self.x1 = x1
        self.y0 = y0
        self.y1 = y1
        self.type = "line"
        self.name = "x0={},y0={}".format(self.x0,self.y0)
        self.color = color
        self.n = refractive_index
        self.a = (self.y1-self.y0)/(self.x1-self.x0)
        self.b = self.y0 - self.a * self.x0
        self.angle = np.arctan(self.a)
        self.unit_vec = np.array([np.cos(self.angle), np.sin(self.angle)])
        self.norm = np.linalg.norm(self.unit_vec) #lenght of vector, should always be 1
        self.perp_vec = np.array([-self.unit_vec[1], self.unit_vec[0]]) 
        self.precision = precision
        self.x_list = np.linspace(0,boarder_width, 2000) #x-list should be unecesary since enumerate of y_list gives the same
        self.y_list = self.a * self.x_list + self.b 

    def set_perp_vec(self, x_enter, y_enter):
        pass

    def get_perp_vec(self):
        return self.perp_vec

    def plot(self):
        plt.plot([self.x_list[0], self.x_list[-1]], [self.y_list[0], self.y_list[-1]], self.color)

class Line(Object_Line):
    """
    This class creates a line object which is used create objects for Rays
    The starting and ending positions does not matter, its only a different way creating lines
    ----------------------------------------------
    x0 - x starting pos
    y0 - y starting pos
    x1 - x ending pos
    y1 - y ending pos
    refractive_index - parameter which decides the refractive index of rays
    color - gives it any color you want based on matplotlibs color scheme
    type - "transparent", "mirror" or "dark" 
    """


    def __init__(self, x0, y0, x1, y1, refractive_index, color, type):
        super().__init__(x0, y0, x1, y1, refractive_index, color)
        self.type = type

    def line_Intersection(self, ray_line): #fiks denne
        """
        Returns the intersection between two linear lines, inside the limits of the object
        """
        if ray_line.a == self.a:                
            return False, None, None
        x = (ray_line.b - self.b)/(self.a - ray_line.a) #x-itersection
        y = (self.a * x + self.b)                   #y-itersection
        if x < 2000 and x > 0 and y < 2000 and y > 0:
            return True, x, y
        else:
            return False, None, None

    def check_collision(self, ray_line):
        coll, x_enter, y_enter = self.line_Intersection(ray_line)
        if coll == True:
            return coll, x_enter, y_enter, None, None, self
        else:
            return False, False, False, None, None, self 


def Setup_walls(x0,y0,x1,y1,thickness,refractive_index,color):
    """
    This function will setup up the walls in a way that the lines in it will always go in a positive x-direction.
    Returns: a list of 4 line objects
    """
    line0 = Object_Line(x0,y0,x1,y1,refractive_index,color)
    perp = line0.perp_vec
    thickness_x = -thickness*perp[0]
    thickness_y = -thickness*perp[1]
    line1 = Object_Line(x0,y0,x0+thickness_x,y0+thickness_y,refractive_index,"r.")
    line2 = Object_Line(x1,y1,x1+thickness_x,y1+thickness_y,refractive_index,"g-")
    line3 = Object_Line(x0+thickness_x,y0+thickness_y,x1+thickness_x,y1+thickness_y,refractive_index,"y-")
    return [line0,line1,line2,line3]


class Wall:
    """
    Creates a wall
    """
    def __init__(self,x0,y0,x1,y1, thickness, refractive_index,type):
        self.type = type
        self.color = "blue"
        self.n = refractive_index
        self.thickness = thickness
        self.x0 = x0
        self.y0 = y0
        self.x1 = x1
        self.y1 = y1
        self.wall = Setup_walls(x0,y0,x1,y1,self.thickness,refractive_index,self.color)

        
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

    def line_Intersection(self,ray_line,object): #fiks denne
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
            return True
        else:
            return False, None, None

    def check_collision(self, ray_line):
        """
        Checking if a ray is inside of the circle. Checks if the ray is inside of the object, and which side of the "wall" it entered. 
        """
        for wall_line in self.wall:
            intersection = self.line_Intersection(ray_line,wall_line)  #fiks denne neste.
            if intersection[0] == True:
                return True, wall_line
        return False, None