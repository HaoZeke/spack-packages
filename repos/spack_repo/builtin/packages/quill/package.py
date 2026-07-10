# Copyright Spack Project Developers. See COPYRIGHT file for details.
#
# SPDX-License-Identifier: (Apache-2.0 OR MIT)

from spack_repo.builtin.build_systems.cmake import CMakePackage

from spack.package import *


class Quill(CMakePackage):
    """Asynchronous low-latency C++ logging library."""

    homepage = "https://github.com/odygrd/quill"
    url = "https://github.com/odygrd/quill/archive/refs/tags/v11.1.0.tar.gz"
    git = "https://github.com/odygrd/quill.git"

    maintainers("HaoZeke")
    license("MIT", checked_by="HaoZeke")

    version("12.0.0", sha256="86974f76a2ca229460b027aed656ee9d3c5c1c5df70507448cb434d5e477d868")
    version("11.1.0", sha256="a4c41068ec51979e1c6d95ae9ab6efc09e654b9815dcb7a1b58b7a430a5cbd13")
    version("11.0.2", sha256="c4208f717e62fc4a7178917c9c39dbb90276d72c3cefd9077d0b973365d72667")

    depends_on("cxx", type="build")
    depends_on("cmake@3.10:", type="build")

    def cmake_args(self):
        return [
            self.define("QUILL_BUILD_EXAMPLES", False),
            self.define("QUILL_BUILD_TESTS", False),
            self.define("QUILL_BUILD_BENCHMARKS", False),
            # Quill is often a subdirectory of another project; force install
            # of headers and pkg-config when built as a Spack package.
            self.define("QUILL_ENABLE_INSTALL", True),
        ]
