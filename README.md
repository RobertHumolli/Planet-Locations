# Planet-Locations
This project visualizes the order of planets in the solar system using a matplotlib graph. Users can view the relative positions of the planets within the solar system.
To properly run this code you would want to download the CSV file as well as without it, you are unable to run it.

This is what the final printout would look like.
![image](https://github.com/RobertHumolli/Planet-Locations/assets/120424157/f518e622-5f04-4c70-97ff-066ecc4145b5)

A few problems that I ran into while making this program.
Problem: initially the circle never printed out, where it only showed the initial y and x locations.
Solution: I used self.ylocation and self.xlocation (lines 48 & 49) which essentially loops the values and enables me to generate the circle that I wasn’t able to generate previously.

Problem: Initially I created a for loop and a temp list that had essentially meant I had to append each value to each specific line, where not only was this impractical as I then needed to append each value to each list, I also constantly ran into IndexError's
Solution: As shown on line 54, I created a for loop that took data from the lines within a certain range of the .csv file removing the first line that has all of the headings.
This was effective as I was able to produce each multiple lists for each respective planet and it's corresponding data which was used in calculations to then plot my graphs

