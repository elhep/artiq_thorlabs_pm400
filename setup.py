from setuptools import find_packages, setup
from setuptools.command.install import install
import subprocess

with open("requirements.txt") as f:
    required = f.read().splitlines()


class PostInstallCommand(install):
    def run(self):
        install.run(self)
        subprocess.call(['bash', 'install.sh'])


setup(
    name="artiq_thorlabs_pm400",
    install_requires=required,
    packages=find_packages(),
    entry_points={
        "console_scripts": [
            "aqctl_artiq_thorlabs_pm400 = artiq_thorlabs_pm400.aqctl_artiq_thorlabs_pm400:main",
        ],
    },
)
