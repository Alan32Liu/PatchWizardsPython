import semver


def parse_version(version: str = '0.0.0'):
    if semver.VersionInfo.isvalid(version):
        return semver.VersionInfo.parse(version)


if __name__ == "__main__":
    parse_version('10.5.2')
