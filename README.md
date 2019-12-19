# DataMining_Spark
擁有泛化運算引擎的叢集管理平台，是資料科學家的好工具！

此資料庫系統，跟 C＊ 不同之處在於，更多的語言支援，不僅限於 Java，還包含 Python 和 Scala。

另外， Spark 可以存取 Hadoop 和 Cassandra 這樣的資料存儲來源。

# 數據處理的各種應用

改良 Hadoop 的運算框架 MapReduce，此資料庫引擎的查詢度執行效率加快，而且擁有豐富的 API，可以做更多的巨量資料處理的相關運用，例如 

    * Iterator, 迭代

    * Batch Process, 批次處理

    * Interactive Query, 交互式查詢

    * Stream Process, 串流

    * ML, 機器學習

    * Graph Process, 影像處理

因為它能充分利用記憶體，故處理速度很快，能處理大量資料，倘若遇到複雜的應用程式，需要透過硬碟處理工作任務時， Spark 也會比 Hadoop 的 MapReduce 來得有效率。

# 叢集管理平台整合的元件


這些功能元件都能與 Spark 核心完美地一起運作。


                HQL      Stream      ML      Graph Process


                               Spark Core


                     Scheduler        Yarn       Mesos

# RDD, 核心元件

Resilient Distributed Dataset 彈性分散式資料就是 Spark 的核心！



(To Be Done...)
