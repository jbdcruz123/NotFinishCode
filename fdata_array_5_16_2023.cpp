
//no backup
//input output files
//reference
//https://en.cppreference.com/w/cpp/io/c/rename
// std::rename(current_name, new_name);

#include<iostream>
#include<fstream>
#include<string>
#include<string.h>
#include <iomanip>

#define _FILENAME "data.db"
#define TRANSFER_FILENAME "transfer.db"

struct stformat { //2
      int password;
      int length;
}; //2

struct stdata {//2

      int number;
      char date[100];
      char name[100];
      double amount;
      
}; //2

std::ifstream gread;
std::ofstream gwrite;
struct stformat gformat;
struct stdata gdata;
struct stdata gblank_data;

//function declaration
void fdisplay_all(  ) ;
void finitial(  );
struct stdata fdata_array( int pindex, struct stdata pinp_data = gblank_data );
void ffail_cin(  );
int fpush_back( struct stdata pinp_data );
int fpop_back(  );
void fremove(  ) ;
void fupdate_length();

void fupdate_length( ) {//2
      //L90 
      gread.open(_FILENAME, std::ios::binary );
   
      if( !gread ) {//5
            std::cout << "\n\nerror file " << _FILENAME << " cannot found for reading...";
            getchar(  );
            return; 
      }//5

      gread.read(  (char*) &gformat, sizeof( struct stformat )  );
      
      gread.close();
}//2

//removes 1 data, user use index to delete
void fremove(  ) {//2
      //L80 

      stdata right_data;

      int index;

      fupdate_length();

      if( gformat.length <= 0 ) { // 15
            std::cout << "\n\nalang laman na data sa file " << _FILENAME << " para mag remove ... ";
            getchar();
            return;
      }//15      

      std::cout << "\n\nremove mode: \nrange from 0 to " << gformat.length -1 << "\ninput index to delete: ";
      std::cin >> index;
      ffail_cin(  );

      if( index <= -1 || index >= gformat.length) {//4 

            std::cout << "\n\nmali input, nasa range lamang dapat ng 0 to " << gformat.length -1 << "\npress any...";
            getchar();
            return;

      }//4

      for( int fir = index; fir < gformat.length -1; fir+=1 ) {//5

            right_data = fdata_array( fir +1);
            
            fdata_array( fir, right_data );

            //debug L83 fdisplay_all 
            //fdisplay_all();

      }//5

      fpop_back(  );

      std::cout << "\n\nsucess deleting index " << index << ", press any..." << "\n";
      getchar();

}//2

//add 1 data, pinp_data is the new data 
//return total length,otherwise false -1
int fpush_back( struct stdata pinp_data ) {//2
      //L70
      
      gread.open( _FILENAME, std::ios::binary );
      gwrite.open( TRANSFER_FILENAME, std::ios::binary );

      if( !gwrite ) {//3
            std::cout << "\n\nerror cannot open file " << TRANSFER_FILENAME << " for writing...\n";
            getchar();
            
            return -1;
      }//3

      if( !gread ) {//4
            std::cout << "\n\nerror cannot open file " << _FILENAME << " for writing...\n";
            getchar();
            
            return -1;
      }//4

      gread.read( (char*) &gformat , sizeof( stformat )  );
      gformat.length +=1;
      gwrite.write( (char*) &gformat , sizeof( stformat )  );

      //std::cout << "\ndebug L71 bef for( --> gformat.length " << gformat.length;

      for( int fir = 1; fir < gformat.length ; fir+=1 ) {//5
         
            gread.read( (char*) &gdata , sizeof( stdata )  );
         
            gwrite.write( (char*) &gdata , sizeof( stdata )  );
            
      }//5

      gdata = pinp_data;

      gwrite.write( (char*) &gdata , sizeof( stdata )  );

      gread.close(  );
      gwrite.close(  );

      //deleting old file
      if( std::remove( _FILENAME ) != 0) {//14
            std::cout << "\n\nerror cannot remove file " <<  _FILENAME << "\n";
            getchar();

      }//14  

      //rename new file
      if( std::rename( TRANSFER_FILENAME , _FILENAME ) != 0) {//12 
            std::cout << "\n\nerror cannot rename file " << TRANSFER_FILENAME << "\n";
            getchar();
      }//12

      return gformat.length;
}//2

