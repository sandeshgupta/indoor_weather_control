# indoor_weather_control


How to run:

1. Ensure that all hardware is connected (Speaker, Sensor)

2. Install modules using requirements.txt 

	pip install -r requirements.txt

3. Start continuous monitoring of temperature
	a. Add telegram token TOKEN_NOTIF for the monitoring channel in file continuous_monitoring.py
	b. Add telegram token TOKEN_CONTROL for the control channel in file continuous_monitoring.py
	c. Add CHAT_ID of the telegram user in file continuous_monitoring.py
	d. [Optional] Update the min and max temperature in farhanhiet in file continuous_monitoring.py
	e. Open terminal and navigate to the directory where file continuous_monitoring.py is present
	f. Run the file 
		python3 continuous_monitoring.py
	g. Check on telegram channel if the notifications are being sent


4. Start smart_control script to change temperature remotely
	a. Add telegram token TOKEN_CONTROL for the control channel in file smart_control.py
	b. Open terminal and navigate to the directory where file smart_control.py is present
	c. Run the file 
		python3 smart_control.py
	d. Run the webserver using ngrok
		ngrok http 5000
	e. Set the webhook for the telegram channel. Run this in any browser
		https://api.telegram.org/bot{TOKEN_CONTROL}/setWebhook?url={NGROK_HTTPS_URL}
	f. Check on telegram channel if the notifications are being sent (Notifications will be sent only when the temperature crosses threshold)
	g. Interact with the bot
		i. /start - Displays info about the bot               
		ii. Set <temp_in_fahrenheit>  - Set the temperature to a specific number
		iii. On  - Switch on the thermostat
		iv. Off  - Switch off the thermostat 