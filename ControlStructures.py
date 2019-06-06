#if statements
robots = ["nomad","Ponginator","Alfred"]
for robot in robots:
    if robot=="nomad":
        print("This is Nomad")
    else:
        print(robot + " is not Nomad")

myRobot = "Nomad"
print(myRobot == "Ponginator")

myRobot == "Nomad"
print(myRobot == "Nomad")

for robot in robots:
    if robot == "Ponginator" or robot == "Alfred":
        print("These aren't the droids I'm looking for.")

#Loops
for robot in robots:
        print(robot)

#for Loop
Nomad = {'color':'black','type':'wheeled'}
for name,data in Nomad.items():
        print(name + ': ' + data)


for num,robot in enumerate(robots):
        print(num,robot)
#whileLoop
count = 1
while count < 5:
    print(count)
    count = count+1
