# Copyright (c) 2022-2024 Adam Karpierz
# Licensed under the zlib/libpng License
# https://opensource.org/licenses/Zlib

import unittest

import pkg_about
from pkg_about import about


class MainTestCase(unittest.TestCase):

    def setUp(self):
        pass

    def test_main(self):
        about("pkg_about")
        self.assertEqual(__title__, "pkg-about")
        self.assertEqual(__version__, "1.1.0")
        self.assertEqual(__version_info__.major, 1)
        self.assertEqual(__version_info__.minor, 1)
        self.assertEqual(__version_info__.micro, 0)
        self.assertEqual(__version_info__.releaselevel, "final")
        self.assertEqual(__version_info__.serial, 0)
        self.assertEqual(__summary__, "Shares Python package metadata at runtime.")
        self.assertEqual(__uri__, " https://pypi.org/project/pkg_about/")
        self.assertEqual(__author__, "Adam Karpierz")
        self.assertEqual(__email__, "adam@karpierz.net")
        self.assertEqual(__author_email__, "adam@karpierz.net")
        self.assertEqual(__maintainer__, "Adam Karpierz")
        self.assertEqual(__maintainer_email__, "adam@karpierz.net")
        self.assertEqual(__license__,
                         "zlib/libpng License ; https://opensource.org/licenses/Zlib")
        self.assertIsNone(__copyright__)
