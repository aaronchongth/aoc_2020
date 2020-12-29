#include "../utils.hpp"

int main()
{
  std::ifstream file("input.txt");
  std::vector<int> input;
  std::string str;
  while (std::getline(file, str))
  {
    input.push_back(atoi(str.c_str()));
  }

  return 0;
}
