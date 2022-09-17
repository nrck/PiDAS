import math


class Filter():
    def __init__(self, coefs):
        self.a = coefs[0]
        self.b = coefs[1]
        self.output_data = [0,0,0]

    def filter_new_sample(self,input_data):

        for i in range(2,0,-1):
            self.output_data[i] = self.output_data[i-1]

        self.output_data[0] = ( -self.a[1] * self.output_data[1] - self.a[2] * self.output_data[2] + self.b[0] *
                     input_data[0] + self.b[1] * input_data[1] + self.b[2] * input_data[2] ) / self.a[0]
        
        return self.output_data

