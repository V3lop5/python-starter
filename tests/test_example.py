import pytest
from bigfoot import FootExample

@pytest.fixture
def app():
    """
    Instance of your application
    """
    return FootExample()
    
    
def test_text(app):
    """
    Checks if text within application is "Hello World!"
    """    
    assert app.text == "Hello World!"

