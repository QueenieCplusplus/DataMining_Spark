# using pyspark
# map() usage in frequently-used transformation & Actions
# by Queenie Chen
# on 2020.3/17 ~ 3/18
# Duration : 2 work days

from pyspark import sc

# map() looks like filter(), but filter() only pass the ele that can be handled in the passing func
# the type of return rdd can be different from the type of input of the map()

parl_nums = sc.parallelize([0, 1, 2, 3, 4, 5]) 
sqrt_nums = parl_nums.map(lambda x: x * x).collect()
print(sqrt_nums.first())
# in scala, sqrt_nums = parl_nums.map(x => x * x).collect()


# flatMap() can handle the result with Iterator
parl_lines = sc.parallelize(["pou pou", "patty appier", "kate", "queen Py"])
words = parl_lines.flatMap(lambda l: l.split(""))
print(words.first())
# in scala, val words = parl_lines.flatMap(l => l.split(""))


