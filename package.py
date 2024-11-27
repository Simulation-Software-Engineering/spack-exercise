# Copyright 2013-2024 Lawrence Livermore National Security, LLC and other
# Spack Project Developers. See the top-level COPYRIGHT file for details.
#
# SPDX-License-Identifier: (Apache-2.0 OR MIT)

# ----------------------------------------------------------------------------
# If you submit this package back to Spack as a pull request,
# please first remove this boilerplate and all FIXME comments.
#
# This is a template package file for Spack.  We've put "FIXME"
# next to all the things you'll want to change. Once you've handled
# them, you can save this file and test your package like this:
#
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
    """This is the example spack packaging exercise of the SSE course."""

    homepage = "https://simulation-software-engineering.github.io/homepage/"
    url = "https://github.com/Simulation-Software-Engineering/spack-exercise/archive/refs/tags/v0.3.0.tar.gz"
    git = "https://github.com/legendofa/spack-exercise"
    maintainers("legendofa")
    
    license("MIT", checked_by="legendofa")

    version("main", branch="main")
    version("0.3.0", sha256="e54a4c037941d85a22fb3e6e73195df8448cf69a96aa44ef374ac518344812f0")
    version("0.2.0", sha256="3dd6b4cc0f7aff179d8e290bc3879056237ae372738a4bd7222f6450fbcdfc77")
    version("0.1.0", sha256="cac78e641cb703e3fe51956f91fe8347ac52f74ef037d8eadae5777c65a19a00")

    variant("boost", default=True, description="Enable Boost support")
    variant("yaml-cpp", default=True, description="Enable YAML-CPP support")

    depends_on("cxx", type="build")
    depends_on("yaml-cpp@0.7:", when="@0.3.0,main+yaml-cpp")
    depends_on("boost@1.65.1:", when="@0.2.0:0.3.0,main+boost")

    def cmake_args(self):
        args = super(SpackExercise, self).cmake_args()

        # Add CMake options based on Spack variants
        if "+boost" in self.spec:
            args.append("-DUSE_BOOST=ON")
        else:
            args.append("-DUSE_BOOST=OFF")

        if "+yaml-cpp" in self.spec:
            args.append("-DUSE_YAML_CPP=ON")
        else:
            args.append("-DUSE_YAML_CPP=OFF")

        return args
