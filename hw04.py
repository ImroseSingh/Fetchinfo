import unittest
import sys
import unittest.mock 
import Mock, patch

from Getinfo import GitHubAPI

class TestGitHubAPI(unittest.TestCase):
    
    def test_myrepo(self):
        fi = GitHubAPI("ImroseSingh")
        self.assertEqual(len(fi.get_repos()), 4,
                         "There are 4 repositores")

    def test_Getrepo(self):
        fi = GitHubAPI("ImroseSingh")
        self.assertEqual(fi.get_repos(), ['Fetchinfo', 'ImroseSingh', 'ssw-567', 'triangle-HW2'], [
                         'Fetchinfo', 'ImroseSingh', 'ssw-567', 'triangle-HW2'])
     @patch('github_api.requests.get')
    def test_return_not_ok(self, mock_get):
        mock_get.return_value.ok = False
        response = list_repositories('testUser')
        self.assertEqual("Invalid response from API", response)


  


if __name__ == "__main__":
    unittest.main()

   

