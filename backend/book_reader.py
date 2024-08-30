# backend/book_reader.py

from ebooklib import epub
import fitz  # PyMuPDF para PDF
import mobi

class BookReader:
    def read_book(self, file_path: str) -> str:
        if file_path.endswith('.pdf'):
            return self.read_pdf(file_path)
        elif file_path.endswith('.epub'):
            return self.read_epub(file_path)
        elif file_path.endswith('.mobi'):
            return self.read_mobi(file_path)
        else:
            raise ValueError("Formato de livro não suportado")

    def read_pdf(self, file_path: str) -> str:
        doc = fitz.open(file_path)
        text = ''
        for page_num in range(doc.page_count):
            page = doc.load_page(page_num)
            text += page.get_text()
        return text

    def read_epub(self, file_path: str) -> str:
        book = epub.read_epub(file_path)
        text = ''
        for item in book.get_items():
            if item.get_type() == epub.ITEM_DOCUMENT:
                text += item.get_content().decode('utf-8')
        return text

    def read_mobi(self, file_path: str) -> str:
        mobi.extract(file_path, "temp_mobi_output")
        with open("temp_mobi_output/mobi7/book.html", "r", encoding='utf-8') as f:
            text = f.read()
        return text
