# Do not modify these lines
__winc_id__ = '71dd124b4a6e4d268f5973db521394ee'
__human_name__ = 'strings'

# Add your code after this line
Player_0="Gullit"
Player_1="Van Basten"
Goal_0="32"
Goal_1="54"
Scorers=(Player_0+" "+Goal_0)+", "+(Player_1+" "+Goal_1)
print(Scorers)
print(f"{Player_0} scored in the {Goal_0}nd minute\n{Player_1} scored in the {Goal_1}th minute")

player="Dejan Jasnic"
x = player.find(" ")
first_name = player[:x]
last_name_len = len(player[x+1:])
name_short = player[x+1:]
z=len(first_name)
chant=(first_name+"! ")*z
good_chant=chant[0:len(chant)-1]
print(good_chant)
