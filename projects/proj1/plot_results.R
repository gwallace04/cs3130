library(tidyverse)

results <- read_csv("Extra/results.csv")
results <- rowid_to_column(results, "number")

iterative <- read_csv("Extra/iterative.csv")

# ggplot(data.frame(num = 1:length(results), rec = results$recursive), aes(x = num, y = rec)) + geom_line()

results %>% 
  ggplot(aes(x = number)) + geom_line(aes(y = recursive)) + geom_line(aes(y = iterative))

iterative %>%  
  ggplot(aes(x = n, y = time)) + geom_line() + geom_smooth()

