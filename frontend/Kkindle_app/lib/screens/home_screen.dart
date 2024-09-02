import 'package:flutter/material.dart';
import 'package:file_picker/file_picker.dart';
import 'book_viewer_screen.dart';

class HomeScreen extends StatelessWidget {
  @override
  Widget build(BuildContext context) {
    return Scaffold(
      appBar: AppBar(
        title: Text('Kkindle - Biblioteca'),
      ),
      body: Center(
        child: ElevatedButton(
          onPressed: () async {
            FilePickerResult? result = await FilePicker.platform.pickFiles(
              type: FileType.custom,
              allowedExtensions: ['pdf', 'epub', 'mobi'],
            );

            if (result != null) {
              String filePath = result.files.single.path!;
              String fileExtension = filePath.split('.').last;

              Navigator.push(
                context,
                MaterialPageRoute(
                  builder: (context) => BookViewerScreen(
                    bookPath: filePath,
                    bookFormat: fileExtension,
                  ),
                ),
              );
            }
          },
          child: Text('Abrir Livro'),
        ),
      ),
    );
  }
}
