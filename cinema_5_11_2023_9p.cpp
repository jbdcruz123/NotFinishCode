
//cinema.cpp project 5/11/2023
#include <iostream>
#include <string>
#include <vector>
#include <iomanip>
#include <climits>
using namespace std;

//function declaration
void showMenu() ;
void showMovies(  );
void finitial_object(  );
void fflush(  );
void fcheck_sale(  );
int ffind_movie_title( int pmovie_number=0 , string pmovie_title ="");
int ffind_seat_number( int pseat_number, int& pstatus );
void fpurchase_ticket(  );
void ftest( int pdisplay_type );
void fshow_seats(  );
void flog_in(  );
void flog_out(  );
void fmenu_movie(  );
void fadd_movie(  );
int ffind_movie_number_from_seat( int pmovie_number, int pstatus );
int fget_movie_number_count_from_seat( int pmovie_number, int& pnext_seat_number );
void fmenu_delete_movie();
int fdelete_movie( int pmovie_number );  
int fdelete_seat( int pmovie_number );   

struct Movie {
      int movie_number;  // id number ng movie
      string movie_title;    // movie title
      double amount;    //price ng movie
      string show_date;
      string show_time;
};
 
struct Ticket {
      int ticket_number;  //id ng tiket
      string movie_title;  //to trace movie title
      int log_in; //use value 1  0
      int seat_number; //trace whre seat located
      double amount; //amount na binayaran
};
 
struct Seat {
      int movie_number; 
      int seat_number;   //id number of seat
      int status;    //x for reserve or occpied other vacant
      int ticket_number; // ito ung xusotmer number na naka occupied
};

struct Sale {
      double total_sale; //sale from begining to last
      int quantity;     //total count of sale from begining to last
      int last_ticket_use;  //record of last ticket use
      int last_movie_number; //last record of movie number
      int last_seat_number;   //last record of seat number
};

//global main data
vector<Movie> movie; 
vector<Seat> seat;
// initialize ticket list
vector<Ticket> ticket;
struct Sale sale;


//process deleting seat, for selected movie number
int fdelete_seat( int pmovie_number ){//2
      //L220 

      int nlen= seat.size( ), still_have =1, sucess = 0;

      //infinite loop, titigil lang ito pag ala nang makita sa pmovie_number
      while( still_have ) { //4

            still_have = 0;
            for( int i_fir=0; i_fir < nlen ;  i_fir+=1 ) {//3

                  //cout << "\nL222 fdelete_seat bef if pmovie_number pmovie_number " << pmovie_number << 
                  //", seat[i_fir].movie_number " << seat[i_fir].movie_number  << "\n";
                  //cout << "L222_2 i_fir " << i_fir << ", nlen " << nlen << "\n"; 
                 
                  if( pmovie_number == seat[i_fir].movie_number  ) { //5
                        sucess =1;                        
                        still_have =1;

                        //delete, aatras ng 1
                        for( ; i_fir < nlen-1 ; i_fir+=1 ) {//7
                              
                              //cout << "\nL223 inside for( ; === i_fir " << i_fir << "\n"; 
                 
                              seat [i_fir] = seat[i_fir + 1];                             
                        } //7
                        
                        //cout << "\nL223_2 pause" << "\n";
                        //getchar(  );

                        //delete ang dulo
                        seat.pop_back(  );
                        nlen = seat.size( );
                        break;

                  } //5

            }//3

      } //4
      
      if( sucess == 1 ){//8

            //sucessfully deleted
            return 0;
      }//8

      return -1;
}//2

//process deleting movie, for selected movie number
int fdelete_movie( int pmovie_number ){//2
      //L210 

      int nlen= movie.size( ), sucess = 0;    

      for( int i_fir=0; i_fir < nlen ;  i_fir+=1 ) {//3
            
            //cout << "\nL212 fdelete_movie bef if pmovie_number pmovie_number " << pmovie_number << 
                  //", movie[i_fir].movie_number " << movie[i_fir].movie_number  << "\n";
            //cout << "\n212_2 i_fir " << i_fir << ", nlen "<< nlen << "\n";

            //pag nakita delete na ito
            if( pmovie_number == movie[i_fir].movie_number  ) { //5
                  sucess =1;
                  
                  //aatras ng 1
                  for( ; i_fir < nlen-1 ; i_fir+=1 ) {//7

                        movie[i_fir] = movie[i_fir + 1];                             
                  } //7

                  //cout << "\nL214 popback" << "\n";

                  //delete ang dulo
                  movie.pop_back(  );
                  nlen = movie.size(  );
                  break;

            } //5

      }//3

      
      if( sucess == 1 ){//8

            //sucessfully deleted
            return 0;
      }//8

      return -1;
}//2

