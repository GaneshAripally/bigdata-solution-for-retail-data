# SCALABLE BIG DATA SOLUTIONS WITH HADOOP ARCHITECTURE AND MAPREDUCE ABSTRACTION

## Note: 

Download the dataset from: https://www.kaggle.com/datasets/prasad22/retail-transactions-dataset

"D:\Software\Retail_Data" is the working directory.

"D:\Software\Retail_Data\Retail_Transactions_Dataset.csv" is the location of the csv file.

"D:\Software\Retail_Data\mapreduce" is the location of the mapreduce files.

If needed you can change them.

Try to store all the files in the same directory like this:
Main directory (Ex. D:\Software\Retail_Data)
│   ml_task.py
│   Retail_Transactions_Dataset.csv
│
└───mapreduce
        mapper.py
        reducer.py

## Commands used:

cd C:\hadoop\sbin
start-dfs.cmd
jps
start-yarn.cmd
jps


hdfs dfs -mkdir /retail_data
hdfs dfs -ls /


hdfs dfs -put D:\Software\Retail_Data\Retail_Transactions_Dataset.csv /retail_data/
hdfs dfs -ls /retail_data

hdfs fsck /retail_data/Retail_Transactions_Dataset.csv -files -blocks -locations

type D:\Software\Retail_Data\Retail_Transactions_Dataset.csv | python mapper.py | more

type D:\Software\Retail_Data\Retail_Transactions_Dataset.csv | python mapper.py | sort | python reducer.py


hdfs dfs -mkdir /mapreduce
hdfs dfs -mkdir /mapreduce/input
hdfs dfs -mkdir /mapreduce/output


hdfs dfs -put D:\Software\Retail_Data\mapreduce\mapper.py /mapreduce/
hdfs dfs -put D:\Software\Retail_Data\mapreduce\reducer.py /mapreduce/


hdfs dfs -ls /mapreduce

hdfs dfs -cp /retail_data/Retail_Transactions_Dataset.csv /mapreduce/input/


hdfs dfs -ls /mapreduce/input
hdfs dfs -rm -r /mapreduce/output


hadoop jar C:\hadoop\share\hadoop\tools\lib\hadoop-streaming-3.3.6.jar -files "mapper.py,reducer.py" -input /mapreduce/input/Retail_Transactions_Dataset.csv -output /mapreduce/output -mapper "python mapper.py" -reducer "python reducer.py"


hdfs dfs -cat /mapreduce/output/part-00000 | more


cd D:\Software\Retail_Data
python ml_task.py


cd C:\hadoop\sbin
stop-yarn.cmd
stop-dfs.cmd
