# TPU

This repository contains a python script able to calculate the daily demand of the entire transport system or one of its routes based on its Origin-Destiny (OD) matrix during peak hours. Also, it is capable of plot a graph representing the system and its most required routes. This entire project was created to solve exercises from TPU (Urban Public Transport) module and was built using Python 3.6.

## Installation

To create a virtual environment and activate it, run the following commands on your terminal.

```
$ python -m virtualenv venv
$ source venv/bin/activate
```

With the virtual activated (indicated by `(venv)` before the folder path on the terminal), install the project requirements by running the command:

```
(venv) $ pip install -r requirements.txt
```

## system_demand.py

This script contains the methods implemented in order to solve the exercises proposed. A complete list of the methods and their functionality can be seen below.  

* _daily_demand_: This method estimates the daily demand on each route of a transport system based on its peak demand and daily number of passengers.
* _occupation_: This method estimates the daily occupation on a given route.
* _graph_: This method constructs a graph representing the travelling demands on the entire system.

## od_matrices

This folder contains the csv files with the OD matrices for two different systems during their peak hours. One of the csv files also contains a coordinates column that will be used to construct the system graph.  