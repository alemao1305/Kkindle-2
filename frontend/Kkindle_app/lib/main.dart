import 'package:flutter/material.dart';
import 'screens/home_screen.dart';

void main() {
  runApp(BookReaderApp());
}

class BookReaderApp extends StatelessWidget {
  @override
  Widget build(BuildContext context) {
    return MaterialApp(
      title: 'Book Reader',
      theme: ThemeData(
        primarySwatch: Colors.blue, // Cor primária do tema
        visualDensity: VisualDensity.adaptivePlatformDensity,
        textTheme: TextTheme(
          headline1: TextStyle(fontSize: 24.0, fontWeight: FontWeight.bold),
          bodyText1: TextStyle(fontSize: 16.0, color: Colors.black87),
        ),
      ),
      home: HomeScreen(), // Tela inicial do aplicativo
    );
  }
}
