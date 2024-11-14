cmake_minimum_required(VERSION 3.16)
project(
  reflect
  VERSION 1.0
  LANGUAGES CXX)

set(CMAKE_CXX_STANDARD 20)
set(CMAKE_CXX_STANDARD_REQUIRED ON)

# find_package(Python3 REQURED)

# add_custom_command(
#   OUTPUT ${CMAKE_CURRENT_SOURCE_DIR}/gen/reflect_gen.h
#   COMMAND Python3::Interpreter ${CMAKE_CURRENT_SOURCE_DIR}/src/generate_meta.py
#   COMMENT "Generating meta"
#   VERBATIM
# )

set(SOURCES src/main.cpp)
add_executable(${PROJECT_NAME} ${SOURCES})

# add_dependencies(${PROJECT_NAME} ${CMAKE_CURRENT_SOURCE_DIR}/gen/reflect_gen.h)

include_directories(src)
