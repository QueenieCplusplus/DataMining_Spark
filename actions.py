# using pyspark
# RDD Wrangling
# by Queenie Chen
# on 2020.3/17 ~ 3/18
# Duration : 2 work days

from pyspark import sc

# 對資料實際做些事情
# 回傳最後結果予驅動程式 | 將資料寫入外部存儲系統
# 這與 rdd.py 內執行的 filter() 不同
# 因為 rdd 回傳新指標，與原來 rdd 記憶體定址不同。

read_readme_rdd = sc.read.text("README.md")

for line_in_readme in read_readme_rdd.take(20):
    print (line_in_readme)

# in scala, 
# read_readme_rdd.take(10).foreach(println)

# tansformater & action used in Spark is lazy-init.

# action called take:
# take() receives partial elements in RDD
# and loop-print in block

# action called collect:
# collect() receives all elements in RDD
# and collect aply to the status taht data set is not too large/big in a machine

# if the data set is large/big, then
# write them in distributed data storage, such as HDFS and AWS S3
# use the actions called saveAsTextFile(), saveAsSequebceFile()

# while every new action is being called,
# entire rdd will be re-computed in cache.
