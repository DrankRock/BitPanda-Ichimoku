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
*This example was obtained with the mode "month" on the default file, on the 10th March 2022*

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



multi-threading, the possibility to use proxies, I'll add another projects of mine to find proxies online, check them, use them, for a completely automatic proxy rotating use, I'll also add the RSI index to the results, to add strength to any conclusion.