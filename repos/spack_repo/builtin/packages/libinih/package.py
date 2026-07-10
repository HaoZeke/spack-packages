# Copyright Spack Project Developers. See COPYRIGHT file for details.
#
# SPDX-License-Identifier: (Apache-2.0 OR MIT)

from spack_repo.builtin.build_systems.meson import MesonPackage

from spack.package import *


class Libinih(MesonPackage):
    """inih (INI Not Invented Here) is a simple .INI file parser written in C."""

    homepage = "https://github.com/benhoyt/inih"
    url = "https://github.com/benhoyt/inih/archive/refs/tags/r62.tar.gz"
    git = "https://github.com/benhoyt/inih.git"

    maintainers("HaoZeke")
    license("BSD-3-Clause", checked_by="HaoZeke")

    version("master", branch="master")
    version("r62", sha256="9c15fa751bb8093d042dae1b9f125eb45198c32c6704cd5481ccde460d4f8151")

    variant("inireader", default=True, description="Build and install the C++ INIReader API")

    depends_on("c", type="build")
    depends_on("cxx", type="build", when="+inireader")

    def meson_args(self):
        return [
            self.define_from_variant("with_INIReader", "inireader"),
            self.define("tests", False),
            self.define("distro_install", True),
        ]
