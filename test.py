from app import app
import unittest
from flask.ext.login import current_user
from flask import request

class FlaskTestCase(unittest.TestCase):
    # Ensure that flask was set up correctly
    def test_index(self):
        tester = app.test_client(self)
        response = tester.get('/', content_type='html/text')
        self.assertEqual(response.status_code, 200)

 	# Ensure home page loads correctly
    def test_home_page_loads(self):
        tester = app.test_client(self)
        response = tester.get('/', content_type='html/text')
        self.assertTrue(b'Touch Pizza' in response.data)

 	# Ensure login page loads correctly
    def test_login_page_loads(self):
        tester = app.test_client(self)
        response = tester.get('/login', content_type='html/text')
        self.assertTrue(b'Log-In' in response.data)

    # Ensure sign-up page loads correctly
    def test_signup_page_loads(self):
        tester = app.test_client(self)
        response = tester.get('/signup', content_type='html/text')
        self.assertTrue(b'Sign-Up' in response.data)

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
        	data=dict(username="wrong", password="wrongwrong"),
        	follow_redirects = True
        )
        self.assertIn(b'Invalid username or password', response.data)

  # Ensure registration behaves correctly and creates a new user
    def test_registration_correct(self):
        tester = app.test_client(self)
        response = tester.post(
        	'/signup',
        	data=dict(username="hashathon7", email="hash7@hash.com", password="secretsecret"),
        	follow_redirects = True
        )
        self.assertIn(b'New User has been created', response.data)

if __name__ == '__main__':
    unittest.main()
