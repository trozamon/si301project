from si301 import email

personal_site_map = {
    "aaronwl.com": "aaronwl.com", ##personal site
    "async.com.br": "async.com.br", ##no site found..
    "betelgeuse.gostai.ensta.fr" : "betelgeuse.gostai.ensta.fr",
    "bothner.com": "bothner.com",
    "bitwi.se": "bitwi.se",
    "bruges.(none)": "bruges.(none)",
    "cante.net": "cante.net",
    "chello.hu": "chello.hu", ##unsure
    "cwilson.fastmail.fm": "cwilson.fastmail.fm",
    "danjou.info": "danjou.info",
    "dcc.unicamp.br", "dcc.unicamp.br",
    "dg-rtp.dg.com": "dg-rtp.dg.com",
    "desrt.ca": "desrt.ca", ## no domain
    "djmnet.org": "djmnet.org",
    "gmail.com": "gmail.com",
    "gnuvola.org":"gnuvola.org",
    "iskunk.org":"iskunk.org",
    "jackkelly.name": "jackkelly.name",
    "joeldenny.org": "joeldenny.org",
    "josefsson.org": "josefsson.org",
    "linux-m68k.org": "linux-m68k.org",
    "lsd.ic.unicamp.br": "lsd.ic.unicamp.br",
    "medozas.de": "medozas.de",
    "meyering.net", "meyering.net",
    "Perennou.com": "Perennou.com",
    "phekda.freeserve.co.uk": "phekda.freeserve.co.uk",
    "pogma.com":"pogma.com",
    "pomf.net": "pomf.net",
    "proulx.com": "proulx.com",
    "raspberryginger.com": "raspberryginger.com",
    "rexx.org": "rexx.org", ##personal
    "rfc1149.net": "rfc1149.net",
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
        "apple.com", "Apple",
        "dell.com": "Dell",
        "stanford.edu": "Stanford University",
        "redhat.com": "RedHat",
        "clisp.org": "CLISP",
        "cs.ucla.edu": "University of California, Los Angeles",
        "gmx.de": "GMX",
        "h-d-gmbh.de": "H&D",
        "email.unc.edu": "University of North Carolina",
        "gnu.org": "GNU",
        "epita.fr": "EPITA",
        "air.net.au": "air.net.au",
        "cs.stanford.edu": "Stanford University",
        "debian.org": "debian",
        "hawkwind.utcs.utoronto.ca": "University of Toronto",
        "ximbiot.com": "ximbiot.com",
        "facebook.com": "Facebook",
        "mvista.com": "Monta Vista",
        "iluvatar.eu.org": "iluvatareu.org",
        "byu.net": "Brigham Young University",
        "twinsun.com": "twinsun.com",
        "student.uu.se": "Uppsala University",
        "splode.com": "splode.com",
        "interfree.it": "interfree",
        "tlinx.org": "tlinx.org",
        "cakra.net": "cakra.net",
        "cygnus.com": "SouthComm",
        "google.com": "Google",
        "dkrz.de": "DKRZ",
        "meyering.net": "meyering.net",
        "red-bean.com": "Red Bean Software",
        "embecosm.com": "EMBECOSM",
        "cisco.com": "Cisco",
        "freefriends.org": "freefriends.org",
        "ucw.cz": "ucw.cz",
        "users.sourceforge.net": "users.sourceforge.net",
        "ftbfs.org": "ftbfs.org",
        "SLAC.Stanford.EDU": "Stanford University",
        "sim.no" : "sim.no",
        "altlinux.org": "altlinux.org",
        "spaceroots.org": "spaceroots.org",
        "codeweavers.com": "codeweavers.com",
        "lrde.epita.fr": "EPITA",
        "googlemail.com": "Google",
        "mail.mcgill.ca":"McGill University",
        "ubuntu.com": "Ubuntu",
        "mcs.anl.gov": "mcs.anl.gov",
        "acm.org": "Association for Computing Machinery",
        "bitron.ch": "Bitron",
        "elliptictech": "Elliptic Technologies", 
        "mppmu.mpg.de": "Max-Planck Institute for Physics",
        "lysator.liu.se": "Linköping University: Lyastor",
        "cam.ac.uk": "Cambridge University",
        "NetBSD.org": "NetBSD",
        "gnome.org": "GNOME",
        "tege@swox.com": "swox",
        "pandora.be": "Zila",
        "gentoo.org":"Gentoo Linux"
        "case.edu": "Case Western Reserve",
        "CS.Berkeley.EDU": "University of California: Berkeley",
        "unidata.ucar.edu": "University Corporation for Atmospheric Research",
        "eggert@twinsun.com": "Twinsun",
        "edamail.fishkill.ibm.com": "IBM",
        "splode.com": "Center for the Study of Sudden Cranial Expansion",
        "ces.clemson.edu": "Clemson University",
        "clemson.edu": "Clemson University",
        "dfki.de": "The German Research Center for Artificial Intelligence",

        }


def get_company(addr):
    em = email.Address(addr)

    try:
        return company_map[em.get_domain()]
    except KeyError:
        pass

    return ''
