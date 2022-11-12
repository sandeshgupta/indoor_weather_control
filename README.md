# indoor_weather_control


## How to run:

1. Ensure that all hardware is connected (Speaker, Sensor)

2. Install modules using requirements.txt 

	```pip install -r requirements.txt```

3. Start `continuous_monitoring.py` for continuous monitoring of temperature
	- Add telegram token `TOKEN_NOTIF` for the monitoring channel in file `continuous_monitoring.py`
	- Add telegram token `TOKEN_CONTROL` for the control channel in file `continuous_monitoring.py`
	- Add `CHAT_ID` of the telegram user in file `continuous_monitoring.py`
	- [Optional] Update the `MIN` and `MAX` temperature in farhanhiet in file `continuous_monitoring.py`
	- Open terminal and navigate to the directory where file `continuous_monitoring.py` is present
	- Run the file 
	
		```python3 continuous_monitoring.py```
	- Check on telegram channel if the notifications are being sent


4. Start `smart_control.py` script to change temperature remotely
	- Add telegram token `TOKEN_CONTROL` for the control channel in file `smart_control.py`
	- Open terminal and navigate to the directory where file `smart_control.py` is present
	- Run the file 
	
		```python3 smart_control.py```
	- Run the webserver using ngrok
	
		```ngrok http 5000```
	- Set the webhook for the telegram channel. Run this in any browser
		```https://api.telegram.org/bot{TOKEN_CONTROL}/setWebhook?url={NGROK_HTTPS_URL}```
	- Check on telegram channel if the notifications are being sent (Notifications will be sent only when the temperature crosses threshold)
	- Interact with the bot
		- `/start` - Displays info about the bot               
		- `Set <temp_in_fahrenheit>`  - Set the temperature to a specific number
		- `On ` - Switch on the thermostat
		- `Off`  - Switch off the thermostat 
