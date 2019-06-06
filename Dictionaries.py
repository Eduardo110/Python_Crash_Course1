Nomad = {'type':'Rover','color':'black','processor':'JetsonTX1'}
print(Nomad['type'])

BARB = {'type':'test-bed','color':'black','type':'wheeled'}
print(BARB)

myRobots = {'BARB':'WIP','Nomad':Nomad,'Llamabot':'WIP'}
print(myRobots)

myRobots['Llamabot'] = 'Getting to it'
print(myRobots)

del myRobots['Llamabot']
print(myRobots)

workingRobots = myRobots.copy()
print(workingRobots)

otherRobots = {'Rasbot-pi':'Pi-bot from book','spiderbot':'broken'}
myRobots.update(otherRobots)
print(myRobots)

robots = ["nomad","Ponginator","Alfred"]
print(robots)

myRobot = robots[0]
print(myRobot)

print(myRobot.capitalize())
