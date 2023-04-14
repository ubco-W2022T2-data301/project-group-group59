## Introduction: 
This analysis is on an air quality dataset containing information on multiple airborne chemical contaminants data collected over a year span in hourly intervals. Analysis 1 is specifically interested in NOx, which is a term used to group nitrogen dioxide and nitric oxide, which are two primary compounds that contribute to smog and the general deterioration of an area's air quality index. Understanding the detrimental health impacts which include decreased lung function and aggravation of respiratory or heart disease in addition to many other harmful effects on the human body and other living organisms (Libretexts, 2023), provides an interest in exploring this data. Analysis 2 had a primary focus on parasitic relationships between the variables, although narrowed it down to if temperature has any correlating relationship to Nitrogen Oxide, Nitrogen Dioxide and Tungsten Oxides (NOx, NO2, WO2 and WO3), and how it can affect over all air quality. I was concerned with determining how these compounds are affected by temperature because of the lasting effects the pollutants could have after being trapped into the ground through temperature inversions. Together we have a common interest in the air quality and if effects on Italy. 

### Question 1 (Analysis 1):

The research question for analysis 1 had a focus on the relationship between time intervals and the average concentration of two major components that contribute to smog and acid rainfall within the Italian region *(Nitrogen Dioxide NO2 and Nitric Oxide NO)*, also including another compound of Carbon Monoxide *(CO)*. The initial question: *“Which month has the greatest concentration of each chemical compound?”* 

To answer this question, we had to refactor the Date and Time variable to only show months, as shown in *Figures 1.1 and 1.2.* The resulting analysis denoted that in December 2004 had the highest average concentration of Carbon Monoxide and in November 2004 contained the highest average concentration of Nitric Oxide. 

![Figure 1.1](/images/Figure-1-1.png) 

![Figure 1.2](/images/Figure-1-2.png) 

Based on the results from question one, the Date and Time filter was modified months to weeks with a focus on days of the week (Monday – Friday), to gain insight on the highest average concentration between Carbon Monoxide and Nitric Oxide. 

The result of this alteration as shown in *Figure 1.2 and 2.2*, is that the highest average concentration of Carbon Monoxide was recorded on Friday’s during the month of December 2004. As for Nitric oxide it was present that on average Thursday’s during the month of November 2004 had the highest concentration activity. An interesting observation was made that for both compounds, Sundays on average had the lowest concentration levels. It was speculated that many chemical pollutants could have an attribute to human activity, and that a relative portion on Italy’s population identifies as Catholic and within those beliefs they think of Sundays as a day of rest, because of this there could be a possible correlation with human activity and air pollutants; further analysis would be needed. 

![Figure 1.2](/images/Figure-1-2.png) 

![Figure 2.2](/images/Figure-2-2.png) 

Question 3 is similar to the questions above although it looks at slightly different variations of the variables. The changes present in the question is we filtered the data from the Date and Time variables, to look at what hour of the day had the highest concentrations of the compounds. The results are shown in *Figures 1.3 and 2.3.* We were able to interpret that the highest concentrations for both compounds were at 6:00 or 18:00. 

![Figure 1.3](/images/Figure-1-3.png) 

![Figure 2.2](/images/Figure-2-3.png) 
 	 
### Question 2 (Analysis 2): 

The research questions for analysis 2 had an initial focus of parasitic relationships between the compounds and the variables, this can be shown in *Figure 1*. The resulting analysis showed that there were possible positive and negative correlations between the compounds Tungsten Oxide *(WO2 and WO3)*, Nitrogen Dioxide *(NO2)* and Nitrogen Oxides *(NOx)* and temperature variables. 

![Figure 1](/images/Figure1.1.png) 

Based on these results, I altered the data to remove the compounds Tungsten Trioxide (WO3) and Non-Metallic Hydrocarbons. Which lead into my second research question, which again focused on parasitic relationships between the Nitrogen parameters and the Tungsten Oxide Parameters, shown in *Figure 2.1.* From the results I was able to see that between some versions of the Nitrogen and Tungsten compounds had different correlations between one another and temperature. 

![Figure 2.1](/images/Figure2.1.png) 


The third research question was taken from the results in question 2 and had a primary focus on Nitric Oxide *(NO)*, Nitrogen Dioxide *(NO2)*, and Tungsten Oxides *(WO2)* and Temperature in degrees Celsius. Presented in *Figures 3.2, 3.3, 3.4 and 3.5.*

From *Figure 3.2*, we were able to gather that from the compound Tungsten Oxides *(PT08.S3; WO2 targeting Nitric Oxides)* against temperature. A perceivably positive correlation was present, such that the Tungsten Oxide *(WO2)* had a high concentration between 600-800 ppm at temperatures between 10-20 degrees Celsius. For the second plot *(Figure 3.3)* which focused on the compound *(PT08.S4; WO2 targeting Nitrogen Dioxide)* against the variable temperature. Again, there was a perceivably positive correlation presents, although the concentration of the correlation was in between in 750-1650 ppm at temperatures between 5-30 degrees Celsius. Based on these results from the plots we could conclude that there is a slight positive relationship happening between Tungsten Oxide and Temperature. 

![Figure 3.2](/images/Figure3.2.png)

![Figure 3.3](/images/Figure3.3.png)

For the next two graphs, they had a primary focus on single compounds which were Nitric Oxide *(NO)* and Nitrogen Dioxide *(NO2)* plotted again with the same Temperature variable along the y-axis. Denoted in Figure 3.4 there appeared to be a slight negative regression happening between Nitric Oxide *(NO)* and temperature. As the density of the variables remained in between a lower average of 0-250 ppm at temperatures in between 0-25 degrees Celsius. In Figure 3.5 a similar negative regression is present with the compound of Nitrogen Dioxide *(NO2)* and temperature, with the variables ranging in between 75-145 ppm at temperatures between 15-25 degrees. Based on the results from these hexagonal density plots, we can conclude that there may be a possible regression happening between these compounds and temperature. 

![Figure 3.4](/images/Figure3.4.png) 

![Figure 3.5](/images/Figure3.5.png) 

## Conclusion: 
Based on the results from our exploratory data analyses, we can deduce that from analysis 1; Carbon Monoxide and Nitric Oxide have greater concentrations between the months of November and December of 2004, which could be an effect of human activities around that specific time of year as it is closer to the holiday seasons. Furthermore, based on the results in analysis 2, Tungsten Oxide, Nitric Oxide and Nitrogen Dioxide, have varying correlations both positive and negative. Although, it is interesting how Nitric Acid specifically has a negative correlation as it would correlate to the results in analysis 1 and help justify our mutual interest on the air quality of Italy and its effects it could present the population. 





