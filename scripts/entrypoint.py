#!/usr/bin/env python3
import os
import yaml


def generate_configuration() -> str:
    config = {
        "modules": {
            "http_2xx": {
                "prober": "http",
                "http": {
                    "preferred_ip_protocol": "ip4",  # No IPv6 in containers :(
                },
            }
        }
    }
    return yaml.dump(config)


def main():
    with open("/tmp/blackbox_exporter.yml", "w") as fh:
        fh.write(generate_configuration())

    return os.execv(
        "/workspace/bin/blackbox_exporter",
        [
            "/workspace/bin/blackbox_exporter",
            "--config.file=/tmp/blackbox_exporter.yml",
            "--log.level=debug",
            "--log.prober=debug",
        ],
    )


if __name__ == "__main__":
    main()
