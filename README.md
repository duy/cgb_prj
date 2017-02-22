# CGB

Work in progress.
Tool to download html pages following next or links given an initial one,
in order to make backups
.
Implemented using Python [Scrapy](https://doc.scrapy.org)

## Installing (Debian/Ubuntu)

Recommended way: `virtualenv`

### Install system dependencies

    sudo apt-get install python-dev

### Obtain virtualenv

Check [Virtualenv installation](https://virtualenv.pypa.io/en/latest/installation.html) or if
Debian equal/newer than Jessie (`virtualenv` >= 1.9), then:

    sudo apt-get install python-virtualenv

### Create a virtual environment

    mkdir ~/.virtualenvs
    virtualenv ~/.virtualenvs/cgb_prjenv source
    ~/.virtualenvs/cgb_prjenv/bin/activate

### Install dependencies in virtualenv

    git clone https://github.com/duy/cgb_prj
    cd cgb_prj
    pip install -r requirements.txt

or run:

    python setup.py install

or run:

    pip install cgb_prj

## Running

List spiders:
    scrapy list

Run `cgb` spider from root project dir:

    scrapy crawl cgb

Run `cgb` spider:

    cd cgb_prj/
    scrapy runspider spiders/cgb.py

Run the script outside project dir:

    cd ../
    bin/cgbc.py


## Download

You can download this project in
[zip](http://github.com/duy/cgb_prj/zipball/master()) or
[tar](http://github.com/duy/cgb_prj/tarball/master) formats.

You can also clone the project with Git by running:

   git clone https://github.com/duy/cgb_prj

## Bugs and features

If you wish to signal a bug or report a feature request, please fill-in
an issue on the [cgb_prj issue
tracker](https://github.com/duy/cgb_prj/issues).

## License

cgb_prj is Copyright 2017 by duy ( duy at systemli dot net), and is
covered by the [GPLv3](http://www.gnu.org/licenses/) license.
