
# Flash Matrix
The matrix gives approximate ActionScript 3 (AS3) support of Shumway, Lightspark, Gnash and Ruffle flash players compared the defacto standard Adobe Flash Player. The matrix is not 100% correct due to the difficulty in measuring API support within the source code of each project.

## Getting Started

### Prerequisites

```
sudo apt-get install python3 git
git clone https://github.com/mozilla/shumway.git
git clone https://github.com/strk/gnash.git
git clone https://github.com/lightspark/lightspark.git
git clone https://github.com/ruffle-rs/ruffle.git
git clone https://github.com/awayfl/playerglobal.git
```

### Inatall
```
sudo apt-get install python3
sudo apt-get install pip3
pip install lxml
pip install requests
```

It may be good to install python-is-python3
```
sudo apt-get install python-is-python3
```

### Building matrix
```
bash re-build-matrix.sh
```

## Building React App

 1. cd into source folder
 2. Run ```build.sh```

## License

This project is licensed under the GPL3 license - see the [LICENSE](LICENSE) file for details.

## Thanks
I'd like to link to Mesa Matrix [here](https://github.com/MightyCreak/mesamatrix) (https://github.com/MightyCreak/mesamatrix). Flash Matrix was created with inspiration from Mesa Matrix, so thanks!
