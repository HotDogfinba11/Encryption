#include <iostream>
using namespace std;

int main()
{
   int i, x;
   char str[100];

   cout << "Please enter a string without spaces:\n";
   cin >> str;

   cout << "\nPlease choose following options:\n";
   cout << "1 = Encrypt the string.\n";
   cout << "2 = Decrypt the string.\n";
   cin >> x;


   switch(x)
   {
      //Encrypt string case
      case 1:
         for(i = 0; (i < 100 && str[i] != '\0'); i++)
            str[i] = str[i] + 3; //the key for encryption is 3 that is added to ASCII value

         cout << "\nEncrypted string: " << str << endl;
         break;

      //Encrypt string case
      case 2:
         for(i = 0; (i < 100 && str[i] != '\0'); i++)
         str[i] = str[i] - 3; //the key for encryption is 3 that is subtracted to ASCII value

      cout << "\nDecrypted string: " << str << endl;
      break;

      default:
         cout << "\nInvalid Input !!!\n";
   }
   return 0;
}
