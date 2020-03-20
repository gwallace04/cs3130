library(tidyverse)

results <- read_csv('results.csv')

get_average_by_alg <- function(type_of_array, raw_data) {
  df <- results %>% filter(arr_type == type_of_array)
  df <- df %>% mutate(time_size = arr_size / time)
  df <- df %>% group_by(alg) %>% summarize(mean = mean(time))
  df <- df %>% arrange(mean)
  return(df)
}

get_average_by_alg("almost", results)
get_average_by_alg("random", results)
