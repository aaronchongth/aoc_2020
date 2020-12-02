#include <iostream>
#include <string>
#include <vector>
#include <fstream>

int main(int argc, char** argv)
{
  std::ifstream file("input.txt");
  std::vector<int> input;
  std::string str;
  while (std::getline(file, str))
  {
    input.push_back(atoi(str.c_str()));
  }

  for (std::size_t i = 0; i < input.size(); ++i)
  {
    for (std::size_t j = 0; j < input.size(); ++j)
    {
      for (std::size_t k = 0; k < input.size(); ++k)
      {if (i == j)
        continue;

      if (input[i] + input[j] + input[k] == 2020)
        std::cout << (input[i] * input[j] * input[k]) << std::endl;
    }}
  }

  std::cout << "all done!" << std::endl;
  return 0;
}

