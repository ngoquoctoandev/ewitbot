from os import path

from devops.utils.version import Version

PROJECT_NAME = "ewit-bot"
PACKAGE_NAME = "src"
VERSION = Version(0, 0, 7)

PACKAGE_DIR = path.dirname(__file__)
PROJECT_DIR = path.dirname(PACKAGE_DIR)
