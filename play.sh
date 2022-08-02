
while true; do
    curl -s -X PUT http://hue.void.lan/api/Nv8SgnpcuwtE7KkpgFIwep5T1gliTm0E0Tj62H-g/lights/1/state -d '{ "on": true, "bri":254, "transitiontime":0}'
    sleep 0.2
    curl -s -X PUT http://hue.void.lan/api/Nv8SgnpcuwtE7KkpgFIwep5T1gliTm0E0Tj62H-g/lights/1/state -d '{ "on": false, "bri":254, "transitiontime":0}'
    sleep 0.2
done
