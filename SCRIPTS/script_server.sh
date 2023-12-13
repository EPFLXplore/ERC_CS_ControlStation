killall redis-server
sudo service redis-server stop
redis-server &
cd /home/evan/Desktop/Xplore/CS_workspace/cs_ws
colcon build
source install/setup.bash
cd src/control_station_pkg/control_station_pkg
python3 manage.py runserver 0.0.0.0:8000
