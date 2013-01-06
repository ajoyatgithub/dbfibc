printf "Enter the data in this format \n<IP address> <Port address start> <Commitment> <Program name> : "
read ip port comm node
printf "" > nodelist
for ((i=1;i<=10;i++))
do
printf "./$node $port%02d certs/$i.pem certs/$i-key.pem contlist 0 %d 0\n" $i $comm>> nodelist
done
printf "1 %s %d01 certs/1.pem L\n" $ip $port > contlist
for ((i=2;i<=10;i++))
do
printf "%d %s %d%02d certs/%d.pem\n" $i $ip $port $i $i >> contlist
done
