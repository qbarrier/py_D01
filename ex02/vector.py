class Vector:
    def __init__(self, value):
        self.value = []
        if type(value) == list:
            self.value = value

        elif type(value) == int:
            for x in range(0, value):
                self.value.append(x)

        elif type(value) == tuple:
            if len(value) != 2 or not isinstance(value[0], int) or not isinstance(value[1], int):
                print('Range like that (<number1>, <number2>)')
                quit()
            else:
                for x in range(value[0], value[1] + 1):
                    self.value.append(x)
        else:
            print("Format Error")
            quit()
        self.value = [float(i) for i in self.value]
        self.size = len(self.value)

    def __add__(self, nb):
        if isinstance(nb, int):
            for x in range(0, self.size):
                self.value[x] += nb
        elif isinstance(nb, list):
            for x in range(0, min(self.size, len(nb))):
                self.value[x] += nb[x]

    def __radd__(self, nb):
        if isinstance(nb, int):
            for x in range(0, self.size):
                self.value[x] += nb
        elif isinstance(nb, list):
            for x in range(0, min(self.size, len(nb))):
                self.value[x] += nb[x]

    def __sub__(self, nb):
        if isinstance(nb, int):
            for x in range(0, self.size):
                self.value[x] -= nb
        elif isinstance(nb, list):
            for x in range(0, min(self.size, len(nb))):
                self.value[x] -= nb[x]

    def __rsub__(self, nb):
        if isinstance(nb, int):
            for x in range(0, self.size):
                self.value[x] = nb - self.value[x]
        elif isinstance(nb, list):
            for x in range(0, min(self.size, len(nb))):
                self.value[x] = nb[x] - self.value[x]

    def __mul__(self, nb):
        if isinstance(nb, int):
            for x in range(0, self.size):
                self.value[x] *= nb
        elif isinstance(nb, list):
            for x in range(0, min(self.size, len(nb))):
                self.value[x] *= nb[x]

    def __rmul__(self, nb):
        if isinstance(nb, int):
            for x in range(0, self.size):
                self.value[x] *= nb
        elif isinstance(nb, list):
            for x in range(0, min(self.size, len(nb))):
                self.value[x] *= nb[x]













    def __str__(self):
        return 'Value :\t{self.value}\nSize :\t{self.size}'.format(self=self)
