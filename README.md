# Kkindle-2

Kkindle é um aplicativo de leitura de livros desenvolvido utilizando Python e Flutter, que permite aos usuários lerem livros em diferentes formatos, como PDF, EPUB e MOBI. O backend do aplicativo utiliza FastAPI e MongoDB para gerenciar os dados dos livros e as preferências dos usuários.

## Funcionalidades

- Leitura de livros nos formatos PDF, EPUB e MOBI.
- Interface amigável e responsiva utilizando Flutter.
- Suporte para adicionar e gerenciar uma coleção de livros.
- Persistência de dados utilizando MongoDB.
- API RESTful para interação com o backend usando FastAPI.

## Tecnologias Utilizadas

- **Frontend**: Flutter
- **Backend**: FastAPI, Python
- **Banco de Dados**: MongoDB
- **Bibliotecas**:
  - `PyMuPDF` para leitura de PDFs.
  - `ebooklib` para leitura de arquivos EPUB.
  - `mobi` para leitura de arquivos MOBI.
  - `pymongo` para integração com MongoDB.

## Estrutura do Projeto

```plaintext
Kkindle/
├── backend/
│   ├── database/
│   │   ├── __init__.py
│   │   ├── mongodb_config.py
│   │   └── models.py
│   ├── utils/
│   │   ├── __init__.py
│   │   ├── epub_reader.py
│   │   ├── mobi_reader.py
│   │   └── pdf_reader.py
│   ├── __init__.py
│   ├── app.py
│   └── book_reader.py
├── frontend/
│   ├── android/
│   ├── ios/
│   └── lib/
│       ├── main.dart
│       └── ...
├── requirements.txt
└── README.md
```

# Configuração

## Requisitos

    Python 3.8 ou superior
    Flutter SDK
    MongoDB

## Passos para Configuração

1. Clone o Repositório
  
```bash
    git clone https://github.com/alemao1305/Kkindle.git
    cd Kkindle
```
2. **Configuração do Backend**

- Navegue até o diretório backend:
  
    ```bash
    cd backend
    ```
- Crie um ambiente virtual (opcional, mas recomendado):
   
    ```bash
    python -m venv venv
    source venv/bin/activate  # No Windows use: venv\Scripts\activate
    ```
- Instale as dependências:
  
    ```bash
    pip install -r requirements.txt
    ```
- Configure o MongoDB:

  - Certifique-se de que o MongoDB está em execução.
  - Atualize as configurações de conexão em mongodb_config.py se necessário.

  - Execute o servidor FastAPI:
  
    ```bash
    uvicorn app:app --reload
    ```
3. Configuração do Frontend (Flutter)

- Navegue até o diretório frontend:
    
    ```bash
    cd ../frontend
    ```
- Execute o aplicativo Flutter:
   
    ```bash
        flutter run
    ```
# Uso

 - Backend: A API estará disponível em http://127.0.0.1:8000. ( **isso para testes** )
 - Frontend: O aplicativo Flutter será executado no dispositivo ou emulador configurado.

# Contribuições

Contribuições são bem-vindas! Siga os passos abaixo para contribuir:

1.  Faça um fork do repositório.
2.  Crie uma nova branch para suas alterações: git checkout -b feature/nome-da-sua-feature.
3.  Faça commit de suas alterações: git commit -m 'Adicionando nova funcionalidade'.
4.  Faça push para a branch: git push origin feature/nome-da-sua-feature.
5.  Abra um Pull Request.

# Licença

Este projeto está licenciado sob a Licença MIT - veja o arquivo [LICENSE](LICENSE) para mais detalhes.

# Contato

Se tiver alguma dúvida ou sugestão, sinta-se à vontade para abrir uma issue ou enviar um e-mail para [olintoguarujas2@gmail.com].


```markdown
### Instruções Adicionais

1. **Substitua** as seções específicas (como o e-mail) com as informações reais do projeto.
2. **Adicione** qualquer configuração específica do MongoDB, detalhes de autenticação ou outras dependências específicas que possam ser relevantes para outros desenvolvedores.
3. **Mantenha o README atualizado** conforme novas funcionalidades são adicionadas ou alterações significativas são feitas no projeto. 

Esse `README.md` fornece uma visão clara e útil para novos desenvolvedores que queiram entender, configurar e contribuir para o projeto Kkindle.
```

