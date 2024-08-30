import 'package:flutter/material.dart';
import 'package:flutter_test/flutter_test.dart';

import 'package:kkindle/main.dart';

void main() {
  testWidgets('Verifica se a tela inicial contém o texto do título', (WidgetTester tester) async {
    // Constrói o app e aciona um frame.
    await tester.pumpWidget(MyApp());

    // Verifica se o texto "Kkindle" está presente.
    expect(find.text('Kkindle'), findsOneWidget);
  });
}
