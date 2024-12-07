"""Test whether review-matrix is installed in the python environment."""

import sys
from importlib.metadata import metadata

try:
    project_info = metadata("review-matrix")
except ModuleNotFoundError:
    print("No package metadata was found for review-matrix")
    input("Press enter to exit...")
    sys.exit()

project_name = project_info["Name"]
project_version = project_info["Version"]

print(f"Project Name: {project_name}")
print(f"Version: {project_version}")
