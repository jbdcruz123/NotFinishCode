
//instruction: Write the function definition of each function specification

#include<stdio.h>
#include<strings.h>
#include<cstring>
#include<stdlib.h>

#define MAX 1000
typedef struct {

      char firstname[20];
      char lastname[20]; 
      char middlename[20];
}NAME;

typedef struct { 
      NAME fullname;
      long id;
      int year;
      char course[10];

      double GPA; 
}STUDENT;

int IsStudentPass( STUDENT *pstu, int pn, int id ){ //2

      int i = 0;
      while( i < pn ) {//3

            if( id == pstu[i].id && pstu[ i].GPA >= 1 && pstu[ i].GPA <= 3) {//4
                  
                return 1;
            }//4

            i+=1;
      }//3

      return 0;
}//2


STUDENT* GetAllFailingStudents( STUDENT *pstu, int pn ){ //2

      STUDENT *res = (STUDENT*) malloc( sizeof(STUDENT) * MAX );
      int nres=0;

      int i = 0;
      while( i < pn ) {//3

            if( pstu[ i].GPA >= 3 && pstu[ i].GPA <= 5) {//4
                  
                  res[nres]= pstu[i];
                  nres +=1;
            }//4

            i+=1;
      }//3
      return res;
}//2


void SelectSort( STUDENT *pstu, int pn ){ //2

      int i = 0;
      int j =0;
      while( i < pn -1) {//3

            j= i+1;
            while( j < pn ) {//4
      
                  if( pstu[ i].id > pstu[ j].id ) {//5
                        
                        STUDENT t = pstu[i];
                        pstu[i] = pstu[j];
                        pstu[j] = t;
                  
                  }//5

                  j+=1;
            }//4

            i+=1;
      }//3
     
}//2


STUDENT GetStudentInfo( STUDENT *pstu, int pn, int inp ){ //2

      STUDENT res;
      
      res.id = -1;

      int i = 0;
      while( i < pn ) {//3

            if( pstu[ i].id == inp) {//4
                  
                  res = pstu[i];

                  return res;
            }//4

            i+=1;
      }//3

      return res;
}//2



void fdis( STUDENT *pstu, int pn ) {//2
      //L20
      int i=0;

      while( i < pn ) {//3

            printf("\nL21 i < ==> i %d, id %ld\n", i , pstu[i].id);
            if( pstu[0].id == (long int) 0 ){//4

                  printf("\nL21_2 == 0 T\n");
            
                  i+=1;
                  continue;
            }//4
            printf( "\n\n\nindex %d\nname %s %s %s\nid %ld\nyear %d course %s\nGPA %.1f", i,  pstu[ i].fullname.firstname, pstu[ i].fullname.middlename, pstu[ i].fullname.lastname, pstu[i].id, pstu[i].year, pstu[i].course , pstu[i].GPA );                   
            i+=1;
      }//3

      printf("\n");
}//2

int main( void ) {//2

      STUDENT student[MAX];
      STUDENT *out;
      STUDENT  sub;
      int len=0, inp=-1;
      
      /////
      strcpy( student[0].fullname.firstname, (const char*) "faa" ); 
      strcpy( student[0].fullname.middlename, (const char*) "maa" );
      strcpy( student[0].fullname.lastname, (const char*) "laa" );
      student[0].id = 1;      
      student[0].year = 2;      
      strcpy( student[0].course, (const char*) "programing" );
      student[0].GPA = 2;      
      len+=1;
      
      /////
      strcpy( student[1].fullname.firstname, (const char*) "fbb" ); 
      strcpy( student[1].fullname.middlename, (const char*) "mbb" );
      strcpy( student[1].fullname.lastname, (const char*) "lbb" );     
      student[1].id = 2;      
      student[1].year = 2;      
      strcpy( student[1].course, (const char*) "programing" );
      student[1].GPA = 5;      
      len+=1;

      /////
      strcpy( student[2].fullname.firstname, (const char*) "fee" ); 
      strcpy( student[2].fullname.middlename, (const char*) "mee" );
      strcpy( student[2].fullname.lastname, (const char*) "lee" );
      student[2].id = 5;      
      student[2].year = 2;      
      strcpy( student[2].course, (const char*) "programing" );
      student[2].GPA = 3;      
      len+=1;

      /////
      strcpy( student[3].fullname.firstname, (const char*) "fdd" ); 
      strcpy( student[3].fullname.middlename, (const char*) "mdd" );
      strcpy( student[3].fullname.lastname, (const char*) "ldd" );
      student[3].id = 4;      
      student[3].year = 2;      
      strcpy( student[3].course, (const char*) "programing" );
      student[3].GPA = 1;      
      len+=1;

      /////
      strcpy( student[4].fullname.firstname, (const char*) "fcc" ); 
      strcpy( student[4].fullname.middlename, (const char*) "mcc" );
      strcpy( student[4].fullname.lastname, (const char*) "lcc" );
      student[4].id = 3;      
      student[4].year = 2;      
      strcpy( student[4].course, (const char*) "programing" );
      student[4].GPA = 4;
      len+=1;


      printf("\n\n\nstarting data: \n");
      
      fdis(student, len);
      getchar();//pause

      printf("\n\n\nGet All Failing Students: \n");

      out = GetAllFailingStudents(student, len); 

      printf("\nresult of GetAllFailingStudents: \n");
      fdis(out, len);
      free(out);
      getchar();//pause

      printf("\n\n\ninput find id: \n");
      scanf("%d", &inp);
      getchar(); //flush      
      sub = GetStudentInfo(student, len, inp);

      printf("\nresult GetStudentInfo: \n");
      fdis(&sub, 1);
      getchar();//pause      

      printf("\n\n\nSelect Sort: \n");
      SelectSort( student, len );      

      printf("\nresult of Select Sort: \n");
      fdis( student, len);
      getchar();//pause      

      printf("\n\n\ninput find id for student pass: \n");
      scanf("%d", &inp);
      getchar(); //flush    

      if( !IsStudentPass(student, len, inp ) ) {//3

            printf("\nmeron nakita ");
      }else {//3

            printf("\nwalang nakita ");
      }//3

      printf("\n\nexit...\n");
      return 0;
}//2


