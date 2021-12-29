# Copyright 2013-2021 Lawrence Livermore National Security, LLC and other
# Spack Project Developers. See the top-level COPYRIGHT file for details.
#
# SPDX-License-Identifier: (Apache-2.0 OR MIT)

from spack import *


class SpackExercise(CMakePackage):
    """This exercise is about packaging code with Spack."""

    homepage = "https://simulation-software-engineering.github.io/homepage/"
    url      = "https://github.com/Simulation-Software-Engineering/spack-exercise/archive/refs/tags/v0.3.0.tar.gz"

    maintainers = ['chlai1012']

    version('0.3.0', sha256='c0c137ab5bf52a36c6c9a000ce32a607dc6f98f808a734ff6d729b4ca01bec9b')
    version('0.2.0', sha256='2d309f0dcf7343d88ceaec7a3daa6cb556603777ed35b90d741671d4dc04ef5d')
    version('0.1.0', sha256='afedc68249587779f1ade08760823ed17cbff62a4cf3d1eaa88d2fe609854470')

    depends_on('boost@1.65.1:',when='@0.2.0:')
    depends_on('yaml-cpp@0.7.0:',when='@0.3.0')

    
