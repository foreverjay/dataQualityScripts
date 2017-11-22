# getting tables from tpcds data 

def get_TPCDS_Tables_Script():
    with open("hiveScripts/getTables.hql", "w") as hql:
        hql.write("use tpcds_parquet;"+"\n")
        hql.write("show tables;")
        hql.close()

#get_TPCDS_Tables_Script()


def store_TPCDS_tables():
    import subprocess
    #process = subprocess.check_output(["hive", "-f", "/home/cloudera/dataQualityScripts/hiveScripts/getTables.hql"]).split("\n")
    process = subprocess.check_output(["beeline", "--showHeader=false", "--outputformat=dsv", "-u", "jdbc:hive2://localhost:10000/default", "-f", "/home/cloudera/dataQualityScripts/hiveScripts/getTables.hql"]).split("\n")
    process.pop()
    tables = []
    for joe in process:
        tables.append(joe)
    with open('hiveScripts/tables.txt', 'w') as results:
        counter = 0
        print len(tables)-1
        for i in tables[:-1]:
            if counter < 2:
                counter += 1
            else:
                results.write(i+"\n")
                
    results.close()
    #for i in tables.pop():
        #print i

store_TPCDS_tables()



