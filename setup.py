from setuptools import setup, find_packages

setup(
    name='DynamiCrafter',
    version='0.1',
    package_dir={'': '.'},
    packages=["DynamiCrafter", "DynamiCrafter.lvdm", "DynamiCrafter.utils"],
    install_requires=[
        # List your project's dependencies here.
        # For example: 'requests', 'numpy'
    ],
    author='Your Name',
    author_email='your.email@example.com',
    description='A short description of your project',
    url='https://github.com/JoshKlev/DynamiCrafter',
    classifiers=[
        'Development Status :: 3 - Alpha',
        'Intended Audience :: Developers',
        'License :: OSI Approved :: MIT License',
        'Programming Language :: Python :: 3',
        'Programming Language :: Python :: 3.6',
        'Programming Language :: Python :: 3.7',
        'Programming Language :: Python :: 3.8',
        'Programming Language :: Python :: 3.9',
    ],
)
