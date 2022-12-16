# License LGPL-3.0 or later (http://www.gnu.org/licenses/lgpl.html).

import setuptools

with open("README.md", "r", encoding="utf-8") as fh:
    long_description = fh.read()

name = "gutdl"
url = f"https://github.com/Le09/{name}"

setuptools.setup(
    name=name,
    version="0.0.0.1",
    author="Woolion",
    author_email="wooliondrawz@gmail.com",
    description="Gutenberg book downloader",
    long_description=long_description,
    long_description_content_type="text/markdown",
    install_requires=["ConfigArgParse>=1.5.3", "requests>=2.28.1", "beautifulsoup4==4.11.1"],
    url=url,
    license="LGPLv3+",
    project_urls={"Bug Tracker": f"{url}/issues"},
    classifiers=[
        "Programming Language :: Python :: 3.8",
        "License :: OSI Approved :: "
        "GNU Lesser General Public License v3 or later (LGPLv3+)",
        "Programming Language :: Python :: 3.8",
    ],
    include_package_data=True,
    packages=setuptools.find_packages(include=[f"{name}", f"{name}.*"]),
    python_requires=">=3.8",
    entry_points=f"""
        [console_scripts]
        {name}={name}.main:main
    """,
)
