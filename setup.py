"""
Setup configuration for Omega Universal OS
"""

from setuptools import setup, find_packages
import os

# Read README for long description
readme_path = os.path.join(os.path.dirname(__file__), 'README.md')
if os.path.exists(readme_path):
    with open(readme_path, 'r', encoding='utf-8') as f:
        long_description = f.read()
else:
    long_description = 'Omega Universal OS - Universal Platform for Ripple Coherence'

setup(
    name='omega-universal-os',
    version='0.1.0',
    author='Omega Universal OS Team',
    description='Universal platform for managing ripple coherence, AI-driven predictions, and ethical reasoning',
    long_description=long_description,
    long_description_content_type='text/markdown',
    url='https://github.com/medicinalElJefe/OmegaUniversalOS',
    packages=find_packages(),
    classifiers=[
        'Development Status :: 3 - Alpha',
        'Intended Audience :: Developers',
        'Intended Audience :: Education',
        'Intended Audience :: Healthcare Industry',
        'Intended Audience :: Science/Research',
        'Topic :: Scientific/Engineering :: Artificial Intelligence',
        'Topic :: Education',
        'Topic :: Scientific/Engineering :: Medical Science Apps.',
        'License :: OSI Approved :: MIT License',
        'Programming Language :: Python :: 3',
        'Programming Language :: Python :: 3.8',
        'Programming Language :: Python :: 3.9',
        'Programming Language :: Python :: 3.10',
        'Programming Language :: Python :: 3.11',
    ],
    python_requires='>=3.8',
    install_requires=[
        # No external dependencies - uses Python standard library only
        # This is an intentional design decision to minimize deployment complexity
        # and ensure maximum compatibility across environments
    ],
    extras_require={
        'dev': [
            'pytest>=7.0.0',
            'pytest-cov>=4.0.0',
            'black>=22.0.0',
            'flake8>=4.0.0',
        ],
    },
    entry_points={
        'console_scripts': [
            'omega-os=main:main',
        ],
    },
    include_package_data=True,
    zip_safe=False,
)
