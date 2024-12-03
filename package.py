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
    """FIXME: Put a proper description of your package here."""

    # FIXME: Add a proper url for your package's homepage here.
    homepage = "https://simulation-software-engineering.github.io/homepage/"
    url = "https://github.com/Simulation-Software-Engineering/spack-exercise/archive/refs/tags/v0.3.0.tar.gz"
    git = "https://github.com/Simulation-Software-Engineering/spack-exercise.git"

    # FIXME: Add a list of GitHub accounts to
    # notify when the package is updated.
    maintainers("mgemaakbar")

    # FIXME: Add the SPDX identifier of the project's license below.
    # See https://spdx.org/licenses/ for a list. Upon manually verifying
    # the license, set checked_by to your Github username.
    license("MIT", checked_by="mgemaakbar")

    version("main", git = git, branch="main")
    version("0.1.0", sha256='cac78e641cb703e3fe51956f91fe8347ac52f74ef037d8eadae5777c65a19a00')
    version("0.2.0", sha256='3dd6b4cc0f7aff179d8e290bc3879056237ae372738a4bd7222f6450fbcdfc77')
    version("0.3.0", sha256='e54a4c037941d85a22fb3e6e73195df8448cf69a96aa44ef374ac518344812f0')

    depends_on("cxx", type="build")

    # FIXME: Add dependencies if required.
    variant('boost', default=True, description='boost dependency')
    variant('yaml-cpp', default=True, description='yaml-cpp dependency')
    depends_on("boost@1.65.1:",when="@0.2.0:")
    depends_on("yaml-cpp@0.7.0:",when="@0.3.0:")
