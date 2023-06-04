#include <fstream>
#include <iostream>
#include <sstream>
#include <vector>


struct person {
    std::string name;
    int age;
};

void write_( std::vector<person>& people );
void read_( std::vector<person>& people );
void delemiter( std::string input, std::vector<person>& people );
void display( std::vector<person>& people );


void write_( std::vector<person>& people ){//2

        people.push_back({"John", 25});
        people.push_back({"Alice", 30});
        people.push_back({"Bob", 35});

        std::ofstream file_write("data.csv");
        if (!file_write) {
                std::cout << "Error opening the file!" << std::endl;
                return ;
        }

        for (const auto& person : people) {
                file_write << person.name << "," << person.age << "\n";
        }

        file_write.close();

        std::cout << "\n\nwriting to data.csv sucessful\n"; 
        people.clear();
}//2

void read_( std::vector<person>& people ){//2

        people.clear( ); //deletes all

        std::ifstream file_read("data.csv");
        if (!file_read) {
                std::cout << "Error opening the file!" << std::endl;
                return ;
        }

        std::string str_;

        while(std::getline( file_read, str_ ) ){

                delemiter( str_, people );
        }

        file_read.close();
        
        std::cout << "\n\nreading to data.csv sucessful\n";
        
}//2

void delemiter( std::string input, std::vector<person>& people ){

        std::istringstream iss(input);
        std::vector<std::string> tokens;

        std::string token;
        while (std::getline(iss, token, ',')) {
                tokens.push_back(token);
        }

        people.push_back( {  tokens[0], stoi( tokens[1] )  } );
        
}


void display( std::vector<person>& people ){//2

        std::cout << "\n\ndisplay data: "; 
        int i = 0;
        for (const auto& person : people ) {
        
                std::cout << "\nindex " << i << ", " << person.name << ", " << person.age ;
                i+=1;  
        }

        std::cout << "\n";
}//2

int main() {


        std::vector<person> people;

        std::string ch;
        while( 1 ){//3

                std::cout << "\n\nMenu: \nw write\nr read\nd display\nq quit:   ";
                std::cin >> ch; 

                if( ch == "w"){//4

                        write_( people );

                }if( ch == "r"){//4

                        read_( people );

                }if( ch == "d"){//4

                        display( people);
                        
                }if( ch == "q"){//4
                        break;
                        std::cout << "\n\nexit...";
                        getchar();
                }//4
        }//3


        return 0;
}
