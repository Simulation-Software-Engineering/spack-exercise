#include <iostream>

int main(int argc, char *argv[]) {
  std::cout << "Let's fight with CMake, Docker, and some dependencies!" << std::endl << std::endl;

  // Debug
  #ifdef _NONE
   std::cout << "DEBUG: Not using any libs" << std::endl;
  #endif
  #ifdef _BOOST
   std::cout << "DEBUG: Using Boost" << std::endl;
  #endif
  #ifdef _YAML
   std::cout << "DEBUG: Using YAML" << std::endl;
  #endif

  #ifdef _BOOST
    #include "flatset/flatset.hpp"
    #include "filesystem/filesystem.hpp"
    std::cout << "Modify a flat set using boost container" << std::endl;
    modifyAndPrintSets();
    std::cout << std::endl;
    std::cout << "Inspect the current directory using boost filesystem" << std::endl;
    inspectDirectory();
    std::cout << std::endl;
  #endif

  #ifdef _YAML
    #include "yamlParser/yamlParser.hpp"
    if ( argc == 2 ) {
      const std::string yamlFile( argv[1] );
      std::cout << "Parse some yaml file with yaml-cpp" << std::endl;
      std::cout << "  " << yamlFile << std::endl;
      parseConfig( yamlFile );
    }
  #endif

  return 0;
}
