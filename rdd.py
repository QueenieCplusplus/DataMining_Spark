# using pyspark
# RDD Wrangling
# by Queenie Chen
# on 2020.3/17 ~ 3/18
# Duration : 2 work days

from pyspark import sc

# create RDD from normal data type such as array_list or set 從外部資料建立 rdd
lines = sc.textFile("./README.md")

# parallelize 平行處理已經存在的資料集合
p_lines = sc.parallelize(["pandas", "numpy", "spark", "b4soup"])
# as same as p_lines = sc.parallelize(list("pandas", "numpy", "spark", "b4soup")) in scala

# persit 保留以備於未來的重複性使用
# as same as calling cache()
lines.persist()

# actions in parallel 啟動平行化運算
lines.count()
lines.first()
# u' ## 'word....'

# transformat via filter()
# return RDD too
# all the action is element-wise 具備元素感知的
# filter not mute the original rdd,
# return a new pointer to rdd
input_rdd = sc.textFile("./README.md")
err_rdd = input_rdd.filter(lambda v: "err" in v)

