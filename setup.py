from setuptools import find_packages, setup

VERSION = "6.0.0"
LONG_DESCRIPTION = """
.. image:: http://pinaxproject.com/pinax-design/patches/pinax-announcements.svg
    :target: https://pypi.python.org/pypi/pinax-announcements/

===================
Pinax Announcements
===================

.. image:: https://img.shields.io/pypi/v/pinax-announcements.svg
    :target: https://pypi.python.org/pypi/pinax-announcements/

``pinax-announcements`` is a well tested, documented, and proven solution
for any site wanting announcements for it's users.

Supported Django and Python Versions
------------------------------------

+-----------------+------+------+------+
| Django / Python | 3.9  | 3.10 | 3.11 |
+=================+======+======+======+
|  4.2            |  *   |  *   |  *   |
+-----------------+------+------+------+
"""

setup(
    author="Pinax Team",
    author_email="team@pinaxproject.com",
    description="a Django announcements app",
    name="pinax-announcements",
    long_description=LONG_DESCRIPTION,
    version=VERSION,
    url="http://github.com/pinax/pinax-announcements/",
    license="MIT",
    packages=find_packages(),
    package_data={
        "announcements": []
    },
    include_package_data=True,
    classifiers=[
        "Development Status :: 5 - Production/Stable",
        "Environment :: Web Environment",
        "Framework :: Django",
        "Framework :: Django :: 4.2",
        "Intended Audience :: Developers",
        "License :: OSI Approved :: MIT License",
        "Operating System :: OS Independent",
        "Programming Language :: Python",
        "Programming Language :: Python :: 3",
        "Programming Language :: Python :: 3.9",
        "Programming Language :: Python :: 3.10",
        "Programming Language :: Python :: 3.11",
        "Topic :: Software Development :: Libraries :: Python Modules",
    ],
    install_requires=[
        "django>=4.2,<5.0",
    ],
    python_requires=">=3.9",
    tests_require=[
        "django-test-plus>=1.0.22",
        "pinax-templates>=1.0.4",
        "mock>=2.0.0",
    ],
    test_suite="runtests.runtests",
    zip_safe=False
)
