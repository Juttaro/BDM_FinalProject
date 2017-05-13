from pyspark import SparkContext

if __name__=='__main__':
    sc = SparkContext()
    rdd = sc.textFile('emma.txt')
    words = rdd.flatMap(lambda x: x.split())
    result = words.map(lambda w: (w, 1))
    result = result.reduceByKey(lambda x, y: x + y)
    result.saveAsTextFile('testfolder')


