import 'dart:convert';

import 'package:flutter/material.dart';
import 'package:http/http.dart' as http;
import 'package:url_launcher/url_launcher.dart';

class MyHome extends StatefulWidget {
  const MyHome({super.key});

  @override
  State<MyHome> createState() => _MyHomeState();
}

class _MyHomeState extends State<MyHome> {
  @override
  initState() {
    fatchdata();
    super.initState();
  }

  List<dynamic>? res;
  @override
  Widget build(BuildContext context) {
    return Scaffold(
      appBar: AppBar(
        title: Text('News'),
        centerTitle: true,
      ),
      body: (res == null)
          ? Center(
              child: CircularProgressIndicator(),
            )
          : ListView.builder(
              itemCount: res!.length,
              itemBuilder: (context, index) => Container(
                margin: EdgeInsets.symmetric(vertical: 5, horizontal: 8),
                padding: EdgeInsets.all(5),
                decoration: BoxDecoration(boxShadow: [
                  BoxShadow(blurStyle: BlurStyle.outer, blurRadius: 4)
                ], borderRadius: BorderRadius.circular(20)),
                child: ListTile(
                  leading: Image.network((res![index]['urlToImage'] != null)
                      ? res![index]['urlToImage']
                      : "https://cdn.pixabay.com/photo/2022/11/01/11/30/breaking-news-7562021__340.jpg"),
                  title: Text(res![index]["title"]),
                  subtitle: Text((res![index]["description"] == null)
                      ? "Breaking news"
                      : res![index]["description"]),
                  onTap: (() => showModalBottomSheet(
                      context: context,
                      builder: (context) => Container(
                            width: MediaQuery.of(context).size.width - 10,
                            decoration: BoxDecoration(
                                borderRadius: BorderRadius.only(
                                    topLeft: Radius.circular(20))),
                            padding: EdgeInsets.all(10),
                            child: Column(
                              mainAxisSize: MainAxisSize.min,
                              children: [
                                Expanded(
                                  child: Image.network(
                                    fit: BoxFit.cover,
                                    (res![index]['urlToImage'] != null)
                                        ? "${res![index]['urlToImage']}"
                                        : "https://cdn.pixabay.com/photo/2022/11/01/11/30/breaking-news-7562021__340.jpg",
                                  ),
                                ),
                                Divider(),
                                Title(
                                  color: Colors.black,
                                  child: Text(
                                    res![index]['title'],
                                    style: TextStyle(
                                      fontWeight: FontWeight.bold,
                                      fontSize: 16,
                                    ),
                                  ),
                                ),
                                Text(
                                  (res![index]['content']!=null)?
                                  res![index]['content']:(res![index]['description']!=null)?res![index]['description']:"Braking News",
                                  style: TextStyle(
                                      fontWeight: FontWeight.w500,
                                      color: Color.fromARGB(255, 82, 82, 82)),
                                ),
                                ElevatedButton(
                                    onPressed: () {
                                      _launchInBrowser(
                                          Uri.parse(res![index]['url']));
                                    },
                                    child: Text("Read More"))
                              ],
                            ),
                          ))),
                ),
              ),
            ),
    );
  }

  fatchdata() async {
    const url =
        "https://newsapi.org/v2/top-headlines?country=in&apiKey=0425ace0066b47fea69ce086e2fec7ec";
    final uri = Uri.parse(url);
    final response = await http.get(uri);
    final body = response.body;
    final json = jsonDecode(body);
    setState(() {
      res = json['articles'];
    });
  }

  Future<void> _launchInBrowser(Uri url) async {
    if (!await launchUrl(
      url,
      mode: LaunchMode.inAppWebView,
    )) {
      throw Exception('Could not launch $url');
    }
  }
}
