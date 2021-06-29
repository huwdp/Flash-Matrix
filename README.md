
# Flash Matrix
The matrix gives approximate support of Shumway, Lightspark, Gnash and Ruffle flash players compared the defacto standard Adobe Flash Player. The matrix is not 100% correct due to the difficulty in measuring API support within the source code of each project.

Adobe Flash support ended on December 31, 2020. Click here for information about the end of life support details.

## Getting Started

### Prerequisites

```
sudo apt-get install python3 git
git clone https://github.com/mozilla/shumway.git
git clone https://github.com/strk/gnash.git
git clone https://github.com/lightspark/lightspark.git
git clone https://github.com/ruffle-rs/ruffle.git
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

## Thanks
I'd like to link to Mesa Matrix [here](https://github.com/MightyCreak/mesamatrix) (https://github.com/MightyCreak/mesamatrix). Flash Matrix was created with inspiration from Mesa Matrix, so thanks!
