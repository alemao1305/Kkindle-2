import 'package:flutter/material.dart';

class BookTitle extends StatelessWidget {
  final String title;
  final TextStyle? style;

  const BookTitle({
    Key? key,
    required this.title,
    this.style,
  }) : super(key: key);

  @override
  Widget build(BuildContext context) {
    return Padding(
      padding: const EdgeInsets.symmetric(vertical: 8.0, horizontal: 16.0),
      child: Text(
        title,
        style: style ?? TextStyle(
          fontSize: 18.0,
          fontWeight: FontWeight.bold,
          color: Colors.black87,
        ),
        maxLines: 2,  // Limita o título a 2 linhas para não ocupar muito espaço
        overflow: TextOverflow.ellipsis,  // Adiciona '...' se o texto for muito longo
      ),
    );
  }
}
