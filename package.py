# Copyright 2013-2024 Lawrence Livermore National Security, LLC and other
# Spack Project Developers. See the top-level COPYRIGHT file for details.
#
# SPDX-License-Identifier: (Apache-2.0 OR MIT)

# ----------------------------------------------------------------------------
#     spack install spack-exercise
#
# You can edit this file again by typing:
#
#     spack edit spack-exercise
#
# See the Spack documentation for more information on packaging.
# ----------------------------------------------------------------------------

from spack.package import *


class SpackExercise(CMakePackage):
    # SPACK Exercise for the SSE Course

    homepage = "https://simulation-software-engineering.github.io/homepage/"
    url = "https://github.com/Simulation-Software-Engineering/spack-exercise/archive/refs/tags/v0.3.0.tar.gz"
    git = "https://github.com/Simulation-Software-Engineering/spack-exercise.git"

    maintainers("SyedMustafaAhmad")

    license("MIT", checked_by="SyedMustafaAhmad")

    version("0.3.0", sha256="e54a4c037941d85a22fb3e6e73195df8448cf69a96aa44ef374ac518344812f0")
    version("0.2.0", sha256="3dd6b4cc0f7aff179d8e290bc3879056237ae372738a4bd7222f6450fbcdfc77")
    version("0.1.0", sha256="cac78e641cb703e3fe51956f91fe8347ac52f74ef037d8eadae5777c65a19a00")
    
    depends_on("cxx", type="build")
    depends_on("boost", when="spack-exercise@0.2.0:")
    depends_on("yaml-cpp", when="spack-exercise@0.3.0:")

    def cmake_args(self):
        args = []
        return args
