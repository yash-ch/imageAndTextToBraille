from setuptools import setup,find_packages

classifiers = [
  'Development Status :: 5 - Production/Stable',
  'Intended Audience :: Education',
  'Operating System :: OS Independent',
  'License :: OSI Approved :: MIT License',
  'Programming Language :: Python :: 3'
]

setup(
    name="imagetobrailleart",
    version="0.0.5.4",
    description="To convert any image or text into braille art",
    long_description=open('README.md').read(),
    long_description_content_type ="text/markdown",
    py_modules=["imagetobrailleart","modifiedbraillegraph"],
    package_dir={' ' :'src'},
    author='Yash Chauhan',
    author_email='chauhanyash1029@gmail.com',
    url="https://pypi.org/project/imagetobrailleart/",
    license="MIT", 
    classifiers=classifiers,
    keywords=['braille', 'art', 'openCV'], 
    packages=find_packages(),
    install_requires=["opencv-python ~= 4.5.3.56", "Pillow ~= 8.3.1"] 
)