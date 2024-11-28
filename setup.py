from setuptools import find_packages, setup

package_name = "square_common_bl"

setup(
    name=package_name,
    version="1.5.0",
    packages=find_packages(),
    package_data={
        package_name: ["data/*"],
    },
    install_requires=[
        "uvicorn>=0.24.0.post1",
        "fastapi>=0.104.1",
        "pydantic>=2.5.3",
        "requests>=2.32.3",
        "square_commons>=1.0.0",
        "square_logger>=1.0.0",
        "square_database_helper>=2.0.0",
        "square_database_structure>=1.0.0",
        "square_authentication_helper>=2.2.0",
    ],
    extras_require={},
    author="thePmSquare",
    author_email="thepmsquare@gmail.com",
    description="common business layer for my personal server.",
    long_description=open("README.md", "r").read(),
    long_description_content_type="text/markdown",
    url=f"https://github.com/thepmsquare/{package_name}",
    classifiers=[
        "Development Status :: 3 - Alpha",
        "Intended Audience :: Developers",
        "License :: OSI Approved :: MIT License",
        "Programming Language :: Python :: 3",
        "Programming Language :: Python :: 3.9",
    ],
)
