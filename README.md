# GitlabAuditor
Auditing users' push/fetch events over SSH on GitLab.

## Usage:
* Put fetcher.sh under cron
```bash
*/30 * * * * /path/to/fetcher.sh > /tmp/bible
```
* Put middleman.sh under nohup
```bash
nohup /path/to/middleman.sh &
```
* Put finder.sh under cron
```bash
* * * * * /path/to/finder.sh
```

## Debugging:
* Replace the <placeholders> in the code with the value, actual links and creds.
  * fetcher.sh
  ```bash
  Line 1 - max=4 //Replace 4 with this value : (RoundUp(TotalNumberOfUsers/100)+1)
  Line 3 - contents=$(curl -s -H "PRIVATE-TOKEN: <your_access_token>" --insecure "<your_gitlab_url>/api/v4/users?order_by=id&page=$i&per_page=100")
  Line 10 - curl -s -H "PRIVATE-TOKEN: <your_access_token>" --insecure "<your_gitlab_url>/api/v4/users/$id/keys" | jq -r ".[] | \"$user\" + \" \" + \"user_id=$i\" + \" \" + \"key_id=\" + (.id|tostring)"
  ```
  * sender.py
  ```python
  Line 13 - url = '<your_webhook_url>'
  Line 21 - content = '<your_gitlab_url>/'+project
  ```
  
## Sample:
![.](https://github.com/lycanthrope10100/GitlabAuditor/blob/master/Image.jpg)
