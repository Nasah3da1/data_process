# Purpose of the project

An automated program to download relevant data file, process, analyze & finally generate
a visualization with interesting aspect of the data. 

## Overview and functionality

## Getting Started

These instructions will get you a copy of the project up and running on your local machine for development and testing purposes.
Execute these step from terminal is recommended 

### Prerequisites

Applications you need to execute the project and how to setup and configure them:

```
Terminal
Python  
PyCharm (IDE)
GIT 
```

### Installing/Configuring

Steps on how to get a development env running:

* Pull project from GIT (URL)
* Required External Libraries
* Install external libraries
* Access to executable shell script file to run from terminal


#### Required External Libraries 
* Requests
* Pandas
* Matplotlib
* Numpy

##### Install external libraries from Terminal or Windows command line

```
pip install requests
```
```
pip install pandas
```
```
pip install matplotlib
```
```
pip install numpy
```

#### Executable access to run shell scrip file
```
chmod +x run.sh
```


## Execution

How to run the automated tests for this system:

There are two ways to execute this program:
1) Terminal 
2) Python Integrated development environment (IDE) i.e. PyCharm. 

If this project is being run from terminal, the shell script that runs the project needs to have an executable access.
This step will be performed only one time.

### Terminal
#### Navigation to project location
```
./run.sh
```
### IDE
Before running project from Python IDE Please run following commands to download external libraries from project location in terminal or windows commandline.
```
pip install -r requirements.txt
```
#### Before running the project from IDE the all external Libraries must be installed

* Launch IDE
* Open project from location in which the project is saved
* Locate process.py file from root level of the project 
* Right click-run->process.py

## Deployment

No Applicable.

##Post Execution 
### For Output files navigate to:

* < Project Path >/output/
* final_data.csv
* charts in .pdf

## Contributing

Please read [READ.md](https://gist.github.com/rshagufta/b24679402957c63ec426) for details on my code of conduct, and the process for submitting pull requests to us.

## Versioning

I have used [GITHub](http://github/) for versioning. For the available versions , see the [tags on this repository](https://github.com/rshagufta/project/tags). 

## Authors

* **S. Ora** - *Initial work* - [GITHub](https://github.com/rshagufta)

See also the list of [contributors](https://github.com/rshagufta/project/contributors) who participated in this project.

## License

This project is licensed under S. Ora


###File extension abbreviation 
Extension  | Abbreviation 
-----------| -------------
.csv        | Comma Separated Value
.pdf        | Portable Document Format
.py         | Python File
.sh         | Shell Script
.txt        | Text File
.md         | Markdown Documentation
