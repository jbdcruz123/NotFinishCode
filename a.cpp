
#include <algorithm>
#include <cstdlib> // C++ version of <stdlib.h>
#include <cstring> // C++ version of <string.h>
#include <iostream>
#include <fstream>
#include <string>
#include <sstream>
#include <iomanip>
 
namespace rondb {
  // `constexpr` variables can be used in a constant-expression.
  constexpr char INDEX_USER1_DB[] = "index_user1.db";
  constexpr char USER1_DB[] = "user1.db";
 
  constexpr int MAX_ENTRIES = 10000;
 
  struct index_user_password_t {
    int password;
    int length;
  };
 
  struct index_user_t {
    int id;
    int marker;
  };
 
  struct entry_t {
    int    id;
    int    date;
    char   product_name[100];
    int    quantity; // number of items
    double item_price; // price per item
    double total_price; // `item_price * quantity`
  };
 
  index_user_password_t index_user_password;
  index_user_t          index_user[MAX_ENTRIES];
  entry_t               user[MAX_ENTRIES];
 
  /*
    Creates and initializes database.
  */
  bool initialize();
 
  /*
    Gets a string from the standard input stream.
  */
  bool get_string(std::string& output);
 
  /*
    Gets an integer from the standard input stream.
  */
  bool get_integer(int& output);
 
  /*
    Gets a floating-point from the standard input stream.
  */
  bool get_floating_point(double& output);
 
  /*
    Displays a range of entries.
    `start` is the starting index.
    `n` is the number of entries.
  */
  void display_entries(int start, int n);
 
  /*
    Finds an entry in the database using an ID.
  */
  int find_entry_by_id(int id);
 
  /*
    Prepares data for a table cell.
    `x` is the data to process.
    `width` is the minimum and maximum width.
  */
  std::string cell_data(std::string x, int width);
  std::string cell_data(int         x, int width);
  std::string cell_data(double      x, int width);
 
  /*
    Used by the `cell_data` functions in preparing the data.
  */
  std::string truncate(std::string s, int max_length);
 
  /*
    Temporarily suspends program execution (to show output).
  */
  void wait_for_keypress();
}
 
/* -------------------------------------------------------------------------- */
 
int main(void) {
  std::string ch;
 
  
 
   
   
  while (1) {
    std::cout
      << "====================\n"
      << "Main Menu\n"
      << "--------------------\n"
      << "D: Display entries\n"
      << "i: initial\n"
      << "Q: Quit\n"
      << "====================\n"
      << "Enter choice: ";
    while ( !(rondb::get_string(ch)) ) {
      std::cout << "ERROR: Invalid input.\n";
    }
 
    if (ch == "q" || ch == "Q") { // quit (exit program)
            std::exit(  0);
    }
    else if (ch == "d" || ch == "D") { // display entries
      int starting_index, length;
 
      std::cout << "Enter starting index: ";
      while ( !(rondb::get_integer(starting_index)) ) {
        std::cout << "ERROR: Invalid input.\n";
      }
 
      std::cout << "Enter length: ";
      while ( !(rondb::get_integer(length)) ) { // FIXME: check for value range
        std::cout << "ERROR: Invalid input.\n";
      }
 
      rondb::display_entries(starting_index, length);
    }
    else if (ch == "i") { // find an entry using an ID
      int column_width[] = { 10, 7, 10, 20, 10, 10, 10 };
      int id;
 
      std::cout << "Enter ID: ";
      while ( !(rondb::get_integer(id)) ) {
        std::cout << "ERROR: Invalid input.\n";
      }
 
      int index = rondb::find_entry_by_id(id);
      if (index == -1) {
        std::cout << "ERROR: ID '" << id << "' not found.\n";
        rondb::wait_for_keypress();
        continue;
      }
 
      std::cout
        << rondb::cell_data("ID",           column_width[0]) << " | "
        << rondb::cell_data("Marker",       column_width[1]) << " | "
        << rondb::cell_data("Date",         column_width[2]) << " | "
        << rondb::cell_data("Product Name", column_width[3]) << " | "
        << rondb::cell_data("Qty.",         column_width[4]) << " | "
        << rondb::cell_data("Amount",       column_width[5]) << " | "
        << rondb::cell_data("Total",        column_width[6]) << "\n"
        << std::string(column_width[0], '-') << "-+-"
        << std::string(column_width[1], '-') << "-+-"
        << std::string(column_width[2], '-') << "-+-"
        << std::string(column_width[3], '-') << "-+-"
        << std::string(column_width[4], '-') << "-+-"
        << std::string(column_width[5], '-') << "-+-"
        << std::string(column_width[6], '-') << "\n";
 
      std::cout
        << rondb::cell_data(rondb::index_user[index].id,     column_width[0]) << " | "
        << rondb::cell_data(rondb::index_user[index].marker, column_width[1]) << " | "
        << rondb::cell_data(rondb::user[index].date,         column_width[2]) << " | "
        << rondb::cell_data(rondb::user[index].product_name, column_width[3]) << " | "
        << rondb::cell_data(rondb::user[index].quantity,     column_width[4]) << " | "
        << rondb::cell_data(rondb::user[index].item_price,   column_width[5]) << " | "
        << rondb::cell_data(rondb::user[index].total_price,  column_width[6]) << "\n";
 
      rondb::wait_for_keypress();
    }
    else {
      std::cout << "ERROR: Invalid input.\n";
    }
  }
 
  return 0;
}
 
