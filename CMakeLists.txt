cmake_minimum_required(VERSION "3.12")

project("spackexample" VERSION 0.3.0)

find_package(Boost 1.65.1 COMPONENTS filesystem)
find_package(yaml-cpp 0.7.0)

#message(${Boost_FOUND})
#message(${yaml-cpp_FOUND})

IF (${Boost_FOUND} AND ${yaml-cpp_FOUND})
  message("### Found Boost and Yaml! ###")
  add_library(spackexamplelib filesystem/filesystem.cpp flatset/flatset.cpp yamlParser/yamlParser.cpp)
  set_target_properties(spackexamplelib
    PROPERTIES
      PUBLIC_HEADER filesystem/filesystem.hpp
      PUBLIC_HEADER flatset/flatset.hpp
      PUBLIC_HEADER yamlParser/yamlParser.hpp
  )
  include_directories(${YAML_CPP_INCLUDE_DIR})
  add_executable(spackexample main.cpp)
  target_link_libraries(spackexample spackexamplelib)
  target_link_libraries(spackexamplelib Boost::filesystem yaml-cpp)
  target_compile_definitions(spackexample PRIVATE _BOOST="YES" _YAML="YES")

ELSEIF (${Boost_FOUND})
  message("### Found only Boost! ###")
  add_library(spackexamplelib filesystem/filesystem.cpp flatset/flatset.cpp)
  set_target_properties(spackexamplelib
    PROPERTIES
      PUBLIC_HEADER filesystem/filesystem.hpp
      PUBLIC_HEADER flatset/flatset.hpp
  )
  add_executable(spackexample main.cpp)
  target_link_libraries(spackexample spackexamplelib)
  target_link_libraries(spackexamplelib Boost::filesystem)
  target_compile_definitions(spackexample PRIVATE _BOOST="YES")

ELSEIF (${yaml-cpp_FOUND})
  message("### Found only Yaml! ###")
  add_library(spackexamplelib yamlParser/yamlParser.cpp)
  set_target_properties(spackexamplelib
    PROPERTIES
      PUBLIC_HEADER yamlParser/yamlParser.hpp
    )
  include_directories(${YAML_CPP_INCLUDE_DIR})
  add_executable(spackexample main.cpp)
  target_link_libraries(spackexample spackexamplelib)
  target_link_libraries(spackexamplelib yaml-cpp)
  target_compile_definitions(spackexample PRIVATE _YAML="YES")
ELSE()
  message("### Did not find any libs!")
  add_library(spackexamplelib main.cpp)
  add_executable(spackexample main.cpp)
  target_link_libraries(spackexample spackexamplelib)
  #target_link_libraries(spackexamplelib)
  target_compile_definitions(spackexample PRIVATE _NONE="YES")
ENDIF()

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
