library(ggplot2)
library(dplyr)
library(choroplethr)
library(choroplethrMaps)
library(openintro)
library(tidyverse)
library(scales)
library(corrgram)
print(getwd)

# read the dataset named vaccination data
d<-read.csv("C:/Users/Sumi/AsiaPopulation2020.csv")
print(d)

# print head and tail rows
print(head(d))
print(tail(d))

# summary of the dataset
print(summary(d))
print(summary(d$TPopulation))
plot(d$Population)

# dimention of data
print(dim(d))

# column names
print(names(d))

# details of population
print(d$Population)

# length
print(length(d$Population))

# structure
print(str(d))

# glimpse
print(glimpse(d))



#  check unique values
print(unique(d))

# statistical values
print(is.na(d))
print(is.data.frame(d))
print(is.name(d))
print(ncol(d))
print(nrow(d))
print(max(d$Population))
print(min(d$Population))
print(sort(d$Population))
print(which.max(d$Population))
print(which.min(d$Population))
print(mean(d$Population))
print(mean(d$Population,trim=0.10))
print(var(d$Population))
print(median(d$Population))
print(mad(d$Population))# mean absolute division
print(sd(d$APopulation))
print(mode(d$Population))
print(range(d$Population))
print(scale(d$Population))
print(sd(d$Population/sqrt(length(d$Density))))
print(max(d$Population-min(d$Density)))
print(quantile(d$Population))
print(quantile(d$Population,c(0.75)))
print(IQR(d$Population))
print(t.test(d$Population))

# data visualisation


# plotting of population
plot(d$Population,col="red",xlab="X-axis",ylab="Y-axis",main="Population")

# column names
print(names(d))


# plotting of density
plot(d$Density,col="red",xlab="X-axis",ylab="Y-axis",main="Density")


# Landarea and Density
plot(x=d$LandArea,y=d$Density,main="Density",xlab="Density",ylab="LandArea",col="blue")


# geographical plot of Density releated to population
gsplot=d %>% group_by(Density) %>% summarise(Population)
View(gsplot)


# country wise total population
countrywise_population=d %>% group_by(Country) %>% summarise(Population) %>% arrange((desc
                                                                                                (Population)))
View(countrywise_population)


# countrywise population using bargraph
countrywisepopulation2=ggplot(d,aes(x=Population,y=Country,fill=Population))+geom_col()
print(countrywisepopulation2)


# countrywise population using scatter plot
countrywisepopulation=ggplot(d,aes(x=Population,y=Country,fill=Population))+geom_point()
print(countrywisepopulation)

# countrywise population using boxplot
Population=ggplot(d,aes(x=Population,y=Country,fill=Population),size=3.0)+geom_boxplot()
print(Population)


# Population  using histogram
  hist(d$Population,col='steelblue',main='Population',xlab='Population')




