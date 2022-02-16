import logging
import semver
import subprocess
import click


@click.group()
def cli():
    pass


@click.command()
def major():
    version = get_version()
    version = version.bump_major()
    release(version=version)


@click.command()
def minor():
    version = get_version()
    version = version.bump_minor()
    release(version=version)


@click.command()
def patch():
    version = get_version()
    version = version.bump_patch()
    v = version.bump_patch()
    release(version=version)


cli.add_command(major)
cli.add_command(minor)
cli.add_command(patch)


def get_version():
    # sets up logging
    format = "[%(asctime)s][%(name)s][%(levelname)s]: %(message)s"
    logging.getLogger().setLevel(logging.INFO)  # configure root logger

    version_str = (
        subprocess.check_output(["git", "describe", "--tags", "--abbrev"])
        .strip()
        .decode()
    )
    return semver.Version.parse(f"{version_str[1:]}")


def release(version):
    logging.info(f"releasing: {version}")
    subprocess.run(
        [
            "gh",
            "release",
            "create",
            f"v{version.major}.{version.minor}.{version.patch}",
            "--generate-notes",
        ]
    )


if __name__ == "__main__":
    logging.info("Starting...")
    cli()
