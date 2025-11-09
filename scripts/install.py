#!/usr/bin/env python3
import os
import subprocess
from pathlib import PosixPath


def main():
    release_version = "0.27.0"

    package_path = PosixPath("/workspace/monitoring_blackbox")
    package_path.mkdir()
    (package_path / "__init__.py").open("w").close()

    bin_path = PosixPath("/workspace/bin")
    bin_path.mkdir(parents=True, exist_ok=True)

    subprocess.run(
        [
            "curl",
            "--silent",
            "--show-error",
            "--fail",
            "-L",
            "-o",
            f"/tmp/blackbox_exporter-{release_version}.linux-amd64.tar.gz",
            f"https://github.com/prometheus/blackbox_exporter/releases/download/v{release_version}/"
            f"blackbox_exporter-{release_version}.linux-amd64.tar.gz",
        ],
        check=True,
    )
    subprocess.run(
        [
            "tar",
            "-C",
            bin_path.as_posix(),
            "-xf",
            f"/tmp/blackbox_exporter-{release_version}.linux-amd64.tar.gz",
            "--strip-components=1",
            f"blackbox_exporter-{release_version}.linux-amd64/blackbox_exporter",
        ],
        check=True,
    )
    os.remove(f"/tmp/blackbox_exporter-{release_version}.linux-amd64.tar.gz")


if __name__ == "__main__":
    main()
