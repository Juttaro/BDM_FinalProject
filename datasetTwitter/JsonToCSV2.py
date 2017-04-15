"""
Requirements:   pip install flatten_json
"""

from flatten_json import flatten
import pandas as pd
import json

# Here we open example.json to test flatting every object in the json file

with open('example.json') as TweetsJson:

    jsonFile = json.load(TweetsJson)  # jsonFile is of type 'list'

    # This creates an array of flatten objects.
    flattenDict = [flatten(obj, '|') for obj in jsonFile]

    '''
    flatten() explanation: 
    
    dic = {
        "a": 1,
        "b": 2,
        "c": [{"d": [2, 3, 4], "e": [{"f": 1, "g": 2}]}]
    }

    And turns it into this:
    
    dic = {
        'a': '1',
        'b': '2',
        'c_0_d_0': '2',
        'c_0_d_1': '3',
        'c_0_d_2': '4',
        'c_0_e_0_f': '1',
        'c_0_e_0_g': '2'
        }
        
    '''

    # print flattenDict # Check the structure

    dataFrame = pd.DataFrame(flattenDict)  # dataFrame is of type <class 'pandas.core.frame.DataFrame'> NOT LIST
    # DataFrame() captures the flatten array

    dataFrame.to_csv('exampleDB.csv', encoding='utf-8')  # outputs to csv file
