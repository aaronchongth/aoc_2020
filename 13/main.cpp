#include <iostream>
#include <fstream>
#include <string>
#include <vector>
#include <cmath>
#include <limits>
#include <unordered_map>
#include <map>
#include <functional>
#include <algorithm>

long get_time_stamp(const std::string& stamp_str)
{
  return atol(stamp_str.c_str());
}

std::vector<long> get_bus_ids(std::string ids_str)
{
  std::vector<long> ids;
  std::string delimiter = ",";
  std::size_t pos = 0;
  while ((pos = ids_str.find(delimiter)) != std::string::npos)
  {
    std::string id_str = ids_str.substr(0, pos);
    ids_str.erase(0, pos + delimiter.length());

    long id = atol(id_str.c_str());
    if (id != 0)
      ids.push_back(id);
  }
  return ids;
}

std::unordered_map<long, long> get_stamp_and_ids(std::string ids_str)
{
  std::unordered_map<long, long> stamp_and_id;
  std::string delimiter = ",";
  std::size_t pos = 0;
  std::size_t curr_stamp = 0;
  while ((pos = ids_str.find(delimiter)) != std::string::npos)
  {
    std::string id_str = ids_str.substr(0, pos);
    ids_str.erase(0, pos + delimiter.length());

    long id = atol(id_str.c_str());
    if (id != 0)
    {
      stamp_and_id[curr_stamp] = id;
    }
    ++curr_stamp;
  }
  return stamp_and_id;
}

std::pair<long, long> get_earliest_bus_id(
  long stamp, const std::vector<long>& buses)
{
  long earliest_stamp = std::numeric_limits<long>::max();
  long earliest_id = 0;
  long smallest_diff = std::numeric_limits<long>::max();
  for (const long id : buses)
  {
    long multiplier = stamp / id;
    if (stamp % id > 0)
      multiplier += 1;

    long diff = multiplier * id - stamp;
    if (diff < smallest_diff)
    {
      smallest_diff = diff;
      earliest_id = id;
      earliest_stamp = id * multiplier;
    }
  }
  return std::make_pair(earliest_id, earliest_stamp);
}

bool is_relative_diff_right(long curr_stamp, long diff, long id)
{
  if ((curr_stamp + diff) % id == 0)
    return true;
  return false;
}

bool check(long multipler, long id,
  const std::vector<long>& ids,
  const std::vector<long>& relative_diffs)
{
  long curr_stamp = id * multipler;
  for (std::size_t i = 0; i < ids.size(); ++i)
  {
    if (!is_relative_diff_right(curr_stamp, relative_diffs[i], ids[i]))
      return false;
  }
  return true;
}

bool check_elems(
  const std::vector<long>& ids,
  const std::vector<long>& relative_diffs,
  long pattern_start)
{
  for (std::size_t i = 0; i < ids.size(); ++i)
  {
    // std::cout << "Checking: " << ids[i] << std::endl;
    if ((pattern_start + relative_diffs[i]) % ids[i] != 0)
      return false;
  }
  return true;
}

long earliest_pattern_stamp(
  const std::vector<long>& ids,
  const std::vector<long>& relative_diffs,
  long new_id)
{
  if (ids.empty())
  {
    return new_id;
  }

  std::vector<long> ids_less_one;
  std::vector<long> relative_diffs_less_one;
  for (std::size_t i = 0; i < ids.size() - 1; ++i)
  {
    ids_less_one.push_back(ids[i]);
    relative_diffs_less_one.push_back(relative_diffs[i]);
  }
  long less_one_extra = ids[ids.size() - 1];
  long prev_earliest_patt = earliest_pattern_stamp(
    ids_less_one, relative_diffs_less_one, less_one_extra);

  long curr_step_size = 0;
  for (std::size_t i = 0; i < ids.size(); ++i)
  {
    curr_step_size *= ids[i];
  }

  long curr_test = prev_earliest_patt;
  while (true)
  {
    if (check_elems(ids, relative_diffs, curr_test))
      return curr_test;
    curr_test += curr_step_size;
  }
}

