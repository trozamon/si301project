from si301 import email

personal_site_map = {
    "aaronwl.com": "aaronwl.com", ##personal site
    "async.com.br": "async.com.br", ##no site found..
    "betelgeuse.gostai.ensta.fr" : "betelgeuse.gostai.ensta.fr",
    "bothner.com": "bothner.com",
    "bitwi.se": "bitwi.se",
    "cante.net": "cante.net",
    "chello.hu": "chello.hu", ##unsure
    "cwilson.fastmail.fm": "cwilson.fastmail.fm",
    "danjou.info": "danjou.info",
    "dcc.unicamp.br": "dcc.unicamp.br",
    "dg-rtp.dg.com": "dg-rtp.dg.com",
    "desrt.ca": "desrt.ca", ## no domain
    "gmail.com": "gmail.com",
    "gnuvola.org":"gnuvola.org",
    "iskunk.org":"iskunk.org",
    "jackkelly.name": "jackkelly.name",
    "josefsson.org": "josefsson.org",
    "lsd.ic.unicamp.br": "lsd.ic.unicamp.br",
    "medozas.de": "medozas.de",
    "meyering.net": "meyering.net",
    "Perennou.com": "Perennou.com",
    "phekda.freeserve.co.uk": "phekda.freeserve.co.uk",
    "pogma.com":"pogma.com",
    "pomf.net": "pomf.net",
    "proulx.com": "proulx.com",
    "rexx.org": "rexx.org", ##personal
    "sc3d.org": "sc3d.org",
    "skeeve.com": "skeeve", ## personal site
    "tartarus.org": "tartarus.org",
    "teleline.es": "teleline.es", ##unsure
    "the-meissners.org": "the-meissners.org", ##personal site
    "tim-landscheidt.de": "tim-landscheidt.de",
    "unixuser.org":"unixuser.org",
    "uruk.org": "uruk.org",
    "warhol.com": "warhol.com",
    "ximbiot.com": "ximbiot.com",
    "yahoo.com":"yahoo.com",
    "zone42.de":"zone42.de" ##no webmaster


}

company_map = {
        "acm.org": "Association for Computing Machinery",
        "altlinux.org": "altlinux.org",
        "anl.gov": "Argonne National Laboratory",
        "apple.com": "Apple",
        "berkeley.edu": "University of California: Berkeley",
        "bitron.ch": "Bitron",
        "boeing.com": "Boeing",
        "bu.edu": "Boston University",
        "byu.net": "Brigham Young University",
        "cakra.net": "cakra.net",
        "caltech.edu": "California Institute of Technology",
        "cam.ac.uk": "Cambridge University",
        "case.edu": "Case Western Reserve",
        "cisco.com": "Cisco",
        "clisp.org": "CLISP",
        "codeweavers.com": "codeweavers.com",
        "cornell.edu": "Cornell University",
        "cygnus.com": "SouthComm",
        "debian.org": "debian",
        "dell.com": "Dell",
        "djmnet.org": "djmnet.org",
        "dkrz.de": "DKRZ",
        "elliptictech.com": "Elliptic Technologies", 
        "embecosm.com": "EMBECOSM",
        "epita.fr": "EPITA",
        "facebook.com": "Facebook",
        "freefriends.org": "freefriends.org",
        "freeshell.org": "SDF Public Access UNIX System",
        "ftbfs.org": "ftbfs.org",
        "gentoo.org":"Gentoo Linux",
        "gmx.de": "GMX",
        "gnome.org": "GNOME",
        "gnu.org": "GNU",
        "google.com": "Google",
        "gostai.com": "gostai.com",
        "h-d-gmbh.de": "H&D",
        "interfree.it": "interfree",
        "liu.se": "Linkoping University",
        "mcgill.ca":"McGill University",
        "meyering.net": "meyering.net",
        "mit.edu": "Massachusetts Institute of Technology",
        "mpg.de": "The Max Planck Society",
        "mvista.com": "Monta Vista",
        "netbsd.org": "NetBSD",
        "pandora.be": "Zita",
        "pitt.edu": "University of Pittsburgh",
        "red-bean.com": "Red Bean Software",
        "redhat.com": "RedHat",
        "rochester.edu": "University of Rochester",
        "sim.no": "sim.no",
        "spaceroots.org": "spaceroots.org",
        "splode.com": "splode.com",
        "stanford.edu": "Stanford University",
        "swox.com": "swox",
        "tlinx.org": "tlinx.org",
        "twinsun.com": "twinsun.com",
        "ubuntu.com": "Ubuntu",
        "uci.edu": "University of California, Irvine",
        "ucla.edu": "University of California, Los Angeles",
        "ucw.cz": "ucw.cz",
        "unc.edu": "University of North Carolina",
        "utoronto.ca": "University of Toronto",
        "uu.se": "Uppsala University",
        "ximbiot.com": "ximbiot.com"
        }


def get_company(addr):
    em = email.Address(addr)

    try:
        return company_map[em.get_domain()]
    except KeyError:
        pass

    return ''
