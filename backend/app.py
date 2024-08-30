# backend/app.py

from fastapi import FastAPI, HTTPException
from backend.database.models import BookModel
from backend.database.mongodb_config import db
from backend.book_reader import BookReader

app = FastAPI()

# Inicializar o leitor de livros
book_reader = BookReader()

@app.get("/")
def read_root():
    return {"message": "Bem-vindo ao Kkindle API"}

@app.post("/books/")
async def create_book(book: BookModel):
    book_dict = book.dict(by_alias=True)
    result = db.books.insert_one(book_dict)
    if result.acknowledged:
        return {"message": "Livro adicionado com sucesso", "id": str(result.inserted_id)}
    else:
        raise HTTPException(status_code=500, detail="Erro ao adicionar o livro")

@app.get("/books/{book_id}")
async def get_book(book_id: str):
    book = db.books.find_one({"_id": book_id})
    if book:
        return book
    else:
        raise HTTPException(status_code=404, detail="Livro não encontrado")

@app.post("/read-book/")
async def read_book(book_path: str):
    try:
        content = book_reader.read_book(book_path)
        return {"content": content}
    except Exception as e:
        raise HTTPException(status_code=500, detail=f"Erro ao ler o livro: {str(e)}")
