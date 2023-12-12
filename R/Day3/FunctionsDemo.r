#character
s<-"Happy Journey"
nchar(s) #Count the Number of Characters
toupper(s)
tolower(s)
substr(s,2,5) #substr(x, start, stop)Substrings of a Character Vector
gsub("p","z",s)#Pattern Matching and Replacement sub and gsub perform replacement of the first and all matches respectively.
gsub(pattern, replacement, x, ignore.case = FALSE)

strsplit(s," ") #Split the Elements of a Character Vector
strsplit(s,NULL)[[1]] #Split on each char

#Numeric
abs(-4)
sqrt(64)
log(10)
log2(10)
log10(10)
exp(2.302585)
floor(12.3)
round(12.3)
ceiling(12.3)