import unittest

import python_repos_visual_copy as prvc


class PythonReposTestCase(unittest.TestCase):
    """Testy dla programu python_repos.py"""

    def setUp(self):

        self.r = prvc.get_response()
        self.repo_dicts = prvc.get_repo_dicts(self.r)
        self.repo_dict = self.repo_dicts[0]
        self.repo_links, self.stars, self.labels = prvc.get_project_data(self.repo_dicts)
    
    def test_get_response(self):
        self.assertEqual(self.r.status_code, 200)
    
    def test_get_repo_dicts(self):
        self.assertEqual(len(self.repo_dicts), 30)

        required_keys = ['name', 'owner','stargazers_count', 'html_url']
        for required_key in required_keys:
            self.assertTrue(required_key in self.repo_dict.keys())

if __name__ == '__main__':
    unittest.main()