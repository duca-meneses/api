from fastapi import FastAPI

app = FastAPI()


@app.get('/')
def helo_word():
    return {'message': 'Olá Mundo!'}