//delete one elements at the back
//return -1 if false, otherwise total length
int fpop_back(  ) {  //2
      //L60 

      int nlen;
      gread.open( _FILENAME, std::ios::binary );
      gwrite.open( TRANSFER_FILENAME, std::ios::binary );

      if( !gwrite ) {//3
            std::cout << "\n\nerror cannot open file " << TRANSFER_FILENAME << " for writing...\n";
            getchar();
            
            return -1;
      }//3

      if( !gread ) {//4
            std::cout << "\n\nerror cannot open file " << _FILENAME << " for writing...\n";
            getchar();
            
            return -1;
      }//4

      gread.read( (char*) &gformat , sizeof( stformat )  );

      nlen = gformat.length;

      if( gformat.length > 0){ //20
              
            gformat.length -=1;
      }//20 

      gwrite.write( (char*) &gformat , sizeof( stformat )  );

      //std::cout << "\ndebug L62 bef for(  gformat.length " << gformat.length << ", nlen " << nlen << "\n";

      for( int fir = 1; fir <= nlen -1 ; fir+=1 ) {//5
         
            gread.read( (char*) &gdata , sizeof( stdata )  );
         
            gwrite.write( (char*) &gdata , sizeof( stdata )  );
            
      }//5

      gread.close(  );
      gwrite.close(  );

       //deleting old file
      if( std::remove( _FILENAME ) != 0) {//14
            std::cout << "\n\nerror cannot remove file " <<  _FILENAME << "\n";
            getchar();

      }//14  

      //rename new file
      if( std::rename( TRANSFER_FILENAME , _FILENAME ) != 0) {//12 
            std::cout << "\n\nerror cannot rename file " << TRANSFER_FILENAME << "\n";
            getchar();
      }//12

      return 0;
}//2

//para nag fail ung cin madalas mangyari ito sa
//inpuy ng number
void ffail_cin(  ) { //2
      //L50 
      char ch;
      if( std::cin.fail(  ) ) {//10

            std::cin.clear( );

            std::cin.ignore( 1000, '\n');
      } else { //10

            while( 1 ){//11

                  ch = getchar(  );
                  if( ch == 10 ) {//3
                        break;
                  }//3

            }//11
                        
      }//10

}//2

//display all data of data.db
void fdisplay_all(  ) {//2
      //L30 
      
      //reset
      gformat.password = -1;
      gformat.length =-1;
      
      gread.open(_FILENAME, std::ios::binary );
   
      if( !gread ) {//5
            std::cout << "\n\nerror file " << _FILENAME << " cannot found for reading...";
            getchar(  );
            return; 
      }//5

      gread.read(  (char*) &gformat, sizeof( struct stformat )  );
      
      //std::cout << "\ndebug L30 password " << gformat.password << ", length " << gformat.length << "\n";            
      
      if( gformat.length <= 0) {//3 
            std::cout << "\n\nerror no load to reload ";
            getchar(  );
            return;      
      }//3

      std::cout << "\n\nstaring to view length is " << gformat.length << "\n";
      std::cout << "\nIpakita lahat ng files gamit ang fdata_array\n";
      std::cout << std::setw( 5 ) << std::right << "index" << std::setw( 10 ) << std::right <<  "number" << std::setw( 15 ) << std::right <<  "date" << std::setw( 15 ) << std::right << "name" << std::setw( 10 ) << std::right << "amount" << "\n";
      
      int fir=0;
      while( fir < gformat.length ) {//4

            gread.read(  (char*) &gdata, sizeof( struct stdata )  );

            std::cout << std::setw( 5 ) << std::fixed << fir;
            std::cout << std::setw( 10 ) << std::fixed << gdata.number ;                  
            std::cout << std::setw( 15 ) << gdata.date ;
            std::cout << std::setw( 15 ) << gdata.name ;
            std::cout << std::setw( 10 ) << std::fixed << std::setprecision(2) << gdata.amount << "\n"; 
            fir+=1;
       }//4

       gread.close(  );             
}//2

void finitial(  ) {//2
      //L20 
      std::string str;
      int nlen = 10, fir = 0;
      gformat.password = 1234;
      
      //we will put the total 3 earlier than data
      gformat.length =nlen;
      
      gwrite.open( _FILENAME, std::ios::binary );
      
      gwrite.write( (const char*) &gformat, sizeof( struct stformat )  ) ;             

       //then puts it back to orig value
      gformat.length = 0;
            
      while(fir < nlen )  {//2
      
            gdata.number = fir +1;
            str = "1/" + std::to_string( fir+1 );
            str += "/2023"; 
            strcpy(  gdata.date, str.c_str(  ) );
            
            str = "name" + std::to_string( fir+1 );
            strcpy(  gdata.name, str.c_str(  ) );            
            gdata.amount = fir +10;
            
            gwrite.write( ( const char*) &gdata, sizeof( struct stdata )  ) ;             
            
            gformat.length+=1;
            fir +=1;            
      }//3

      gwrite.close(  );
            
}//2

//its like an array of object  output --> data_array[ index ] = input 
//pindex is index, pinp_data is input, return is output
struct stdata fdata_array( int pindex, struct stdata pinp_data){//2
      //L40 
      //std::cout << "\ndebug L41 pinp_data.number " << pinp_data.number << "\n";

      gread.open( _FILENAME, std::ios::binary);

