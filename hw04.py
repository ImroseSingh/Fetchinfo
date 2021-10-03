import unittest
import sys

from Getinfo import GitHubAPI

class TestGitHubAPI(unittest.TestCase):

    def test_myrepo(self):
        gh = GitHubAPI("ImroseSingh")
        self.assertEqual(len(gh.get_repos()), 4,
                         "There are 4 repositores")

    def test_Getrepo(self):
        gh = GitHubAPI("ImroseSingh")
        self.assertEqual(gh.get_repos(), ['Fetchinfo', 'ImroseSingh', 'ssw-567', 'triangle-HW2'], [
                         'Fetchinfo', 'ImroseSingh', 'ssw-567', 'triangle-HW2'])


  


if __name__ == "__main__":
    unittest.main()

   

