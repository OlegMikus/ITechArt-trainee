from src.config.app import app

client = app.test_client()


def test_login() -> None:
    response = client.get('/login')
    assert response.status_code == 405
