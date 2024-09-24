## TextExtractor
TextExtractor is a simple graphical user interface (GUI) program that allows users to extract text from images,   
edit the extracted text, and save it as a .txt or .doc file.   
The application is built using tkinter and pytesseract (licensed under the [Apache License 2.0](https://opensource.org/licenses/Apache-2.0)).  

### Features
- Upload Images: Users can upload an image containing text. 
- Choose Language: Select the language of the text on the image for more accurate extraction.  
- Extract Text: Convert the text from the image into editable text.  
- Edit and Save: Modify the extracted text as needed and save it as a .txt or .doc file.  
- Append New Text: Upload another image and press the "to text ->" button to append the new text to the end of the current text.

### Installation
Requirements
- Python 3.x
- tkinter (comes with Python)
- pytesseract

To use TextExtractor, you'll need to download and install Tesseract OCR.   
You can download and install Tesseract from [here](https://github.com/UB-Mannheim/tesseract/wiki).  
After installation, the executable should be located in a directory like     
`C:\Program Files\Tesseract-OCR\tesseract.exe` (Windows).  


After installation, provide the path to the Tesseract executable in the code by setting:
in   
`text_extract.py`   
find  
`PATH_TO_PYTESSERACT = r'add your path'`  
Ensure you use the correct path where Tesseract is installed on your system.  


### Installing Dependencies  
You can install the necessary dependencies by running:  
`pip install pytesseract pillow`


### License
This project uses [pytesseract](https://github.com/madmaze/pytesseract) and [Tesseract OCR](https://github.com/tesseract-ocr/tesseract), 
both licensed under the Apache License 2.0.


### Acknowledgements  
This project uses the following libraries:  
- [pytesseract](https://github.com/madmaze/pytesseract): A Python wrapper for Google's Tesseract-OCR Engine,     
licensed under the [Apache License 2.0](https://opensource.org/licenses/Apache-2.0).  