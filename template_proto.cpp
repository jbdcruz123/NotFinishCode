



//test dont delete this 
//UNDER OBSERVATION

#include<iostream>
#include<curses.h>
#include<sstream>

//max range
int maxY=20;
int maxX=30;

//gumagalaw
int runY= 0;
int runX= 0;

int regulate( int, std::string);
std::string float_str( double, int );

template <typename T>
std::string string_precision(const T, const int );             

struct Data{
      int id;
      std::string s;
      double num;
};

int regulate( int a, std::string s){//2

      s = s.substr( 0, maxX);      
      if(  runY + a > maxY -2){//3
            move(maxY -1, runX);
            printw("reach the max Y %d", maxY);            
            getch( );
            clear( );
            runY = 0;
            move( runY, runX);
            printw( "%s", s.c_str( ) );  
            
            return 0;
      }//3
    
      runY +=a;    
      move( runY, runX);
      printw( "%s", s.c_str( ) );  
      return 1;    
}//2

std::string float_str( double val, int precision){//2

      return std::to_string(  val  ).substr(0, std::to_string(val  ).find( "." ) + precision +1   );             

}//2

template <typename T>
std::string string_precision(const T a_value, const int n = 6) {//2            
       std::ostringstream out;
       out.precision(n);
       out << std::fixed << a_value;
       return std::move(out).str();
}//2

template< typename Arr >
class Stack_{//2
      public:
            Arr *arr;
            int len;
            
            Stack_(  ): len( 0){  }
      
            void add( Arr a){//72
                   len+=1;
                   arr = new Arr[ len ];
                   arr[ len-1] = a;
             }//72
       
             void del( void) {//73
                   len-=1;
                   delete arr[len+1];   
             }//73
             
             void disp(void) {//44
                  std::string s;
                                     
                  s="display all ";     
                  regulate(2 , s);
                  for(int I=0 ;   I < len;  I+=1 ){//45
                        
                        s = "Index " + std::to_string( I);
                        regulate( 2, s  );
                        
                        s = "Id " + std::to_string( arr[ I ].id  );                  
                        regulate( 1, s  );
                        
                        s = "Name " +  arr[ I ].s;            
                        regulate(1, s  );
                        
                        s = "amount " + float_str( arr[ I ].num ,2);            
                        regulate( 1, s  ); 
                        
                   }//45
                   s = "pause...";
                   regulate( 1, s);
                   getch( );                  
            }//44                                             
               
}; //2

//old type
class mal_{//2
      public:
            int len;
            struct Data *arr;
            
            mal_(  ){ //50 
                  len=0; 
            }//50
            
            void add( struct Data a ){//60
                  len+=1;
                  if( len == 1 ){//63
                        arr = (struct Data*) malloc( sizeof( struct Data) * len );           
                        arr[ len -1 ] = a;    
                        return;      
                  }//63
                  arr = (struct Data*) realloc( arr, sizeof( struct Data) * len );                
                  arr[ len -1 ] = a;
                  
                  //disp(  );
            }//60
            
            void del( void) {//70
                   len-=1;
                   arr = (struct Data*) realloc(  arr, sizeof( struct Data ) * len);      
             }//70
             
             void disp(void) {//100
                  std::string s;
                                     
                  s="display all ";     
                  regulate(2 , s);
                  for(int I=0 ;   I < len;  I+=1 ){//103
                        
                        s = "Index " + std::to_string( I);
                        regulate( 2, s  );
                        
                        s = "Id " + std::to_string( arr[ I ].id
                        );                  
                        regulate( 1, s  );
                        
                        s = "Name " +  arr[ I ].s;            
                        regulate(1, s  );
                        
                        s = "amount " + float_str( arr[ I ].num ,2); 
                        regulate( 1, s  ); 
                        
                   }//103
                   s = "pause...";
                   regulate( 1, s);
                   getch( );                  
            }//100                                             
               
};//2

int main( void) {//2
      
      initscr( );
      Stack_< Data> A;
      mal_ B;
      struct Data D;
      std::string s;
      
      s = "precision ex: "+ string_precision( 12.3456, 2 );

       //printw(  "\n\nm for malloc test\nn for new test'\npress others to cancel   ");
      s="m for malloc test";
      regulate( 2, s );
      s= "n for new test'";
      regulate( 1, s );
      s = "press others to cancel";
      regulate( 1, s );   
      char c = getch(  );
      
      if( c == 'm' or c== 'M' ){//11
            //malloc test
            s = "choosing malloc test";
            regulate( 2, s );
            for( int I = 0; I < 5 ; I +=1  ){//30
      
                  D.id = I+1;
                  D.s = "name " + std::to_string(  I + 1);
                  D.num = (I+1 ) *10 + .02;
                  B.add( D );
            }//30        
      
            B.disp( );
      } else if( c == 'n' or c== 'N' ){//10
           //new test
            printw( "\n\nchoosing new test");
            
            for( int I = 0; I < 5 ; I +=1  ){//20
      
                  D.id = I+1;
                  D.s = "name " + std::to_string(  I + 1);
                  D.num = ( I + 1)  *10 + .02;
                  A.add( D );
            }//20        
      
            //disable this not perminent
            A.disp( );            
      }//10
            
      
      s = "Exit...";
      regulate( 2, s);
      s = "";
      regulate( 1, s);
      getch( );            
      endwin( );
      return 0;
}//2


