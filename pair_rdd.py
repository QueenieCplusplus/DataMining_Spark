# using pyspark
# create a tuple as pair rdd in return
# by Queenie Chen
# on 2020.3/17 ~ 3/18
# Duration : 2 work days

from pyspark import sc

lines = sc.textFile("./README.md")
pairs_byFirst_string_inLine = lines.map(lambda a: (a.split("")[0], a))

# in scala, val pairs_byFirst_string_inLine = lines.map(a => (a.split("")[0], a))

# create pair RDD
# tuples:(k, v)
qs_pair_rdd = sc.parallelize({(1, 2), (3, 4), (3, 6)})

# pair rdd'S ATTRS
show_key = qs_pair_rdd.keys()
show_val = qs_pair_rdd.values()

# sort
sorted_res = qs_pair_rdd.sortByKey()

# rdd.reduceByKey(func_called)
qs_pair_rdd.reduceByKey(lambda a, b : a + b)
# in lambda, qs_pair_rdd.reduceByKey((a, b) => a + b)

# filter
# return result will not contain the result with valuesm length greater than 5
result = qs_pair_rdd.filter(lambda v: len(v)<5)

# mapValues(func_called) as same as map{case(k, v): (k, func(v))}
# to compute in val, not compute in key
qs_pair_rdd.mapValues(lambda v: v + 1)
# {(1, 3), (3, 5), (3, 7)}

# flatMapValues(func_called)
# looper

# subtractByKey(other_pair_rdd)
# delete the pair RDD by the same key matched
qs_pair_rdd.subtractByKey({3, 0})
# {(1, 2)}

# join()
# inner join
qs_pair_rdd.join({3, 9})
# {(3, (4, 9)), (3, (6, 9))}

# other 
# rightOuterJoin
# leftInnerJoin
# cogroup


