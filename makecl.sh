printf "Enter the IP address and the port addr type : "
read ip port
printf "1 %s %d01 certs/1.pem L\n" $ip $port > contlist
for ((i=2;i<=10;i++))
do
printf "%d %s %d%02d certs/%d.pem\n" $i $ip $port $i $i >> contlist
done
