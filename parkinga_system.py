class ParkingSystem(object):
    spots = {}

    def __init__(self, big, medium, small):
        """
        :type big: int
        :type medium: int
        :type small: int
        """
        self.spots[1] = big
        self.spots[2] = medium
        self.spots[3] = small

    def addCar(self, carType):
        """
        :type carType: int
        :rtype: bool
        """
        if self.spots[carType] > 0 :
            self.spots[carType] -= 1
            return True
        else:
            return False


# Your ParkingSystem object will be instantiated and called as such:
# obj = ParkingSystem(big, medium, small)
# param_1 = obj.addCar(carType)