full_name = "Amith Nishantha Senevirathna"

# print("Length of full name : %d" %len(full_name))
# print("Count of Letter \"t\" happened : %d" %full_name.count("t"))


print(f"Length of full name : {len(full_name)}")
print(f"Count of Letter 't' happened {full_name.count('t')}")

print(f"In uppercase :{full_name.upper()}")
print(f"In lowercase :{full_name.lower()}")


print(f"index of 't' letter : {full_name.index('t')}")
print(f"print range of index 3 to 12 : {full_name[3:12]}")
print(f"print range of index -13 to -2 : {full_name[-13:-2]}")
print(f"start = 3 , end =12 , skip =2  : {full_name[3:12:2]}")

emails = "anis@gmail.com ,test@gmail.com"
print(f"slipts from ',' : {emails.split(',')}")