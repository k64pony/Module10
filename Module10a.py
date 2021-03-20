from plotnine.data import mtcars
from plotnine import ggplot, aes, geom_point

ggplot(mtcars) + aes(x="mpg", y="name") + geom_point()








