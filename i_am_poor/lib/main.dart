import 'package:flutter/material.dart';

void main() {
  runApp(
    MaterialApp(
      home: Scaffold(
        backgroundColor: Colors.amberAccent,
        appBar: AppBar(
          title: Text('I am Poor'),
          backgroundColor: Colors.deepOrange[300],
        ),
        body: Center(
          child: Image(
            image: AssetImage('images/coal.jpg'),
          ),
        ),
      ),
    ),
  );
}
