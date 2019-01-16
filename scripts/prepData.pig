/*prepData.pig */
lines = LOAD 'data/curGraph.txt' USING PigStorage(' ') as (url:chararray, link:chararray);
url_list = GROUP lines by url;
data_ready = FOREACH url_list GENERATE group as url,1.0 as rank,lines.link as links;

STORE data_ready
INTO 'data/pagerank_data_simple'
USING PigStorage(' ');
