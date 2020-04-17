cmake_minimum_required(VERSION 2.8 FATAL_ERROR)
set(CMAKE_CXX_STANDARD 11)
set(INCLUDE "${CMAKE_SOURCE_DIR}/libs")

project(viewer)

find_package(PCL 1.7.2 REQUIRED)

include_directories(${INCLUDE})
include_directories(${PCL_INCLUDE_DIRS})

link_directories(${PCL_LIBRARY_DIRS})
add_definitions(${PCL_DEFINITIONS})

add_executable(pclviewer pclviewer.cpp)

target_link_libraries(pclviewer ${PCL_LIBRARIES})
