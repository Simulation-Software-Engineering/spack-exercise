# Copyright 2013-2022 Lawrence Livermore National Security, LLC and other
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
    """Spack exercise created for the SSE Lecture WT22/23"""

    homepage = "https://simulation-software-engineering.github.io/homepage/"
    url = "https://github.com/Simulation-Software-Engineering/spack-exercise/archive/refs/tags/v0.1.0.tar.gz"
    maintainers = ["uygarkov"]

    version("0.1.0", sha256="7e9513c1ff32152a707d3004bc6be91e077002963f9945cd5b16c04fc010d8ba")
    version("0.2.0", sha256="c421df16911fd774aa072d7f6dd1746d0890918f7d0661202771382fbc9cf3db")
    version("0.3.0", sha256="53f926a12a5dfee9c6ae20f979a9da5b8b128178f150fc9ea4427ac06876588d")


    depends_on("boost@1.65.1", when="@0.2.0")
    depends_on("yaml-cpp@0.7.0", when="@0.3.0")