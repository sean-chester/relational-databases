cmake_minimum_required( VERSION 3.4 )
project( db-gen )

set(CMAKE_CXX_STANDARD 17)
set(CMAKE_CXX_STANDARD_REQUIRED ON)
set(CMAKE_CXX_EXTENSIONS OFF)


set( CMAKE_CXX_FLAGS
  "${CMAKE_CXX_FLAGS} \
    -fopenmp \
    -march=native \
    -mavx \
    -Wall \
    -g \
    -ansi \
    -Wextra \
    -Wdisabled-optimization \
    -Wunsafe-loop-optimizations \
    -Wpedantic \
    -Wshadow"
)
set( CMAKE_CXX_FLAGS_DEBUG
  "${CMAKE_CXX_FLAGS_DEBUG} \
    -Og"
) 
set( CMAKE_CXX_FLAGS_RELEASE
  "${CMAKE_CXX_FLAGS_RELEASE}"
)
set(
  basepath
    "${CMAKE_SOURCE_DIR}"
)

include_directories( "${basepath}/include" )

# Production code
add_subdirectory(src)

# Unit tests
option(BUILD_TESTS "Build all the unit tests" OFF)
if(BUILD_TESTS)
  add_subdirectory(test)
endif(BUILD_TESTS)
