library(leaflet)
library(stringr)
library(dplyr)

setwd("C:/Users/emily/Documents/UT/Fall23/HackTX23")
data = read.csv("coord_rating_data.csv")

new_data = data[data$coords != "",]
new_data[c('lat', 'lng')] <- str_split_fixed(new_data$coords, ', ', 2)
new_data = subset(new_data, select = -c(coords) )
new_data$lat = as.numeric(new_data$lat)
new_data$lng = as.numeric(new_data$lng)

user_pref = round(runif(n=13, min=1, max=5), 0)
scores = subset(new_data, select = -c(coffee_shop_name, num_reviews, rating, lat, lng) )
scores = as.data.frame(t(t(scores)*user_pref))
scores = scores %>%
  mutate(sum = rowSums(., na.rm=TRUE))
pref_score = (scores$sum - min(scores$sum)) / (max(scores$sum - min(scores$sum)))
new_data$pref_score = pref_score
new_data$busy = round(runif(n=nrow(new_data), min=1, max=5), 0)

# blue/1 means less busy, red/5 means very busy
new_data$m_color <- with(new_data, ifelse(busy==1, "#0000FF", ifelse(busy==2, "#3300CC", ifelse(busy==3, "#660099", ifelse(busy==4, "#990066", "#CC0033")))))


m <- leaflet(data=new_data) %>%
  addTiles() %>%
  addCircleMarkers(
    color = ~m_color,
    fillOpacity = ~pref_score,
    label = ~coffee_shop_name
  )
m