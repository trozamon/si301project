class Address:

    def __init__(self, addr):
        self.addr = addr

    def get_domain(self):
        if '@' not in self.addr:
            # try splitting on ' '
            tmp = self.addr.split(' ')
            if len(tmp) >= 3:
                return '.'.join(tmp[-2:])

        return self.addr.split("@")[-1]

    def __str__(self):
        return self.addr
