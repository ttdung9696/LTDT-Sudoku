class Coordinator:
    def __init__(self, x , y):
        self.x = x
        self.y = y

    def compare(self, cor2):
        if self.x == cor2.x and self.y == cor2.y:
            return True
        return False