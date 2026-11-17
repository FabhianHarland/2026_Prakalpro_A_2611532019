phone = "082611532019"
masked = phone[:4] + "*"*(len(phone)-7) + phone[-3:]
print(masked)