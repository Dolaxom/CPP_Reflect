#pragma once

#include <string>
#include <common/types.hpp>

struct User {
  uint64 id;
  std::string name;
  int32 age;
};

struct Article {
  uint64 id;
  std::string title;
  std::string body;
  bool is_draft;
};
