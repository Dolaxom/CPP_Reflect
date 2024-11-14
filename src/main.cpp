#include <iostream>
#include <variant>
#include "reflect_gen.h"


std::string GetFromAny(std::any value, std::string type) {
  if (type == "int32") {
    return std::to_string(std::any_cast<int32>(value));
  } else if (type == "uint64") {
    return std::to_string(std::any_cast<uint64>(value)); 
  }
  else if (type == "std::string") {
    return std::any_cast<std::string>(value); 
  }
}

int main()
{
  User user {0, "Bob", 20};

  auto meta = GetMeta<decltype(user)>(user);

  for (size_t i = 0; i < meta.data.size(); ++i) {
    // std::visit([](const auto &val) {std::cout << val << std::endl;}, meta.data[i]);
    std::cout << "{" << meta.fields[i].first << ", " << meta.fields[i].second << "} = " << GetFromAny(meta.data[i], meta.fields[i].first) << std::endl;
  }
}