from setuptools import setup, find_packages

setup(
    name="dev_abertoV2",  # Your package name
    version="0.2.0",  # Initial release version
    author="Rodrigo Patelli",
    description="Just a test package",  # Short package description
    long_description=open('README.md').read(),
    long_description_content_type="text/markdown",  # Ensures Markdown rendering on PyPI
    packages=['dev_abertoV2'],  # Automatically find packages in your project
    scripts=['scripts/hello.py'],  # Executable scripts
    classifiers=[
        "Programming Language :: Python :: 3",
        "License :: OSI Approved :: MIT License",  # Or any other license you choose
        "Operating System :: OS Independent",
    ],
    python_requires='>=3.12',  # Specify Python version compatibility
    install_requires=[  # List dependencies
        "requests", 
        "setuptools",
        "wheel",
    ],
)
