import os, sys

# path for spark source folder

# os.environ['SPARK_HOME'] =  'D:\Spark\spark-2.4.0-bin-hadoop2.7'

# append pyspark to python path

# sys.path.append("C:\Users\109009\AppData\Local\Programs\Python\Python37\")help('modules')

try:

    from pyspark import SparkContext
    from pyspark import SparkConf

    print("successfully import Spark Modules.")

except ImportError as IE:

    print("can't import Spark Module", IE)
    sys.exit(1000)

    # IE: (c:\Users\109009\Desktop\spark\pyspark.py)
    # [Running] python -u "c:\Users\109009\Desktop\spark\spark-submit TestPyEnv.py"
    # can't import Spark Module cannot import name 'SparkContext' from 'pyspark' (c:\Users\109009\Desktop\spark\pyspark.py)
    # [Done] exited with code=1000 in 0.207 seconds