import unittest
import sys
import json
from unittest.mock import MagicMock as Mock
from unittest.mock import patch

from Getinfo import GitHubAPI

class TestGitHubAPI(unittest.TestCase):
    
    
    @patch("Getinfo.print_data")
    def test_Getrepo(self):
        fi = GitHubAPI("ImroseSingh")
        self.assertEqual(fi.get_repos(), ['Fetchinfo', 'ImroseSingh', 'ssw-567', 'triangle-HW2'], [
                         'Fetchinfo', 'ImroseSingh', 'ssw-567', 'triangle-HW2'])
    


  


if __name__ == "__main__":
    unittest.main()
    suite = unittest.TestLoader().loadTestsFromTestCase(TestGetRepo)
    unittest.TextTestRunner(verbosity = 2).run(suite)

   