//a menu for deleting movie
void fmenu_delete_movie(){//2
      //L200 

      string ch;
      int movie_number, movie_index, _return;

      cout << "\n\ndelete movie mode: ";
      cout << "\ninput movie number to delete: ";
      cin >> movie_number;
      
      movie_index = ffind_movie_title(movie_number );
      if( movie_index == -1 ){//3

            cout << "\n\ndid not found movie number " << movie_number << "\npress any...";
            getchar(  );
            return;
      }//3

      cout << "\n\nare u sure u want to delete movie_number and its seat number\ny to yes, any if cancel: ";
      cin >> ch;

      if(ch != "Y" and ch != "y") {//4

            cout << "\n\nU press cancel\npress any...";
            getchar(  );
            
            return;
      }//4

      _return = fdelete_seat( movie_number );

      if( _return == -1 ) { //5

            cout << "\n\ninternal error: didnt see any seat data records for movie number " << movie_number <<"\npress any...";
            getchar(  );
            
            return;
      } //5

      _return = fdelete_movie( movie_number );

      if( _return == -1 ) { //5

            cout << "\n\ninternal error: didnt see any movie data records for movie number " << movie_number <<"\npress any...";            
            getchar(  );
            
            return;
      } //5

      cout << "\n\nsucessfully deleted movie number " << movie_number <<"\npress any...";            
      getchar(  );



}//2

//get all the count in one movie_number and get the next seat number
//ex:     10 to 19 next seat must be 20
int fget_movie_number_count_from_seat( int pmovie_number, int& pnext_seat_number ){
      //L190

      int i_fir=0, nlen = seat.size(  ), count=0, another_turn=0;
      
      for( ; i_fir < nlen;i_fir+=1 ){

            if( pmovie_number == seat[ i_fir ].movie_number ) {
                  another_turn =1;
                  count +=1;
            } else if( another_turn ==1 ){

                  pnext_seat_number = seat[ i_fir ].seat_number;
                  return count;
            }

      }

       pnext_seat_number = INT_MAX;

      //ala nang karugtong
      if( another_turn ==1 ){
           
            return count;
      }

      return -1;
}

//find movie number then get the index
int ffind_movie_number_from_seat( int pmovie_number, int pstatus ){
      //L180

      //asume it is ascending order the seat
      int nlen = seat.size();

      for(int i_fir; i_fir < nlen; i_fir+=1) {

            if( pmovie_number == seat[i_fir].movie_number){
                  //found it
                  pstatus = 1;
                  return i_fir;
            }
      }

      pstatus = -1;
      return -1;
}

