user_id = 	["frodo", "fradi", "crodo", "abc123", "frodoc"]
banned_id = ["fr*d*", "abc1**"]

def check(user_id, banned_id):
    for i in range(len(user_id)):
        if len(user_id[i]) 