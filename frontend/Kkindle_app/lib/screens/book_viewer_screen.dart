import 'package:flutter/material.dart';
import 'package:flutter_pdfview/flutter_pdfview.dart';
import 'package:epub_view/epub_view.dart';
import 'package:flutter_html/flutter_html.dart';

class BookViewerScreen extends StatelessWidget {
  final String bookPath;
  final String bookFormat;

  BookViewerScreen({required this.bookPath, required this.bookFormat});

  @override
  Widget build(BuildContext context) {
    return Scaffold(
      appBar: AppBar(
        title: Text('Leitor de Livro'),
      ),
      body: _buildBookViewer(),
    );
  }

  Widget _buildBookViewer() {
    switch (bookFormat) {
      case 'pdf':
        return PDFView(
          filePath: bookPath,
        );
      case 'epub':
        return EpubView(
          controller: EpubController(document: EpubDocument.openAsset(bookPath)),
        );
      case 'mobi':
        // Para arquivos MOBI, você precisará de um parser que converta para HTML.
        // Aqui está um exemplo genérico, dependendo de como você os converte.
        return FutureBuilder<String>(
          future: _convertMobiToHtml(bookPath), // Função fictícia para conversão
          builder: (context, snapshot) {
            if (snapshot.connectionState == ConnectionState.waiting) {
              return Center(child: CircularProgressIndicator());
            } else if (snapshot.hasError) {
              return Center(child: Text('Erro ao carregar livro.'));
            } else {
              return SingleChildScrollView(
                child: Html(data: snapshot.data),
              );
            }
          },
        );
      default:
        return Center(child: Text('Formato de livro não suportado.'));
    }
  }

  Future<String> _convertMobiToHtml(String path) async {
    // Implementação de conversão de MOBI para HTML (Exemplo fictício)
    // Use uma biblioteca de terceiros ou um serviço para esta conversão
    return "<h1>Exemplo de MOBI convertido para HTML</h1>";
  }
}
