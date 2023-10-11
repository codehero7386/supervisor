from setuptools import setup
from supervisor.const import SUPERVISOR_VERSION

# Additional package metadata
metadata = {
    "name": "Supervisor",
    "version": SUPERVISOR_VERSION,
    "license": "BSD License",
    "author": "The Home Assistant Authors",
    "author_email": "hello@home-assistant.io",
    "url": "https://home-assistant.io/",
    "description": "Home Assistant Supervisor: An open-source private cloud OS for Home Assistant based on HassOS",
    "long_description": (
        "Home Assistant Supervisor is a maintenance-free private cloud operator system that sets up a Home Assistant instance."
        " It's based on HassOS and provides a powerful platform for running Home Assistant securely."
    ),
    "keywords": ["docker", "home-assistant", "api"],
    "zip_safe": False,
    "platforms": "any",
}

# Define package structure and dependencies
packages = [
    "supervisor.addons",
    "supervisor.api",
    "supervisor.backups",
    "supervisor.dbus.network",
    "supervisor.dbus.network.setting",
    "supervisor.dbus",
    "supervisor.discovery.services",
    "supervisor.discovery",
    "supervisor.docker",
    "supervisor.homeassistant",
    "supervisor.host",
    "supervisor.jobs",
    "supervisor.misc",
    "supervisor.plugins",
    "supervisor.resolution.checks",
    "supervisor.resolution.evaluations",
    "supervisor.resolution.fixups",
    "supervisor.resolution",
    "supervisor.security",
    "supervisor.services.modules",
    "supervisor.services",
    "supervisor.store",
    "supervisor.utils",
    "supervisor",
]

# Include package data (if any)
include_package_data = True

setup(
    **metadata,  # Pass metadata as keyword arguments
    packages=packages,  # Define package structure
    include_package_data=include_package_data,  # Include package data
)
