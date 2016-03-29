from si301 import email


company_map = {
        "dell.com": "Dell",
        "stanford.edu": "Stanford University",
        "redhat.com": "RedHat",
        "clisp.org": "CLISP",
        "cs.ucla.edu": "University of California, Los Angeles",
        "gmx.de": "GMX",
        "h-d-gmbh.de": "H&D",
        "aaronwl.com": "aaronwl.com" ##personal site
        "email.unc.edu": "University of North Carolina",
        "gnu.org": "GNU",
        "epita.fr": "EPITA",
        "gmail.com": "Gmail",
        "skeeve.com": "skeeve" ## personal site
        "air.net.au": "air.net.au",
        "cs.stanford.edu": "Stanford University",
        "debian.org": "debian",
        "hawkwind.utcs.utoronto.ca": "University of Toronto",
        "ximbiot.com": "ximbiot.com",
        "djmnet.org": "djmnet.org",
        "facebook.com": "Facebook",
        "mvista.com": "Monta Vista",
        "iluvatar.eu.org": "iluvatareu.org",
        "byu.net": "Brigham Young University",
        "twinsun.com": "twinsun.com",
        "uruk.org": "uruk.org",
        "student.uu.se": "Uppsala University",
        "splode.com": "splode.com",
        "interfree.it": "interfree",
        "the-meissners.org": "the-meissners.org" ##personal site
        "tlinx.org": "tlinx.org",
        "dg-rtp.dg.com": "dg-rtp.dg.com",
        "cakra.net": "cakra.net",
        "cygnus.com": "SouthComm",
        "google.com": "Google",
        "dkrz.de": "DKRZ",
        "meyering.net": "meyering.net",
        "red-bean.com": "Red Bean Software"
        "embecosm.com": "embecosm.com",
        "warhol.com": "warhol.com",
        "cisco.com": "Cisco",
        "freefriends.org": "freefriends.org",
        "ucw.cz": "ucw.cz",
        "users.sourceforge.net": "users.sourceforge.net",
        "ftbfs.org": "ftbfs.org"
        "SLAC.Stanford.EDU": "Stanford",
        "sim.no" : "sim.no",
        "altlinux.org": "altlinux.org",
        "spaceroots.org": "spaceroots.org",
        "rexx.org": "rexx.org", ##personal
        
        }


def get_company(addr):
    em = email.Address(addr)

    try:
        return company_map[em.get_domain()]
    except KeyError:
        pass

    return ''
