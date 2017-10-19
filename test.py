from app import app
import unittest


class FlaskTestCase(unittest.TestCase):

    # Ensure that flask was set up correctly
    def test_index(self):
        tester = app.test_client(self)
        response = tester.get('/', content_type='html/text')
        self.assertEqual(response.status_code, 200)

 	# Ensure login page loads correctly
    def test_login_page_loads(self):
        tester = app.test_client(self)
        response = tester.get('/login', content_type='html/text')
        self.assertTrue(b'Log-In' in response.data)

    # Ensure login behaves correctly given correct credentials
    def test_correct_login(self):
        tester = app.test_client(self)
        response = tester.post(
        	'/login',
        	data=dict(username="HashTest1", password="secretsecret"),
        	follow_redirects = True
            )
        self.assertEqual(response.status_code, 200)

    # Ensure login behaves correctly given incorrect credentials
    def test_incorrect_login(self):
        tester = app.test_client(self)
        response = tester.post(
        	'/login',
        	data=dict(username="wrong", password="wrong"),
        	follow_redirects = True
        )
        self.assertIn(b'Invalid username or password', response.data)

if __name__ == '__main__':
    unittest.main()
