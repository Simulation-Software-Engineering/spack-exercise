from spack import *


class SpackExercise(CMakePackage):
    """Package for the Spack Exercise"""

    homepage = "https://simulation-software-engineering.github.io/homepage/"
    url      = "https://github.com/Simulation-Software-Engineering/spack-exercise"

    maintainers = ['cheriimoya']

    version('0.3.0', '64805c8c7147f70edfa843df81816edd')
    version('0.2.0', '6e947de92fa2f508ccfc8a977d2cebf4')
    version('0.1.0', 'b6a52fb41b57a5e5ac1bcc52ad7188be')

    depends_on('boost@1.65.1:', when='spack-exercise@0.2.0:')
    depends_on('yaml-cpp@0.7.0:', when='spack-exercise@0.3.0:')

    def url_for_version(self, version):
        return f'{self.url}/archive/refs/tags/v{version}.tar.gz'
