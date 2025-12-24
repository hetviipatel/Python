
# You are given a mapping of user roles to their allowed permissions, and a list of user requests.
# Each request consists of:
# A username
# The user’s role
# An action the user wants to perform
# A request is considered allowed if and only if the requested action exists in the permission set assigned to that role.
# Your task is to classify each request as either allowed or denied.

#LOGIC
# 1. create two list one for allow and one for denied
# 2. use of loop each request in the 'requests' list.
# 3. for each action check with permission 
#     if action permission the add to allowed else denied
permissions = {
    "admin": {"read", "write", "delete"},
    "editor": {"read", "write"},
    "viewer": {"read"}
}
requests = [
    ("alice", "admin", "delete"),
    ("bob", "viewer", "write"),
    ("carol", "editor", "read")
]
allowed_list = []
denied_list = []

for i , j ,k in requests:
    if (k in permissions[j]):
        allowed_list.append((i, j, k))
    else:
        denied_list.append((i, j, k))

print(allowed_list)
print(denied_list)