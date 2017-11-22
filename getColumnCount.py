# getting column count from a specified databases' table
import subprocess

def getColumnCount(database, table, column):
    with open("gettingColumnCount.hql", "w") as hql:
        hql.write("USE "+database+";"+"\n")
        hql.write("SELECT COUNT("+column+") FROM "+table+";"+"\n")
    hql.close()
    process = subprocess.check_output(["beeline", "--showHeader=false", "--outputformat=dsv", "-u", "jdbc:hive2://localhost:10000/default", "-f", "gettingColumnCount.hql"]).split("\n")
    results = []
    for joe in process:
        results.append(joe)
    with open('results.txt', 'w') as resultsFile:
        counter = 0
        counter2 = 0
        dummie = 0
        for i in results[:-1]:
            if counter < 2:
                counter += 1
            if counter2 < 4:
                counter2 += 1
            if counter2 == 3 and counter >= 2:
                resultsFile.write(i+"\n")
            else:
                dummie = 1
    resultsFile.close()


dbName = "tpcds_parquet"
tableName = "et_customer"
columnName = "c_customer_id"

getColumnCount(dbName, tableName, columnName)
