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

* download spark pkg tgz 

https://archive.apache.org/dist/spark/spark-2.4.0/?C=M;O=A

choose => 

    spark-2.4.0-bin-without-hadoop.tgz  

Download the .tgz file to D:\Spark

* Set Env =>

    SPARK_HOME = D:\Spark\spark-2.4.0-bin-hadoop2.7 (tgz)

    PATH += D:\Spark\spark-2.4.0-bin-hadoop2.7\bin

* extract tar file =>

    $ cd D:\Spark\

    $ tar xvf spark-2.4.0-bin-hadoop2.7.tgz

    $ cd D:\Spark\spark-2.4.0-bin-hadoop2.7

    $ cd bin

    D:\Spark\spark-2.4.0-bin-hadoop2.7\bin$ .pyspark

* bug issued

    when using spark==2.4, python==3.7

    but bug issued, while running spark in bash.

https://xbuba.com/questions/53304303

* pip install

        $pip install pyspark
        > Successfully installed py4j-0.10.7 pyspark-2.4.5

* init Spark Context Object
    
        see pyspark.py

* interact with Spark Shell

        cd to bin\pyspark in windows system 
        $pyspark

* create my pyspark file & project 

    $cd <mySpark_Project_root>/

    $spark-shell

            20/03/18 09:51:13 ERROR Shell: Failed to locate the winutils binary in the hadoop binary path
            java.io.IOException: Could not locate executable null\bin\winutils.exe in the Hadoop binaries.
                    at org.apache.hadoop.util.Shell.getQualifiedBinPath(Shell.java:379)
                    at org.apache.hadoop.util.Shell.getWinUtilsPath(Shell.java:394)
                    at org.apache.hadoop.util.Shell.<clinit>(Shell.java:387)
                    at org.apache.hadoop.util.StringUtils.<clinit>(StringUtils.java:80)
                    at org.apache.hadoop.security.SecurityUtil.getAuthenticationMethod(SecurityUtil.java:611)
                    at org.apache.hadoop.security.UserGroupInformation.initialize(UserGroupInformation.java:273)
                    at org.apache.hadoop.security.UserGroupInformation.ensureInitialized(UserGroupInformation.java:261)
                    at org.apache.hadoop.security.UserGroupInformation.loginUserFromSubject(UserGroupInformation.java:791)      
                    at org.apache.hadoop.security.UserGroupInformation.getLoginUser(UserGroupInformation.java:761)
                    at org.apache.hadoop.security.UserGroupInformation.getCurrentUser(UserGroupInformation.java:634)
                    at org.apache.spark.util.Utils$$anonfun$getCurrentUserName$1.apply(Utils.scala:2422)
                    at org.apache.spark.util.Utils$$anonfun$getCurrentUserName$1.apply(Utils.scala:2422)
                    at scala.Option.getOrElse(Option.scala:121)
                    at org.apache.spark.util.Utils$.getCurrentUserName(Utils.scala:2422)
                    at org.apache.spark.SecurityManager.<init>(SecurityManager.scala:79)
                    at org.apache.spark.deploy.SparkSubmit.secMgr$lzycompute$1(SparkSubmit.scala:348)
                    at org.apache.spark.deploy.SparkSubmit.org$apache$spark$deploy$SparkSubmit$$secMgr$1(SparkSubmit.scala:348) 
                    at org.apache.spark.deploy.SparkSubmit$$anonfun$prepareSubmitEnvironment$7.apply(SparkSubmit.scala:356)     
                    at org.apache.spark.deploy.SparkSubmit$$anonfun$prepareSubmitEnvironment$7.apply(SparkSubmit.scala:356)     
                    at scala.Option.map(Option.scala:146)
                    at org.apache.spark.deploy.SparkSubmit.prepareSubmitEnvironment(SparkSubmit.scala:355)
                    at org.apache.spark.deploy.SparkSubmit.org$apache$spark$deploy$SparkSubmit$$runMain(SparkSubmit.scala:774)  
                    at org.apache.spark.deploy.SparkSubmit.doRunMain$1(SparkSubmit.scala:161)
                    at org.apache.spark.deploy.SparkSubmit.submit(SparkSubmit.scala:184)
                    at org.apache.spark.deploy.SparkSubmit.doSubmit(SparkSubmit.scala:86)
                    at org.apache.spark.deploy.SparkSubmit$$anon$2.doSubmit(SparkSubmit.scala:920)
                    at org.apache.spark.deploy.SparkSubmit$.main(SparkSubmit.scala:929)
                    at org.apache.spark.deploy.SparkSubmit.main(SparkSubmit.scala)
            20/03/18 09:51:13 WARN NativeCodeLoader: Unable to load native-hadoop library for your platform... using builtin-java classes where applicable
            Using Spark's default log4j profile: org/apache/spark/log4j-defaults.properties
            Setting default log level to "WARN".
            To adjust logging level use sc.setLogLevel(newLevel). For SparkR, use setLogLevel(newLevel).
            Spark context Web UI available at http://MIS0-24.concords.com.tw:4040
            Spark context available as 'sc' (master = local[*], app id = local-1584496280854).
            Spark session available as 'spark'.
            Welcome to
                  ____              __
                / __/__  ___ _____/ /__
                _\ \/ _ \/ _ `/ __/  '_/
              /___/ .__/\_,_/_/ /_/\_\   version 2.4.5
                  /_/

            Using Scala version 2.11.12 (Java HotSpot(TM) 64-Bit Server VM, Java 1.8.0_211)
            Type in expressions to have them evaluated.
            Type :help for more information.

            scala> 

* doc

<https://spark.apache.org/docs/latest/quick-start.html>

<https://databricks.com/spark/getting-started-with-apache-spark>

<https://medium.com/big-data-engineering/how-to-install-apache-spark-2-x-in-your-pc-e2047246ffc3>

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
