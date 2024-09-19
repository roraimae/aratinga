{{ sitename }} website
Code for site at: http://{{ domain }}

# Primeiros passos
Certifique-se de que uma versão recente do Python esteja instalada em seu sistema. Abra esse diretório em um prompt de comando e, em seguida:

1. Insta-le o Software:
     ```
     pip install -r requirements.txt
     ```
2. Crie um super usuário:
    ```
    python manage.py createsuperuser
    ```
3. Run the development server:
    ```
    python manage.py runserver
    ```
   
Vá para http://localhost:8000/ no seu browser, ou http://localhost:8000/admin/ para logar e começar a trabalhar!