void fedit_movie(  ){
      //L170 

      string ch;
      Movie blank_movie;
      Seat blank_seat;
      vector<int> per_seat;

      int movie_number, movie_index, nlen, past_seat_number, status, seat_index, next_seat_number= 0;

      cout << "\n\nedit movie mode:\ninput movie number: ";
      cin >> movie_number;
      fflush(  );

      movie_index = ffind_movie_title( movie_number );
      if( movie_index == -1 ){
            cout << "\n\ndid not see movie number " << movie_number << " ";
            getchar(  );
            return;
      }
      
      blank_movie.movie_number = movie_number;

      cout << "\nold Title is " << movie[movie_index].movie_title << "\n Enter Title: ";
      getline( cin>> ws , blank_movie.movie_title);
     
      cout << "\nold amount is " << movie[movie_index].amount << "\n Enter amount: ";
      cin >> blank_movie.amount;
      fflush();

      cout << "\nold date is " << movie[movie_index].show_date << "\n Enter date: ";     
      getline( cin>> ws , blank_movie.show_date);
           
      cout << "\nold time is " << movie[movie_index].show_time << "\n Enter time: ";
      getline( cin>> ws , blank_movie.show_time);
   
      past_seat_number = sale.last_seat_number;

      seat_index = ffind_movie_number_from_seat( movie_number, status );

      sale.last_seat_number = seat[seat_index].seat_number;

      if( seat_index == -1 ){
            cout << "\n\ndid not see movie number " << movie_number << " ";
            getchar(  );
            return;
      }

      nlen = fget_movie_number_count_from_seat( movie_number, next_seat_number );
            
      for( int i_fir = 0 ; i_fir < nlen ; i_fir+=1 ){

            cout << "\n\nold seat number "<< sale.last_seat_number << " must higher than this and must lower than " << next_seat_number << " next seat number\ninput " << i_fir +1 << " :";
            per_seat.push_back( 0 );
            
            while( 1 ) {

                  cin >> per_seat[i_fir];
                  fflush();
                  if( sale.last_seat_number < per_seat[i_fir] &&  per_seat[i_fir] < next_seat_number){

                        sale.last_seat_number = per_seat[i_fir]; 
                        break;
                  }

                  cout << "\n\nmust be greater than " << sale.last_seat_number << " and lower than " << next_seat_number <<" repeat: ";
            }
  
      }

      cout << "\n\n\nfillup is finish for edit mode, do you want to save it y to yes, any for no:  ";
      cin >> ch;
      fflush(  );

      if(ch != "Y" && ch != "y"){
            cout << "\n\nit is canceled...";

            //get back the past values
            sale.last_seat_number = past_seat_number ;
            getchar();
            return;
      }

      movie[movie_index] = blank_movie;

      for( int i_fir; i_fir < nlen ; i_fir+=1 ){

            seat[ i_fir ].seat_number  = per_seat[i_fir];
            
      }

      cout << "\n\nsucessfully been edited the movie number " << movie_number << "\npress any...";
      getchar();
}

//add new movie
void fadd_movie(  ) {
      //L160

      Movie blank_movie;
      Seat blank_seat;
      vector<int> per_seat;
      int nlen, past_seat_number; 
      string ch;

      cout << "\n\nadd movie mode: ";
      cout << "\nEnter Title: ";
      getline( cin>> ws , blank_movie.movie_title);
     
      cout << "\nEnter Amount: ";
      cin >> blank_movie.amount;
      fflush();

      cout << "\nEnter date: ";
      getline( cin>> ws , blank_movie.show_date);
     
      cout << "\nEnter time: ";     
      getline( cin>> ws , blank_movie.show_time);
 
      sale.last_movie_number+=1;

      blank_movie.movie_number = sale.last_movie_number;
    
      cout << "\n\nHow many seats u want to create: ";
      cin >> nlen;
      fflush();

      //std::cout << "\nL164 bef_past_number  nlen | " << nlen << "|\n";


      past_seat_number = sale.last_seat_number;

      for( int i_fir = 0 ; i_fir < nlen ; i_fir+=1 ){

            cout << "\n\nmust higher than "<< sale.last_seat_number << "\ninput " << i_fir +1 << " :";
            per_seat.push_back( 0 );
            
            while( 1 ) {

                  cin >> per_seat[i_fir];
                  fflush();
                  if( sale.last_seat_number < per_seat[i_fir] ){

                        sale.last_seat_number = per_seat[i_fir]; 
                        break;
                  }

                  cout << "\n\nmust be greater than " << sale.last_seat_number << " repeat: ";
            }
            
      }

      cout << "\n\n\nfillup is finish for save mode, do you want to save it y to yes, any for no:  ";
      cin >> ch;
      fflush(  );
      
      std::cout << "\n165 ch | " << ch << "|\n";

      if(ch != "Y" && ch != "y"){
            cout << "\n\nit is canceled...";

            //get back the old values
            sale.last_seat_number = past_seat_number ;
            sale.last_movie_number -=1;
            getchar();
            return;
      }

      for ( int i_fir =0; i_fir < nlen ; i_fir+=1 ) {
 
            blank_seat.movie_number = blank_movie.movie_number;
            blank_seat.seat_number = per_seat[i_fir];
            blank_seat.status = 0;
            blank_seat.ticket_number = 0;
            seat.push_back( blank_seat );
          
      }

      movie.push_back(blank_movie);
      //sale.last_seat_number = per_seat[nlen-1];

      cout << "\n\nsucessfully been saved the movie number " << blank_movie.movie_title << "\npress any...";
      getchar();

}

