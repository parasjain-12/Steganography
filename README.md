# Steganography
This program will hide text in png imagesand unhide text.

To hide text in image from terminal : 
```
python3 main.py hide_text 'message to hide' inputImageName.png OutputImageName.png
```

To unhide text in Image from terminal:
```
python3 main.py unhide_text OutputImageName.png
>>> message to hide
```
## If you want to hide text in jpg 
* Step1 : use jpgtopdf.py to convert jpg to png
* Step2: use that png file to hide text
* Step 3: again convert it back to jpg 
           
