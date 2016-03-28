class Address:

    def __init__(self, addr):
        self.addr = addr

    def get_domain(self):
        return self.addr.split("@")[-1]

    def __str__(self):
        return self.addr
