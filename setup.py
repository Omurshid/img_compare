from setuptools import setup

setup(
    name="img_compare",
    version='0.1',
    py_modules=['cli'],
    install_requires=[
        'Click',
        'numpy',
        'pandas',
        'Pillow'
    ],
    entry_points='''
        [console_scripts]
        img_compare=cli:main
    ''',
)