int main()
{
  std::ifstream file("input.txt");
  // std::ifstream file("input_test.txt");
  // std::ifstream file("input_test2.txt");

  std::string line;
  std::getline(file, line);

  long stamp = get_time_stamp(line);

  std::getline(file, line);
  // auto bus_ids = get_bus_ids(line);

  // for (const auto i : bus_ids)
  //   std::cout << i << std::endl;

  // auto best = get_earliest_bus_id(stamp, bus_ids);
  // std::cout << "ID: " << best.first << std::endl;
  // std::cout << "Time difference: " << best.second - stamp << std::endl;
  // std::cout 
  //   << "Multiplied: " << best.first * (best.second - stamp) 
  //   << std::endl;

  auto stamp_and_id = get_stamp_and_ids(line);
  std::vector<long> id_order;
  std::unordered_map<long, long> tmp_id_to_stamp;
  for (auto it : stamp_and_id)
  {
    id_order.push_back(it.second);
    tmp_id_to_stamp[it.second] = it.first;

    // std::cout << it.second << ": " << it.first << std::endl;
  }

  std::sort(id_order.begin(), id_order.end(), std::less_equal<long>());
  long smallest_id = id_order[0];
  std::vector<long> ids;
  std::vector<long> relative_diffs;
  for (std::size_t i = 0; i < id_order.size(); ++i)
  {
    // std::cout << id_order[i] << std::endl;

    ids.push_back(id_order[i]);
    long diff = tmp_id_to_stamp[id_order[i]] - tmp_id_to_stamp[smallest_id];
    relative_diffs.push_back(diff);

    std::cout << ids[i] << ": " << diff << std::endl;
  }

  long first_occur = ids[0];
  long curr_step_size = ids[0];
  for (std::size_t i = 1; i < ids.size(); ++i)
  {
    std::size_t check_till = i;

    while (true)
    {
      bool ok = true;
      for (std::size_t j = 1; j <= check_till; ++j)
      {
        long adding_diff = first_occur + relative_diffs[j];
        long remainder = adding_diff % ids[j];

        // std::cout << "val: " << adding_diff << std::endl;
        // std::cout << "rem: " << remainder << std::endl;

        if (remainder != 0)
        {
          ok = false;
          break;
        }
      }

      if (!ok)
      {
        first_occur += curr_step_size;
        // std::cout << first_occur << std::endl;
      }
      else
      {
        break;
      }
    }

    curr_step_size *= ids[i];
  }

  std::cout << "first of the smallest: " << first_occur << std::endl;

  long lowest_diff = std::numeric_limits<long>::max();
  for (std::size_t i = 0; i < relative_diffs.size(); ++i)
  {
    if (relative_diffs[i] < lowest_diff)
      lowest_diff = relative_diffs[i];
  }

  long first_stamp_to_occur = first_occur + lowest_diff;
  std::cout << "first stamp of pattern: " << first_stamp_to_occur << std::endl;

  // long earliest_patt = earliest_pattern_stamp(
  //   ids,
  //   relative_diffs,
  //   id_order[id_order.size() - 1]);
  // std::cout << "earliest: " << earliest_patt << std::endl;

  // long min_id = std::numeric_limits<long>::max();
  // long min_stamp = std::numeric_limits<long>::max();
  // for (auto it : stamp_and_id)
  // {
  //   if (it.second < min_id)
  //   {
  //     max_id = it.second;
  //     max_stamp = it.first;
  //   }
  //   // std::cout << it.first << ": " << it.second << std::endl;
  // }

  // std::unordered_map<long, long> relative_diff_required;
  // for (auto it : stamp_and_id)
  // {
  //   long relative_diff = it.first - max_stamp;
  //   relative_diff_required[it.second] = relative_diff;
  //   id_order.push_back(it.second);
  //   std::cout << it.second << ": " << relative_diff << std::endl;
  // }

  // std::sort(id_order.begin(), id_order.end(), std::greater<long>());

  // std::vector<long> ids;
  // std::vector<long> relative_diffs;
  // for (std::size_t i = 1; i < id_order.size(); ++i)
  // {
  //   ids.push_back(id_order[i]);
  //   relative_diffs.push_back(relative_diff_required[id_order[i]]);
  // }

  // long at_least = 100000000000000;
  // long multiplier = 1;
  // while (true)
  // {
  //   if (multiplier % 100000000 == 0)
  //   {
  //     std::cout << "Still " << at_least - (multiplier * max_id) << " away..."
  //       << std::endl;
  //   }

  //   if (check(multiplier, max_id, ids, relative_diffs))
  //     break;
  //   ++multiplier;
  // }

  // std::cout << "Current multiplier: " << multiplier << std::endl;
  // std::cout << "Max ID stamp: " << multiplier * max_id << std::endl;
  // std::cout << "Earliest pattern stamp: " 
  //   << multiplier * max_id - max_stamp << std::endl;

  return 0;
}

// 3, 7
// 6
// 27
// 48

// 3, x, 7
// 45
