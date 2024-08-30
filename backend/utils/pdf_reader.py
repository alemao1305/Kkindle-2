import fitz  # PyMuPDF

class PDFReader:
    def __init__(self, file_path):
        self.file_path = file_path

    def get_text(self):
        """Lê e retorna o texto de um arquivo PDF."""
        try:
            doc = fitz.open(self.file_path)
            text = ""
            for page_num in range(doc.page_count):
                page = doc.load_page(page_num)
                text += page.get_text()
            return text
        except Exception as e:
            print(f"Erro ao ler o PDF: {str(e)}")
            return ""

# Exemplo de uso
if __name__ == "__main__":
    reader = PDFReader('caminho/para/seu/arquivo.pdf')
    book_text = reader.get_text()
    print(book_text)  # Exibe o conteúdo do livro no console
