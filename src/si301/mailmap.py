from si301 import email


company_map = {
        "dell.com": "Dell",
        "stanford.edu": "Stanford University"
        }


def get_company(addr):
    em = email.Address(addr)

    try:
        return company_map[em.get_domain()]
    except KeyError:
        pass

    return ''
