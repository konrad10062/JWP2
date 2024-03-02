import math
import numpy as np


class Vector3D:

    def __init__(self, x, y, z):
        self.x = x
        self.y = y
        self.z = z

    def __str__(self):
        return f"Vector3D({self.x},{self.y},{self.z}"

    def show_x_y_z(self):
        print(self)

    def set_x(self, x):

        self.x = x

    def set_y(self, y):
        self.y = y

    def set_z(self, z):
        self.z = z

    def norm(self):
        return math.sqrt(self.x*self.x+self.y+self.y+self.z*self.z)

    def __add__(self, other):
        return Vector3D(self.x+self.x, self.y+self.y, self.z+self.z)

    def __sub__(self, other):
        return Vector3D(self.x - self.x, self.y - self.y, self.z - self.z)

    def __mul__(self, other):
        return Vector3D(self.x*other, self.y*other, self.z*other)

    def dot(self, vector):
        return self.x*vector.x+self.y*vector.y+self.z*vector.z

    def cross(self, vector):
        a = [self.x, self.y, self.z]
        b = [vector.x, vector.y, vector.z]
        x = np.cross(a, b)

        return Vector3D(x[0], x[1], x[2])

    @staticmethod
    def are_orthogonal(vector_a, vector_b):
        return True if vector_a.dot(vector_b) == 0 else False
