import os

# Override env variables
os.environ['SQLALCHEMY_DATABASE_URI'] = "sqlite:///:memory:"
os.environ['SERVER_NAME'] = "Counter Test"
