# using pyspark
# pass a method with ref to a field
# by Queenie Chen
# on 2020.3/17 ~ 3/18
# Duration : 2 work days

from pyspark import sc

# Not Do !
# Danger
# this ref to field
# ref to Globe ~
class sparkFunc(object):

    def __init__(self, query_key):
        self.query_ky = query_key

    def isMatch(self, one_in_any):
        return self.query_ky in one_in_any 
        # return result in Bool

    def get_Matched_Ref(self, rdd):
        return rdd.filter(self.isMatch)
        # self.isMatch ref to all the self

# Recommend DO
# Safer than above class 
# recommend not to ref to field
# ref to Local ~
class sparkFuncNoRef(object):

    def __init__(self, query_key):
        self.globe_query = query_key
    
    def getMathed(self, rdd):
        local_query =  self.globe_query
        return rdd.filter(lambda x: local_query in x)





