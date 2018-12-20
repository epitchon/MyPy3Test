import unittest
import p10


class BoxUnitTests(unittest.TestCase):

    def test_get_box_basearea_10(self):
        self.assertEquals( \
            p10.get_box_basearea(10), \
            100)

    def test_get_box_basearea_12(self):
        self.assertEquals( \
            p10.get_box_basearea(12), \
            144)


    def test_get_box_valume_11(self):
        self.assertEquals( \
            p10.get_box_valume(11), \
            1331)



