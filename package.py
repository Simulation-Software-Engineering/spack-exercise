# Copyright 2013-2022 Lawrence Livermore National Security, LLC and other
# Spack Project Developers. See the top-level COPYRIGHT file for details.
#
# SPDX-License-Identifier: (Apache-2.0 OR MIT)

from spack.package import *

class SpackExercise(CMakePackage):
    """This is the spack-exercise package. Its use is to train students in the art of spack packaging."""

    # Add a proper url for your package's homepage here.
    homepage = "https://simulation-software-engineering.github.io/homepage/"
    url = "https://github.com/Simulation-Software-Engineering/spack-exercise/archive/refs/tags/v0.1.0.tar.gz"

    # Add a list of GitHub accounts to
    # notify when the package is updated.
    maintainers = ["Till223"]

    version("0.3.0", sha256="53f926a12a5dfee9c6ae20f979a9da5b8b128178f150fc9ea4427ac06876588d")
    version("0.2.0", sha256="c421df16911fd774aa072d7f6dd1746d0890918f7d0661202771382fbc9cf3db")
    version("0.1.0", sha256="7e9513c1ff32152a707d3004bc6be91e077002963f9945cd5b16c04fc010d8ba")

    # Add dependencies if required.
    depends_on("boost@1.65.1:", when="@0.2.0:")
    depends_on("yaml-cpp@0.7.0:", when="@0.3.0:")
