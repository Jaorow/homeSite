## INFO
- for easer dev use micro 


## raspi hosting
check with
- sudo systemctl status startup_site_script.service

restart service
- sudo systemctl stop startup_site_script.service
- sudo systemctl start startup_site_script.service


# control light on board:
### (Optional) Turn on (1) or off (0) the PWR LED.
echo 1 | sudo tee /sys/class/leds/led1/brightness
echo 0 | sudo tee /sys/class/leds/led1/brightness

# layout
							ribbon
							---------
							| 1 | 2 |	5V - TEMP (middle)
							|-------|
							| 3 | 4 |	5V
							|-------|
							| 5 | 6 |	Ground - TEMP (-)
							|-------|
							| 7 | 8 |
							|-------|
							| 9 | 10|
							|--------
		(s)	TEMP - GPIO17	|11 | 12|
							|-------|
							|13 | 14|
							|--------
							|15 | 16|
							|-------|
							|17 | 18|
							|--------
	BOARD					|19 | 20|  
							|-------|
							|21 | 22|
							|-------|
							|23 | 24|
							|-------|
							|25 | 26|
							|-------|
							|27 | 28|
							|-------|
							|29 | 30|
							|-------|
							|31 | 32|
							|-------|
							|33 | 34|
							|-------|
							|35 | 36|
							|-------|
							|37 | 38|
							|-------|
							|39 | 40|
							---------
							usb input
