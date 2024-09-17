cd docker_humble_desktop
./run_cs.sh

sleep(10)

docker exec cs_humble_desktop cd src
docker exer cs_humble_desktop ./launch.sh
