import numpy as np
import matplotlib.pyplot as plt
from matplotlib.animation import FuncAnimation


class Model:
    def __init__(self):
        self.size = 100
        self.max_steps = 100
        self.a = np.random.rand(self.size, self.size).round()
        self.step = 0
        self.fig = plt.figure()
        self.im = plt.imshow(self.a)
        self.animation = FuncAnimation(self.fig, self.update, interval=50)
        plt.show()

    def update(self, i):
        for n in np.arange(self.a.shape[0]):
            for m in np.arange(self.a.shape[1]):
                try:
                    sum_n = (
                        # + self.a[n-1, m-1]
                        # + self.a[n + 1, m + 1]
                        # + self.a[n + 1, m - 1]
                        # + self.a[n - 1, m + 1]
                        + self.a[n, m - 1]
                        + self.a[n - 1, m]
                        + self.a[n, m + 1]
                        + self.a[n + 1, m]
                    )
                    if sum_n == 4 or sum_n == 0:
                        self.a[n, m] = 0
                    else:
                        self.a[n, m] = 1
                except IndexError:
                    self.a[m, n] = 1
            self.im.set_data(self.a)


if __name__ == '__main__':
    Model()
