# You are given system logs organized by date. Each date maps to a list of event records.
# Each event record contains:
# user: the username who performed the action
# action: the action performed
# status: either "success" or "failure"
# 1. Count the total number of actions performed by each user.
# 2. Count the total number of failed actions per user.
# 3. Identify and list all users who have more than 2 failed actions.

#LOGIC
#1. create two set for total action , failed action  
#2. use of loop for each date in logs
#3. second loop for access value of dict from list
#4. extract user , action , status from dict
#5. if user not in total action set then add user with 0 value
#6. if user not in failed action set then add user with 0 value
#7. inside loop check status of action
#8. if status is failure increment failed action else increment total action
#9. finally check failed action greater than 2 then print user

logs = {
    "2025-12-20": [
        {"user": "alice", "action": "login", "status": "success"},
        {"user": "bob", "action": "login", "status": "failure"},
        {"user": "bob", "action": "upload", "status": "failure"}
    ],
    "2025-12-21": [
        {"user": "alice", "action": "upload", "status": "success"},
        {"user": "bob", "action": "login", "status": "failure"},
        {"user": "carol", "action": "login", "status": "success"}
    ]
}

total_actions = {}
failed_actions = {}

for date in logs:
    for record in logs[date]:
        user = record["user"]
        status = record["status"].strip().lower()

        if user not in total_actions:
            total_actions[user] = 0
        if user not in failed_actions:
            failed_actions[user] = 0

        total_actions[user] += 1

        if status == "failure":
            failed_actions[user] += 1

# identify users with more than 2 failures
for user in failed_actions:
    if failed_actions[user] > 2:
        print(user)

print("Total Actions:", total_actions)
print("Failed Actions:", failed_actions)

           