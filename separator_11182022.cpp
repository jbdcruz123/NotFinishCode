


#include<iostream>
#include<string>
#include<vector>

std::string fget(std::string arr, std::string inp, size_t fir, size_t las){//2
      //L30 

      std::cout << "\nL30 "  << "\n";
      size_t u=0;      
      int i = 0;
      
      i = static_cast<size_t>(u);

      while(i < las){//3  abcd

            inp +=arr[fir + i];
            i+=1;
      }//3

      return inp;
}//2


auto ffun(std::string arr, std::vector<std::string> out, size_t n)->std::vector<std::string> {//2

      //L20 

      auto flag = 1;
      size_t fir=1000;
      size_t las=1000;  
    
      std::string inp;
      size_t i= 0;

      std::cout << "\nL21 i " << i << " ,n " << n << "\n";

      while(i < n){//3

            std::cout << "\nL22 i " << i << " ,arr[i] " << arr[i] << " ,flag " << flag << "\n";

            if(flag == 1){//4
                  
                  if(arr[i] != ' '){//7
  
                        flag = 0;
                        fir = i;
                        std::cout << "\nL22_b i " << i << " ,n " << n << "\n";
                        std::cout << "   fir " << fir << " ,las " << las << "\n";

                        i+=1;
                        //value 10000 for wlang ' ' sa dulo
                        las = 10000;

                        continue;
                  }//7

            }else {//4

                  
                  if(arr[i] == ' '){//7
                        
                        flag = 1;
                        
                        las = i;
                        i+=1;                        
                        inp="";

                        std::cout << "\nL22_c i " << i << " ,n " << n << "\n";
                        std::cout << "   fir " << fir << " ,las " << las << " ,(las- fir) " << las- fir << "\n";

                        out.push_back( fget(arr, inp, fir, las- fir) );

                        continue;
                  }//7

            }//4

            i+=1;
      }//3

      std::cout << "\nL24 " << "\n";

      if(las == 10000){//8
            //alang ' ' ang dulo ng string

            std::cout << "\nL24_b " << "\n";
            std::cout << "   fir " << fir << " ,las " << las << " ,(n- fir) " << n- fir << "\n";

            inp ="";
            out.push_back( fget(arr, inp, fir, n- fir) );
      }//8

      return out;
}//2


void fdis(std::vector<std::string> out){//2

      std::cout << "\n\noutput is: " << "\n";
      size_t n = out.size();
      int i = 0;
      while( (size_t) i < n){//3

            std::cout << "index " << i << ", out |" << out[i] << "|\n";

            i+=1;
      }//3


}//2

int main(){//2
      
      std::vector<std::string> out;

      //                   012345678
      //std::string arr = "ab cde fg hijk";

      //std::string arr = "";

      std::string arr = " my town is Cabanatuan    City , Nueva ecija";

      auto n = arr.size();

      out = ffun(arr, out, n);
      
      fdis(out);
      return 0;

}//2
