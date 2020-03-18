# using pyspark
# create a tuple as pair rdd in return
# by Queenie Chen
# on 2020.3/17 ~ 3/18
# Duration : 2 work days

from pyspark import sc

qs_pair_rdd = sc.parallelize({(1, 2), (3, 4), (3, 6)})

#rdd.lookup(key)
#return array of val
qs_pair_rdd.lookup(3)
#[4, 6]

#rdd.collectAsMap()
# return value in Map{}
qs_pair_rdd.collectAsMap((1, 2), (3, 4), (3, 6))

#rddd.countByKey()
# return result of rdd counts num based on key
# result: (key, countsNum) as tuples in {}
qs_pair_rdd.countByKey()
# {(1, 1), (3, 2)}

