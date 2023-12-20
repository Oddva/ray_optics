import numpy as np
import matplotlib.pyplot as plt
import functions as f
precision = 2000
boarder_height = 1000
boarder_width = 2000

class RayLine:
    """
    Is a line which can be used for ray lines
    """
    def __init__(self,x0,y0, angle, permativity, color):
        self.type = "rayline"
        self.name = "x0={},y0={}".format(x0,y0)
        self.color = color
        self.angle = angle
        self.n = permativity
        self.unit_vec = np.array([np.cos(angle), np.sin(angle)])
        self.x0 = x0
        self.y0 = y0
        self.norm = np.linalg.norm(self.unit_vec) #lenght of vector, should always be 1
        self.perp_vec = np.array([-self.unit_vec[1], self.unit_vec[0]]) 
        # creates the precision and x-axis of the plot
        self.precision = precision
        self.x_list = np.linspace(0,2000, self.precision) #x-list should be unecesary since enumerate of y_list gives the same
        self.a = np.tan(self.angle)
        self.b = self.y0 - self.a * self.x0
        self.y_list = self.a * self.x_list + self.b #you should not use the values before the line starts and after it ends
        self.x1 = self.x_list[-1]
        self.y1 = self.y_list[-1]
        print(self.y_list)


class Ray:
    """
    Is a projectile with a start(x0,y0) and a angle(radians).
    This contains a list of lines which represents either the refractions or the reflections of a ray
    """
    def __init__(self,x0,y0, angle):
        self.state = False #var tidligere en variabel som ble brukt inne i legmer, men nå trur jeg den ikke brukes lengre
        self.type = "ray"
        self.color = "blue"
        self.precision = precision
        self.step = 1
        self.x0 = x0
        self.y0 = y0
        self.n = 1
        self.line_list = []
        line = RayLine(x0,y0,angle, self.n, self.color)
        self.line_list.append(line)

    def plot(self):
        for line in self.line_list:
            plt.plot(line.x_list, line.y_list, label="{}".format(line.name))
        
    def append_line(self,line):
        """
        Line is a Line(x0,y0,angle,color)-object
        """
        self.line_list.append(line) 

    def get_last_line(self):
        """
        Gets the last line-object which is used a lot for calculating the next line
        """
        return self.line_list[-1]


    def set_new_line(self, xn, yn, angle):
        """
        Should calculate a new angle using snells law
        """
        new_line = RayLine(xn,yn,angle,self.n,self.color)
        self.line_list.append(new_line)
        
    def refraction(self,ray_line,x,y,obj):
        """
        Makes a new ray_line based on the refraction of the ray.
        """
        incident_angle,flip = f.angleBetweenUnitVectors(obj.get_perp_vec, ray_line.unit_vec)
        new_angle = f.set_new_angle(ray_line, incident_angle,flip,obj)
        self.set_new_line(x,y,new_angle)

    def reflection(self,ray_line,x,y,obj):
        """
        Makes a new ray_line based on the reflection of the ray.
        """
        

    def check_collision(self, objects):
        """
        Should check if the ray and the closest object collide. If they collide then there will be created a new line with angle
        equal to the refraction line of the object.
        """
        ray_line = self.get_last_line()
        
        for object in objects:
            #sjekk kollisjoner med forskjellige objekter og vinkelene som man får ut fra disse.
            collision = object.check_collision(ray_line)      #vegg kollisjon som tar inn linje objektet                START
            if collision[0]==True:
                return collision    #returns this collison
        return collision            #returns that no collision happened

    def Calculated(self, objects):
        """
        Will calculate the projection of a ray and alter it if it collides with a object inside of the limits.
        This uses check_collision which adds new lines to the ray
        """
        coll = True
        while coll:
            coll, x,y,obj = self.check_collision(objects) #this function should return a coll = false, if there is no collisions
            if coll:
                ray_line = self.get_last_line()
                self.refraction(ray_line,x,y,obj)
                self.reflection(ray_line,x,y,obj)
                break

