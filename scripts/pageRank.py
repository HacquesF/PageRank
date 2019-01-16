#!/usr/bin/python
from org.apache.pig.scripting import *
P = Pig.compile("""

oldRank = LOAD '$docs_in' USING PigStorage(' ') AS ( url: chararray, rank: float, links:{ link: ( url: chararray ) } );


sumRank = FOREACH oldRank GENERATE rank/COUNT(links) AS rank, FLATTEN(links) as to_url;
newRank = FOREACH( COGROUP sumRank BY to_url,oldRank BY url INNER) GENERATE group AS url, 0.15 + 0.85*SUM(sumRank.rank) as pagerank, FLATTEN(oldRank.links) AS links;


STORE newRank
INTO '$docs_out'
USING PigStorage(' ');
""")

params = { 'docs_in': 'data/pagerank_data_simple' }

for i in range(10):
    out = "out/pagerank_data_" + str(i + 1)
    params["docs_out"] = out
    Pig.fs("rmr " + out)
    stats = P.bind(params).runSingle()
    params["docs_in"] = out
    if not stats.isSuccessful():
        raise 'failed'
