import json
import sys
import re
import urllib
from bs4 import BeautifulSoup

def opentoNum(string):
    str=re.sub(',', '', string)
    return int(str)

def contractAsJson(filename):
    jsonQuoteData = {}
    newfile= open(filename)
    soup =BeautifulSoup(newfile,"html.parser")

    for price in soup.find_all(class_="time_rtq_ticker"):
        currPrice = float(price.string)
    #print(currPrice)

    dateUrls=[]
    yahoo_string="http://finance.yahoo.com"
    for link in soup.find_all('a'):
        hrefvalue= str(link)#(link.get('href'))
        if re.search("^<a href=\"/q/o.{10,22}-(\d){2}", hrefvalue):
            hrefvalue=hrefvalue.split("\"")
            #print((hrefvalue)
            dateUrls.append(yahoo_string + hrefvalue[1])
    #print (dateUrls)

    optionQuotes=[]
    logs=[]
    log_count=0
    for tag in soup.find_all(class_="yfnc_datamodoutline1"):
        for big_row in tag.find_all('tr'):
            for row in big_row.find_all('tr'):
                log_count += 1
                rows=[]
                for col in row.find_all('td'):
                    if (col.string!=None):
                        rows.append(col.string)
                    else:
                        change_object=col.span.b
                        str_change=change_object.string
                        change_color=change_object.get('style')
                        if(change_color=="color:#cc0000;"):
                            str_change ="-" + str_change
                        elif (change_color=="color:#008800;"):
                            str_change ="+" + str_change
                        else:
                            str_change = " " + str_change
                        rows.append(str_change)
                if (len(rows)!=0):
                    rows.append(log_count)
                    logs.append(rows)

    #print(logs)
    logs= sorted(logs, key=lambda x:(-opentoNum(x[-2]),x[-1]))
    for optionQuoteslog in logs:
        optionQuotesdict = {}
        date_value=optionQuoteslog[1][-15:-9]
        type_value=optionQuoteslog[1][-9]
        symol_value=optionQuoteslog[1][:-15]

        optionQuotesdict['Ask']= optionQuoteslog[5]
        optionQuotesdict['Bid']= optionQuoteslog[4]
        optionQuotesdict['Change'] = optionQuoteslog[3]
        optionQuotesdict['Date'] = date_value
        optionQuotesdict['Last'] = optionQuoteslog[2]
        optionQuotesdict['Open'] = optionQuoteslog[7]
        optionQuotesdict['Strike'] = optionQuoteslog[0]
        optionQuotesdict['Symbol'] = symol_value
        optionQuotesdict['Type'] = type_value
        optionQuotesdict['Vol'] = optionQuoteslog[6]
        optionQuotes.append(optionQuotesdict)
    #print(optionQuotes)

    jsonQuoteData['currPrice']=currPrice
    jsonQuoteData['dateUrls'] = dateUrls
    jsonQuoteData['optionQuotes'] = optionQuotes
    return json.dumps(jsonQuoteData)

#contractAsJson("aapl.dat")