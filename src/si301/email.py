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
        dom_arr = dom.split('.')

        if dom_arr[-1] == 'uk':
            return '.'.join(dom_arr[-3:])
        else:
            return '.'.join(dom_arr[-2:])

    def __str__(self):
        return self.addr
