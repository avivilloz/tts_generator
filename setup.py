from setuptools import setup, find_packages

setup(
    name="tts",
    version="0.1.0",
    packages=find_packages(where="src"),
    package_dir={"": "src"},
    install_requires=[
        "TTS",
    ],
    author="Aviv Illoz",
    author_email="avivilloz@gmail.com",
    description=(
        "Provides a simple interface for text-to-speech conversion using a "
        "multilingual TTS model, allowing users to generate speech from text "
        "with customizable voice characteristics."
    ),
    long_description=open("README.md").read(),
    long_description_content_type="text/markdown",
    url="https://github.com/avivilloz/tts",
    python_requires=">=3.9.0, <3.12",
    classifiers=[
        "Programming Language :: Python :: 3",
        "License :: OSI Approved :: MIT License",
        "Operating System :: OS Independent",
    ],
)
