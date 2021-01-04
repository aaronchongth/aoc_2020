#ifndef UTILS_HPP
#define UTILS_HPP

#include <map>
#include <array>
#include <string>
#include <vector>
#include <fstream>
#include <iostream>
#include <optional>
#include <unordered_map>
#include <unordered_set>

std::vector<std::string> split_strings(
  std::string full_str,
  std::string delimiter)
{
  std::vector<std::string> strs;
  std::size_t pos = 0;
  while ((pos = full_str.find(delimiter)) != std::string::npos)
  {
    strs.push_back(full_str.substr(0, pos));
    full_str.erase(0, pos + delimiter.length());
  }
  strs.push_back(full_str);
  return strs;
}

#endif // UTILS_HPP
