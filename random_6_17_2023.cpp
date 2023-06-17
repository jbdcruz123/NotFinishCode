


#include<iostream>
#include<random>

#define length 10

//std::random_device random_;
std::mt19937 generator( std::random_device{}( ) );
std::uniform_int_distribution<int> distribution;
int initial_random =0, start_=0 , last_ =0;

using param_type_ = std::uniform_int_distribution<int>::param_type;

int random_f( int start, int last ){//2


        initial_random = 1;
        start_ = start;
        last_ = last;
        return distribution(generator, param_type_{ start_, last_ });
}//2


int random_f(  ){//2

        if( initial_random == 0 ){ //3
                std::cout << "\n\nno initial first and last value \n";
                return -1;
        }//3
        return distribution(generator, param_type_{ start_, last_ });
}//2



int main(  ){//2

        int arr[ length];

        int i =0;
        random_f( 1, 100 );
        std::cout << "\n"; 

        while( i < length ){//3

                arr[i ] = random_f();
                std::cout << arr[i] << " "; 
                i+=1;
        }//3

        std::cout << "\n"; 


        return 0;
}//2