/* -------------------------------------------------------------------------- */
 
void rondb::display_entries(int start, int n) {
  int column_width[] = { 10, 7, 10, 20, 10, 10, 10 };
 
  std::cout
    << rondb::cell_data("ID",           column_width[0]) << " | "
    << rondb::cell_data("Marker",       column_width[1]) << " | "
    << rondb::cell_data("Date",         column_width[2]) << " | "
    << rondb::cell_data("Product Name", column_width[3]) << " | "
    << rondb::cell_data("Qty.",         column_width[4]) << " | "
    << rondb::cell_data("Item Price",   column_width[5]) << " | "
    << rondb::cell_data("Total",        column_width[6]) << "\n"
    << std::string(column_width[0], '-') << "-+-"
    << std::string(column_width[1], '-') << "-+-"
    << std::string(column_width[2], '-') << "-+-"
    << std::string(column_width[3], '-') << "-+-"
    << std::string(column_width[4], '-') << "-+-"
    << std::string(column_width[5], '-') << "-+-"
    << std::string(column_width[6], '-') << "\n";
 
  for (int i = start, stop = n; i <= stop; i += 1) {
    std::cout
      << rondb::cell_data(rondb::index_user[i].id,     column_width[0]) << " | "
      << rondb::cell_data(rondb::index_user[i].marker, column_width[1]) << " | "
      << rondb::cell_data(rondb::user[i].date,         column_width[2]) << " | "
      << rondb::cell_data(rondb::user[i].product_name, column_width[3]) << " | "
      << rondb::cell_data(rondb::user[i].quantity,     column_width[4]) << " | "
      << rondb::cell_data(rondb::user[i].item_price,   column_width[5]) << " | "
      << rondb::cell_data(rondb::user[i].total_price,  column_width[6])
      << "\n";
  }
}
 
