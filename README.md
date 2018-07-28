# BINARY ↔ ASCII CONVERTER

This tool provides encoding - decoding with Binary-Ascii.

**CommandLine $ python3 binascii.py -h**

```
usage: binascii.py [-h] [-t TEXT] [-c CONVERSION]

optional arguments:
  -h, --help                show this help message and exit
  
  -t TEXT, --text TEXT      File path for text. Example: textname {without '.txt'}
  
  -c CONVERSION, --conversion CONVERSION
                            Select conversion type. Example:'-c encode' or '-c decode'

```

 **CommandLine $ python3 binascii.py -t TextFileName -c encode**
 ```
 Note: There must be a txt file named TextFileName in same directory with binascii.py

 [-] TextFilename.txt includes text "user"
 [+] Output on commandlines: 01110101 01110011 01100101 01110010
```
Attention:Only Educational Purposes.