void fmenu_movie(  ) {
      //L150 
      string ch;
      cout << "\n\nMenu movie: \na to add, e to edit, r to remove, press any to cancel : ";
      cin >> ch;
      fflush();
      
      std::cout << "\n152 fmenu_movie ch | " << ch << "|\n";

      switch(ch[0]) {
      
            case 'A':
            case 'a':
                  fadd_movie(  );
                  break;

            case 'E':
            case 'e':
                  fedit_movie(  );
                  break;
            
            case 'R':
            case 'r':

                  fmenu_delete_movie();
                  break;
            default:

                  cout << "\n\nu press any it is canceled...";
                  getchar();

      }

}

//returns -1 if fails to find
//plog_in -1 if fails otherwise 1 or 0
int ffind_ticket_number( int pticket_number, int plog_in){
      //140
      int iind=0, nlen = ticket.size(  );

      while( iind < nlen ) {

            if( pticket_number ==  ticket[iind].ticket_number ) {
                  plog_in = ticket[iind].log_in;
                  return iind;
            }
      
            iind+=1;
      }

      //did not found -1 all values
      plog_in = -1;
      return -1;
}


//process for log out
void flog_out( ){
      //L130

      string ch;
      int seat_status =-1, seat_index = -1, movie_number = -1, movie_index = -1, ticket_number, log_in, ticket_index = -1;
      cout << "\n\nlog out:\npress 0 to cancel, Enter seat number: ";
      cin >> ch;

      fflush( );

      //menu is canceled
      if(stoi(ch) == 0) {
            cout << "\n\nu press cancel...";
            getchar();
            return;
      }

      //find in seat
      
      seat_index = ffind_seat_number( stoi(ch), seat_status );
      //not found
      if( seat_status == -1 ){

            cout << "\n\ndid not found " << ch; 
            return;
      //its vacant, cannot logout
      }else if( seat_status == 0 ) {

            cout << "\n\n" << ch << " is vacant\ncannot logout..."; 
            return;
 
     }
      //look for ticket_number
      ticket_number = seat[ seat_index].ticket_number;

      ticket_index = ffind_ticket_number( ticket_number, log_in );
      
      //not found
      if( log_in == -1 ){

            cout << "\n\ndid not found in ticket data, the seat " << ch; 
            return;
      }

      //reinitialize status for vacant
      seat[seat_index].status = 0;
      //log out the customer
      ticket[ticket_index].log_in = 0; 

      cout << "\n\nsucessfully logout seat " << ch;
      getchar();

      cout << "\n\n";

}

//process for log in
void flog_in( ){
      //L120

      string ch;
      int seat_status =-1, seat_index = -1, movie_number = -1, movie_index = -1;
      cout << "\n\nlog in:\npress 0 to cancel, Enter seat number: ";
      cin >> ch;

      fflush( );

      //menu is cancelled
      if(stoi(ch) == 0) {
            cout << "\n\nu press cancel...";
            getchar();
            return;
      }

      //find in seat      
      seat_index = ffind_seat_number( stoi(ch), seat_status );
      //not found that seats, not exists
      if( seat_status == -1 ){

            cout << "\n\ndid not found " << ch; 
            return;
       //its not vacant, cannot give to customer
      }else if( seat_status != 0 ) {

            cout << "\n\n" << ch << " is occupied "; 
            return;
 
     }

      movie_number = seat[seat_index].movie_number;

      //cout << "\nL60 movie_number " << movie_number << "\n";

      //find movie number
      movie_index = ffind_movie_title( movie_number );      

      //cannot find movie in the list
      if( movie_index == -1 ){

            cout << "\n\ndid not found in movie the seat " << ch; 
            return;
      }

      //save the new ticket
      sale.last_ticket_use +=1;
      
      Ticket ticket_blank;

      ticket_blank.ticket_number = sale.last_ticket_use; 
      ticket_blank.movie_title = movie[movie_index].movie_title; 
      ticket_blank.seat_number = seat[seat_index].seat_number; 
      ticket_blank.log_in = 1;

      ticket_blank.amount = movie[movie_index].amount; 
      
      ticket.push_back( ticket_blank );

      cout << "\n\nsucessfully save seat " << ch;
      getchar();

      //sucessfully edited the seat data
      seat[seat_index].status = 1;

      cout << "\n\n";

}

