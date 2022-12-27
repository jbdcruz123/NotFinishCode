
//vector< vectoc< > >

#include<iostream>
#include<vector>

using vec = std::vector< std::vector< char > > ;

size_t n_row = 30, n_col = 40;

void finit(vec *point){//2

      size_t i= 0;
      size_t j =0;

      point->reserve(n_row);

      while( i < n_row){//3

            auto &row = point->emplace_back();

            row.reserve(n_col);

            j=0;
            while(j < n_col){//3

                  row.push_back('.');

                  
                  j+=1;
            }//3

            i+=1;

      }//3

}//2

void finput(vec *point){//2

      int size;
      std::cout << "input size for one side triangle:  ";
      std::cin >> size;

      int i, j, back;

      i= 0;
     
      while( i < size){//3

            std::cout << "\nL22 " << i << ", size " << size << "\n";
            j = (size-1) - i;

            while( j < size ){//4

                  (*point)[i][j] = '*';
                  j+=1;
            }//4

            i+=1;
            back-=1;
      }//3

}//2

void fdisp(vec *point){//2

      size_t i= 0;
      size_t j =0;

      i=0;
      while( i < n_row){//3

            j=0;
            while(j < n_col){//3

                  std::cout << (*point) [i][j];

                  j+=1;
            }//3

            std::cout << "\n";

            i+=1;

      }//3


}//2


int main(void){//2
      
      vec scr;

      std::cout << "\n\ntest b\n";

      finit(&scr);

      //display
      fdisp(&scr);

      //input
      finput(&scr);

      //display
      fdisp(&scr);

      return 0;
}//2
