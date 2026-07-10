# Copyright Spack Project Developers. See COPYRIGHT file for details.
#
# SPDX-License-Identifier: (Apache-2.0 OR MIT)

from spack_repo.builtin.build_systems.generic import Package

from spack.package import *


class ReadconCore(Package):
    """Rust CON/convel trajectory I/O library with a C/C++ FFI (cargo-c)."""

    homepage = "https://github.com/lode-org/readcon-core"
    url = "https://github.com/lode-org/readcon-core/archive/refs/tags/v0.13.1.tar.gz"
    git = "https://github.com/lode-org/readcon-core.git"

    maintainers("HaoZeke")
    license("MIT", checked_by="HaoZeke")

    version("0.13.1", sha256="a261e69b87228dcc8f161eef800590b0395b4c93605b838c6216d40a1780f0bf")

    depends_on("c", type="build")
    depends_on("rust@1.88:", type="build")
    # package.metadata.capi.min_version
    depends_on("cargo-c@0.10.17:", type="build")
    depends_on("pkgconfig", type="build")

    def install(self, spec, prefix):
        cargo = which("cargo")
        with working_dir(self.stage.source_path):
            cargo(
                "cinstall",
                "--locked",
                "--release",
                f"--prefix={prefix}",
                "--libdir=lib",
                "--includedir=include",
                "--pkgconfigdir=lib/pkgconfig",
            )
