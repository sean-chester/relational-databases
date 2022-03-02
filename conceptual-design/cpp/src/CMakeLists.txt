add_subdirectory( converter )

add_executable(
  db-gen
    main.cpp
)

set_target_properties(
  db-gen
    PROPERTIES
      ARCHIVE_OUTPUT_DIRECTORY "../lib/"
      LIBRARY_OUTPUT_DIRECTORY "../lib/"
      RUNTIME_OUTPUT_DIRECTORY "../"
)

target_link_libraries(
  db-gen
    ${Boost_LIBRARIES}
    converter
)
