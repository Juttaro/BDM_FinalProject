from pyspark import SparkContext
from pyspark.sql import SQLContext
import pyspark.sql.functions as sf

if __name__ == '__main__':
    sc = SparkContext()
    sqlContext=SQLContext(sc)
    #load json object as sqlContext
    df1 = sqlContext.read.load('/user/dobi000/project/Datasets/trumpTwitter/dataset1_may15.jsonl', format='json')
    df2 = sqlContext.read.load('/user/dobi000/project/Datasets/trumpTwitter/dataset2_may15.jsonl', format='json')
    df3 = sqlContext.read.load('/user/dobi000/project/Datasets/trumpTwitter/dataset3_may16.jsonl', format='json')

    df4 = sqlContext.read.load('/user/dobi000/project/Datasets/trumpTwitter/dataset4_may18.jsonl', format='json')

    df5 = sqlContext.read.load('/user/dobi000/project/Datasets/trumpTwitter/dataset5_may21.jsonl', format='json')

    # DataSet 1
    timeline1 = df1.select('retweeted_status.created_at').dropna()
    timeline1 = timeline1.select(timeline1.created_at.substr(sf.length(timeline1.created_at)-25, sf.length(timeline1.created_at)-27).alias("Month")\
               ,timeline1.created_at.substr(sf.length(timeline1.created_at)-4, sf.length(timeline1.created_at)).alias("Year"))
    timeline1 = timeline1.select(sf.concat(timeline1.Month, timeline1.Year).alias('date'))

    # DataSet 2
    timeline2 = df2.select('retweeted_status.created_at').dropna()
    timeline2 = timeline2.select(timeline2.created_at.substr(sf.length(timeline2.created_at)-25, sf.length(timeline2.created_at)-27).alias("Month")\
               ,timeline2.created_at.substr(sf.length(timeline2.created_at)-4, sf.length(timeline2.created_at)).alias("Year"))
    timeline2 = timeline2.select(sf.concat(timeline2.Month, timeline2.Year).alias('date'))

    # DataSet 3
    timeline3 = df3.select('retweeted_status.created_at').dropna()
    timeline3 = timeline3.select(timeline3.created_at.substr(sf.length(timeline3.created_at)-25, sf.length(timeline3.created_at)-27).alias("Month")\
               ,timeline3.created_at.substr(sf.length(timeline3.created_at)-4, sf.length(timeline3.created_at)).alias("Year"))
    timeline3 = timeline3.select(sf.concat(timeline3.Month, timeline3.Year).alias('date'))

    # DataSet 4
    timeline4 = df4.select('retweeted_status.created_at').dropna()
    timeline4 = timeline4.select(timeline4.created_at.substr(sf.length(timeline4.created_at)-25, sf.length(timeline4.created_at)-27).alias("Month")\
               ,timeline4.created_at.substr(sf.length(timeline4.created_at)-4, sf.length(timeline4.created_at)).alias("Year"))
    timeline4 = timeline4.select(sf.concat(timeline4.Month, timeline4.Year).alias('date'))

    # DataSet 5
    timeline5 = df5.select('retweeted_status.created_at').dropna()
    timeline5 = timeline5.select(timeline5.created_at.substr(sf.length(timeline5.created_at)-25, sf.length(timeline5.created_at)-27).alias("Month")\
               ,timeline5.created_at.substr(sf.length(timeline5.created_at)-4, sf.length(timeline5.created_at)).alias("Year"))
    timeline5 = timeline5.select(sf.concat(timeline5.Month, timeline5.Year).alias('date'))

    # combine DataSet1, DataSet2 and DataSet3
    dfu1 = timeline1.union(timeline2)
    dfu2 = timeline3.union(timeline4)
    dfu3 = dfu1.union(dfu2)
    dfRecord = dfu3.union(timeline5)
    #Group by and Order by counts
    dfRecord = dfRecord.groupBy('date').count().orderBy('count', ascending = False)
    dfRecord = dfRecord.select('date', dfRecord['count'].alias('retweet_Monthly'))


    ''' Save as a textFile'''
    dfRecord.rdd.saveAsTextFile('/user/dobi000/project/Datasets/trumpResults/trumpTimeline')