void fcheck_sale(  ){
      //L110

      int total_quantity, iind = 0, nlen = ticket.size( );
      double total_sale=0;
      cout << "\n\ncheck sales \n";
      cout << setw(20) << right << "Ticket Number" << setw(20) << right << "Title"<< setw(20) << right << "seat number"<< setw(20) << right << " amount "<< "\n";
      while(  iind < nlen ){
      
            cout << setw(20) << right << ticket[iind].ticket_number << setw(20) << right << ticket[iind].movie_title << setw(20) << right << ticket[iind].seat_number << setw(20) << right << ticket[iind].amount << "\n";
      
            total_sale += ticket[iind].amount;
            iind+=1;
      }

     
      total_quantity = iind;

      sale.total_sale = total_sale;
      sale.quantity = total_quantity;

      cout << setw(10) << " quantity " << sale.quantity << "\n";
      cout << setw(10) << " total Sale " << sale.total_sale << "\n\n"<< "press any...";

      getchar();

 
}

//nag flush ng newline pag naka encounter ng output overflow
void fflush(  ){
      //L100

      char ch;
      while( 1 ){

            ch = getchar();

            //std::cout << "\nL101 fflush  bef if (ch  ch |" <<  ch << "|\n"; 

            if( ch == 10 or ch == 13){
                  break;
            }
      }
}

//find the movie number or movie title in movie data
//return -1 did not found
int ffind_movie_title( int pmovie_number , string pmovie_title ){
      //L90 

      
      int nlen = movie.size(  ), iind=0;

      if( pmovie_number != 0  ){

            //return 0 fail, > 0 sucess this is the index
            iind = 0;
            while( iind < nlen ){

                  //cout << "\nL90 insde while( iind === iind " << iind << ", pmovie_number " << pmovie_number << ", movie[iind].movie_number " << movie[iind].movie_number << "\n";
                  if( pmovie_number == movie[iind].movie_number){
                        
                        return iind;
                  }
              
                  iind+=1;
            }

      } else {

            iind = 0;        
            while( iind < nlen ){

                  if( pmovie_title == movie[iind].movie_title ){
                        
                        return iind;
                  }
              
                  iind+=1;
            }
      }

      //did not found
      return -1;
}

//find seat number in seat data
int ffind_seat_number( int pseat_number, int& pstatus ){
      //L80
      
      //return 0 fail, > 0 sucess this is the index
      int nlen = seat.size(  ), iind=0;
      while( iind < nlen ){
            
            //cout << "\nL81 iind " << iind << ", pseat_number "  << pseat_number << " , seat[iind].seat_number " << seat[iind].seat_number << "\n" ; 
            if( pseat_number == seat[iind].seat_number ){
                  
                  pstatus =  seat[iind].status;
                  return iind;

            } 
              
            iind+=1;
      }

      //did not found
      pstatus = -1;
      return -1;
}

//showing all seats and there status vacant, occupied
void fshow_seats(  ){  

      //L70  

      int iind=0, nlen = seat.size(  ), movie_number, count=0;

      if(  nlen <= 0){
            //a blank database
            cout << "\n\nno database in seat...";
            getchar();
            return;
      }

      movie_number = seat[0].movie_number; 

      int movie_index = ffind_movie_title( movie_number );

      cout << "\n\nTitle " << seat[0].movie_number << "  " << movie[ movie_index ].movie_title << "\n";

      
      while( iind < nlen ) {

            if( seat[iind].movie_number != movie_number ){
                  //restart of label
                  movie_number = seat[iind].movie_number;

                  movie_index = ffind_movie_title( movie_number );

                  cout << "\n\nTitle " << seat[iind].movie_number <<  "  " << movie[ movie_index ].movie_title << "\n";


                  continue;
            }
       
            //for each box showing x occupied not x is vacant
            if( seat[iind].status == 0){

                  cout << "[ " << (char) (96 +  seat[iind].movie_number) << " " << seat[iind].seat_number << " ] ";
            
            } else{
                  //not 0
                  cout << "[ X " << seat[iind].seat_number << " ] ";
            
            }
            iind+=1;
      }
}

