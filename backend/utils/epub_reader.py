from ebooklib import epub

class EpubReader:
    def __init__(self, file_path):
        self.file_path = file_path
        self.book = None

    def load_book(self):
        """Carrega o livro EPUB especificado no caminho do arquivo."""
        try:
            self.book = epub.read_epub(self.file_path)
            return True
        except Exception as e:
            print(f"Erro ao carregar o livro EPUB: {str(e)}")
            return False

    def get_text(self):
        """Extrai e retorna o texto do livro EPUB."""
        if not self.book:
            print("Nenhum livro carregado. Use o método 'load_book' primeiro.")
            return ""

        text_content = ""
        try:
            for item in self.book.get_items():
                if item.get_type() == epub.ITEM_DOCUMENT:
                    text_content += item.get_content().decode('utf-8')
            return text_content
        except Exception as e:
            print(f"Erro ao extrair o conteúdo do livro EPUB: {str(e)}")
            return ""

# Exemplo de uso
if __name__ == "__main__":
    # Substitua 'caminho/para/seu/arquivo.epub' pelo caminho real do arquivo EPUB
    reader = EpubReader('caminho/para/seu/arquivo.epub')
    if reader.load_book():
        book_text = reader.get_text()
        print(book_text)  # Exibe o conteúdo do livro no console
    else:
        print("Falha ao carregar o livro EPUB.")
