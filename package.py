# Copyright 2013-2021 Lawrence Livermore National Security, LLC and other
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

from spack import *


class SpackExercise(CMakePackage):
    """Spack Exercise of Simulation software engineering course"""

    # Add a proper url for your package's homepage here.
    homepage = "https://simulation-software-engineering.github.io/homepage/"
    url      = "https://github.com/Simulation-Software-Engineering/spack-exercise/archive/refs/tags/v0.3.0.tar.gz"
    # Add a list of GitHub accounts to
    # notify when the package is updated.
    maintainers = ['mohamad-altaweel']

    # all versions provided
    version('0.3.0', sha256='c0c137ab5bf52a36c6c9a000ce32a607dc6f98f808a734ff6d729b4ca01bec9b')
    version('0.2.0', sha256='2d309f0dcf7343d88ceaec7a3daa6cb556603777ed35b90d741671d4dc04ef5d')
    version('0.1.0', sha256='afedc68249587779f1ade08760823ed17cbff62a4cf3d1eaa88d2fe609854470')

    # Add dependencies if required.
    depends_on('boost@1.65.1:', when='@0.2.0:')
    depends_on('yaml-cpp@0.7.0:', when='@0.3.0:')