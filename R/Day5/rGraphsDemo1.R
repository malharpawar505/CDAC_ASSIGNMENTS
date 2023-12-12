# Plot the 'pressure' dataset
plot(pressure)

# Change the shape of the points
plot(pressure, pch=17)


# Change the border color to blue and background color to lightblue
plot(pressure, pch=21, col="blue", bg="lightblue")


plot(pressure, pch=19, col="red")
#--------------------------------------------
#barplot

survey <- c(apple=40, kiwi=15, grape=30, banana=50, pear=20, orange=35)
survey

barplot(survey)



barplot(survey, col="dodgerblue3")

barplot(survey,
        col=c("red2", "green3", "slateblue4", "yellow2", "olivedrab2", "orange"))


#Histogram
hist(trees$Height, breaks = 10, col = "orange", main = "Histogram of Tree heights", xlab = "Height Bin")



#Scatterplot

attach(trees)
plot(Girth, Height, main = "Scatterplot of Girth vs Height", xlab = "Tree Girth", ylab = "Tree Height")
abline(lm(Height ~ Girth), col = "blue", lwd = 2)

#Boxplot
boxplot(trees, col = c("yellow", "red", "cyan"), main = "Boxplot for trees dataset")


boxplot(ToothGrowth$len)

boxplot(ToothGrowth$len, horizontal = TRUE)


# Creating one box plot for each factor level (dose)
boxplot(len ~ dose, data = ToothGrowth)

#with color
boxplot(len ~ dose, data = ToothGrowth,
        col = "dodgerblue1")

boxplot(len ~ dose, data = ToothGrowth,
        col = c("orange1", "dodgerblue1", "olivedrab2"))
