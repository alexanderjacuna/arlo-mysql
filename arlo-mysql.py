from pyarlo import PyArlo
import mysql.connector
import time
import sys

# MySQL CONNECTION INFO
mysqlConnection = mysql.connector.connect(
  host="MYSQL_ADDRESS",
  user="MYSQL_USER",
  passwd="MYSQL_PASSWORD",
  database="MYSQL_DATABASE"
)
mysqlCursor = mysqlConnection.cursor()

# ARLO CONNECTION INFO
arlo  = PyArlo('ARLO_USERNAME', 'ARLO_PASSWORD')

def writeData(i,base):
	serial_number = arlo.cameras[i].serial_number
	name = arlo.cameras[i].name
	model = arlo.cameras[i].model_id
	battery_level = arlo.cameras[i].battery_level
	signal_strength = arlo.cameras[i].signal_strength
	sql = "INSERT INTO arlo.telemetry(serial_number,name,model,battery_level,signal_strength) VALUES(%s,%s,%s,%s,%s)"
	mysqlCursor.execute(sql, (serial_number,name,model,battery_level,signal_strength))
	mysqlConnection.commit()

def main():
	cams = arlo.cameras
	cams = len(cams)
	if cams is not 0:
		base = arlo.base_stations[0]
		base = base.properties.get("modelId")
		for cam in range(cams):
			writeData(cam,base)
			time.sleep(60)
	else:
		sys.exit()

if __name__ == "__main__":
	main()
