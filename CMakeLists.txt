cmake_minimum_required(3.10)
project(reflect)

set(CMAKE_CXX_STANDARD 17)

find_package(Python3 REQURED)

add_custom_command(
  OUTPUT ${CMAKE_CURRENT_SOURCE_DIR}/gen/reflect_gen.h
  COMMAND Python3::Interpreter ${CMAKE_CURRENT_SOURCE_DIR}/src/generate_meta.py
  COMMENT "Generating meta"
  VERBATIM
)

set(SOURCES src/main.cpp gen/reflect_gen.h)
add_executable(${PROJECT_NAME} ${SOURCES})

add_dependencies(${PROJECT_NAME} ${CMAKE_CURRENT_SOURCE_DIR}/gen/reflect_gen.h)

include(${CMAKE_CURRENT_SOURCE_DIR}/gen)
include(${CMAKE_CURRENT_SOURCE_DIR}/src)
