# Flash Matrix
Flash Matrix displays Adobe Flash Playerand alternative Flash players compliance. The feature grid is generated using build-matrix.py script.

## Getting Started
'''
python3 build-matrix.py
'''

### Prerequisites

```
sudo apt-get install python3 git
git clone https://github.com/mozilla/shumway.git
git clone https://github.com/strk/gnash.git
git clone https://github.com/lightspark/lightspark.git
```

## Inatall
```
sudo apt-get install python3
sudo apt-get install pip3
pip install lxml
pip install requests
```

## License

This project is licensed under the GPL3 license - see the [LICENSE](LICENSE) file for details.

# Todo
 1. Grab every method in every class from Adobe's AS3 documentation.
 2. Check whether methods exist in code and check whether there are no log methods to see if they are not implemented. So if the method exists then set feature to true. Then if there is a log method for the method then set the feature to false.
