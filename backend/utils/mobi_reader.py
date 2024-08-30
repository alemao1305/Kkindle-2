import mobi

class MobiReader:
    def __init__(self, file_path):
        self.file_path = file_path
        self.extracted_folder = "extracted_mobi"

    def extract_book(self):
        """Extrai o conteúdo do arquivo MOBI para uma pasta temporária."""
        try:
            mobi.extract(self.file_path, self.extracted_folder)
            return True
        except Exception as e:
            print(f"Erro ao extrair o arquivo MOBI: {str(e)}")
            return False

    def get_text(self):
        """Lê e retorna o conteúdo extraído do arquivo MOBI."""
        try:
            with open(f"{self.extracted_folder}/mobi7/book.html", "r", encoding="utf-8") as f:
                return f.read()
        except Exception as e:
            print(f"Erro ao ler o conteúdo do arquivo MOBI extraído: {str(e)}")
            return ""

# Exemplo de uso
if __name__ == "__main__":
    reader = MobiReader('caminho/para/seu/arquivo.mobi')
    if reader.extract_book():
        book_text = reader.get_text()
        print(book_text)  # Exibe o conteúdo do livro no console
    else:
        print("Falha ao extrair o arquivo MOBI.")
