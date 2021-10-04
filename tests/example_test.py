import pytest
from package_name import StarterExample

@pytest.fixture
def app():
    """
    Instance of your application
    """
    return StarterExample()
    
    
def test_text(app):
    """
    Checks if text within application is "Hello World!"
    """    
    assert app.text == "Hello World!"

