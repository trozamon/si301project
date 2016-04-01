from unittest import TestCase
from si301 import email

class EmailTest(TestCase):

    def testNormalDomain(self):
        em = email.Address('alec@alectenharmsel.com')
        self.assertEqual(em.get_domain(), 'alectenharmsel.com')

    def testSpaceSeparatedDomain(self):
        em = email.Address('rolland ghs com')
        self.assertEqual(em.get_domain(), 'ghs.com')
