#include <iostream>
#include <fstream>
#include <string>
#include <vector>
#include <cmath>
#include <unordered_map>
#include <chrono>

std::vector<long> split_numbers(std::string nums_str)
{
  std::string delimiter = ",";
  std::vector<long> longs;
  std::size_t pos = 0;
  while ((pos = nums_str.find(delimiter)) != std::string::npos)
  {
    longs.push_back(atol(nums_str.substr(0, pos).c_str()));
    nums_str.erase(0, pos + delimiter.length());
  }
  return longs;
}

int main()
{
  std::ifstream file("input.txt");
  // std::ifstream file("input_test.txt");
  // std::ifstream file("input_test2.txt");

  std::string nums_line;
  std::getline(file, nums_line);

  auto longs = split_numbers(nums_line);

  std::cout << next << std::endl;
  return 0;
}
