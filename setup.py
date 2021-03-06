from setuptools import setup, find_packages


version = '0.1.4.10'

setup(
    name='django-file-form',
    version=version,
    packages=find_packages(),
    license='Apache License, Version 2.0',
    include_package_data=True,
    zip_safe=False,
    author='Marco Braak',
    author_email='mbraak@ridethepony.nl',
    description='Django-file-form helps you to write forms with a pretty ajax upload',
    install_requires=['ajaxuploader==0.3.4.1', 'six', 'path.py'],
    dependency_links=[
        'https://github.com/mbraak/django-ajax-uploader/archive/0.3.4.1.tar.gz#egg=ajaxuploader-0.3.4.1',
    ],
    classifiers=[
        "Development Status :: 5 - Production/Stable",
        "Framework :: Django",
        "Intended Audience :: Developers",
        "License :: OSI Approved :: Apache Software License",
        "Programming Language :: Python :: 2.6",
        "Programming Language :: Python :: 2.7",
        "Programming Language :: Python :: 3.3",
    ]
)
