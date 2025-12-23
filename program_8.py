data = {
    "users": {
        "user1": {
            "id": 101,
            "profile": {
                "name": "Neel",
                "skills": {"python": 4, "ml": 3}
            }
        },
        "user2": {
            "id": 102,
            "profile": {
                "name": "Amit",
                "skills": {"python": 5, "ml": 4}
            }
        }
    }
}
print(data["users"]["user1"]["profile"]["skills"]["ml"])