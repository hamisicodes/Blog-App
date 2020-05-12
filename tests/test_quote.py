import unittest
from app.models import Quote

class TestQuote(unittest.TestCase):
    def setUp(self):
        
        self.new_quote = Quote('hamisi','I have no quote')


    def test_check_instance_variables(self):
        self.assertEquals(self.new_quote.author,'hamisi')
        self.assertEquals(self.new_quote.quote,'I have no quote')