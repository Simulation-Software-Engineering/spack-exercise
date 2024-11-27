#include "yamlParser.hpp"

#include <iostream>

#ifdef WITH_YAML

#include "yaml-cpp/yaml.h"

void parseConfig(const std::string yamlFile){
  YAML::Node config = YAML::LoadFile(yamlFile);
  std::cout << "Version: " << config["version"].as<std::string>() << std::endl;
}

#else

void parseConfig(const std::string yamlFile) {
  std::cout << "Yaml-Parser was disabled at build time. Build package with '+yaml' to enable functionality" << std::endl;
}

#endif
