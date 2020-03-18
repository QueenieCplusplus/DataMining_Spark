# using pyspark
# create a tuple as pair rdd in return
# by Queenie Chen
# on 2020.3/17 ~ 3/18
# Duration : 2 work days

from pyspark import sc

# partitionBy(2) - splitting data into 2 chunks using default hash partitioner,

# hash_part = HashPartitioner(100)

link_RDD = sc.objectFile(['']).partitionBy(100).persist()

# 初始化 rank = 1.0
# 使用 mapValues()
# 讓 link_RDD 與 rank 有相同的 Partioner


# below for-loop seems error in syntax, plz re-code


mapper = lambda pageLink.map{d: d, rank/pageLink.size} if pageID, (pageLink, rank)

rank = link_RDD.mapValues(v = 1.0) 

for i in range(0, 11):

    contribution = link_RDD.join(rank).flatMap(mapper)

    rank =contribution.reduceByKey(lambda x, y: x + y).mapValues(v: 0.15 + 0.85*v)

rank.saveAsTextFile("rank")