import one_away as oa
import unittest


class Test(unittest.TestCase):

    dataT = [('pale','ple'),('pales','pale'),('pale','bale')]
    dataF = [('pale','bae')]

    def test_true(self):

        # true check
        for s in self.dataT:
            result = oa.one_away(s[0],s[1])
            self.assertTrue(result)

        # false check
        for s in self.dataF:
            result = oa.one_away(s[0],s[1])
            self.assertFalse(result)

if __name__ == "__main__":
    unittest.main()