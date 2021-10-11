import unittest
import json
import get_repo
from unittest.mock import MagicMock as Mock
from unittest.mock import patch

from Getinfo import GitHubAPI

class TestGitHubAPI(unittest.TestCase):
    
    def testConnection(self, mock_connect):
        fi = GitHubAPI("ImroseSingh")
        self.assertEqual(len(fi.get_repos()), 4,
                         "There are 4 repositores")
    @patch("get_repo.connect")
    def testConnection(self, mock_connect):
        mock_connect.return_value = [200, {"CS-523-Web-Programming-1": "1",
                                     "CS555---GEDCOM-Project": "13",
                                     "GitHubAPI567": "12",
                                     "HelloWorldRepo": "3",
                                     "Triangle567": "8"}]
        self.assertTrue(get_repo.connect("cmontero201")[0])
    


  


if __name__ == "__main__":
    unittest.main()
     suite = unittest.TestLoader().loadTestsFromTestCase(TestGetRepo)
    unittest.TextTestRunner(verbosity = 2).run(suite)

   

