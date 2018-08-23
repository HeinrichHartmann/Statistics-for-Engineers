# Statistics for Engineers

## Abstract

Gathering all kinds of telemetry data is key to operating reliable distributed systems at scale. Once you have set-up your monitoring systems and recorded all relevant data, the challenge becomes to make sense of it and extract valuable information, like:

* Are we fulfilling our SLA?
* How did our query response times change with the last update?

Statistics is the art of extracting information from data. In this tutorial, we address the basic statistical knowledge that helps you at your daily work as a system operator. We will cover probabilistic models, summarizing distributions with mean values, quantiles, and histograms and their relations. Also advanced topics like time series forecasting and scalability analysis will be touched.

The tutorial focuses on practical aspects and will give you hands on knowledge of how to handle, import, analyze, and visualize telemetry data with UNIX command line tools, gnuplot, and the iPython toolkit.

## Episodes

0. [Introduction](Episode%200%20--%20Introduction.ipynb)
1. [Visualizing Data](Episode%201%20--%20Visualizing%20Data.ipynb)
2. [Histograms](Episode%202%20--%20Histograms.ipynb)
3. [Summary Statistics](Episode%203%20--%20Summary%20Statistics.ipynb)
4. [Quantiles and Outliers](Episode%204%20--%20Quantiles%20and%20Outliers.ipynb)
5. [Forecasing](Episode%205%20--%20Forecasting.ipynb)

## Events

This workshop has been held in at a number of events in slightly different forms.

* 2018-08-29 [SRECon18](https://www.usenix.org/conference/srecon18europe), Düsseldorf, Germany
* 2016-06-12 [SRECon16](https://srecon16europe.sched.org/event/7VkQ/statistics-for-engineers), Dublin, Ireland
* 2015-10-28 [Velocity](http://velocityconf.com/devops-web-performance-eu-2015/public/schedule/detail/45241), Amsterdam, Netherlands
* 2015-07-29 [StatsCraft](http://www.statscraft.org.il/), Tel-Aviv, Israel
* 2015-05-14 [SRECon15](https://www.usenix.org/conference/srecon15europe/program), Dublin, Ireland

If you want to be informed about upcoming events consider watch out for the following hashtag on Twitter: [#StatsForEngineers](https://twitter.com/search?q=%23statsforengineers&src=typd)

## Further Reading

* Mathematics
  - Wasserman - All of Statistics: A Concise Course in Statistical Inference  
  - Downey - Think Stats: Probability and Statistics for Programmers  
  - Rice - Mathematical Statistics and Data Analysis (advanced)

* Tools
  - Janert - Data Analysis with Open Source tools
  - Janssens - Data Science at the Command Line (O'Reilly 2015)  
  - Johnson - Pro Bash Programming (Apress, 2009)
  - McKinney - Python for Data Anlaysis  


## Datasets

* [dc1cpu.csv](datasets/dc1cpu.csv) - CPU utilization of a machine cluster

* [LogDB.out](datasets/LogDB.out) - DB log file

* [LogDB.csv](datasets/LogDB.csv) - Parsed into CSV
  
* [API_latencies.csv](datasets/API_latencies.csv) - API latency for individual requests

* [ReqMultiNode.csv](datasets/ReqMultiNode.csv) - Request rates for a cluster of nodes

* [WebLatency.csv](datasets/WebLatency.csv) - Ping latencies for a server measured from different locations
