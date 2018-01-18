library(plyr)
setwd ("~/Documents/Git/PythonClass-2015/Project")
catch <- read.csv("europeanParliamentMinutes.csv", strip.white = TRUE)
catch2 <- strsplit(as.character(catch$Catch.the.Eye), ', ')
catch3 <- data.frame(Catch.the.Eye=unlist(catch2), Date=rep(catch$Date, sapply(catch2, FUN=length)))
catch4 <- strsplit(as.character(catch3$Catch.the.Eye), ' and ')
catch5 <- data.frame(Catch.the.Eye=unlist(catch4), Date=rep(catch3$Date, sapply(catch4, FUN=length)))
names(catch5)[names(catch5) == 'Catch.the.Eye'] <- 'Name'
countries <- read.csv("~/Dropbox/MEP Vote Seeking/ballotStructure/data/7EP/7th EP Votes/EP7votes.csv", encoding="UTF-8")
countries <- countries[!duplicated(countries[2:3]),]
countries <- countries[c("Name", "State")]
catch5 <-join(catch5, countries, by = "Name")
Date <- aggregate(Name ~ Date, data = catch5, FUN = length, na.action = na.pass)
MEP <- aggregate(Date ~ Name, data = catch5, FUN = length, na.action = na.omit)

pdf ("catchDate.pdf", h=5, w=5)
plot(density(Date$Name), main="Catch The Eye Invoked by Date", xlab="Number of debates", axes=F)
axis(1, labels=T); axis(2, labels=T)
dev.off()
pdf ("catchMEP.pdf", h=5, w=5)
plot(density(MEP$Date), main="Catch The Eye Invoked by Individual MEPs", xlab="Number of Procedures Invoked", axes=F)
axis(1, labels=T); axis(2, labels=T)
dev.off()