# Quakey

## Introduction

> Quakey is a simple script to scrape Iran's earthquake data from http://irsc.ut.ac.ir/
This python program can be used for monitoring etc.



## Code Samples

```python
from quakey import Equake

obj = Equake() # Create the object
obj.miner() # Scrape latest data 
lrg = obj.largevn() # Save large event to a variable

print(obj.content) # Print all scraped data
print(lrg) # Print large event  


```

## Installation

> Git clone the repository. Import it to your program. 
