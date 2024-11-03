import numpy as np
class Population2D():
    def __init__(self, N, z):
        self.susceptible = np.ones(N)
        self.infections = np.array([1] * z + [0] * (N-z))
        np.random.shuffle(self.infections)
        self.susceptible -= self.infections
        self.removed = np.zeros(N)
        self.positions = np.random.rand(N, 2)
        self.N = N
    
    def iterate(self, p, q, k):
        # move
        self.move(p)

        # infection
        dist = self.calculate_dist()
        infected = np.nonzero(self.infections) # i infected people
        within_range = (dist[infected] < q).sum(axis=0) > 0 # N
        self.infections = self.infections + within_range * self.susceptible
        self.susceptible = self.susceptible - within_range * self.susceptible

        # recover
        r = round(self.N*k)
        recover = np.array([1] * r + [0] * (self.N-r))
        np.random.shuffle(recover)
        self.removed = self.removed + self.infections * recover
        self.infections = self.infections - self.infections * recover
        return self.susceptible.sum(), self.infections.sum(), self.removed.sum()

    def move(self, p):
        dpos = np.random.randn(self.N, 2)
        dpos = p * dpos / np.linalg.norm(dpos, axis=1).reshape(-1, 1)
        new_pos = self.positions + dpos
        within_bds = (((new_pos < 1).astype(int) + (new_pos > 0).astype(int)).sum(axis = 1) == 4).astype(int).reshape(-1, 1)
        self.positions = self.positions + dpos * within_bds

    def calculate_dist(self):
        ext_pos1 = self.positions.reshape(self.N, 1, 2).repeat(self.N, axis=1)
        ext_pos2 = self.positions.reshape(1, self.N, 2).repeat(self.N, axis=0)
        dist = np.sqrt(np.power(ext_pos1 - ext_pos2, 2).sum(axis=2)) + 20 * np.identity(self.N)
        return dist
