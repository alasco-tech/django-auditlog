from distutils.core import setup

setup(
    name="django-auditlog3",
    version="0.1",
    packages=[
        "auditlog",
        "auditlog.migrations",
        "auditlog.management",
        "auditlog.management.commands",
    ],
    package_dir={"": "src"},
    url="https://github.com/alasco-tech/django-auditlog",
    license="MIT",
    author="Alasco GmbH (Forked from: Jan-Jelle Kester)",
    description="Audit log app for Django",
    install_requires=["django-jsonfield>=1.0.0", "python-dateutil>=2.6.0"],
    zip_safe=False,
    classifiers=[
        "Programming Language :: Python :: 3",
        "Programming Language :: Python :: 3.5",
        "Programming Language :: Python :: 3.6",
        "Programming Language :: Python :: 3.7",
        "Framework :: Django",
        "Framework :: Django :: 2.1",
        "Framework :: Django :: 2.2",
        "License :: OSI Approved :: MIT License",
    ],
)
