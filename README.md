# PageRank
Comparison of Spark and Pig on PageRank

# Spark

Using PageRank implementation offered as [example](https://github.com/apache/spark/blob/master/examples/src/main/java/org/apache/spark/examples/JavaPageRank.java).

*Will change to the normal one*

# Pig

Using PageRank available [here](https://hortonworks.com/blog/pagerank-implementation-in-pig/). Modified so I could use the same datasources as Spark.

*Will change to [dataFu's](https://datafu.apache.org/) if I can compile it*

# Datas

Input graphs goes to data/graphsPageRank.

Results arrived in result_data/graphsPageRank for Pig and results_data/Spark for Spark. Times are in res.log file of each experiments.

Graphs generation can be done with:

```
python scripts/genData.py NumberOfSites AverageLinks
```

Every sites will have around the same number of links (on average) and the targets are randomly chosen.