//menu for purchase ticket, shows the status of vacant seats and occupied
void fpurchase_ticket(  ){
      //L60 
      string ch;
     
      cout << "\n\nPURCHASE TICKET\nlegend: X is occupied, other leters ( not X is vacant) ";
      fshow_seats(  );
      
      //buy ticket   
      cout << "\n\n\ny to Log in, n to log out, other key to cancel\npress not y and not n to canceled:  ";
      cin >> ch;
      fflush();

      switch( ch[0] ){

            case 'Y':
            case 'y':

                  flog_in();
                  break;

            case 'N':
            case 'n':
                  
                  flog_out( );      
                  break;
            default:

                  cout << "\n\nu press others not y not n,\nit is canceled...";
                  getchar();
                  return;
      }      

}

void ftest( int pdisplay_type ){
      //L50 
      cout  << "\n\n\ntest database: \n";

        if(  pdisplay_type == 1) {
            //seat

            cout  << "\n\nmovie: \n";
            int iind = 0, nlen = movie.size( );

            while( iind < nlen ){

                  cout << "\nmovie_number " << movie[ iind ].movie_number;
                  cout << "\nmovie_title " << movie[ iind ].movie_title;
                  cout << "\nprice " << movie[ iind ].amount;                  
                  cout << "\nshow date " << movie[ iind ].show_date << "\n";
                  cout << "\nshow time " << movie[ iind ].show_time << "\n\n";
                  iind+=1;
            }

      } else if(  pdisplay_type == 2) {
            //ticket

            cout  << "\n\nticket: \n";
            int iind = 0, nlen = ticket.size( );

            while( iind < nlen ){

                  cout << "\nmovie_number " << ticket[ iind ].ticket_number;
                  
                  cout << "\nseat_number " << ticket[ iind ].movie_title;
                  
                  cout << "\nstatus " << ticket[ iind ].seat_number;
                  
                  cout << "\nticket_number " << ticket[ iind ].amount << "\n\n";
                  iind+=1;
            }

      } else if(  pdisplay_type == 3) {
            //seat

            cout  << "\n\nseat: \n";
            int iind = 0, nlen = seat.size( );

            while( iind < nlen ){

                  cout << "\nmovie_number " << seat[ iind ].movie_number;
                  
                  cout << "\nseat_number " << seat[ iind ].seat_number;
                  
                  cout << "\nstatus " << seat[ iind ].status;
                  
                  cout << "\nticket_number " << seat[ iind ].ticket_number << "\n\n";
                  iind+=1;
            }

      } else if(  pdisplay_type == 4) {      
            cout  << "\n\nsale: \n";
            cout  << "\nTotal Sale: " << sale.total_sale;
            cout  << "\nquantity: " << sale.quantity;
            cout  << "\nlast ticket use " << sale.last_ticket_use;
            cout  << "\nlast movie number " << sale.last_movie_number;
            cout  << "\nlast seat number " << sale.last_seat_number;
      }
}

// function to show menu options
void showMenu() {
      //L40

      cout<< "\n\t||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||";
      cout<< "\n\t|                                                                |";
      cout<< "\n\t|                   CINEMO BOOKING TICKET                        |";
      cout<< "\n\t|                                                                |";
      cout <<"\n\t||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||\n";
      cout << "\n\t A. SHOW MOVIES\n";
      cout << "\n\t B. PURCHASE TICKET\n";
      cout  << "\n\t C. CHECK SALES\n";
      cout   << "\n\t D. EXIT\n";
      cout<< "\n\t Enter your choice : ";
}
 
