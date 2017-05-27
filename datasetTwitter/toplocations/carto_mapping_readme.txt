This SQL Statement was used to find give location_names their corresponding geo-location coordinates which were predefined as per the coordinates_april27th set. as precision of the location was less important for the user to be able to see visually the trends in a region. we can make this assumption because typically as seen from the data places that had the same location name in example new york,ny they would again use the same bounding box. therefore we were able to reduce the work, for the map reduce job to just location names hash tags and not consider the exact location coordinates of each tweet. 




SELECT distinct(hashtagmap2.cartodb_id), hashtagmap2.location_name, hashtagmap2.hash_tag, hashtagmap2.ht_count , coordinates_april27.the_geom, coordinates_april27.the_geom_webmercator FROM hashtagmap2, coordinates_april27 WHERE hashtagmap2.location_name = coordinates_april27.location_name




Relevant  Data Sets:

Most Popular Hashtag Dataset May 8th
https://juttaro.carto.com/tables/hashtagmap2/public

Most Popular Hashtag Dataset April 27th
https://juttaro.carto.com/tables/hashtagmap/public

All tweet coordinates from april 27th 
https://juttaro.carto.com/tables/coordinates_april27/public





Maps :

HeatMap of all Tweets from April 27th
https://juttaro.carto.com/builder/19e09312-38f3-11e7-88b5-0e3ff518bd15/embed

Hashtag Map May 8th 
https://juttaro.carto.com/builder/72cf7b1e-3957-11e7-932d-0e3ff518bd15/embed

Hashtag Map April 27th
https://juttaro.carto.com/builder/b87e2f8a-3965-11e7-a49b-0e3ebc282e83/embed
