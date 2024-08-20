import service
import pytest,requests
import unittest.mock as mock


@mock.patch("service.get_user_from_db")
def test_get_user_from_db(mock_get_user_from_db):
    mock_get_user_from_db.return_value = "Mocked Alice"
    user_name = service.get_user_from_db(1)
    
    assert user_name == "Mocked Alice"

@mock.patch("requests.get")
def test_get_user(mock_get):
    mock_response = mock.Mock()
    mock_response.status_code = 200
    mock_response.json.return_value = {"id":1,"name":"Eric Yang"}
    mock_get.return_value = mock_response
    
    data = service.get_users()
    assert data == {"id":1,"name":"Eric Yang"}
    
@mock.patch("requests.get")
def test_get_user_httperror(mock_get):
    mock_response = mock.Mock()
    mock_response.status_code = 404
    mock_get.return_value = mock_response
    
    with pytest.raises(requests.HTTPError):
        service.get_users()



