#include<iostream>
using namespace std;
int main(){
    int n=5;
    // int num=1;
     int num=5
    for(int i=0;i<n;i++)
    {
        for(int j=0;j<n-i-1;j++)
        {
            cout<<"-";

        }
        for(int j=0;j<=i;j++)
        {   
            cout<<num;

        }
        cout<<endl;
    }
    return 0;
}
// #include <iostream>
// using namespace std;

// int main() {
//     int n = 5;
//     int num = 1;

//     for (int i = n; i > 0; i--) {
//         // Print spaces
//         for (int j = 1; j <= i - num; j++) {
//             cout << "-";
            
//         }

//         // Print numbers in the pattern
//         for (int k = i; k <= n-i+1; k++) {
//             cout << k;
//         }
//         num++;
//         cout << endl;
//     }

//     return 0;
// }
