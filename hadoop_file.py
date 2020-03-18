# using pyspark
# create a tuple as pair rdd in return
# by Queenie Chen
# on 2020.3/17 ~ 3/18
# Duration : 2 work days

from pyspark import sc

def hadoopFile[K, V, F <: InputFormat[K, V]](path: String)(implicit km: ClassManifest[K], vm: ClassManifest[V], fm: ClassManifest[F]): RDD[(K, V)]

# Smarter version of hadoopFile() 
# that uses class manifests to figure out the classes of keys, values and the InputFormat 
# so that users don't need to pass them directly.
