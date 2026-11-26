# Copyright Spack Project Developers. See COPYRIGHT file for details.
#
# SPDX-License-Identifier: (Apache-2.0 OR MIT)

from spack_repo.builtin.build_systems.cmake import CMakePackage
from spack.package import *


class SpackExercise(CMakePackage):
    """A C++ example demonstrating software packaging and
    dependency management with Spack and CMake."""

    homepage = "https://simulation-software-engineering.github.io/homepage/"
    url = "https://github.com/Simulation-Software-Engineering/spack-exercise/archive/refs/tags/v0.1.0.tar.gz"

    maintainers("hazalkntr")

    license("MIT", checked_by="hazalkntr")

    version("0.3.0", sha256="94a017921b35be2a49580b51f1a5689f211f92aece4861f5993663c067e8483c")
    version("0.2.0", sha256="78cd3a5df770dd34dd2dd8a092e9c07214079a192ff7feefc479989f8d078fcf")
    version("0.1.0", sha256="d336ea7954fc019f0d2cf1b6cbcfce7cb8b4d68fb3c103766fa9c950054a26ae")

    depends_on("c", type="build")
    depends_on("cxx", type="build")
    depends_on("cmake@3.12:", type="build")

    def patch(self):
        # Release 0.1.0 incorrectly compiles sources requiring
        # Boost and yaml-cpp despite disabling these features.
        if self.spec.satisfies("@=0.1.0"):
            with open("spackexamplelib_stub.cpp", "w") as f:
                f.write("void spackexamplelib_stub() {}\n")

            filter_file(
                "add_library(spackexamplelib filesystem/filesystem.cpp flatset/flatset.cpp yamlParser/yamlParser.cpp)",
                "add_library(spackexamplelib spackexamplelib_stub.cpp)",
                "CMakeLists.txt",
                string=True,
            )

    depends_on("boost@1.65.1:+filesystem", when="@0.2.0:")
    depends_on("yaml-cpp@=0.7.0", when="@=0.3.0")
