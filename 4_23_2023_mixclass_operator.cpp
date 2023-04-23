

#include<iostream>

//create constructor for int float double

//crate operator for +-/*

class clfloat;

class clinit{//2

      private:
            long long int minit;
      
      public:
            clinit( int a ){

                  this->minit = a;
            };
            
            long long int fget(){

                  return this->minit;
            };

            friend clinit operator+( clinit a, clfloat b);
            
            friend clinit operator-( clinit a, clfloat b);

            friend clinit operator*( clinit a, clfloat b);

            friend clinit operator/( clinit a, clfloat b);
            
            friend clfloat operator+( clfloat pfloat, clinit pinit);

            friend clfloat operator-( clfloat pfloat, clinit pinit);

            friend clfloat operator*( clfloat pfloat, clinit pinit);
      
            friend clfloat operator/( clfloat pfloat, clinit pinit);


};//2



class clfloat{//2

      private:
            float mfloat;
      
      public:
            clfloat(float a ){

                  this->mfloat = a;
            };
            
            float fget(  ){

                  return this->mfloat;
            };

            friend clinit operator+( clinit a, clfloat b);
            
            friend clinit operator-( clinit a, clfloat b);

            friend clinit operator*( clinit a, clfloat b);

            friend clinit operator/( clinit a, clfloat b);
       
            friend clfloat operator+( clfloat pfloat, clinit pinit);

            friend clfloat operator-( clfloat pfloat, clinit pinit);

            friend clfloat operator*( clfloat pfloat, clinit pinit);
            
            friend clfloat operator/( clfloat pfloat, clinit pinit);


};//2


clinit operator+( clinit a, clfloat b){

      clinit r(0); 
      r.minit = a.minit + b.mfloat;

      return r;
}


clinit operator-( clinit a, clfloat b){

      clinit r(0); 
      r.minit = a.minit - b.mfloat;

      return r;

}

clinit operator*( clinit a, clfloat b){

      clinit r(0); 
      r.minit = a.minit * b.mfloat;

      return r;

}

clinit operator/( clinit a, clfloat b){

      clinit r(0); 
      r.minit = a.minit / b.mfloat;

      return r;

}

clfloat operator+( clfloat pfloat, clinit pinit){
      
      clfloat r(0);
      r.mfloat = pfloat.mfloat + pinit.minit;
      return r;
}


clfloat operator-( clfloat pfloat, clinit pinit){
      
      clfloat r(0);
      r.mfloat = pfloat.mfloat - pinit.minit;
      return r;
}


clfloat operator*( clfloat pfloat, clinit pinit){
      
      clfloat r(0);
      r.mfloat = pfloat.mfloat * pinit.minit;
      return r;
}


clfloat operator/( clfloat pfloat, clinit pinit){
      
      clfloat r(0);
      r.mfloat = pfloat.mfloat / pinit.minit;
      return r;
}
           
int main(void) {//2

      clinit first(10);
      clfloat second(21.02);
      clinit total_int(0);
      clfloat total_float(0);

      std::cout << "\n\ninput in first " << first.fget();
      std::cout << "\n\ninput in second " << second.fget();
   
      total_int =  first + second;
      std::cout << "\n\nin plus total_int is "<< total_int.fget() << "\n";
      
      
      std::cout << "\n\ninput in first " << first.fget();
      std::cout << "\n\ninput in second " << second.fget();
   
      total_int =  first - second;
      std::cout << "\n\nin minus total_int is "<< total_int.fget() << "\n";
      
      
      std::cout << "\n\ninput in first " << first.fget();
      std::cout << "\n\ninput in second " << second.fget();
   
      total_int =  first * second;
      std::cout << "\n\nin times total_int is "<< total_int.fget() << "\n";
      
      
      std::cout << "\n\ninput in first " << first.fget();
      std::cout << "\n\ninput in second " << second.fget();
   
      total_int =  first / second;
      std::cout << "\n\nin divide total_int is "<< total_int.fget() << "\n";
      

      std::cout << "\n\ninput in first " << first.fget();
      std::cout << "\n\ninput in second " << second.fget();

      total_float =  second + first;

      std::cout << "\n\nin plus total_float is "<< total_float.fget() << "\n";

      std::cout << "\n\ninput in first " << first.fget();
      std::cout << "\n\ninput in second " << second.fget();

      total_float =  second - first;

      std::cout << "\n\nin minus total_float is "<< total_float.fget() << "\n";


      std::cout << "\n\ninput in first " << first.fget();
      std::cout << "\n\ninput in second " << second.fget();

      total_float =  second * first;

      std::cout << "\n\nin times total_float is "<< total_float.fget() << "\n";

      std::cout << "\n\ninput in first " << first.fget();
      std::cout << "\n\ninput in second " << second.fget();

      total_float =  second / first;

      std::cout << "\n\nin divide total_float is "<< total_float.fget() << "\n";
      
      std::cout << "\n\n\nexit..."<< "\n";
      return 0;
}//2



