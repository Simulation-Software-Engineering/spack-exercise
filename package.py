# Copyright Spack Project Developers. See COPYRIGHT file for details.
#
# SPDX-License-Identifier: (Apache-2.0 OR MIT)

from spack_repo.builtin.build_systems.cmake import CMakePackage

from spack.package import *


class SpackExercise(CMakePackage):
    """Spack exercise"""

    homepage = "https://simulation-software-engineering.github.io/homepage/"
    url = "https://github.com/Simulation-Software-Engineering/spack-exercise/archive/refs/tags/v0.3.0.tar.gz"
    git = "https://github.com/Simulation-Software-Engineering/spack-exercise"

    maintainers("madebyTimo")

    license("MIT", checked_by="madebyTimo")

    version("main", branch="main")
    version("0.3.0", sha256="94a017921b35be2a49580b51f1a5689f211f92aece4861f5993663c067e8483c")
    version("0.2.0", sha256="78cd3a5df770dd34dd2dd8a092e9c07214079a192ff7feefc479989f8d078fcf")
    version("0.1.0", sha256="d336ea7954fc019f0d2cf1b6cbcfce7cb8b4d68fb3c103766fa9c950054a26ae")

    depends_on("cxx", type="build")
    depends_on("c", type="build")
    depends_on("yaml-cpp")
    # depends_on("yaml-cpp", when="@0.3.0:")
