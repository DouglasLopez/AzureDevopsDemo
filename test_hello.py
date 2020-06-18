# test_hello.py
from myWebApp import app

def test_hello():
    response = app.test_client().get('/')

    assert response.status_code == 200
    assert response.data == b'Ola k aze'
