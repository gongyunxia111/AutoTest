# coding=utf-8
import unittest

from unittestcase.delete_person import DeletePerson
from unittestcase.get_person import GetPerson
from unittestcase.post_person import PostPerson


def suite():
    suite = unittest.TestSuite()
    suite.addTests(unittest.makeSuite(PostPerson))
    suite.addTests(unittest.makeSuite(GetPerson))
    suite.addTests(unittest.makeSuite(DeletePerson))
    return suite


if __name__ == "__main__":
    unittest.TextTestRunner(verbosity=2).run(suite())
