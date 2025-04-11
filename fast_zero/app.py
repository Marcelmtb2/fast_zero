from fastapi import FastAPI
from fastapi.responses import HTMLResponse
from fast_zero.schemas import Message
from http import HTTPStatus



app = FastAPI()


@app.get('/', status_code=HTTPStatus.OK, response_model=Message)
def read_root():
    return {'message': 'Olá Mundo!'}


# @app.get('/', response_class=HTMLResponse)
# def read_root():
#     return """
#     <html>
#       <head>
#         <title> Nosso olá mundo!</title>
#       </head>
#       <body>
#         <h1> Olá Mundo </h1>
#       </body>
#     </html>"""
