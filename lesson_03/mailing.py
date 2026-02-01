from address import Address


class Mailing:
    def __init__(self, to_address, from_address, cost, track):
        self.to_add = to_address
        self.from_add = from_address
        self.cost = cost
        self.track = track

        def __str__(self):
            return f"{self.to_add} {self.from_add}, {self.cost}, {self.track}"
