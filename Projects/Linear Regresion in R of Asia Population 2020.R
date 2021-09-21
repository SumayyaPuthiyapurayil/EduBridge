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


print(is.na(d))

# print column names
print(colnames(d))
print((names(d)))

# statistical values
print(nrow(d))
print(ncol(d))
print(summary(d))
print(str(d))
print(mean(d$income))
print(mean(is.na(d)))
print(unique(d))

#Histogram of Population
print(hist(d$Population))

print(plot(Population~Density,data=d))

lr=lm(Population~Density,data=d)
print(lr)

summary(lr)

par(mfrow=c(2,2))

plot(lr)

i<-ggplot(d,aes(x=Population,y=Density))+geom_point()
print(i)

i<-i+geom_smooth(method="lm",col="blue")
print(i)
