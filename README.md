# data-processing

## Instructions: 
To access this program, clone this repository, cd into the selected folder, and run the Python script using these 3 commands below:

``` git clone https://github.com/mattchooo/data-processing```
```cd data-processing```
```python3 dataprocessing.py```

This will then direct you to the Data Processing CLI:

```Welcome to the transaction database!```
```-----------------------------------```
```1: Begin Transaction```
```2: Insert/Put New Value```
```3: Get Value```
```4: Commit Transaction```
```5: Rollback```
```6: Exit```

### Options:
1. __Begin Transaction__ - Calls the begin_transaction() function and switches the database into transaction mode.
2. __Insert/Put New Value__ - If in transaction mode, inserts a key-value pair into the transaction database given a string key and an integer value.
3. __Get Value__ - Retrieves a value from the permanent database given a key that exists within this database.
4. __Commit Transaction__ - If in transaction mode, merges the transaction database into the permanent database.
5. __Rollback__ - If in transaction mode, clears the transaction database.
6. __Exit__ - Exits the CLI.

## Modifications for Official Assignment:
To be considered an official assignment, I think this assignment needs to be more standardized. I think it could work if it were similar to the React.js or the unit testing activities, in that a student would need to clone the repository, make small changes to the code, and analyze results. There also should be a bigger emphasis on how transactions work behind the scenes. This would fall more in line with the class material in understanding software engineering practices, rather than coding a transaction database application from scratch.
