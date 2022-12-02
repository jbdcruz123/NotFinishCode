#include<iostream>
#include<vector>

//important wag kakalimutan ung buffer na newline
//kada get ng char


int global_row=0;
int global_col=0;


void _fflush(char key){//2
     
      //std::cout << "\nL21 key |" << key << "|\n";

      if(key== '\n'){//3

            return;
      }//3


      char c='#';

      //std::cout << "\nL22 c |" << c << "|\n";
      
      c = getchar();

      //std::cout << "\nL23 c |" << c << "|\n";
     
       while(c != '\n' && c != 0){//3

            //std::cout << "\nL24 c |" << c << "|\n";

            c = getchar();
      }//3

}//2

void fscreen(std::vector< std::vector<char> > *matrix, int row, int col){//2

      int i, j;
      i =0;
      while(i < row){//3
            
            matrix->push_back({ });
            j=0;
            while( j < col){//4

                  (*matrix)[i].push_back('.');

                  j+=1;
            }//4

            i+=1;
      }//3

}//2

void fdisp( std::vector< std::vector<char> > matrix ){//2

      size_t i, j;
      i=0;
      while( i < matrix.size() ){//3
            j=0;

           
            while( j < matrix[i].size() ){//4

                  std::cout << matrix[i][j];

                  j+=1;
            }//4


            std::cout << "\n";

            i+=1;
      }//3
}//2

void fmove( std::vector< std::vector<char> > *matrix ){//2

      int pass_row = 0;
      int pass_col = 0;

      int row = 0;
      int col = 0;

      (*matrix)[row][col] = 'O';
      fdisp( *matrix );
      char key;

      while(1){//3

            //std::cout << "\nL11 aakey: " ; 
            key = getchar();
            //std::cout << "\nL12 key: |" << key <<"|\n" ;

            _fflush(key);

            if(key == 's' or key == 'S' ){//5
                  //down

                  if(row +1 >= global_row ){//7 

                        system("clear");
                        std::cout << "\n\nerror row down\n";
                        _fflush(' ');
                        system("clear");
                        fdisp( *matrix );
                        continue;
                  }//7

                  //deleteng pass

                  (*matrix)[pass_row][pass_col] = '.';

                  row +=1;
                  (*matrix)[row][col] = 'O';

                  pass_row = row;
                  pass_col = col;

               


            } else if(key == 'w' or key == 'W' ){//5
                  //up

                  if(row -1 < 0 ){//7 

                        system("clear");
                        std::cout << "\n\nerror row up\n";
                        _fflush(' ');

                        system("clear");
                        fdisp( *matrix );
                        
                        continue;
                  }//7
                  
                  
                  (*matrix)[pass_row][pass_col] = '.';

                  row -=1;

                  (*matrix)[row][col] = 'O';

                  pass_row = row;
                  pass_col = col;

                  
            } else if(key == 'a' or key == 'A' ){//5
                  //left

                  //std::cout << " col " << col;                  
                  //getchar();
                  if(col -1 < 0 ){//7 

                        system("clear");
                        std::cout << "\n\nerror col left\n";
                        _fflush(' ');
                        
                        system("clear");
                        fdisp( *matrix );
                        continue;
                  }//7


                  (*matrix)[pass_row][pass_col] = '.';
                  col -=1;

                  (*matrix)[row][col] = 'O';

                  pass_row = row;
                  pass_col = col;

                  
            } else if(key == 'd' or key == 'D' ){//5
                  //right

                 if(col+1 >= global_col ){//7 

                        system("clear");
                        std::cout << "\n\nerror col right\n";
                        _fflush(' ');
                        system("clear");
                        fdisp( *matrix );      
                        continue;
                  }//7
                  


                  (*matrix)[pass_row][pass_col] = '.';

                  col +=1;

                  (*matrix)[row][col] = 'O';


                  pass_row = row;
                  pass_col = col;

                  
            } else if(key == 'q' or key == 'Q' ){//5
                  //right


                  system("clear");
                  std::cout<< "\n\nend of prog....";
                  break;
                
                  
            } else{ //5

                  std::cout << "\ndapat ay a d s w lang ang gagamitin... " << "\n";
                  _fflush(' ' );
            }//5    

            system("clear");
            fdisp( *matrix );

            //std::cout << "\nL18 row " << row << ", col " << col << "\n";

      }//3

}//2


int main(  ){//2

      std::vector< std::vector<char> > matrix;
      
      global_row = 10;

      global_col = 10;
      system("clear");

      std::cout << "\n\n\nsample testing moving character\ngamit ang 2d array vector\ncontrol a left, d right, w up, s down\n\n\n\n\npress any key...";

      
      _fflush(' ');

      system("clear");

      fscreen(&matrix, global_row, global_col);

      fmove(&matrix);

      return 0;
}//2
