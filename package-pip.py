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
#     spack install py-diffusion2d
#
# You can edit this file again by typing:
#
#     spack edit py-diffusion2d
#
# See the Spack documentation for more information on packaging.
# ----------------------------------------------------------------------------

from spack.package import *


class PyDiffusion2d(PythonPackage):
    """This package solves the diffusion equation in 2D over a square domain which is at a certain temperature"""

    homepage = "https://simulation-software-engineering.github.io/homepage/"

    url = "https://github.com/legendofa/diffusion2D/archive/refs/tags/v0.0.7.tar.gz"

    maintainers("legendofa")

    license("CC-BY-4.0", checked_by="legendofa")

    version("0.0.7", sha256="ec6cf0f809caf592342e228b81b32465679ccd1ea040b2653d89c4630786082e")

    depends_on("python@3.6:", type=("build", "run"))
    depends_on("py-setuptools", type="build")
    depends_on("py-versioneer", type="build")
