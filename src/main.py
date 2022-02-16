import logging
import semver
import subprocess

# TODO: add click and make it easy to bump versions

def main():
    # sets up logging
    format = "[%(asctime)s][%(name)s][%(levelname)s]: %(message)s"
    logging.basicConfig(format=format, level=logging.INFO)

def run():
    version = get_version()
    logging.info(version)


def get_version():
    version_string = subprocess.check_output(["git", "describe", "--tags"]).strip().decode()
    return semver.VersionInfo.parse(f"{version_string[1:]}")

if __name__ == '__main__':
    main()