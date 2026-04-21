from app import app

def test_home():
    client = app.test_client()
    response = client.get("/")
    assert response.status_code == 200
    assert b"Hola Mundo, aqui ismael polanco (Matricula 2021-0293(!)" in response.data