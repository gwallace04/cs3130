library(tidyverse)

plot_results <- function(df, title, filename = "temp.png") {
  df %>% 
    group_by(arr_type) %>% 
    ggplot(aes(x = arr_size, y = time, color = arr_type)) +
    ggtitle(title) +
    scale_x_continuous(trans = "log10") +
    geom_line() +
    facet_wrap(~ alg, nrow = 2) +
#    geom_smooth(se = FALSE) + 
    ylab("Time (sec)") 
    
  ggsave(filename, width = 6, height = 3, units = "in")
}

results = read_csv('results.csv')

bubble_with_swaps <- results %>% filter(alg == 'bubble_with_swaps')
insertion <- results %>% filter(alg == 'insertion')
mergesort <- results %>% filter(alg == 'mergesort')

plot_results(bubble_with_swaps, "Bubble with swaps", "bubble_with_swaps.png")
plot_results(insertion, "Insertion", "insertion.png")
plot_results(mergesort, "Merge sort", "mergesort.png")
plot_results(results, "All", "all.png")
