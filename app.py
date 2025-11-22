# app.py na raiz do projeto
from app import create_app

# O Vercel procurará uma variável chamada 'app'
# Esta linha executa sua Application Factory e atribui 
# a instância do Flask à variável 'app'.
app = create_app()

# Se você quiser rodar localmente com python app.py:
# if __name__ == '__main__':
#     app.run(debug=True)