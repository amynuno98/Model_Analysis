

#   Data Analysis of Forecast Models
##  Package consists of statistical analysis and accuracy check for forecast and/or nowcast data

##  Data Utilized 
###     Central & Northern California Ocean Observing System (CeNCOOS) Nowcast
###     Real-Time Ocean Forecast System (RTOFS) Forecast
###     SST Observed Data 'https://www.ndbc.noaa.gov/data/realtime2/46237.txt'
###     Salinity Observed Data 'http://www3.mbari.org/lobo/cgi-bin/GetLOBOData.exe?timeunit=SPECIFY&min_date=08012021&max_date=1132021&dataquality=GQ&station=M1SURF.TXT&x=day&y=salinity&autoscale=On&xmin=&xmax=&ymin=&ymax=&ystack=On&data_format=Text&submit=SEND'
###     Salinity Climatology 'https://coastwatch.pfeg.noaa.gov/erddap/griddap/hycom_GLBa008_tdyx.csv?salinity%5B(2009-01-01):1:(2017-12-31T23:59:59Z)%5D%5B(0.0):1:(0.0)%5D%5B(2000):1:(2000)%5D%5B(2050):1:(2050)%5D'

###Model_Analysis.ipynb

description: notebook example of use of functions found in model_analysis.py

input: 
    2 Forecasts/Nowcasts, Climatology, Observed Data Sets
output:
    Precision, Recall, Accuracy, F1 Score for Both Forecasts/Nowcasts
    Produces plot with both Forecasts/Nowcasts, 2 standard deviations, Observed Data, Climatology

![github image](https://github.com/amynuno98/Model_Analysis/blob/11746d0b9b30f350b94346be4d5aef8205f82979/images/SalinityForcastAnalysis.png)

### Forecast_Stats_Analysis.ipynb
description: notebook example of use of functions found in statistical_analysis.py

input:
    Forecasts and Observed Data
output:
    Mean Bias, Root Mean Squared Error, Percent Gross Error
    and Mean Absolute Percentage Error

### Nowcast_Stats_Analysis.ipynb
description: notebook example of use of functions found in statistical_analysis.py

input:
    Nowcasts and Observed Data
output:
    Mean Bias, Root Mean Squared Error, Percent Gross Error and Mean Absolute Percentage Error 
    Plots Nowcast vs Observed Data

![github imgage](https://github.com/amynuno98/Model_Analysis/blob/11746d0b9b30f350b94346be4d5aef8205f82979/images/CenCOOSvsObs.png)

Information:
    All data must be averaged per day.
    Month and Day columns values needed for merge.
    Forecast Lead day column is required
    Package not designed for data not within the same year.    


