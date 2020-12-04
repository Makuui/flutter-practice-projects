import 'package:flutter/material.dart';

void main() {
  runApp(MyApp());
}

class MyApp extends StatelessWidget {
  @override
  Widget build(BuildContext context) {
    return MaterialApp(
      home: Scaffold(
        backgroundColor: Colors.teal,
        body: SafeArea(
          child: Column(
            mainAxisAlignment: MainAxisAlignment.center,
            children: <Widget>[
              CircleAvatar(
                radius: 50.0,
                backgroundImage: AssetImage('images/IMG_0883.JPG'),
              ),
              Text(
                'Mark Vincent Atinon',
                style: TextStyle(
                  fontFamily: 'NerkoOne',
                  fontSize: 40.0,
                  color: Colors.white,
                  fontWeight: FontWeight.bold,
                ),
              ),
              Text(
                'Flutter Developer',
                style: TextStyle(
                  fontFamily: 'SourceSansPro',
                  fontSize: 20.0,
                  color: Colors.white,
                ),
              ),
              SizedBox(
                height: 20.00,
                width: 150.00,
                child: Divider(
                  color: Colors.teal.shade100,
                ),
              ),
              Card(
                margin: EdgeInsets.symmetric(vertical: 10.0, horizontal: 25.0),
                child: ListTile(
                  leading: Icon(
                    Icons.phone,
                    size: 30.00,
                    color: Colors.teal,
                  ),
                  title:
                    Text(
                      '+63 995 9888 885',
                      style: TextStyle(
                        color: Colors.teal.shade900,
                        fontFamily: "SourceSansPro",
                        fontSize: 20.0,
                      ),
                    ),
                  ),
                ),
              Card(
                margin:
                    EdgeInsets.symmetric(vertical: 10.00, horizontal: 25.00),
                child: ListTile(
                  leading: Icon(
                    Icons.email,
                    color: Colors.teal,
                  ),
                  title: Text(
                    'mvatinon@wvsu.edu.ph',
                    style: TextStyle(
                      color: Colors.teal.shade900,
                      fontFamily: 'SourceSansPro',
                      fontSize: 20.00,
                    ),
                  ),
                ),
              ),
            ],
          ),
        ),
      ),
    );
  }
}
