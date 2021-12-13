# imagetobrailleart

##### A python library to convert image into braille art.

Convert any image into braille. I have used openCV, PIL and braillegraph by  [Chris bouchard] but i have slightly upgraded his library.

# Installation

This package is hosted on PyPI, so installation should be as simple as
```
% pip install imagetobrailleart
```
Note that this package requires at least Python 3.3, so if your default Python installation is still Python 2, make sure you use pip3.

openCV is necessary for this library. If it is not installed then please install it.
```
%pip install opencv-python
``` 
I am using 4.5.3.56 version.

Pillow is also necessary for this library. If it is not installed then please install it.
```
%pip install pillow
``` 
I am using 8.3.1 version.

Again, use python3 if necessary.

# Usage

Import imagetobrailleart to start using it.

```
imagetobraille("location_of_image", size = 100, inverse = 'n')
```
100 is the minimum we recommend and to inverse the image use 'y' and if you don't want ot inverse it then use 'n' or left it blank.
Example to print face of a girl:
```
>>> import imagetobrailleart as itb
>>> a = itb.imagetobraille("C:\\Users\\yash\\Desktop\\face2.jpg") 
>>> print(a)
```
![GIRL braille art](https://imgur.com/a/NMyqun6)

## License

MIT

**Free Code, Hell Yeah!**

[//]: # (These are reference links used in the body of this note and get stripped out when the markdown processor does its job. There is no need to format nicely because it shouldn't be seen. Thanks SO - http://stackoverflow.com/questions/4823468/store-comments-in-markdown-syntax)

   [Chris bouchard]: <https://github.com/chrisbouchard/braillegraph>