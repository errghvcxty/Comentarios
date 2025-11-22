# Arquivo: app.py (na raiz do seu projeto)

# 1. Importa a função Application Factory do seu módulo 'app'
from app import create_app

# 2. Executa a função e atribui a instância do Flask à variável 'app'
# Esta é a variável EXPOSTA que o Vercel procura
app = create_app()