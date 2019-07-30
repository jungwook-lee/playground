cmake_minimum_required(VERSION 3.5)
project(ctci_proj)

add_definitions(-std=c++11)
add_definitions(-Werror) # stop compile on warning

set(CMAKE_CXX_FLAGS "${CMAKE_CXX_FLAGS} -D_GLIBCXX_DEBUG")

add_executable(is_unique is_unique.cc)
add_executable(check_permutation check_permutation.cc)
