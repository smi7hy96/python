# LOOKING AT LISTS

# Organised with Index. (starts at 0)

football_teams = ['Liverpool', 'Bournemouth', 'Wolves', 'Sheffield Utd']
#        Index = [     0     ,       1      ,     2   ,        3       ]
# Lists can contain any different data types; including other lists!

# Print all of the list
print(football_teams)

# access one entry
print(football_teams[0])
print(football_teams[-1])  # ACCESS LAST ENTRY

# RE-ASSIGN ENTRY

football_teams[1] = "Newcastle Utd"
print(football_teams)

# REMOVE ENTRY

football_teams.pop(-1)
print(football_teams)
#  ALTERNATIVE OPTION USE .remove(x) WHERE X IS A STRING.
#  THIS WILL REMOVE THE *FIRST* INSTANCE OF X FROM THE LIST

# ADD ENTRY
# APPEND
football_teams.append("West Ham Utd")
print(football_teams)
# INSERT
football_teams.insert(2, "Norwich City")
print(football_teams)