docker build -t nearby_earthquakes_image .
docker run -dit --name nearby_earthquakes nearby_earthquakes_image
docker exec -it nearby_earthquakes bash