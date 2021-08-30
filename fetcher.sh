max=4	
for ((i=1; i<$max; i+=1)); do	
    contents=$(curl -s -H "PRIVATE-TOKEN: <your_access_token>" --insecure "<your_gitlab_url>/api/v4/users?order_by=id&page=$i&per_page=100")	
    echo "$contents" | jq -r '.[] | (.id|tostring) + " " + .name' >> /tmp/contents	
done	
while IFS= read -r line	
do	
        id=$(echo $line | awk '{print $1}')	
        user=$(echo $line | awk '{print $2}')	
        curl -s -H "PRIVATE-TOKEN: <your_access_token>" --insecure "<your_gitlab_url>/api/v4/users/$id/keys" | jq -r ".[] | \"$user\" + \" \" + \"user_id=$i\" + \" \" + \"key_id=\" + (.id|tostring)"	
done < /tmp/contents	
rm -rf /tmp/contents
