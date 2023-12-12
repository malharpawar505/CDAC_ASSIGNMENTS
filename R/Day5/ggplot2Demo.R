survey <- data.frame(fruit=c("Apple", "Banana", "Grapes", "Kiwi", "Orange", "Pears"),
                     people=c(40, 50, 30, 15, 35, 20))
survey

# Create a basic bar graph with ggplot
library(ggplot2)
ggplot(survey, aes(x=fruit, y=people)) +
  geom_bar(stat="identity")

# Change the colors of individual bars (default fill colors)
ggplot(survey, aes(x=fruit, y=people, fill=fruit)) + 
  geom_bar(stat="identity")


#-------------------------------------------------
# Create a basic scatter plot with ggplot
ggplot(iris, aes(x=Petal.Length, y=Petal.Width)) +
  geom_point()

# Change the shape of the points and scale them down to 1.5
ggplot(iris, aes(x=Petal.Length, y=Petal.Width)) +
  geom_point(shape=3, size=1.5)

# Group points by 'Species' mapped to color
ggplot(iris, aes(x=Petal.Length, y=Petal.Width, colour=Species)) +
  geom_point()

# Group points by 'Species' mapped to shape
ggplot(iris, aes(x=Petal.Length, y=Petal.Width, shape=Species)) +
  geom_point()

# A continuous variable 'Sepal.Width' mapped to size
ggplot(iris, aes(x=Petal.Length, y=Petal.Width, colour=Species, size=Sepal.Width)) +
  geom_point(alpha=0.3)


ggplot(iris, aes(x=Petal.Length, y=Petal.Width)) +
  geom_point() +
  stat_smooth(method=lm)

# Add one regression lines for each group
ggplot(iris, aes(x=Petal.Length, y=Petal.Width, colour=Species)) +
  geom_point() +
  stat_smooth(method=lm)

#--------------------------------------------------
# Create a basic box plot with ggplot
ggplot(ToothGrowth, aes(x=factor(dose), y=len)) +
  geom_boxplot()

# Change the colors of individual boxes (default fill colors)
ggplot(ToothGrowth, aes(x=factor(dose), y=len, fill=factor(dose))) +
  geom_boxplot()

#Horizontal Box Plot
ggplot(ToothGrowth, aes(x=factor(dose), y=len, fill=factor(dose))) +
  geom_boxplot() +
  coord_flip()

# Plot the two supplement levels in separate (panel) plots
ggplot(ToothGrowth, aes(x=factor(dose), y=len, fill=factor(dose))) +
  geom_boxplot() +
  facet_grid(. ~ supp)
