#include <iostream>

// Conditionally include Boost and YAML-CPP based on CMake options
#ifdef USE_BOOST
#include "flatset/flatset.hpp"
#include "filesystem/filesystem.hpp"
#endif

#ifdef USE_YAML_CPP
#include "yamlParser/yamlParser.hpp"
#endif

int main(int argc, char *argv[])
{
  std::cout << "Let's fight with CMake, Docker, and some dependencies!" << std::endl << std::endl;

  std::cout << "Modify a flat set using boost container" << std::endl;
  modifyAndPrintSets();
  std::cout << std::endl;

  std::cout << "Inspect the current directory using boost filesystem" << std::endl;
  inspectDirectory();
  std::cout << std::endl;

  if ( argc == 2 )
  {
    const std::string yamlFile( argv[1] );
    std::cout << "Parse some yaml file with yaml-cpp" << std::endl;
    std::cout << "  " << yamlFile << std::endl;
    parseConfig( yamlFile );
  }

  return 0;
}

