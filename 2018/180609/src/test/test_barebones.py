#!/usr/bin/env python
PKG = 'ros-works-dojos'
import roslib; roslib.load_manifest(PKG)

import sys
import unittest

## A sample python unit test
class TestBareBones(unittest.TestCase):

    def test_one_equals_one(self):
        self.assertEquals(1, 1, "1!=1")

    def test_one_dont_equals_two(self):
        self.assertNotEquals(1, 2, "2!=1")

if __name__ == '__main__':
    import rosunit
    rosunit.unitrun(PKG, 'test_bare_bones', TestBareBones)
