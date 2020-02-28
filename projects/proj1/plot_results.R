library(tidyverse)

iterative <- read_csv("iterative.csv")
recursive <- read_csv("recursive.csv")

# ggplot(data.frame(num = 1:length(results), rec = results$recursive), aes(x = num, y = rec)) + geom_line()

iterative %>%  
  ggplot(aes(x = n, y = time)) +
  ggtitle("Iterative algorithm") +
  geom_point() +
  geom_smooth(se = FALSE) + 
  ylab("Time (sec)") 
ggsave("iterative_plot.png")


recursive %>% 
  ggplot(aes(x = n, y = time)) +
  ggtitle("Recursive algorithm") +
  geom_point() +  
  geom_smooth(se = FALSE) +
  ylab("Time (sec)")
ggsave("recursive_plot.png")

