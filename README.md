# BitPanda-Ichimoku
 An Automated Ichimoku Kinko Hyo Calculator using BitPanda's API

## Usage
`python BP_Ichimoku.py -i <input file> -m <mode> `  
**default values**  
`input = BitPanda_All_Ticker.txt ; mode = month`  

### Arguments
**input**  
A file containing a list of tickers to check on BitPanda. The default file contains every one of them. If it's incomplete, you can update it running :  
`sh BitPandaIdGather.sh`

**mode**  
Defines the time-span on which to apply the ichimoku. The available mode on BitPanda are :
`day, week, month, year`.   
To execute every modes, chose the mode `all`  

### Results
*This example was obtained with the mode "all" on the file head10.txt, on the 11th March 2022 at 20:35*
```text
 -- [number] -- Ticker -- Kumo value -- RSI value
[info]  Top 10 in day mode :  
 -- [1] -- BRK = 0.9165879029569624 -- 51.246001041726124  
 -- [2] -- TSM = -0.8372280611233123 -- 50.60346918106628  
 -- [3] -- AAPL = -1.6267299671542048 -- 67.96743515145465  
 -- [4] -- MSFT = -1.94036700596439 -- 54.22527235342231  
 -- [5] -- FB = -2.476815636809306 -- 67.43878686703903  
 -- [6] -- NVDA = -2.6592955762589554 -- 58.128378184302285  
 -- [7] -- UNH = -3.856274186129099 -- 54.62049722193833  
 -- [8] -- AMZN = -12.735898299953988 -- 61.56911256895072  
 -- [9] -- TSLA = -18.54016116821117 -- 44.395430681469435  
 -- [10] -- GOOGL = -23.155150902140576 -- 55.24326662327064  
[info]  Top 10 in week mode :  
 -- [1] -- AMZN = 102.11750638013746 -- 54.49041003776589  
 -- [2] -- GOOGL = 55.548431533530675 -- 41.66561250462884  
 -- [3] -- NVDA = 5.764227794923158 -- 43.649256269754126  
 -- [4] -- UNH = 5.100439446665234 -- 36.29176198846919  
 -- [5] -- MSFT = 5.011016419564271 -- 47.09307277278864  
 -- [6] -- BRK = 3.6588840558962374 -- 62.294780230951254  
 -- [7] -- TSM = 1.9598969106536543 -- 32.3458792547556  
 -- [8] -- AAPL = -0.661307431346529 -- 39.36923791747966  
 -- [9] -- FB = -0.6831329552618968 -- 38.87936107507789  
 -- [10] -- TSLA = -2.490836647787887 -- 23.45533316770873 (oversold)  
[info]  Top 10 in month mode :  
 -- [1] -- BRK = 6.15555385147195 -- 61.63770307526736  
 -- [2] -- UNH = 6.035457535242699 -- 48.32686187001535  
 -- [3] -- TSLA = 0.7955950818047768 -- 40.77153334752654  
 -- [4] -- AAPL = -5.109862676923399 -- 37.73444037173789  
 -- [5] -- MSFT = -7.00168403915751 -- 48.80927118268493  
 -- [6] -- TSM = -8.996726550958954 -- 47.56752108024391  
 -- [7] -- FB = -13.283855580698344 -- 37.447971992540204  
 -- [8] -- NVDA = -14.054835562914406 -- 50.01193611322161  
 -- [9] -- GOOGL = -50.77032968819594 -- 53.4294464953253  
 -- [10] -- AMZN = -91.26220060015157 -- 57.208053119754986  
[info]  Top 10 in year mode :  
 -- [1] -- BRK = 8.626563720928004 -- 69.66632038170592  
 -- [2] -- UNH = 1.8711792159999732 -- 69.03712051104475  
 -- [3] -- AAPL = -5.117369635624698 -- 48.66958534543855  
 -- [4] -- TSM = -13.5300604521087 -- 45.22737413108865  
 -- [5] -- MSFT = -16.778564589470648 -- 56.48183325471938  
 -- [6] -- NVDA = -27.40347491221968 -- 51.35592013619708  
 -- [7] -- FB = -39.25301778836513 -- 48.39695006315677  
 -- [8] -- GOOGL = -54.70977693349323 -- 61.777277349655556  
 -- [9] -- AMZN = -130.4976678959797 -- 53.59128801986476  
 -- [10] -- TSLA = -139.8777482854507 -- 51.31694806550492  
 ```

### Side Note
- The parameters of the Ichimoku are 10-30-60 if there are 60 or more values given by the API.  
If not, the values are (total number/6) - (total number/2) - (total number)  
- I have near to no knoledge in trading and have never actually invested in anything found to be worth by this script.  

## What next ?
In the next updates, I'll add : 
-> Multi-threading  
-> Proxies  
-> Auto Proxies  
-> RSI Index  
-> single Ticker as Argument  
-> Output file  
-> Debug Mode  


## Contact
For any feedback, improvement I could make, bug you found, or just to talk, you can contact me on [my Discord server]().


