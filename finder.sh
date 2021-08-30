whitelist=(jenkins)
start=$(cat /tmp/offset)
start2=$(($start+1))
end=$(cat /tmp/events | wc -l)
sed -n "${start2},${end}p;" /tmp/events > /tmp/data
while IFS= read -r line
do
        key_id=$(echo $line | awk '{print $2}')
        user=$(cat /tmp/bible | grep -w "$key_id" | awk '{print $1}')
        time=$(echo $line | awk '{print $1}')
        time=$(echo $time | cut -d'.' -f1)
        project=$(echo $line | awk '{print $3}')
        remote_ip=$(echo $line | awk '{print $4}')
        if [ -z "$user" ]
        then
                continue;
        else
                echo "$user $line"
                [[ " ${whitelist[@]} " =~ " ${user} " ]] && echo Skip $user || python sender.py $user $project $remote_ip $time
        fi
done < /tmp/data
rm -rf /tmp/data
echo $end > /tmp/offset
