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

### Side Note
The parameters of the Ichimoku are 10-30-60 if there are 60 or more values given by the API.  
If not, the values are (total number/6) - (total number/2) - (total number)

