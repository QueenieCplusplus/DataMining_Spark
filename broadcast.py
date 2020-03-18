# using pyspark
# create a tuple as pair rdd in return
# by Queenie Chen
# on 2020.3/17 ~ 3/18
# Duration : 2 work days

from pyspark import sc


def broadcast[T](value: T): Broadcast[T]

# Broadcast a read-only variable to the cluster, returning a spark.
# Broadcast object for reading it in distributed functions.
# to do 