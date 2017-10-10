# Statistics for Engineers

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

* 2015-05-14 [SRECon15](https://www.usenix.org/conference/srecon15europe/program), Dublin, Ireland
* 2015-07-29 [StatsCraft](http://www.statscraft.org.il/), Tel-Aviv, Israel
* 2015-10-28 [Velocity](http://velocityconf.com/devops-web-performance-eu-2015/public/schedule/detail/45241), Amsterdam, Netherlands
* 2016-06-12 [SRECon16](https://srecon16europe.sched.org/event/7VkQ/statistics-for-engineers), Dublin, Ireland

Discussin on Twitter [#StatsForEngineers](https://twitter.com/search?q=%23statsforengineers&src=typd)

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

## Slides for an earlier version

1. [Descriptive Statistics](Part_I_Descriptive_Statistics.ipynb)
2. [Data Handling Tools](Part_II_Data_Handling.ipynb)
3. [Hands on](Part_III_Hands_On_Session.ipynb)

## DataSets

* [dc1cpu.csv](DataSets/dc1cpu.csv) - CPU utilization of a machine cluster

```
|-------------+-------------------+-------------------+-------------------+-------------------+-------------------+--------------------|
|  column1    | column2           | column3           | column4           | column5           | column6           | column7            |
|-------------+-------------------+-------------------+-------------------+-------------------+-------------------+--------------------|
|  1430033280 | 0.466690003871918 | 0.449970006942749 | 0.5               | 0.516683876514435 | 0.515455365180969 | 0.500216782093048  |
|  1430033340 | 0.46674445271492  | 0.466666668653488 | 0.500008344650269 | 0.516253650188446 | 0.534678936004639 | 0.499875038862228  |
|  1430033400 | 3.18041801452637  | 2.71607828140259  | 6.02768754959106  | 5.95377063751221  | 0.548345804214478 | 0.599810063838959  |
|  1430033460 | 3.40147399902344  | 6.5851993560791   | 3.97570967674255  | 3.18354558944702  | 6.15220022201538  | 5.7498083114624    |
|  1430033520 | 0.466830044984817 | 0.58323609828949  | 0.483365565538406 | 0.516658067703247 | 3.1507351398468   | 3.78554153442383   |
|  1430033580 | 0.466658890247345 | 0.566628873348236 | 0.499875038862228 | 0.516632199287415 | 1.16660833358765  | 0.499916672706604  |
|  1430033640 | 1.24981248378754  | 0.583012700080872 | 0.500125050544739 | 0.500066697597504 | 0.899835050106049 | 0.500016689300537  |
```

* [LogDB.out](DataSets/LogDB.out) - DB log file

```
192.168.13.72 - - [08/May/2015:12:00:00 -0000] "POST /doc/0 HTTP/1.1" 200 138 0.155
192.168.13.85 - - [08/May/2015:12:00:00 -0000] "PUT /doc/1 HTTP/1.1" 200 265 11.933
192.168.13.75 - - [08/May/2015:12:00:00 -0000] "POST /doc/2 HTTP/1.1" 200 138 1.190
192.168.13.85 - - [08/May/2015:12:00:01 -0000] "PUT /doc/1 HTTP/1.1" 200 265 34.552
192.168.13.13 - - [08/May/2015:12:00:01 -0000] "GET /doc/3 HTTP/1.1" 200 4047 0.394
192.168.13.13 - - [08/May/2015:12:00:01 -0000] "GET /doc/4 HTTP/1.1" 200 795 0.080
192.168.13.85 - - [08/May/2015:12:00:01 -0000] "PUT /doc/1 HTTP/1.1" 200 265 11.649
```

* [LogDB.csv](DataSets/LogDB.csv) - Parsed into CSV
  
```
|----------+-----------+---------+---------+-------------|
|  column1 | column2   | column3 | column4 | column5     |
|----------+-----------+---------+---------+-------------|
|  POST    | /doc/0    | 200     | 138     | 0.155       |
|  PUT     | /doc/1    | 200     | 265     | 11.933      |
|  POST    | /doc/2    | 200     | 138     | 1.190       |
|  PUT     | /doc/1    | 200     | 265     | 34.552      |
|  GET     | /doc/3    | 200     | 4047    | 0.394       |
|  GET     | /doc/4    | 200     | 795     | 0.080       |
|  PUT     | /doc/1    | 200     | 265     | 11.649      |
```

* [API_latencies.csv](DataSets/API_latencies.csv) - API latency for individual requests

```
|----------------+---------------+---------------+----------------|
|  column1       | column2       | column3       | column4        |
|----------------+---------------+---------------+----------------|
|  20.7694780928 | 20.0139839886 | 20.9794136042 | 205.000103604  |
|  20.4130138094 | 20.482340238  | 20.6106162853 | 208.849332291  |
|  20.6498944701 | 20.9024087799 | 20.3754038448 | 207.779212163  |
|  20.3340033224 | 20.4109110099 | 20.4158256865 | 202.737921956  |
|  20.8329489288 | 20.205855921  | 20.454802266  | 202.438354752  |
|  20.8080852905 | 20.5305048738 | 20.0643793944 | 2025.80376526  |
|  20.3396761932 | 20.1682249129 | 20.1209775532 | 2096.88699047  |
```

* [ReqMultiNode.csv](DataSets/ReqMultiNode.csv) - Request rates for a cluster of nodes

```
|-------------+-------------------+-------------------+-------------------+-------------------+-------------------+--------------------|
|  column1    | column2           | column3           | column4           | column5           | column6           | column7            |
|-------------+-------------------+-------------------+-------------------+-------------------+-------------------+--------------------|
|  1398756900 | 1.21666705608368  | 0.99666702747345  | 1.23333299160004  | 0.883333027362824 | 1.03666305541992  | 1.02333295345306   |
|  1398757200 | 1.14333295822144  | 0.866666972637176 | 1.12999999523163  | 0.866666972637176 | 0.939999997615814 | 0.943333029747009  |
|  1398757500 | 1.05333304405212  | 0.836667001247406 | 1.06666696071625  | 0.77999997138977  | 0.963337004184723 | 0.906666994094849  |
|  1398757800 | 1.03333294391632  | 0.863332986831665 | 1.09333300590515  | 0.773333013057709 | 0.899999976158142 | 0.866666972637176  |
|  1398758100 | 0.989997029304504 | 0.77666699886322  | 1.13999998569489  | 0.816667020320892 | 0.896667003631592 | 0.860000014305115  |
|  1398758400 | 1.41667103767395  | 1.0900000333786   | 1.49666702747345  | 1.05333304405212  | 1.24666202068329  | 1.13666701316834   |
|  1398758700 | 0.773330986499786 | 0.716666996479034 | 0.836667001247406 | 0.60666698217392  | 0.766667008399963 | 0.743332982063294  |
```

* [WebLatency.csv](DataSets/WebLatency.csv) - Ping latencies for a server measured from different locations

```
|-------------+------------------+------------------+------------------+------------------+---------+-------------------|
|  column1    | column2          | column3          | column4          | column5          | column6 | column7           |
|-------------+------------------+------------------+------------------+------------------+---------+-------------------|
|  1422761400 | 42               | 180.6            | 309.8            | 182.6            | 218.4   | 224.8             |
|  1422761700 | 41.8             | 125.2            | 303.2            | 181.4            | 215.8   | 229               |
|  1422762000 | 42               | 177              | 303              | 181.6            | 231.4   | 229.2             |
|  1422762300 | 41.8             | 118              | 313.8            | 182              | 229.2   | 230.4             |
|  1422762600 | 41.8             | 118              | 310.8            | 184.4            | 214.4   | 227.4             |
|  1422762900 | 41.8             | 112.6            | 324              | 184.6            | 227.8   | 228.6             |
|  1422763200 | 41.6             | 114.2            | 312.8            | 183.4            | 215.2   | 227               |
```
