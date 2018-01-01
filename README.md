# Publisher

Publisher is a Python package for publishing comics from illustrator files. In a nutshell what it does is takes a list of illustrator files and creates a bunch of PDF documents, including:

* Print ready PDF (currently CreateSpace only)
* Digital PDF (high quality and low quality)
* A directory of PNG files (image per page) ready to share on the web
* CBZ
* Takes a printer ready cover and extracts the front page to be added in front of digital fiels etc.


It uses ghostscript and imagemagick.

## Installation

* Download and unzip

* Open a terminal, `cd` to the directory and then inside the folder (as always, it is advisable to use a virtual environment):

    > pip install .

* To check that the package has been installed, in the Python shell type::

    > from publisher import *

* If everything works correctly, the package will be imported without errors.

## Dependencies

* You'll need to install ghostscript and imagemagick.
* You need python3
* Not sure if this works on Windows (I have a Mac)

## How to use

This is python, so you'll need to create a python file somewhere. For example `my_comic_publisher.py`.

In that file, first import the script...

```python
from publisher import *

```

Then supply a name for your comic. Try not to use spaces in the name (I don't, so not sure if it'll work okay).

Pass this name to initialise the python script.

```python
proj_name = "My-Super-Book"
mycomic = Publisher(proj_name)
```

Now all you need to do is supply a list of source files and an output directory.

For example, if you have a bunch of Illustrator file(s) you want turned into PDF (multiple artboards should work fine), then supply the full path to each file separated by spaces.


```python
source_files = "/path/to/files/page1.ai /path/to/files/page2.ai"

```

Supply an output directory...

```python
output_dir = "/path/to/output"

```

Now you're ready to generate your PDF files.

To create a high resolution digital file:

```python
mycomic.digital_hi(source_files, output_dir)

```

To create a high resolution print file for CreateSpace with final dimensions of 7.125 inches by 10.25 inches (basically a 7"x10" book with a bleed):

```python
mycomic.printer(source_files, output_dir)

```

To create a low resolution digital file AND a CBZ, as well as a directory of PNG of the pages ready to upload to websites etc.:

```python
mycomic.digital_lo(source_files, output_dir)

```

Full example:

```python
from publisher import *

proj_name = "My-Super-Book"
mycomic = Publisher(proj_name)

source_files = "/path/to/files/page1.ai /path/to/files/page2.ai"
output_dir = "/path/to/output"

mycomic.digital_hi(source_files, output_dir)
mycomic.printer(source_files, output_dir)
mycomic.digital_lo(source_files, output_dir)

```


## Limitations

Your artboards for your Illustrator files must be 7 inches by 10.25 inches, for a final output size of 7.125 inches by 10.25 inches.

Let me know if you want support for more sizes. At the moment, I'm tailoring this for publishing through CreateSpace.
