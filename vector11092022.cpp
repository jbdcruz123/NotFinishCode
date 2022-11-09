#include<iostream>
#include<string>
#include<vector>

using namespace std;


int main(void){//2

      string _input{"ab cd "}, sub="" ;
      vector<string_view> output;

      auto i=0, n=0;

      n = _input.length();
      while(i < n ){//3


            if(_input[i] == ' '){//4

                  if(sub != ""){//5

                        //sub add new data column here
                        output.push_back( sub );
                        cout << "L22 debug _input[i] " << _input[i]<< ", sub " << sub << endl;
                        sub="";
                  }//5
                  i+=1;
                  continue;
            }//4


            sub += _input[i];

            cout << "L21 debug _input[i] " << _input[i]<< ", sub " << sub << endl;
            i+=1;
      }//3

      if(sub != ""){//5

            //sub add new data column here
            cout << "L22_b debug sub " << sub << endl;
            output.push_back( sub);
            
            sub="";
      }//5

      cout << "\n\ninput: " << _input <<  endl;
      cout << "\n\nresult: " << endl; 
     
       //display
          
      int index = 0;
      while(index < output.size()){//4

            cout << "index " << index << " ,output "  << output[index] << endl; 
            index+=1;
      }//4


      return 0;
}//2


