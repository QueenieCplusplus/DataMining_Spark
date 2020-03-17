# using pyspark
# init SparkContext Object
# by Queenie Chen
# on 2020.3/17 ~ 3/18
# Duration : 2 work days

from pyspark import SparkContext, SparkConf 
from pyspark.sql.functions import *
# https://spark.apache.org/docs/latest/quick-start.html#more-on-dataset-operations

conf = SparkConf().setMaster("local").setAppName("QueenPySparkApp")
sc = SparkContext(conf= conf)

# create data frame

def dataFrame_generator():

    textFile = sc.read.text("./README.md")
    # or using sc.textFile("")
    print(textFile.count)
    print(textFile.first())
    # show row
    print(textFile.filter(textFile.value.contains("Spark Core")))
    print(type(textFile))

# define func name & pass func by name to Spark Engine
def pass_func_to_Spark():
    rdd = sc.textFile("./README.md")
    spark_word = rdd.filter(lambda s: 'spark' in s)

def pass_func2_to_Spark():
    rdd = sc.textFile("./README.md")
    spark_word = rdd.filter(a_func)

def a_func():
    print("play spark.")

if __name__ == 'main':

    dataFrame_generator()
