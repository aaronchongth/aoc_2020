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

// long update_and_get_next(
//   long spoken,
//   long turn,
//   std::unordered_map<long, long>& mem)
// {
//   auto it = mem.find(spoken);
//   if (it == mem.end())
//   {
//     mem[spoken] = turn;
//     return 0;
//   }
  
//   long prev_turn = it->second;
//   long age = turn - prev_turn;
//   mem[spoken] = turn;
//   return age;
// }

long update_and_get_next(
  long spoken,
  long turn,
  std::vector<long>& mem)
{
  long val = mem[spoken];
  if (val == -1)
  {
    mem[spoken] = turn;
    return 0;
  }

  long prev_turn = val;
  long age = turn - prev_turn;
  mem[spoken] = turn;
  return age;
}

int main()
{
  std::ifstream file("input.txt");
  // std::ifstream file("input_test.txt");
  // std::ifstream file("input_test2.txt");

  std::string nums_line;
  std::getline(file, nums_line);

  auto longs = split_numbers(nums_line);
  // std::vector<long> longs = {0, 3, 6};
  // std::vector<long> longs = {1, 3, 3};

  // std::unordered_map<long, long> mem;
  std::vector<long> mem(30000000, -1);

  long curr_turn = 1;
  long next = -1;

  for (const long l : longs)
  {
    // std::cout << l << std::endl;
    next = update_and_get_next(l, curr_turn, mem);
    ++curr_turn;
  }

  // for (const auto it : mem)
  // {
  //   std::cout << it.first << ": " << it.second << std::endl;
  // }

  // long target = 2020;
  long target = 30000000;
  while (curr_turn < target)
  {
    next = update_and_get_next(next, curr_turn, mem);
    ++curr_turn;
    // std::cout << next << std::endl;
  }

  std::cout << next << std::endl;
  return 0;
}
