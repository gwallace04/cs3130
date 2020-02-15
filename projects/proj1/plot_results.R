library(tidyverse)

iterative <- read_csv("iterative.csv")
recursive <- read_csv("recursive.csv")

# ggplot(data.frame(num = 1:length(results), rec = results$recursive), aes(x = num, y = rec)) + geom_line()

iterative %>%  
  ggplot(aes(x = n, y = time)) + geom_point() + geom_smooth(se = FALSE)

recursive %>% 
  ggplot(aes(x = n, y = time)) + geom_point() + geom_smooth(se = FALSE)

