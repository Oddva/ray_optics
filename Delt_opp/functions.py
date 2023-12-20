"""
Functions by Oddvar
-------------------
This should give you all the necesarry functions for the program\n\n
Snells_law(theta_0, n_0, n_1)\n
Vec_angle(vector)\n
angleBetweenUnitVectors(vec1, vec2)\n
get_incidence_angle(self, object)\n
set_new_angle(ray_line, incident_angle, flip, object)\n
Point_line_distance(x,y,line_obj)

"""

import numpy as np
import matplotlib.pyplot as plt
precision = 2000
boarder_height = 1000
boarder_width = 2000

def Snells_law(theta_0, n_0, n_1):
    """
    Calculates the new angle from the refraction.
    n_0 * sin(theta_0) = n_1 * sin(theta_1)
    """
    theta_1 = np.arcsin(np.sin(theta_0) * n_0/n_1)
    return theta_1, True

def Vec_angle(vector):
    """
    Returns angle of an unit vector with [x,y]
    """
    return np.arctan(vector[1]/vector[0])/(np.sqrt(vector[0]**2 + vector[1]**2))

def angleBetweenUnitVectors(vec1, vec2):
    """
    Calculates the angle between two unit vectors, where you get the smallest angle between them by following variable desc.
    vec_closest_to_0 is the vector with its angle closest to zero
    dont need to devide by anything to get the angle since we use unit_vectors for the calculation
    """
    return np.arccos(np.dot(vec1,vec2))


def get_incidence_angle(self, object):
    """
    Gets the incidence angle which is always positive. 
    Since the perp vector can have two directions, flip is added to notify the user of this, which will be used for other calculations.
    """
    line = self.get_last_line()
    flip = False    #if flip is false then the perp_vec and ray.unit_vec have the same direction
    incident_angle = angleBetweenUnitVectors(line.unit_vec, object.perp_vec)
    if incident_angle > np.pi/2: #works since the incident angle should pick the closest perp_vector out the two.
        incident_angle = np.pi-incident_angle
        flip = True
    return incident_angle, flip 

def set_new_angle(ray_line, incident_angle, flip, object): 
    """
    Denne funksjonen skal bruke snells lov til å finne en ny vinkel for refraksjonen av stårlen som går inn i et medium.
    Denne bør gi riktig retning uten at man trenger å tenke hvilken vectorene har. Er perp vector, i motsatt retning av strålen bør ikke dette ha noe å si.
    ray_line: er et linje objekt uten begrensninger
    incident_angle: er innfallsvinkel
    flip: er noe som er bestemt tidligere som finner ut om strålen er i retning med perp vector(flip == False) eller om den er i motsatt retning av flip(flip == True)
    obj: er et objekt som må ha en perp_vec og en n(permativitet), som brukes i utregninger
    """
    if ray_line.state == False: 
        refraction_angle = Snells_law(incident_angle, ray_line.n, object.n)[0]
        if flip:
            new_angle = Vec_angle(-object.perp_vec) +  refraction_angle
            ray_line.state = True
            return new_angle
        if flip == False:
            new_angle = Vec_angle(object.perp_vec) +  refraction_angle
            ray_line.state = True
            return new_angle
    elif ray_line.state == True:
        refraction_angle = Snells_law(incident_angle, object.n, ray_line.n,)[0]
        if flip:
            new_angle = Vec_angle(-object.perp_vec) +  refraction_angle                      
            ray_line.state = False
            return new_angle
        if flip == False:
            new_angle = Vec_angle(object.perp_vec) +  refraction_angle              
            ray_line.state = False                
            return new_angle

def Point_line_distance(x,y,line_obj):
    """
    This function should calculate the distance between a point(x,y) and a line
    which is represented with by = ax + c, where b = 1. I have used the c variable as line_obj.b in my code.

    d = |(ax+by+c)/(sqrt(a^2+b^2))|
    """
    print(line_obj.a)
    print(x)
    print(y)
    print(line_obj.b)
    d = abs((line_obj.a*x + y + line_obj.b)/(np.sqrt(line_obj.a**2 + 1)))
    return d

def Boarder(y_list):
    """
    Returnere om en ray er innenfor området man ser på.
    Hvis man er innenfor returnerer den False, None
    Hvis man er utenfor returnere den True, n. Der n er hvilken iterasjon dette skjedde på.
    Denne funksjonen skal bestemme grensen der bølger stopper.\n
    Bølger stopper for x verdier allerede, men ikke for y verdier.\n
    Hvis en verdi går mot evig y verdi får man problemer.\n
    Denne klassen skal stoppe den hvis man får en y verdi over 1000.
    """
    for n,height in enumerate(y_list):
        if height < 0:
            return True, n #returnerer at den traff kanten av y grensa og hvilken iterasjon dette skjedde på
        if height > 1000:
            return True, n



if __name__ == "__main__":
    
    class test:
        def __init__(self,a,b):
            self.a = a
            self.b = b
    
    p = (1,0)
    obj = test(0,1)
    r = 2 
    d = Point_line_distance(1,0, obj)
    print(d)
    e = r * np.cos(np.arcsin(d/r))
    print("+-",e)