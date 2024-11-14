#pragma once

#include <string>
#include <common/types.h>

struct User {
  uint64 id;
  std::string name;
  int32 name;
};

struct Artile {
  uint64_t id;
  std::string title;
  std::string body;
  bool is_draft;
};
