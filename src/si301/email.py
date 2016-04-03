class Address:

    def __init__(self, addr):
        self.addr = addr

    def get_domain(self):
        if '@' not in self.addr:
            # try splitting on ' '
            tmp = self.addr.split(' ')
            if len(tmp) >= 3:
                return '.'.join(tmp[-2:])

        dom = self.addr.split('@')[-1]

        if len(dom.split('.')) == 2:
            return dom.split("@")[-1]
        else:
            return '.'.join(dom.split('.')[-2:])

    def __str__(self):
        return self.addr
