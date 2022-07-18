When provided with a reasonably large dataset, we'd like to just rename everything in a uniform manner that's also incrementing in value for uniqueness and predictable in manner. This makes it easier to process. To streamline this, we can use the rename script from Homebrew. 

Example:
`rename -e 's/.*/traffic_picture_$N.jpg/' *.jpg` will change some files named `sjd78x7sd.jpg`, `wwwwww332.jpg`, `not_a_jpg.jpg` into `traffic_picture_1.jpg`, `traffic_picture_2.jpg`, `traffic_picture_3.jpg`. 

This file is basically for a reminder for us to make sure to know how to do stuff later.