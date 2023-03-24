


#include<iostream>

#include<fstream>
#include<string>
#include<string.h>


struct m_d {//2
      
      char id[10];
      char item[50];
      char date[100][50];  
      char amo[100][50];	
}; //2

//total number of id
int gid;

//main data na mag dadala ng value pa write sa textfile at pa read sa textfile
struct m_d data;

//stream ng read at write to a textfile
std::ifstream gread;
std::ofstream gwri;

//flusher para sa newline input	
void fflush(  ) {//2

      char ch;

      while( 1 ) {//3
            
            ch = getchar();

            //std::cout << "\nch |" << ch << "|, num " << (int) ch;
            if( ch == '\n' || ch == 13 ) {//4
                  
                   break;

            }//4
      
      }//3

}//2

//input value sa data
void finp( ) {//2

      std::string inp;
      gid +=1;
      sprintf(data.id , "%d", gid );

      std::cout << "\n\ninput item: ";
      std::cin >> inp;
      fflush(  );

      sprintf(data.item , "%s", inp.c_str( ) );
      
      int i =0;
      
      while( i < 3 ) {//3
            
            std::cout << "\ninput date: ";
            std::cin >> inp;
            fflush(  );
            sprintf(data.date[ i ] , "%s", inp.c_str( ) );		
      
            std::cout << "\ninput amount: ";
            std::cin >> inp;
            fflush(  );
            sprintf(data.amo[ i ] , "%s", inp.c_str( ) );		
      
                        
            i+=1;
      }//3
}//2

//print out ng 1 row ng data
void fdis( ) {//2

      std::cout << "\n\ninput item: " << data.id;

      std::cout << "\nitem: " << data.item;

      int i =0;
      
      while( i < 3 ) {//3
            
            std::cout << "\ndate: " << data.date[ i ];
            
	
            std::cout << "\namount: " << data.amo[ i ] ;
            
            i+=1;
      }//3
}//2


int main(void) {//2

      //pang restart ng value ng data
      struct m_d bla;
      strcpy( bla.id ,"");
      strcpy( bla.item ,"");
      strcpy( bla.date[0] ,"");
      strcpy( bla.amo[0] ,"");
      strcpy( bla.date[1] ,"");
      strcpy( bla.amo[1] ,"");
      strcpy( bla.date[2] ,"");
      strcpy( bla.amo[2] ,"");
   
      std::string ch;
      gid = 0;
      gwri.open( "test.txt", std::ios::out | std::ios::binary ); 
      gread.open( "test.txt", std::ios::in  | std::ios::binary ); 

      if(! gwri ){//10
            std::cout << "\nfalse";
      }//10

      data = bla;

      while( ch != "q" ) {//3

             std::cout << "\na input q to quit, a to add, d display ";
             std::cin >> ch;
             fflush(  );	
	
             if( ch == "a" ) {//4
                  //addnew data mode

                   finp(  );
                   gwri.seekp(0, gwri.end );
                   gwri.write( (char*) &data, sizeof( struct m_d)  );
                   data = bla;
                   gwri.flush(  );
             }//4
      

             if( ch == "d" ) {//4
                  //display the first row in data

                   gread.seekg( 0, gread.beg );
                   gread.read( (char*) &data, sizeof( struct m_d)   );
                   fdis(  );
                   data = bla;   
             }//4

             
      }//3


      gread.close(  );
      gwri.close(  );

      std::cout << "\n\nexiting...\n ";
        
}//2









  
