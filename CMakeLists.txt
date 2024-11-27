cmake_minimum_required(VERSION "3.12")

project("spackexample" VERSION 0.3.0)

# Set options for optional dependencies
option(USE_BOOST "Enable Boost support" ON)
option(USE_YAML_CPP "Enable YAML-CPP support" ON)

# Find Boost if enabled
if(USE_BOOST)
    find_package(Boost 1.65.1 REQUIRED filesystem)
    if(Boost_FOUND)
        message(STATUS "Boost found: ${Boost_INCLUDE_DIRS}")
    else()
        message(WARNING "Boost not found, even though USE_BOOST is ON")
    endif()
endif()

# Find yaml-cpp if enabled
if(USE_YAML_CPP)
    find_package(yaml-cpp 0.7.0 REQUIRED)
    if(YAML_CPP_FOUND)
        message(STATUS "yaml-cpp found: ${YAML_CPP_INCLUDE_DIR}")
    else()
        message(WARNING "yaml-cpp not found, even though USE_YAML_CPP is ON")
    endif()
endif()

# Add the library
add_library(spackexamplelib
    filesystem/filesystem.cpp
    flatset/flatset.cpp
    yamlParser/yamlParser.cpp
)

# Set the public header files
set_target_properties(spackexamplelib
  PROPERTIES
    PUBLIC_HEADER "filesystem/filesystem.hpp;flatset/flatset.hpp;yamlParser/yamlParser.hpp"
)

# Add the executable
add_executable(spackexample main.cpp)

# Link libraries
target_link_libraries(spackexample spackexamplelib)

# Conditionally link Boost and yaml-cpp if enabled
if(USE_BOOST AND Boost_FOUND)
    target_link_libraries(spackexamplelib Boost::filesystem)
endif()

if(USE_YAML_CPP AND YAML_CPP_FOUND)
    target_link_libraries(spackexamplelib yaml-cpp)
    target_include_directories(spackexamplelib PRIVATE ${YAML_CPP_INCLUDE_DIR})
endif()

# Include directories for spackexamplelib
target_include_directories(spackexamplelib
    PRIVATE
        ${CMAKE_CURRENT_SOURCE_DIR}/spackexamplelib
    PUBLIC
        $<BUILD_INTERFACE:${CMAKE_CURRENT_SOURCE_DIR}/spackexamplelib>
        $<INSTALL_INTERFACE:${CMAKE_INSTALL_INCLUDEDIR}/spackexamplelib>
)

# Create install targets
include(GNUInstallDirs)
install(TARGETS spackexample spackexamplelib
  LIBRARY DESTINATION ${CMAKE_INSTALL_LIBDIR}
  ARCHIVE DESTINATION ${CMAKE_INSTALL_LIBDIR}
  RUNTIME DESTINATION ${CMAKE_INSTALL_BINDIR}
  PUBLIC_HEADER DESTINATION ${CMAKE_INSTALL_INCLUDEDIR}/spackexample
  INCLUDES DESTINATION ${CMAKE_INSTALL_INCLUDEDIR}/spackexample
)
