import unittest
from app.models import Blog, User
from app import db

class TestPitch(unittest.TestCase):
    def setUp(self):
        self.user_James = User(username='James', password='potato', email='james@ms.com')
        self.new_blog = Blog(description = 'Hello flask', user = self.user_James)


    def test_check_instance_variables(self):
        self.assertEquals(self.new_blog.description,'Hello flask')
        self.assertEquals(self.new_blog.user.username,'James')