bool rondb::initialize() {
  std::ofstream index_user_write;
  std::ofstream user_write;
 
  index_user_write.open(rondb::INDEX_USER1_DB, std::ios::binary);
  user_write.open(rondb::USER1_DB, std::ios::binary);
 
  if ( !(index_user_write.is_open()) || !(user_write.is_open()) ) {
    return false;
  }
 
  rondb::index_user_password.password = 1234;
  rondb::index_user_password.length = rondb::MAX_ENTRIES;
 
  index_user_write.write(
    (char*)&rondb::index_user_password,
    sizeof(rondb::index_user_password_t)
  );
 
  user_write.write(
    (char*)&rondb::index_user_password,
    sizeof(rondb::index_user_password_t)
  );
 
  std::string _str = ""; // sub string
  int id = 10;
 
  for (int fir = 0; fir < rondb::MAX_ENTRIES;  fir += 1) {
    rondb::index_user[fir].id = id;
    rondb::index_user[fir].marker = 1;
 
    rondb::user[fir].id = id;
    rondb::user[fir].date = (id -10) +1;
    _str = "name" + std::to_string( (id -10) + 1 );
    std::strcpy( rondb::user[fir].product_name, _str.c_str() );
    rondb::user[fir].quantity = 2;
    rondb::user[fir].item_price =  (id -10) +1;
    rondb::user[fir].total_price = rondb::user[fir].quantity * rondb::user[fir].item_price;
 
    id += 1;
  }
 
  index_user_write.write(
    (char*)&rondb::index_user,
    sizeof(rondb::index_user_t) * rondb::MAX_ENTRIES
  );
 
  user_write.write(
    (char*) rondb::user,
    sizeof(rondb::entry_t) * rondb::MAX_ENTRIES
  );
 
  index_user_write.close();
  user_write.close();
 
 rondb::display_entries( 0, 10 ); 
 
 
  return true;
}
 
bool rondb::get_string(std::string& output) {
  // If an error occurs, `output` is left empty.
  std::getline(std::cin, output);
 
  bool fail = std::cin.fail();
  std::cin.clear(); // clear error flags
 
  return !fail;
}
 
bool rondb::get_integer(int& output) {
  std::string s;
  std::istringstream iss;
 
  if ( !(rondb::get_string(s)) ) {
    return false;
  }
 
  iss.str(s); // assign a new string buffer to the input stream
  output = 0;
  // If an error occurs, `output` is not modified.
  iss >> output;
 
  return !(iss.fail());
}
 
 
bool rondb::get_floating_point(double& output) {
  std::string s;
  std::istringstream iss;
 
  if ( !(rondb::get_string(s)) ) {
    return false;
  }
 
  iss.str(s); // assign a new string buffer to the input stream
  output = 0;
  // If an error occurs, `output` is not modified.
  iss >> output;
 
  return !(iss.fail());
}
 
// This implementation uses binary search algorithm.
int rondb::find_entry_by_id(int id) {
  int left = 0, right = rondb::MAX_ENTRIES, mid = (left + right) / 2;
 
  while (left < right) {
    if (id < rondb::user[mid].id) {
      right = mid;
      mid = (left +  mid) / 2;
    }
    else if (id > rondb::user[mid].id) {
      left = mid;
      mid = (mid + right) / 2;
    }
    else { // entry found
      return mid;
    }
  }
 
  // entry not found
  return -1;
}
 
std::string rondb::cell_data(std::string x, int width) {
  std::ostringstream oss;
 
  oss << std::setw(width) << std::left << rondb::truncate(x, width);
 
  return oss.str();
}
 
std::string rondb::cell_data(int x, int width) {
  std::string s;
  std::ostringstream oss;
 
  oss << x;
  s = rondb::truncate(oss.str(), width);
  oss.str(""); // reset internal string buffer
  oss << std::setw(width) << std::right << s;
 
  return oss.str();
}
 
std::string rondb::cell_data(double x, int width) {
  std::string s;
  std::ostringstream oss;
 
  oss << std::fixed << std::setprecision(2) << x;
  s = rondb::truncate(oss.str(), width);
  oss.str(""); // reset internal string buffer
  oss << std::setw(width) << std::right << s;
 
  return oss.str();
}
 
std::string rondb::truncate(std::string s, int max_length) {
  if ((int)s.size() > max_length) {
    s.erase(s.begin() + max_length - 1, s.end());
    s += '~'; // signify that truncation has occurred
  }
 
  return s;
}
 
void rondb::wait_for_keypress() {
  std::system("PAUSE");
}
 
