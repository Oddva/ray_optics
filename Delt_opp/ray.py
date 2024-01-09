import numpy as np
import matplotlib.pyplot as plt
import functions as f
precision = 20000
boarder_height = 1000
boarder_width = 2000

class RayLine:
    """
    Is a line which can be used for ray lines
    """
    def __init__(self,x0,y0, unit_vec, permativity, color):
        self.type = "rayline"
        self.name  = "orgin, [{}, {}]".format(round(x0), round(y0))
        self.color = color
        self.n = permativity
        self.unit_vec = unit_vec
        # print("Dette skal være enhetsvektoren: ", self.unit_vec)
        self.angle = f.Vec_angle(self.unit_vec)
        self.x0 = x0
        self.y0 = y0
        self.norm = np.linalg.norm(self.unit_vec) #lenght of vector, should always be 1
        self.perp_vec = np.array([-self.unit_vec[1], self.unit_vec[0]]) 
        self.x_list = np.linspace(x0,self.unit_vec[0]*2000, precision) #x-list should be unecesary since enumerate of y_list gives the same
        if self.unit_vec[0] < 0:
            self.x_list = np.linspace(x0, self.unit_vec[0]*2000, precision) 
        self.a = np.tan(self.angle)
        self.b = self.y0 - self.a * self.x0
        self.y_list = self.a * self.x_list + self.b #you should not use the values before the line starts and after it ends
        self.x1 = self.x_list[-1]
        self.y1 = self.y_list[-1]
        self.state = False

    def set_name(self, name):
        self.name = "{}, [{}, {}]".format(name, round(self.x0), round(self.y0))

    def set_state(self, state):
        """
        bestemmer om et objekt er inni eller utenfor et et annet objekt
        slik at man snur på permativitetene i snells lov.
        """
        self.state = state

    def change(self, x_enter, y_enter):        

        self.x_list = np.array([x_enter, self.x0]) 
        self.y_list = np.array([y_enter, self.y0])

class Ray:
    """
    Is a projectile with a start(x0,y0) and a angle(radians).
    This contains a list of lines which represents either the refractions or the reflections of a ray
    
    """
    def __init__(self,x0,y0, ray_unit_vec):
        self.type = "ray"
        self.color = "blue"
        self.precision = precision
        self.step = 1
        self.x0 = x0
        self.y0 = y0
        self.n = 1
        self.line_list = []
        line = RayLine(x0,y0,ray_unit_vec, self.n, self.color)
        self.line_list.append(line)
        self.retired_line_list = []

    def plot(self):
        for line in self.retired_line_list:
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

    def set_new_line(self, xn, yn, ray_unit_vec):
        """
        Should calculate a new angle using snells law
        """
        new_line = RayLine(xn,yn,ray_unit_vec,self.n,self.color)
        self.line_list.append(new_line)
        return new_line

    def retire_line(self, ray_line):
        """
        Retires a line so it doesn't calculate intersections for the same line
        """
        self.retired_line_list.append(ray_line)

    def remove_line(self, ray_line):
        """
        Removes a rat_line from the line list
        """
        self.line_list.remove(ray_line) #this does not involve indexing


    def get_incidence_angle(self, ray_line, object, x, y):
        """
        Gets the incidence angle which is always positive. 
        Since the perp vector can have two directions, flip is added to notify the user of this, 
        which will be used for other calculations.
        
        AI is creating summary for get_incidence_angle

        Args:
            ray_line ([object]): ray_line objects
            object ([object]): [description]
            x ([float]): [description]
            y ([float]): [description]

        Returns:
            [type]: [description]
        """
        flip = False    #if flip is false then the perp_vec and ray.unit_vec have the same direction
        incident_angle = f.angleBetweenUnitVectors(object.get_perp_vec(), ray_line.unit_vec)
        if incident_angle > np.pi/2: #works since the incident angle should pick the closest perp_vector out the two.
            incident_angle = np.pi-incident_angle
            flip = True
        return incident_angle, flip 

    def refraction(self, ray_line, x_enter, y_enter, x_exit, y_exit, obj):
        """
        Makes a new ray_line based on the refraction of the ray.
        """
        obj.set_perp_vec(x_enter, y_enter)
        ref_vec = f.Snells_law_vectors(ray_line, obj)
        new_line = self.set_new_line(x_enter,y_enter,ref_vec)
        new_line.set_name("refraction")
        #gjelder bare for sirkeler
        if x_exit is not None:
            obj.set_perp_vec(x_exit, y_exit)
            # new_line.set_state(True)
            ref_vec = f.Snells_law_vectors(ray_line, obj)
            new_line = self.set_new_line(x_exit, y_exit,ref_vec)
            new_line.set_name("refraction")

            # incident_angle,flip = self.get_incidence_angle(new_line, obj, x_exit, y_exit)
            # new_line.set_state(False)
            # new_angle = f.set_new_angle(new_line, incident_angle,flip,obj)
            # new_line = self.set_new_line(x_exit,y_exit,new_angle)
            # new_line.set_name("refraction")

    def reflection(self,ray_line,x,y,obj):
        """
        Makes a new ray_line based on the reflection of the ray.
        """
                # KAN BRUKE DETTE
        cosI = np.dot(ray_line.unit_vec, obj.perp_vec)  #dette cos(incidence angle)
        d_out = ray_line.unit_vec - 2.0*cosI*obj.perp_vec #dette gir den nye reflekterte vektoren
        # reflection_angle = f.Vec_angle(d_out)
        # print("vector out is: ", d_out)
        # print("reflection angle: ", reflection_angle)
        new_line = self.set_new_line(x,y,d_out)
        new_line.set_name("reflection")


    def check_collision(self, ray_line, objects):
        """
        Should check if the ray and objects collide. 
        If they collide it returns 
        [True, intersection_x, intersection_y, 
        possible_intersection_x2, possible_intersection_y2, object].
        """
        for object in objects: 
            collision = object.check_collision(ray_line)
            if collision[0]==True:
                print("collision[1] == ray_line.x0 and collision[2] == ray_line.y0\n", 
                      collision[1], "==", ray_line.x0, collision[2], "==", ray_line.y0)
                if collision[1] == ray_line.x0 and collision[2] == ray_line.y0:
                    continue
                return collision 
        return False, None, None, None, None, None      

    def Calculated(self, objects):
        """
        Will calculate the projection of a ray and alter it if it collides with a object inside of the limits.
        \nThis uses check_collision which adds new lines to the ray
        """
        coll = True
        n = 0 
        while coll:
            print(self.line_list)
            for ray_line in self.line_list:
                coll, x_enter, y_enter, x_exit, y_exit, obj = self.check_collision(ray_line, objects) #this function should return a coll = false, if there is no collisions
                if coll:
                    ray_line.change(x_enter, y_enter)
                    self.retire_line(ray_line) 
                    self.remove_line(ray_line) #removes the ray_line from the list, since it should not interact with other objects anymore
                    obj.set_perp_vec(x_enter,y_enter)
                    self.refraction(ray_line, x_enter, y_enter, x_exit, y_exit, obj)
                    self.reflection(ray_line, x_enter, y_enter, obj)
                    n += 1
                    if n > 99:
                        coll = False
                        print("Line_list = ", len(self.line_list))
                        break
        for line in self.line_list:
            self.retire_line(line)

