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
    
#  ggsave(filename)
}

results = read_csv('results.csv')
results_quick = read_csv('results_quick.csv')

bubble <- results %>% filter(alg == 'bubble')
insertion <- results %>% filter(alg == 'insertion')

to_exclude = c("bubble", "selection")
no_bubble_or_selection <- results %>% filter(!alg %in% to_exclude)

plot_results(results, "All")

plot_results(no_bubble_or_insertion, "No bubble or selection")