      if( !gread ) {//4
            std::cout << "\n\nerror cannot open file " << _FILENAME << " for reading...\n";
            getchar();
          
            return gblank_data;
      }//4

      if( pinp_data.number == -1 ) {//3
            //output 
     
            //std::cout << "\ndebug L42 inside if pinp_data.number true " << "\n";

            gread.read(  (char*) &gformat, sizeof( struct stformat )  );
            
            for( int fir=1; fir <= gformat.length; fir+=1 ) {//4

                  gread.read(  (char*) &gdata, sizeof( struct stdata )  );
                  
                  if( fir -1 == pindex ) {//5
                        //it found
                                            
                        break;
                  }//5
                  
            }//4

      }else {//3
            //edit elements

            //std::cout << "\ndebug L42_2 inside if pinp_data.number false " << "\n";

            gwrite.open( TRANSFER_FILENAME, std::ios::binary);

            if( !gwrite ) {//4
                  std::cout << "\n\nerror cannot open file " << _FILENAME << " for writing...\n";
                  getchar();
                  
                  return gblank_data;
            }//4

            gread.read(  (char*) &gformat, sizeof( struct stformat )  );
            
            gwrite.write( (const char*) &gformat, sizeof( struct stformat )  ) ;   

            for( int fir=1; fir <= gformat.length; fir+=1 ) {//10
            
                  //std::cout << "\ndebug L42_3 inside for( int fir   fir " << fir << " , pindex " << pindex <<"\n";

                  gread.read(  (char*) &gdata, sizeof( struct stdata )  );
                  
                  if( fir -1 == pindex ) {//11
                        
                        gdata = pinp_data;
                        
                  }//11

                  gwrite.write(  (char*) &gdata, sizeof( struct stdata )  );

            }//10
      
            gwrite.close(  );

            //deleting old file
            if( std::remove( _FILENAME ) != 0) {//14
                  std::cout << "\n\nerror cannot remove file " <<  _FILENAME << "\n";
                  getchar();

            }//14  

            //rename new file
            if( std::rename( TRANSFER_FILENAME , _FILENAME ) != 0) {//12 
                  std::cout << "\n\nerror cannot rename file " << TRANSFER_FILENAME << "\n";
                  getchar();
                  
            }//12

      }//3

      gread.close(  );

      return gdata;

}//2


int main( void ) {  //2

      //L10 
     
      int index;
      std::string ch;
       //dont change default number for gblank_data
      gblank_data.number = -1;
     
      std::cout << "\n\nUnang run ng program. Gusto mo bang mag initialize ng elements sa file " << _FILENAME << "\npress Y for Yes or press any for No :  ";
      std::cin >> ch;
      ffail_cin(  );

      
      if( ch == "Y" ||  ch == "y"){//10
            
            finitial(  );

            std::cout << "\n\nSucess na nai add ung 10 elemnts sa file " << _FILENAME << "\npress any key....";
            getchar(  );      
      }//10      
      

      while(  1 ){ //11

            std::cout << "\n\nMAIN MENU:\na for add, e for edit, r for remove, d for display all\npress q to quit..\ninput: " ;
            std::cin >> ch;
            ffail_cin(  );

            if( ch == "Q" || ch == "q" ){//12
           
                  break;
            }else if ( ch == "A" || ch == "a" ) {//12

                  std::cout << "\n\nadd mode:";
                  
                  std::cout << "\n\ninput number  date  name  amount\n       ";
                  std::cin >> gdata.number >> gdata.date >> gdata.name >>  gdata.amount;      
                  ffail_cin(  );

                  fpush_back(gdata);

                  std::cout << "\n\nsucess adding, press any..." << "\n";
                  getchar();

            }else if ( ch == "E" || ch == "e" ) {//12

                  fupdate_length( );

                  if( gformat.length <= 0 ) { // 15
                        std::cout << "\n\nalang laman na data sa file " << _FILENAME << " ... ";
                        getchar();
                        continue;
                  }//15

                  std::cout << "\n\nedit mode:";
                  std::cout << "\ninput ang index na i edit range 0 to " << gformat.length -1 << " :  ";
                  std::cin >> index;      
                  ffail_cin(  );

                  std::cout << "\n\ninput number  date  name  amount\n       ";
                  std::cin >> gdata.number >> gdata.date >> gdata.name >>  gdata.amount;      
                  ffail_cin(  );

                  fdata_array(index, gdata);
            
                  std::cout << "\n\nsucess editing, press any... ";
                  getchar();

            }else if ( ch == "R" || ch == "r" ) { //12

                  fremove(  ) ;
            }else if ( ch == "D" || ch == "d" ) { //12
                  
                  std::cout << "\n\ndisplay all \n";
                  fdisplay_all(  );
                   
            }//12
      }//11

      std::cout << "\n\nccexit..." << "\n";
      getchar();
      return 0;
}//2


















