# using pyspark
# create a tuple as pair rdd in return
# by Queenie Chen
# on 2020.3/17 ~ 3/18
# Duration : 2 work days

from pyspark import sc


def accumulator[T](initialValue: T)(implicit param: AccumulatorParam[T]): Accumulator[T]

# Create an Accumulator variable of a given type, 
# which tasks can "add" values to using the += method.

# to do 