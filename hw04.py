import unittest
import sys

from Getinfo import GitHubAPI

class TestGitHubAPI(unittest.TestCase):

    def test_myrepo(self):
        gh = GitHubAPI("ImroseSingh")
        self.assertEqual(len(gh.get_repos()), 4,
                         "There are 4 repositores")

    def test_Getrepo(self):
        gh = GitHubAPI("Liam-Brew")
        self.assertEqual(gh.get_repos(), ['ssw-567','triangle-HW2','Fetchinfo','ImroseSingh'], [
                         'ssw-567','triangle-HW2','Fetchinfo','ImroseSingh'])


    def test_run_status_ok(self):
        gh = GitHubAPI("ImroseSingh")
        self.assertEqual(gh.run(), 200, "Run status should be ok")

    def test_nonuser(self):
        gh1 = GitHubAPI("im0")
        self.assertEqual(gh1.run(), 404, "This user is not on GitHub")


if __name__ == "__main__":
    unittest.main()

   

