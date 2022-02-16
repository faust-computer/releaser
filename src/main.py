import logging
import semver
import subprocess
import click


@click.command()
def bump_major():
    version = get_version()
    version.bump_major()
    release(version=version)


@click.command()
def bump_minor():
    version = get_version()
    version.bump_minor()
    release(version=version)


@click.command()
def bump_patch():
    version = get_version()
    version.bump_patch()
    release(version=version)


def get_version():
    # sets up logging
    format = "[%(asctime)s][%(name)s][%(levelname)s]: %(message)s"
    logging.getLogger().setLevel(logging.INFO)  # configure root logger

    version_str = (
        subprocess.check_output(["git", "describe", "--tags", "--abbrev"])
        .strip()
        .decode()
    )
    return semver.VersionInfo.parse(f"{version_str[1:]}")


def release(version):
    subprocess.check_output(
        [
            "gh release create",
            f"v{version.major}.{version.minor}.{version.patch} --generate-notes",
        ]
    )


if __name__ == "__main__":
    logging.info("Starting...")
    bump_major()
    bump_minor()
    bump_patch()
