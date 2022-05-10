# The-Effect-of-Natural-Social-Distancing-in-Covid-19

# Background

The advent of Covid-19 has changed our lifestyle. To ensure public safety in the event of the pandemic, the government has enforced preemptive measures involving vaccination and social distancing.

Due to the changing environment, the government has recently announced the reopening, which lifts the strict social distancing policy. According to the statistics on the vaccination rate, more than 66% have been fully vaccinated.

While not all populations have been vaccinated, this rate has not been drastically changing over the year. This phenomenon means that the overdrive to get the vaccination rate up might not be as effective as other means. Therefore, we could assume that the vaccination rate is a controlled variable in covid-19 cases.

With vaccination being a controlled variable, the only meaningful variable that might affect the case would be the social distancing policy, which is getting lifted. In exchange, in this research, I have used natural distancing to see if it helps prevent the spread of covid-19.

# Raw data

Covid-19 cases data: us-counties-recent.csv (source: New York Times)
County data: co-est2021-alldata.csv, LND01.csv (source: US Census Bureau)

# Notable variables

c_avg_100: average Covid-19 cases per capita in county level for recent 7 days
d_avg_100: average Covid-19 deaths per capita in county level for recent 7 days
density: population density per square mile in county level

# Data table

covid cases per capita.csv: all data sorted high from low in c_avg_100
death cases per capita.csv: all data sorted high from low in d_avg_100
total pop.csv: intermediary data for calculating pop density (total population of each county)
land area.csv: intermediary data for calculating pop density (land area for each county)
density.csv: all data sorted high from low in density

# Figures

Covid Cases.png: Top 10 counties with most recent covid cases
Covid Deaths.png: Top 10 counties with most recent covid deaths
Pop Density.png: Top 9 counties with most population density

# Findings

According to the analysis, the covid spread seemed to be more severe among high-density counties than low-density counties. This result suggests that natural social distancing might be a significant factor since no other protective measure is considered.

# Limitations

While severe social distancing has been lifted, some minor policies are still active, such as masking in public. Therefore, for this finding to be more valid, the masking rate should be considered. Moreover, while the aggregated vaccination was controlled, the actual vaccination rate differed by region, suggesting that the difference in vaccination rate might still affect covid spreading.
