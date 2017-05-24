from pyspark import SparkContext
from pyspark.sql import SQLContext
import pyspark.sql.functions as sf

if __name__ == '__main__':
    sc = SparkContext()
    sqlContext=SQLContext(sc)
    dfhtag1 = sqlContext.read.load('/user/dobi000/project/Datasets/Twitter/stream_twt_may11.jsonl', format='json')
    timeline = dfhtag1.select('quoted_status.created_at').dropna()

    timeline = timeline.select(timeline.created_at.substr(sf.length(timeline.created_at)-25, sf.length(timeline.created_at)-27).alias("Month"),timeline.created_at.substr(sf.length(timeline.created_at)-4, sf.length(timeline.created_at)).alias("Year"))

    timeline = timeline.select(sf.concat(timeline.Month, timeline.Year).alias('date'))
    timeline = timeline.groupBy('date').count().orderBy('count', ascending = False)

    timeline.rdd.saveAsTextFile('/user/dobi000/project/Datasets/results/may11_quoted_timeline')
