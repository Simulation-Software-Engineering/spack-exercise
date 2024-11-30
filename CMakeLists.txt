cmake_minimum_required(VERSION "3.12")

project("spackexample" VERSION 0.3.0)

option(ENABLE_BOOST "Enable use of boost." OFF)
option(ENABLE_YAML "Enable use of yaml-cpp." OFF)

set(SOURCES)

if(ENABLE_BOOST)
  find_package(Boost
    1.65.1
    REQUIRED
    filesystem
    )
    list(APPEND SOURCES filesystem/filesystem.cpp flatset/flatset.cpp)
endif()

if(ENABLE_YAML)
  find_package(yaml-cpp
    0.7.0
    REQUIRED
    )
    list(APPEND SOURCES yamlParser/yamlParser.cpp)
    include_directories(${YAML_CPP_INCLUDE_DIR})
endif()

if(SOURCES)
  add_library(spackexamplelib ${SOURCES})
  if(ENABLE_BOOST)
    set_target_properties(spackexamplelib
    PROPERTIES
      PUBLIC_HEADER filesystem/filesystem.hpp
      PUBLIC_HEADER flatset/flatset.hpp
    )
  endif()
  if(ENABLE_YAML)
  set_target_properties(spackexamplelib
    PROPERTIES
      PUBLIC_HEADER yamlParser/yamlParser.hpp
    )
  endif()
endif()



add_executable(spackexample main.cpp)

if(SOURCES)
target_link_libraries(spackexample spackexamplelib)
  if(ENABLE_BOOST)
    target_link_libraries(spackexample Boost::filesystem)
    target_compile_definitions(spackexample PRIVATE BOOST)
  endif()
  if(ENABLE_YAML)
    target_link_libraries(spackexample yaml-cpp)
    target_compile_definitions(spackexample PRIVATE YAML)
  endif()
endif()


if(SOURCES)
  target_include_directories(spackexamplelib
      PRIVATE
          ${CMAKE_CURRENT_SOURCE_DIR}/spackexamplelib
      PUBLIC
          $<BUILD_INTERFACE:${CMAKE_CURRENT_SOURCE_DIR}/spackexamplelib>
          $<INSTALL_INTERFACE:${CMAKE_INSTALL_INCLUDEDIR}/spackexamplelib>
    )
endif()

# Create install targets
include(GNUInstallDirs)
if(SOURCES)
  install(TARGETS spackexample spackexamplelib
    LIBRARY DESTINATION ${CMAKE_INSTALL_LIBDIR}
    ARCHIVE DESTINATION ${CMAKE_INSTALL_LIBDIR}
    RUNTIME DESTINATION ${CMAKE_INSTALL_BINDIR}
    PUBLIC_HEADER DESTINATION ${CMAKE_INSTALL_INCLUDEDIR}/spackexample
    INCLUDES DESTINATION ${CMAKE_INSTALL_INCLUDEDIR}/spackexample
    )
else()
  install(TARGETS spackexample
    LIBRARY DESTINATION ${CMAKE_INSTALL_LIBDIR}
    ARCHIVE DESTINATION ${CMAKE_INSTALL_LIBDIR}
    RUNTIME DESTINATION ${CMAKE_INSTALL_BINDIR}
    PUBLIC_HEADER DESTINATION ${CMAKE_INSTALL_INCLUDEDIR}/spackexample
    INCLUDES DESTINATION ${CMAKE_INSTALL_INCLUDEDIR}/spackexample
    )
endif()
