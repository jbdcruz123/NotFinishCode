#include <iostream>
#include <string>
#include <vector>
#include <iomanip>
 
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
};

//global main data
vector<Movie> movie; 
vector<Seat> seat;
// initialize ticket list
vector<Ticket> ticket;
struct Sale sale;


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

      //log in and log out

      
      cout << "\n\n\ny to Log in, n to log out, other key to cancel\npress not y and n to canceled:  ";
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
                  
                  cout << "\nshow date " << movie[ iind ].show_date << "\n\n";
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
            cout << index_first + 1 << ".      "<< setw(20) << left << movie[index_first].movie_title << " Php "  << setw(15) << left << setprecision(2)  << fixed << movie[index_first].amount 
            << setw(15)<< movie[index_first].show_date << setw(15) << movie[index_first].show_time << endl;
      }

      cout << endl;

}

void finitial_object(  ){
      //L20    
       // initialize movie list

      sale.total_sale = 0;
      sale.quantity = 0;
      sale.last_ticket_use = 0;

      Movie movie1= {1,"Inception", 400, "2023-04-16", "8:00-10:00AM"};
      Movie movie2= {2,"Goodfellas", 300,"2023-04-18", "7:30-8:50PM"};
      Movie movie3= {3,"Blurred", 400,"2023-04-16", "8:00-10:00AM"};
      Movie movie4= {4,"Titanic", 400,"2023-04-16", "8:00-10:00AM"};

      movie.push_back(movie1);

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

      //ftest(3);

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
                        break;
                  case 'B':
                  case 'b':
                        fpurchase_ticket();

                        break;
                  case 'C':
                  case 'c':
                       
                        /*ftest( 1 );
                        ftest( 2 );
                        ftest( 3 );
                        */

                        fcheck_sale(  );

                        break;
                  case 'D':
                  case 'd':
                        cout << "Thanks for using our program!\n";
                        break;
                  default:
                        cout << "Invalid choice. Please try again.\n";
                        break;
            }

            //cout << "\nL11 bef while(choice === choice " << choice;

      } while (choice != 'D' and choice != 'd');
       
      return 0;
       
}
