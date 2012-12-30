printf "Enter port address start and commitment type[0/1] : "
read port comm
printf "" > nodelist
for ((i=1;i<=10;i++))
do
printf "./node_8_0 $port%02d certs/$i.pem certs/$i-key.pem contlist 0 %d 0\n" $i $comm>> nodelist
done
