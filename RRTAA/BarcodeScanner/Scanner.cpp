#include <iostream>
#include <bits/stdc++.h>
#include <string>

using namespace std;
#define MAXN 100001
#define MOD 1000000007
#define x first
#define y second
typedef long long ll;
typedef unsigned long long ull;
typedef pair<int,int>ii;
typedef pair<ll,int>lli;
typedef pair<ii,int>piii;
struct Point{
    double x,y;
};
typedef struct{
    string type,data;
    vector<Point>location;
} decodedObject;


//Find and decode barcodes and QR codes
void decode(Mat &im, vector<decodedObject>&decodedObjects){
  ImageScanner scanner;
  // change zbar_none to http://zbar.sourceforge.net/api/zbar_8h.html#f7818ad6458f9f40362eecda97acdcb0
  scanner.set_config(ZBAR_NONE, ZBAR_CFG_ENABLE, 1);
  Mat imGray;
  cvtColor(im, imGray,CV_BGR2GRAY);
  Image image(im.cols, im.rows, "Y800", (uchar *)imGray.data, im.cols * im.rows);
  int n = scanner.scan(image);
  for(Image::SymbolIterator symbol = image.symbol_begin(); symbol != image.symbol_end(); ++symbol){
    decodedObject obj;
    obj.type = symbol->get_type_name();
    obj.data = symbol->get_data();
    cout << "Type : " << obj.type << endl;
    cout << "Data : " << obj.data << endl << endl;
    for(int i = 0; i< symbol->get_location_size(); i++){
      obj.location.push_back(Point(symbol->get_location_x(i),symbol->get_location_y(i)));
    }
    decodedObjects.push_back(obj);
  }
}
// Display barcode and QR code location
void display(Mat &im, vector<decodedObject>&decodedObjects){
  for(int i = 0; i < decodedObjects.size(); i++){
    vector<Point> points = decodedObjects[i].location;
    vector<Point> hull;
    if(points.size() > 4)
      convexHull(points, hull);
    else
      hull = points;
    int n = hull.size();
    for(int j = 0; j < n; j++){
      line(im, hull[j], hull[ (j+1) % n], Scalar(255,0,0), 3);
    }
  }
  imshow("Results", im);
  waitKey(0);

}
int main(int argc, char* argv[]){
  Mat im = imread("zbar-test.jpg");
  vector<decodedObject> decodedObjects;
  decode(im, decodedObjects);
  display(im, decodedObjects);

  return EXIT_SUCCESS;
}
