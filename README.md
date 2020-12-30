
# Flash Matrix
The matrix gives approximate support of [Shumway](https://mozilla.github.io/shumway/), [Lightspark](https://lightspark.github.io/) and [Gnash](https://www.gnu.org/software/gnash/) flash players compared the defacto standard Adobe Flash Player. The matrix is not 100% correct due to the difficulty in measuring API support within the source code of each project. 

The matrix can be found here [here](https://huwdp.github.io/Flash-Matrix/)  (https://huwdp.github.io/Flash-Matrix/)

Adobe Flash support will end on December 31, 2020. Click [here](https://www.adobe.com/products/flashplayer/end-of-life.html#) for information about the end of life support details.



## Getting Started

### Prerequisites

```
sudo apt-get install python3 git
git clone https://github.com/mozilla/shumway.git
git clone https://github.com/strk/gnash.git
git clone https://github.com/lightspark/lightspark.git
```

### Inatall
```
sudo apt-get install python3
sudo apt-get install pip3
pip install lxml
pip install requests
```
### Building matrix
```
python3 build-matrix.py
```


## License

This project is licensed under the GPL3 license - see the [LICENSE](LICENSE) file for details.

## Todo
 1. Grab every method in every class from Adobe's AS3 documentation.
 2. Check whether methods exist in code and check whether there are no log methods to see if they are not implemented. So if the method exists then set feature to true. Then if there is a log method for the method then set the feature to false.
 3. Add other Flash implementations

## Thanks
I'd like to link to Mesa Matrix [here](https://github.com/MightyCreak/mesamatrix) (https://github.com/MightyCreak/mesamatrix). Flash Matrix was created with inspiration from Mesa Matrix, so thanks!