// function to show movie list
void showMovies(  ) {
      //L30 

      cout << "\t\t\t**********MOVIE LIST**********\n\n";
      cout << "No. \tMovie Name\t\tPrice \t\tShow Date \tShow Time\n";

      for (int index_first = 0; index_first < movie.size(); index_first++) {
            cout << movie[index_first].movie_number << ".      "<< setw(20) << left << movie[index_first].movie_title << " Php "  << setw(15) << left << setprecision(2)  << fixed << movie[index_first].amount 
            << setw(15)<< movie[index_first].show_date << setw(15) << movie[index_first].show_time << endl;
      }

      cout << "\n\nmain record last movie index " << sale.last_movie_number << "\nlast ticket use " << sale.last_ticket_use << 
      "\nlast seat number " << sale.last_seat_number << "\n";
      
}

void finitial_object(  ){
      //L20    
       // initialize movie list

      sale.total_sale = 0;
      sale.quantity = 0;
      sale.last_ticket_use = 0;
      sale.last_movie_number = 0;
      sale.last_seat_number = 0;

      Movie movie1= {1,"Inception", 400, "2023-04-16", "8:00-10:00AM"};
      Movie movie2= {2,"Goodfellas", 300,"2023-04-18", "7:30-8:50PM"};
      Movie movie3= {3,"Blurred", 400,"2023-04-16", "8:00-10:00AM"};
      Movie movie4= {4,"Titanic", 400,"2023-04-16", "8:00-10:00AM"};

      movie.push_back(movie1);
      sale.last_movie_number +=1;

      Seat seat_blank;     
      int iind = 0;

      while( iind < 5 ) {
 
            seat_blank.movie_number = 1;
            seat_blank.seat_number = iind +1 +10;
            seat_blank.status = 0;
            seat_blank.ticket_number = 0;
            seat.push_back( seat_blank );
            iind+=1;
      }

      movie.push_back(movie2);
      sale.last_movie_number +=1;
       
      iind = 0;

      while( iind < 5 ) {
 
            seat_blank.movie_number = 2;
            seat_blank.seat_number = iind +1 +20;
            seat_blank.status = 0;
            seat_blank.ticket_number = 0;
            seat.push_back( seat_blank );
            iind+=1;
      }

      movie.push_back(movie3);
      sale.last_movie_number +=1;

      iind = 0;

      while( iind < 5 ) {
 
            seat_blank.movie_number = 3;
            seat_blank.seat_number = iind +1 +30;
            seat_blank.status = 0;
            seat_blank.ticket_number = 0;
            seat.push_back( seat_blank );
            iind+=1;
      }


      movie.push_back(movie4);
      sale.last_movie_number +=1;

      iind = 0;

      while( iind < 5 ) {
 
            seat_blank.movie_number = 4;
            seat_blank.seat_number = iind +1 +40;
            seat_blank.status = 0;
            seat_blank.ticket_number = 0;
            seat.push_back( seat_blank );
            iind+=1;
      }

      sale.total_sale =0;
      sale.quantity = 0;

      //get last seat number
      sale.last_seat_number = seat_blank.seat_number;
                  
      //cout << "\n\npause standby";
      //getchar( );
}       
  
 
int main() { 

     //L10 
 
       finitial_object(  );

      char choice;
      do {
            showMenu();
            cin >> choice;
            fflush( );

            switch (choice) {
                  case 'A':
                  case 'a':
                        showMovies( );

                        fmenu_movie(  );

                        break;
                  case 'B':
                  case 'b':
                        fpurchase_ticket();

                        break;
                  case 'C':
                  case 'c':

                        fcheck_sale(  );

                        break;
                  case 'D':
                  case 'd':
                        cout << "Thanks for using our program!\n";
                        break;

                  case 'Z':
                  case 'z':

                        cout << "\n\ndisplay all\n";
                        ftest( 1 );
                        ftest( 2 );
                        ftest( 3 );
                        ftest( 4 );
                        
                        break;
                  default:
                        cout << "Invalid choice. Please try again.\n";
                        break;
            }

            //cout << "\nL11 bef while(choice === choice " << choice;

      } while (choice != 'D' and choice != 'd');
       
      return 0;  
}
