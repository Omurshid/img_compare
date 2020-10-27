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
    author='Osama Murshid',
    author_email='omurshid@uwaterloo.ca',
    License='MIT',
    entry_points='''
        [console_scripts]
        img_compare=cli:main
    ''',
)
