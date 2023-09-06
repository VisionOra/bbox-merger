from distutils.core import setup

setup(
    name="bbox_merger",  # How you named your package folder (MyLib)
    packages=["bbox_merger"],  # Chose the same as "name"
    version="0.0.1",  # Start with a small number and increase it with every change you make
    license="",  # Chose a license from here: https://help.github.com/articles/licensing-a-repository
    description="This Module will help you out in merging your bboxes if overlaps",  # Give a short description about your library
    author="Sohaib Anwaar",  # Type in your name
    author_email="sohaibanwaar36@gmail.com",  # Type in your E-Mail
    url="https://github.com/SohaibAnwaar",  # Provide either the link to your github or to your website
    download_url="https://github.com/SohaibAnwaar/bbox-merger/archive/refs/tags/v_001.tar.gz",  # I explain this later on
    keywords=[
        "bbox",
        "merge",
        "Computer Vision",
        "Image processing",
        "Object Detection",
        "Segmentation",
    ],  # Keywords that define your package best
    install_requires=["shapely==2.0.1"],  # I get to this in a second
    classifiers=[
        "Development Status :: 3 - Alpha",  # Chose either "3 - Alpha", "4 - Beta" or "5 - Production/Stable" as the current state of your package
        "Intended Audience :: Developers",  # Define that your audience are developers
        "Topic :: Software Development :: Build Tools",
        "Programming Language :: Python :: 3.8",
    ],
)
