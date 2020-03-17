# Spark 

    結合 Hadoop 資料存儲結構與 Pandas 分析的目的的叢集運算平台，

    Smart Pandas Tool using in AI & ad hoc Data Analysis 專案性資料分析或是 Batch or Bulk 批次性資料。

    比起同時運行 5 - 10 個獨立的系統，將其組合運行在同一系統中，可以縮小其他成本，然而 Spark 其實能同時運行在數千台運算節點中。

    例如:

    (1) Deploy

    (2) Maintain

    (3) Test

# Spark Core UML

    RDD API is defined in Core of Spark,  RDD is resilient distributed dataset, this data type (object Set) can be handled parallelly in many machines. 

                         
                         Spark Compute Engine

                                  |
                                |   |  
                                  |


                            Driver Program
                          including Main Func
                      wrapped in SC, SparkContext


                                  |
                                |   |  
                                  |


                              scheduler 
                     (叢集管理器 == spark 獨立排程器)
                         can also use Mesos or Yarn
 
                              /   |   \
                             /    |    \
                            /     |     \

                         node    node   node ...
                       worker1  worker1 worker2 ...
                      Executor Executor1 Executor2 ... 
                    /             |            \
                   /              |             \
                  /               |              \
                Tasks...        Tasks...         Tasks...

----------------------------------------------------------------------------------

# RDD and Dictionary

  RDD can be create by Hadoop InputFormat or using PySapark DataFrame.

  RDD 是分散式元素的抽象集合! 對此種資料結構的操作包含:

  (1) create

  (2) transformat

  (3) operation == manipulation

  (4) Spark Compute Engine helps to Encapsulate the data obj in RDD and distributes them in Cluster of Worker Nodes to run Multi-Tasks in Parallel.

# RDD & its Partitions   

  RDD is immutable, but can be split in Partitions, every Partition can be computed in many and different working nodes to do task-running.


                List or Set  =>  RDD  =>  Partitions 

# RDD Manipulations


        Create RDD           Filter RDD           Mapped RDD

            |
            V

         inputRDD

----------------------------------------------------------------------------------

# Spark Code in local machine (single machine, 單機模式)

   support programming languages: 

   - [X] (1) Java

   - [X] (2) Python

   - [X] (3) Scala

* pip install

        $pip install pyspark
        > Successfully installed py4j-0.10.7 pyspark-2.4.5

* init Spark Context Object
    
        see pyspark.py

* interact with Spark Shell

        cd to bin\pyspark in windows system 
        $pyspark

* doc

<https://spark.apache.org/docs/latest/quick-start.html>

<https://databricks.com/spark/getting-started-with-apache-spark>

* Dataset == DataFrame == Row

Spark’s primary abstraction is a distributed collection of items called a Dataset. 

Datasets can be created from Hadoop InputFormats (such as HDFS files) or by transforming other Datasets. 

Due to Python’s dynamic nature, we don’t need the Dataset to be strongly-typed in Python. As a result, all Datasets in Python are Dataset[Row], and we call it DataFrame to be consistent with the data frame concept in Pandas and R. 

Let’s make a new DataFrame from the text of the README file in the Spark source directory:

         textFile = spark.read.text("README.md")

----------------------------------------------------------------------------------

# Map Reducer, 運算框架

    遇到較為複雜的 code 而透過 disk 處理時，可使用此框架。

----------------------------------------------------------------------------------

# Spark Streaming Processor, 串流處理

   * 適用情境: streaming-formated file such as logfiles and internet status records.

   * 重要屬性: load balance, thoughput, extensible

   * 交互工具: 硬碟資料與串流資料的切換

----------------------------------------------------------------------------------

# Spark SQL, 資料庫即時互動式查詢

    using HQL, Hive QL

----------------------------------------------------------------------------------

# Spark ML, 機器學習

  (to be continued...)