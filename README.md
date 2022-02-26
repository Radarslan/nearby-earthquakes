# nearby-earthquakes

## requirements

* **Docker**
  * If you use Windows or macOS please make sure Docker Desktop is installed and running.
    Instructions could be found here https://docs.docker.com/desktop/#download-and-install
  * If you are using Linux please make sure Docker Engine installed and running.
    Instructions could be found here https://docs.docker.com/engine/install/

## start or stop application

To run the application use terminal or command prompt and scripts in directory.
For macOS and Linux users check the `_nix` one and for Windows take a look at the `windows` one.

### linux or macOS
```commandline
sh ./scripts/_nix/start.sh
```
```commandline
sh ./scripts/_nix/stop.sh
```
### windows
```commandline
./scripts/windows/start.cmd
```
```commandline
./scripts/windows/stop.cmd
```

## run application
Once you have application started you will see something like this
```commandline
app_user@d13540e2382c:~$
```
it means it started successfully
Type in the following command
```commandline
python src/nearby_earthquakes.py
```
and you will be presented with invitation
to enter `city's latitude` and `city's longitude`
```commandline
app_user@d13540e2382c:~$ python src/nearby_earthquakes.py
enter the city's latitude: 40.730610
enter the city's longitude: -73.935242
``` 
hit Enter (return) and wait until the application finishes
```commandline
app_user@d13540e2382c:~$ python src/nearby_earthquakes.py 
enter the city's latitude: 40.730610
enter the city's longitude: -73.935242
trying to get all earthquakes that happened during last 30 days
getting distances
filtering 10 closest earthquakes

10 closest earthquakes result:

M 1.8 - 5 km NNW of Contoocook, New Hampshire || 336
M 1.9 - New York || 404
M 1.8 - 7 km SE of Alexander, New York || 425
M 2.9 - 0 km SSW of Gorham, New Hampshire || 465
M 1.9 - 0 km NNE of Gorham, New Hampshire || 466
M 1.5 - 2 km ENE of Lewiston, Maine || 486
M 1.9 - 2 km N of Dillwyn, Virginia || 525
M 2.7 - 8 km WNW of L'Épiphanie, Canada || 573
M 2.3 - 9 km WSW of Forest, Virginia || 604
M 2.0 - 1 km WNW of Willowick, Ohio || 641
app_user@d13540e2382c:~$ 
```