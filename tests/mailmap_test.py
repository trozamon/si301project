from si301 import mailmap
from unittest import TestCase, main


class MailmapTest(TestCase):

    def testEasy(self):
        self.assertEqual('Dell', mailmap.get_company('joe.blow@dell.com'))

    def testHard(self):
        self.assertEqual('Dell', mailmap.get_company('joe.blow dell com'))

    def testSubdomain(self):
        self.assertEqual('Dell',
                mailmap.get_company('joe.blow@support.dell.com'))


if __name__ == '__main__':
    main()
