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

def writeData(cam):
	sql = "INSERT INTO arlo.telemetry(serial_number,name,model,battery_level,signal_strength) VALUES(%s,%s,%s,%s,%s)"
	mysqlCursor.execute(sql, (cam.serial_number,cam.name,cam.model_id,cam.battery_level,cam.signal_strength))
	mysqlConnection.commit()

def main():
	cams = arlo.cameras
	for cam in cams:
		writeData(cam)
		time.sleep(2)
	else:
		sys.exit()

if __name__ == "__main__":
	main()
