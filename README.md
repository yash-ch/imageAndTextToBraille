# imagetobrailleart

##### A python library to convert image or text into braille art.

Convert any image or text into braille. I have used openCV, PIL and braillegraph by  [Chris bouchard] but i have slightly upgraded his library.

# Installation

This package is hosted on PyPI, so installation should be as simple as
```
$ pip install imagetobrailleart
```
Note that this package requires at least Python 3.3, so if your default Python installation is still Python 2, make sure you use pip3.

openCV and pillow are necessary for this library. They will be automatically installed in package. If it is not installed or not working then follow these commands.

```
$ pip install opencv-python==4.5.3.56
``` 

```
$ pip install pillow==8.3.1
``` 

Again, use python3 if necessary.

# Usage

You can either use ```imagetobraille``` or ```texttobraille```

Import imagetobrailleart to start using it.

### Image to Braille

```
imagetobraille("location_of_image", size = 100, inverse = 0)
```
100 is the minimum size we recommend and to inverse the image use 1 and if you don't want ot inverse it then use 0 or left it blank.

Example to print face of a girl:
```
>>> import imagetobrailleart as itb
>>> a = itb.imagetobraille("C:\\Users\\yash\\Desktop\\face2.jpg") 
>>> print(a)
```
![GIRL braille art](https://i.imgur.com/XYxyM7b.png)

### Text to Braille

```
texttobraille("font_location","text", size = 100, inverse = 0)
```
To inverse the image use 1 and if you don't want ot inverse it then use 0 or left it blank.

Example to print HEY:
```
>>> import imagetobrailleart as itb
>>> a = itb.texttoimage("arial.tff","HEY", 100, 0)
>>> print(a)
```
![HEY braille art](https://i.imgur.com/FmcX7lM.png)

## License

MIT

**Free Code, Hell Yeah!**

[//]: # (These are reference links used in the body of this note and get stripped out when the markdown processor does its job. There is no need to format nicely because it shouldn't be seen. Thanks SO - http://stackoverflow.com/questions/4823468/store-comments-in-markdown-syntax)

   [Chris bouchard]: <https://github.com/chrisbouchard/braillegraph>