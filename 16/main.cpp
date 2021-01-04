#include "../utils.hpp"

class Field
{
public:

  Field(const std::string& field_line)
  {
    auto name_split = split_strings(field_line, ": ");
    name = name_split[0];

    auto limit_splits = split_strings(name_split[1], " or ");
    for (const auto& l : limit_splits)
    {
      auto num_splits = split_strings(l, "-");
      limits.push_back(
        std::make_pair(
          std::atol(num_splits[0].c_str()),
          std::atol(num_splits[1].c_str())));
    }
  };

  bool is_within_limit(long num) const
  {
    for (const auto& l : limits)
    {
      if (num >= l.first && num <= l.second)
        return true;
    }
    return false;
  }

  std::string name;
  std::vector<std::pair<long, long>> limits;
};

class Ticket
{
public:

  Ticket(const std::string& ticket_line)
  {
    ticket_str = ticket_line;
    auto num_splits = split_strings(ticket_line, ",");
    for (const auto& n : num_splits)
    {
      field_nums.push_back(std::atol(n.c_str()));
    }
  }

  std::string ticket_str;
  std::vector<long> field_nums;
};

bool check_fields(
  const std::vector<Field>& fields,
  long num)
{
  for (const auto& f : fields)
  {
    if (f.is_within_limit(num))
      return true;
  }
  return false;
}

long ticket_scanning_error_rate(
  const std::vector<Field>& fields,
  const std::vector<Ticket>& nearby_tickets)
{
  long error = 0;
  for (const auto& t : nearby_tickets)
  {
    for (long l : t.field_nums)
    {
      bool valid = check_fields(fields, l);
      if (!valid)
        error += l;
    }
  }
  return error;
}

bool check_ticket(
  const std::vector<Field>& fields,
  const Ticket& ticket)
{
  for (const long l : ticket.field_nums)
  {
    if (!check_fields(fields, l))
      return false;
  }
  return true;
}

std::vector<Ticket> get_valid_tickets(
  const std::vector<Field>& fields,
  const std::vector<Ticket>& nearby_tickets)
{
  std::vector<Ticket> valid_tickets = {};
  for (const auto& t : nearby_tickets)
  {
    if (check_ticket(fields, t))
      valid_tickets.push_back(t);
  }
  return valid_tickets;
}

bool is_only_candidate(
  const std::unordered_set<long>& candidates)
{
  if (candidates.size() == 1)
    return true;
  return false;
}

void initialize_candidates(
  const Ticket& first_ticket,
  const std::vector<Field>& fields,
  std::vector<std::unordered_set<std::size_t>>& candidates)
{
  candidates = {};
  candidates.resize(first_ticket.field_nums.size());
  for (std::size_t i = 0; i < candidates.size(); ++i)
  {
    std::unordered_set<std::size_t> field_candidates;
    for (std::size_t j = 0; j < fields.size(); ++j)
    {
      if (fields[j].is_within_limit(first_ticket.field_nums[i]))
        field_candidates.insert(j);
    }
    candidates[i] = field_candidates;
  }
}

void clean_up_candidates_except(
  std::size_t except_index,
  std::vector<std::unordered_set<std::size_t>>& all_candidates)
{
  auto except_set = all_candidates[except_index];
  std::size_t to_delete = *except_set.begin();
  for (std::size_t i = 0; i < all_candidates.size(); ++i)
  {
    if (i == except_index)
      continue;

    auto& curr_set = all_candidates[i];
    auto it = curr_set.find(to_delete);
    if (it != curr_set.end())
      curr_set.erase(it);
  }
}

void update_all_candidates(
  const Ticket& new_ticket,
  const std::vector<Field>& fields,
  std::vector<std::unordered_set<std::size_t>>& all_candidates)
{
  for (std::size_t i = 0; i < all_candidates.size(); ++i)
  {
    long val = new_ticket.field_nums[i];
    auto& field_candidate_set = all_candidates[i];

    std::vector<std::size_t> candidates_to_remove = {};
    for (auto it = field_candidate_set.begin();
      it != field_candidate_set.end();
      ++it)
    {
      std::size_t field_index = *it;
      if (!fields[field_index].is_within_limit(val))
        candidates_to_remove.push_back(field_index);
    }

    for (std::size_t c : candidates_to_remove)
    {
      auto it = field_candidate_set.find(c);
      if (it != field_candidate_set.end())
        field_candidate_set.erase(it);
    }

    if (field_candidate_set.empty())
      std::cout << "FUCK" << std::endl;

    if (field_candidate_set.size() == 1)
    {
      clean_up_candidates_except(*field_candidate_set.begin(), all_candidates);
    }
  }
}

// void clean_up_all_candidates(
//   std::vector<std::unordered_set<long>>& all_candidates,
//   std::size_t index)
// {
//   std::size_t num_candidates = all_candidates[index].size();
//   if (num_candidates != 1)
//     return;

//   long single_candidate = *all_candidates[index].begin();
//   for (std::size_t i = 0; i < all_candidates.size(); ++i)
//   {
//     if (i == index)
//       continue;
//     auto& index_candidates = all_candidates[i];
//     auto it = index_candidates.find(single_candidate);
//     if (it == index_candidates.end())
//       continue;
//     index_candidates.erase(it);
//   }
// }

// void remove_candidates_except(
//   std::vector<std::unordered_set<long>>& all_candidates,
//   std::size_t except_index)
// {
  
// }

// void clean_up_candidates(
//   std::vector<std::unordered_set<long>>& all_candidates)
// {

// }

int main()
{
  // std::ifstream file("input.txt");
  // std::ifstream file("input_test.txt");
  std::ifstream file("input_test2.txt");

  std::vector<Field> fields = {};
  bool fields_done = false;
  Ticket* my_ticket = nullptr;
  std::vector<Ticket> nearby_tickets = {};

  std::string str;
  while (std::getline(file, str))
  {
    if (!fields_done)
    {
      if (str == "")
      {
        fields_done = true;
        continue;
      }
      fields.push_back(Field(str));
    }

    if (str == "" ||
      str == "your ticket:" ||
      str == "nearby tickets:")
      continue;

    if (fields_done && !my_ticket)
    {
      my_ticket = new Ticket(str);
      continue;
    }

    if (fields_done && my_ticket)
    {
      nearby_tickets.push_back(Ticket(str));
    }
  }

  // get error
  // long error_rate = ticket_scanning_error_rate(fields, nearby_tickets);
  // std::cout << error_rate << std::endl;

  // get valid tickets
  auto valid_tickets = get_valid_tickets(fields, nearby_tickets);
  // std::cout << valid_tickets.size() << std::endl;

  // initialize candidates
  std::vector<std::unordered_set<std::size_t>> all_candidates = {};
  initialize_candidates(
    nearby_tickets[0],
    fields,
    all_candidates);

  for (std::size_t i = 1; i < valid_tickets.size(); ++i)
  {
    update_all_candidates(
      valid_tickets[i],
      fields,
      all_candidates);
  }

  for (const auto& c : all_candidates)
  {
    // std::cout << c.size() << std::endl;
    for (auto it = c.begin(); it != c.end(); ++it)
      std::cout << *it << " ";
    std::cout << std::endl;
  }

  // std::cout << nearby_tickets.size() << std::endl;
  // for (const auto& t : nearby_tickets)
  // {
  //   std::cout << t.ticket_str << std::endl;
  // }

  delete my_ticket;
  return 0;
}
