import math


class Filter():
    def __init__(self, sampling_hz):
        self.__dt = 1.0 / sampling_hz
        self.__f0 = 0.45
        self.__f1 = 7.0
        self.__f2 = 0.5
        self.__f3 = 12.0
        self.__f4 = 20.0
        self.__f5 = 30.0
        self.__h2a = 1.0
        self.__h2b = 0.75
        self.__h3 = 0.9
        self.__h4 = 0.6
        self.__h5 = 0.6
        self.__g = 1.262
        self.__pi = math.pi

    def __func_A14(self, hc, fc, input_data):
        # A14
        omega_c = 2 * self.__pi * fc
        a0 = 12 / (self.__dt * self.__dt) + (12 * hc * omega_c) / \
            self.__dt + (omega_c * omega_c)
        a1 = 10 * (omega_c * omega_c) - 24 / (self.__dt * self.__dt)
        a2 = 12 / (self.__dt * self.__dt) - (12 * hc * omega_c) / \
            self.__dt + (omega_c * omega_c)
        b0 = omega_c * omega_c
        b1 = 10 * (omega_c * omega_c)
        b2 = omega_c * omega_c

        return self.__func_A15(a0, a1, a2, b0, b1, b2, input_data)

    def __func_A15(self, a0, a1, a2, b0, b1, b2, input_data:list[float]):
        output_data = []

        # 1つめ
        k1 = (b0 * input_data[0]) / a0
        output_data.append(k1)

        # 2つめ
        k2 = (-a1 * output_data[0] + b0 *
              input_data[1] + b1 * input_data[0]) / a0
        output_data.append(k2)

        # 3つめ以降
        for k in range(2, len(input_data)):
            value = (-a1 * output_data[k-1] - a2 * output_data[k-2] + b0 *
                     input_data[k] + b1 * input_data[k-1] + b2 * input_data[k-2]) / a0
            output_data.append(value)

        return output_data

    def __filter01(self, input_data):
        fa1 = self.__f0
        fa2 = self.__f1

        # A11
        omega_a1 = 2 * self.__pi * fa1
        omega_a2 = 2 * self.__pi * fa2

        a0 = 8 / (self.__dt * self.__dt) + (4 * omega_a1 + 2 * omega_a2) / \
            self.__dt + omega_a1 * omega_a2
        a1 = 2 * omega_a1 * omega_a2 - 16 / (self.__dt * self.__dt)
        a2 = 8 / (self.__dt * self.__dt) - (4 * omega_a1 + 2 * omega_a2) / \
            self.__dt + omega_a1 * omega_a2
        b0 = 4 / (self.__dt * self.__dt) + 2 * omega_a2 / self.__dt
        b1 = -8 / (self.__dt * self.__dt)
        b2 = 4 / (self.__dt * self.__dt) - 2 * omega_a2 / self.__dt

        return self.__func_A15(a0, a1, a2, b0, b1, b2, input_data)

    def __filter02(self, input_data):
        fa3 = self.__f1

        # A12
        omega_a3 = 2 * self.__pi * fa3
        a0 = 16 / (self.__dt * self.__dt) + 17 * omega_a3 / self.__dt + (omega_a3 * omega_a3)
        a1 = 2 * omega_a3 * omega_a3 - 32 / (self.__dt * self.__dt)
        a2 = 16 / (self.__dt * self.__dt) - 17 * omega_a3 / self.__dt + (omega_a3 * omega_a3)
        b0 = 4 / (self.__dt * self.__dt) + 8.5 * omega_a3 / self.__dt + (omega_a3 * omega_a3)
        b1 = 2 * omega_a3 * omega_a3 - 8 / (self.__dt * self.__dt)
        b2 = 4 / (self.__dt * self.__dt) - 8.5 * omega_a3 / self.__dt + (omega_a3 * omega_a3)

        return self.__func_A15(a0, a1, a2, b0, b1, b2, input_data)

    def __filter03(self, input_data):
        hb1 = self.__h2a
        hb2 = self.__h2b
        fb = self.__f2

        # A13
        omega_b = 2 * self.__pi * fb
        a0 = 12 / (self.__dt * self.__dt) + (12 * hb2 * omega_b) / \
            self.__dt + (omega_b * omega_b)
        a1 = 10 * (omega_b * omega_b) - 24 / (self.__dt * self.__dt)
        a2 = 12 / (self.__dt * self.__dt) - (12 + hb2 * omega_b) / \
            self.__dt + (omega_b * omega_b)
        b0 = 12 / (self.__dt * self.__dt) + (12 * hb1 * omega_b) / \
            self.__dt + (omega_b * omega_b)
        b1 = 10 * (omega_b * omega_b) - 24 / (self.__dt * self.__dt)
        b2 = 12 / (self.__dt * self.__dt) - (12 * hb1 * omega_b) / \
            self.__dt + (omega_b * omega_b)

        return self.__func_A15(a0, a1, a2, b0, b1, b2, input_data)

    def __filter04(self, input_data):
        hc = self.__h3
        fc = self.__f3
        return self.__func_A14(hc, fc, input_data)

    def __filter05(self, input_data):
        hc = self.__h4
        fc = self.__f4
        return self.__func_A14(hc, fc, input_data)

    def __filter06(self, input_data):
        hc = self.__h5
        fc = self.__f5
        return self.__func_A14(hc, fc, input_data)

    def __filter07(self, input_data):
        output_data = []
        gd = self.__g

        for k in range(0, len(input_data)):
            output_data.append(input_data[k] * gd)

        return output_data

    def exec(self, input_data: list[float]):
        return self.__filter07(self.__filter06(self.__filter05(self.__filter04(self.__filter03(self.__filter02(self.__filter01(input_data)))))))
