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
    def test_correct_output(self, mock_get):
        repo_list = [
            {'name': "test_repo1"},
            {'name': "test_repo2"}
        ]
        commit_list_1 = [
            {'node_id': 'NDKSJHMDKNSUHDH'},
            {'node_id': 'kshdahoedaenodeno'}
        ]
        commit_list_2 = [
            {'node_id': 'NDKSJHMDKNSUHDH'}
        ]
        mock_get.return_value.ok = True
        mock_get.return_value.json.side_effect = [repo_list, commit_list_1, commit_list_2]
        response = list_repositories('testUser')
        self.assertEqual([['test_repo1', 2], ['test_repo2', 1]], response)


  


if __name__ == "__main__":
    unittest.main()

   

