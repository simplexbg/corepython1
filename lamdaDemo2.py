from pyspark.sql import *
from pyspark.sql.functions import *
import findspark
from pyspark import SparkContext
from pyspark.streaming import StreamingContext

sc = SparkContext('local[2]','NetworkWorkCount')
ssc = StreamingContext(sc,1)
lines = ssc.socketTextStream('localhost',9999)
words = lines.flatMap(lambda line:line.split(' '))
print(words)
pairs = words.map(lambda word:(word,1))
word_counts = pairs.reduceByKey(lambda num1,num2:num1+num2)
word_counts.pprint()
ssc.start()

