"""
CODE TO BE RUN ON THE CLUSTER

"""

from pyspark import SparkContext
from pyspark.sql import SQLContext
import pyspark.sql.functions as sf

if __name__=='__main__':
    sc = SparkContext()
    sqlContext = SQLContext(sc)

    dfTweets = sqlContext.read.load('samplestream_twt.jsonl', format='json')

    status = dfTweets.select('retweeted_status.entities.urls.url', 'retweeted_status.id_str', 'retweeted_status.lang',
                             'retweeted_status.favorite_count', 'retweeted_status.retweet_count',
                             'retweeted_status.text')

    retweet_status = dfTweets.select('place.bounding_box', 'place.full_name')
    retweet_status.registerTempTable('toplocations')

    occurrence = sqlContext.sql('select bounding_box, full_name, count(full_name) as occurrence from toplocations group by full_name, bounding_box').dropna()
    toploc = occurrence.orderBy('occurrence', ascending=False)  # order by descending order based on occurrence

    toploc.rdd.saveAsTextFile('/user/eames01/TopLocations/toplocationsout', encoding='utf-8')

