from setuptools import setup, find_packages

setup(
    name='cgb_prj',
    version='0.1',
    packages=find_packages(),
    entry_points={'scrapy': ['settings = cgb_prj.settings']},
    scripts=['bin/cgbc.py'],
    # scripts=['cgb_prj/cgbc.py'],
    dependency_links=[
        "https://pypi.python.org/simple/scrapy",
    ],
    description='TBD',
    long_description='TBD',
    author='duy',
    author_email='duy@systemli.org',
    license='GPLv3+',
    url='https://github.com/duy/cgb_prj',
    keywords='python scrapy html',
    classifiers=[
        'Development Status :: 3 - Alpha',
        "Environment :: Console",
        'Intended Audience :: End Users/Desktop',
        'Intended Audience :: Developers',
        'License :: OSI Approved :: GNU General Public License v3 ' +
        'or later (GPLv3+)',
        'Operating System :: OS Independent',
        'Programming Language :: Python',
        "Topic :: Software Development :: Libraries :: Python Modules",
    ],
)
