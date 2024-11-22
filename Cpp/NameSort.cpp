#include <iostream>
#include <vector>
#include <string>
#include <algorithm>
using namespace std; 

int main(){
 vector <string> names(5); 
 cout << "Name 5 names \n";
 for (int i=0; i < 5; i++){
    cin >> names[i];
 } 
 sort(names.begin(), names.end(), greater<string>());

cout << "Here's the sorted list of names! \n";

 for(const auto& name : names){
    cout << name << "\n";
 }
 return 0; 
}
