#this shell script will rerun the main code after it has been edited
echo "in runner"
#sleep 20
pkill -f findvalue.py #first stops the running old script
sleep 1 #wait for 5 seconds before restart
python findvalue.py

