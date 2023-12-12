
v<-c(12,34,NA,45,0/0,4,23/0,Inf,7,-Inf)
v
is.na(v)

v
is.nan(v)

v
is.finite(v)

v
is.infinite(v)



#----------------------------------------
> v<-c(12,34,NA,45,0/0,4,23/0,Inf,7,-Inf)
> v
[1]   12   34   NA   45  NaN    4  Inf
[8]  Inf    7 -Inf
> is.na(v)
[1] FALSE FALSE  TRUE FALSE  TRUE FALSE
[7] FALSE FALSE FALSE FALSE
> 
  > v
[1]   12   34   NA   45  NaN    4  Inf
[8]  Inf    7 -Inf
> is.nan(v)
[1] FALSE FALSE FALSE FALSE  TRUE FALSE
[7] FALSE FALSE FALSE FALSE
> 
  > v
[1]   12   34   NA   45  NaN    4  Inf
[8]  Inf    7 -Inf
> is.finite(v)
[1]  TRUE  TRUE FALSE  TRUE FALSE  TRUE
[7] FALSE FALSE  TRUE FALSE
> 
  > v
[1]   12   34   NA   45  NaN    4  Inf
[8]  Inf    7 -Inf
> is.infinite(v)
[1] FALSE FALSE FALSE FALSE FALSE FALSE
[7]  TRUE  TRUE FALSE  TRUE
> 