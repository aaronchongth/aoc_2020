#include <iostream>
#include <fstream>
#include <string>
#include <vector>
#include <cmath>

class Ferry
{
public:

  enum class Instructions : uint8_t
  {
    North,
    South,
    East,
    West,
    Left,
    Right,
    Forward
  };

  static std::pair<Instructions, long> split_instructions(
    const std::string& line)
  {
    std::size_t mag_len = line.size() - 1;
    return std::make_pair(
      str_to_instruction(line.substr(0, 1)),
      atoi(line.substr(1, mag_len).c_str()));
  }

  static Instructions str_to_instruction(const std::string& str)
  {
    if (str == "N")
      return Instructions::North;
    else if (str == "S")
      return Instructions::South;
    else if (str == "E")
      return Instructions::East;
    else if (str == "W")
      return Instructions::West;
    else if (str == "F")
      return Instructions::Forward;
    else if (str == "L")
      return Instructions::Left;
    else
      return Instructions::Right;
  }

  Ferry(long wp_east, long wp_north)
  : wp_x(wp_east),
    wp_y(wp_north)
  {}

  void move(const std::pair<Instructions, long>& instruction)
  {
    switch (instruction.first)
    {
    case Instructions::Forward:
      forward(instruction.second);
      break;
    case Instructions::Left:
      rotate_waypoint(instruction.second);
      break;
    case Instructions::Right:
      rotate_waypoint(-instruction.second);
      break;
    case Instructions::North:
    case Instructions::South:
    case Instructions::East:
    case Instructions::West:
      translate_waypoint(instruction.first, instruction.second);
    default:
      break;
    }
  }

  void print_location() const
  {
    std::cout << "x: " << x << std::endl;
    std::cout << "y: " << y << std::endl;
  }

  std::pair<int, int> location() const
  {
    return std::make_pair(x, y);
  }

  int manhattan_dist() const
  {
    return abs(x) + abs(y);
  }

private:

  void forward(int magnitude)
  {
    x += magnitude * wp_x;
    y += magnitude * wp_y;
  }

  void rotate_waypoint(long magnitude)
  {
    long new_wp_x =
      round(cos(magnitude * M_PI / 180) * wp_x 
      - sin(magnitude * M_PI / 180) * wp_y);
    long new_wp_y =
      round(sin(magnitude * M_PI / 180) * wp_x
      + cos(magnitude * M_PI / 180) * wp_y);
    wp_x = new_wp_x;
    wp_y = new_wp_y;
  }

  void translate_waypoint(Instructions direction, long magnitude)
  {
    switch (direction)
    {
    case Instructions::North:
      wp_y += magnitude;
      break;
    case Instructions::South:
      wp_y -= magnitude;
      break;
    case Instructions::East:
      wp_x += magnitude;
      break;
    case Instructions::West:
      wp_x -= magnitude;
      break;
    default:
      std::cout << "Passed wrong instructions to translate function"
        << std::endl;
      break;
    }
  }

  long wp_x;
  long wp_y;

  long x;
  long y;
};

int main()
{
  std::ifstream file("input.txt");
  // std::ifstream file("input_test.txt");
  // std::ifstream file("input_test2.txt");

  // Ferry ferry;
  Ferry ferry(10, 1);
  std::string curr_instruction;
  while (std::getline(file, curr_instruction))
  {
    auto instruction = Ferry::split_instructions(curr_instruction);
    ferry.move(instruction);
  }
  ferry.print_location();
  std::cout << "Manhattan dist: " << ferry.manhattan_dist() << std::endl;

  return 0;
}
