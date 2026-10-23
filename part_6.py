scores = [45, 70, 85, 30,90, 55]
no_fail = 0
no_pass = 0
for score in scores:
    if score <= 40:
        no_fail += 1
    else:
        no_pass += 1

print(f"No Pass: {no_pass}")
print(f"No Fail: {no_fail}")