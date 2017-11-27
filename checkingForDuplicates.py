'''
Looking For Duplicate Rows in a Table
'''

import subprocess
import os
from collections import Counter

def getRowsInAList(database, table):
    with open('getRowList.hql','w') as hqlScript:
        hqlScript.write("use "+database+";")
        hqlScript.write("SELECT * FROM "+table+";")
    hqlScript.close()
    # start calling for output
    process = subprocess.check_output(["beeline", "--showHeader=false", "--outputformat=dsv", "-u", "jdbc:hive2://localhost:10000/default", "-f","getRowList.hql"]).split("\n")
    results = []
    resultsDuplicate = []
    for joe in process:
        results.append(joe)
    print len(results)
    # the set function creates a list based off the previous list with no duplicates
    print len(set(results))
    # if both lens are the same, then there are no duplicates
    # to find where the duplicate is maybe, loop through both lists

dbName = "tpcds_parquet"
tableName = "et_promotion"


getRowsInAList(dbName, tableName)

    
