#KMOOC 일반인을 위한 물리코딩_기말고사_문제코드.txt
GlowScript 3.0 VPython

################################################################################
#ground
ground = box(pos=vec(0,0,-1), size=vec(150, 70, 1), color = vec(0.1, 0.5, 0.1))

#ball box
ball_box = box(pos=vec(0,0,0), size=vec(2, 1, 2), color = color.blue)
ball_box.pos.x = -ground.size.x/2 + ball_box.size.x/2
ball_box.pos.y = 0
ball_box.pos.z = ground.size.z/2

#ball
ball = sphere(pos=vec(0,0,0), radius=1, color = color.orange)
ball.pos.x = -ground.size.x/2 + ball.radius/2
ball.pos.y = ball_box.size.y + ball.radius/2
ball.pos.z = ground.size.z/2
ball.f = vec(0, 0, 0)
ball.a = vec(0, 0, 0)
ball.m = 0.5
ball.v = vec(10,0,0)
attach_arrow(ball, "v", shaftwidth = 0.5, scale = 0.5, color=color.yellow)

#goal area
goal_center_pos = 0

goal_1 = box(pos=vec(0,0,0), size=vec(1, 10, 1), color = color.red)
goal_1.pos.x = ground.size.x/2 + 5
goal_1.pos.y = goal_center_pos
goal_1.pos.z = 0

goal_2 = box(pos=vec(0,0,0), size=vec(5, 1, 1), color = color.red)
goal_2.pos.x = ground.size.x/2 + goal_2.size.x/2
goal_2.pos.y = goal_center_pos +goal_1.size.y/2 - goal_2.size.y/2
goal_2.pos.z = 0

goal_3 = box(pos=vec(0,0,0), size=vec(5, 1, 1), color = color.red)
goal_3.pos.x = ground.size.x/2 + goal_3.size.x/2
goal_3.pos.y = goal_center_pos -goal_1.size.y/2 + goal_2.size.y/2
goal_3.pos.z = 0

#obstacles
ground_x0 = -ground.size.x/2 #ground area
ground_y0 = ground.size.y/2
ground_x1 = ground.size.x/2
ground_y1 = -ground.size.y/2
    
obstacles = []
for i in range(5):
    obstacles.append(sphere(radius = 4, v = vec(0, 0, ground.size.z/2), m = 0.5))
    
obstacles[0].pos = vec(ground.size.x/6 - ground.size.x/2, ground.size.y/3, 0)
obstacles[1].pos = vec(2*ground.size.x/6 - ground.size.x/2, -ground.size.y/3, 0)
obstacles[2].pos = vec(3*ground.size.x/6 - ground.size.x/2, ground.size.y/3, 0)
obstacles[3].pos = vec(4*ground.size.x/6 - ground.size.x/2, -ground.size.y/3, 0)
obstacles[4].pos = vec(5*ground.size.x/6 - ground.size.x/2, ground.size.y/3, 0)
    
###############################################################################
#slider

#goal area position
scene.append_to_caption(' \nGoal Area Position: ')
goalAreaPosSlider = slider(min = -ground.size.y/2 + goal_1.size.y/2, max = ground.size.y/2 - goal_1.size.y/2, value = 0, bind = setGoalAreaPos)
scene.append_to_caption(goalAreaPosSlider.min, 'to' ,goalAreaPosSlider.max, '\n')

def setGoalAreaPos():
    #########################################################
    #                                                                                                       
    # (1) set goal area position                                                                     
    #                                                                                                       
    #########################################################
    pass
    
#ball initial position
scene.append_to_caption(' \nBall Initial Position: ')
ballInitPosSlider = slider(min = -ground.size.y/2, max = ground.size.y/2 - ball_box.size.y - ball.radius*2, value = 0, bind = setBallInitPos)
scene.append_to_caption(ballInitPosSlider.min, 'to' ,ballInitPosSlider.max, '\n')

def setBallInitPos():
    #########################################################
    #                                                                                                       
    # (2-1) set ball initial position                                                                  
    #                                                                                                       
    #########################################################
    pass
    
#ball initial velocity
scene.append_to_caption(' \nBall Initial Velocity X: ')
ballInitVelXSlider = slider(min = 0, max = 100, value = 10, bind = setBallInitVelX)
scene.append_to_caption(ballInitVelXSlider.min, 'to' ,ballInitVelXSlider.max, '\n')

def setBallInitVelX():
    #########################################################
    #                                                                                                       
    # (2-2) set ball initial velocity x                                                                
    #                                                                                                       
    #########################################################
    pass
    
scene.append_to_caption(' \nBall Initial Velocity Y: ')
ballInitVelYSlider = slider(min = -100, max = 100, value = 10, bind = setBallInitVelY)
scene.append_to_caption(ballInitVelYSlider.min, 'to' ,ballInitVelYSlider.max, '\n')

def setBallInitVelY():
    #########################################################
    #                                                                                                       
    # (2-3) set ball initial velocity y                                                                
    #                                                                                                       
    #########################################################
    pass

#gravity
scene.append_to_caption(' \nGravity: ')
gravitySlider = slider(min = 0, max = 10, value = 9.8, bind = setGravity)
scene.append_to_caption(gravitySlider.min, 'to' ,gravitySlider.max, '\n')

def setGravity():
    #########################################################
    #                                                                                                       
    # (3) set gravity                                                                                    
    #                                                                                                       
    #########################################################
    pass
    
#obstacles initial position
scene.append_to_caption(' \nObstacle 0 Init Position X: ')
obstacle0InitPosXSlider = slider(min = -ground.size.x/2, max = ground.size.x/2, value = obstacles[0].pos.x, bind = setObstacle0InitPosX)
scene.append_to_caption(obstacle0InitPosXSlider.min, 'to' ,obstacle0InitPosXSlider.max, '\n')

def setObstacle0InitPosX():
    #########################################################
    #                                                                                                       
    # (4-1) set obstacle 0 initial poaition x                                                      
    #                                                                                                       
    #########################################################
    pass

scene.append_to_caption(' \nObstacle 0 Init Position Y: ')
obstacle0InitPosYSlider = slider(min = -ground.size.y/2, max = ground.size.y/2, value = obstacles[0].pos.y, bind = setObstacle0InitPosY)
scene.append_to_caption(obstacle0InitPosYSlider.min, 'to' ,obstacle0InitPosYSlider.max, '\n')

def setObstacle0InitPosY():
    #########################################################
    #                                                                                                       
    # (4-2) set obstacle 0 initial poaition y                                                      
    #                                                                                                       
    #########################################################
    pass
    
scene.append_to_caption(' \nObstacle 1 Init Position X: ')
obstacle1InitPosXSlider = slider(min = -ground.size.x/2, max = ground.size.x/2, value = obstacles[1].pos.x, bind = setObstacle1InitPosX)
scene.append_to_caption(obstacle1InitPosXSlider.min, 'to' ,obstacle1InitPosXSlider.max, '\n')

def setObstacle1InitPosX():
    #########################################################
    #                                                                                                       
    # (4-3) set obstacle 1 initial poaition x                                                      
    #                                                                                                       
    #########################################################
    pass
    
scene.append_to_caption(' \nObstacle 1 Init Position Y: ')
obstacle1InitPosYSlider = slider(min = -ground.size.y/2, max = ground.size.y/2, value = obstacles[1].pos.y, bind = setObstacle1InitPosY)
scene.append_to_caption(obstacle1InitPosYSlider.min, 'to' ,obstacle1InitPosYSlider.max, '\n')

def setObstacle1InitPosY():
    #########################################################
    #                                                                                                       
    # (4-4) set obstacle 1 initial poaition y                                                      
    #                                                                                                       
    #########################################################
    pass
    
scene.append_to_caption(' \nObstacle 2 Init Position X: ')
obstacle2InitPosXSlider = slider(min = -ground.size.x/2, max = ground.size.x/2, value = obstacles[2].pos.x, bind = setObstacle2InitPosX)
scene.append_to_caption(obstacle2InitPosXSlider.min, 'to' ,obstacle2InitPosXSlider.max, '\n')

def setObstacle2InitPosX():
    #########################################################
    #                                                                                                       
    # (4-5) set obstacle 2 initial poaition x                                                      
    #                                                                                                       
    #########################################################
    pass
    
scene.append_to_caption(' \nObstacle 2 Init Position Y: ')
obstacle2InitPosYSlider = slider(min = -ground.size.y/2, max = ground.size.y/2, value = obstacles[2].pos.y, bind = setObstacle2InitPosY)
scene.append_to_caption(obstacle2InitPosYSlider.min, 'to' ,obstacle2InitPosYSlider.max, '\n')

def setObstacle2InitPosY():
    #########################################################
    #                                                                                                       
    # (4-6) set obstacle 2 initial poaition y                                                      
    #                                                                                                       
    #########################################################
    pass
    
scene.append_to_caption(' \nObstacle 3 Init Position X: ')
obstacle3InitPosXSlider = slider(min = -ground.size.x/2, max = ground.size.x/2, value = obstacles[3].pos.x, bind = setObstacle3InitPosX)
scene.append_to_caption(obstacle3InitPosXSlider.min, 'to' ,obstacle3InitPosXSlider.max, '\n')

def setObstacle3InitPosX():
    #########################################################
    #                                                                                                       
    # (4-7) set obstacle 3 initial poaition x                                                      
    #                                                                                                       
    #########################################################
    pass
    
scene.append_to_caption(' \nObstacle 3 Init Position Y: ')
obstacle3InitPosYSlider = slider(min = -ground.size.y/2, max = ground.size.y/2, value = obstacles[3].pos.y, bind = setObstacle3InitPosY)
scene.append_to_caption(obstacle3InitPosYSlider.min, 'to' ,obstacle3InitPosYSlider.max, '\n')

def setObstacle3InitPosY():
    #########################################################
    #                                                                                                       
    # (4-8) set obstacle 3 initial poaition y                                                      
    #                                                                                                       
    #########################################################
    pass
    
scene.append_to_caption(' \nObstacle 4 Init Position X: ')
obstacle4InitPosXSlider = slider(min = -ground.size.x/2, max = ground.size.x/2, value = obstacles[4].pos.x, bind = setObstacle4InitPosX)
scene.append_to_caption(obstacle4InitPosXSlider.min, 'to' ,obstacle4InitPosXSlider.max, '\n')

def setObstacle4InitPosX():
    #########################################################
    #                                                                                                       
    # (4-9) set obstacle 4 initial poaition x                                                      
    #                                                                                                       
    #########################################################
    pass
    
scene.append_to_caption(' \nObstacle 4 Init Position Y: ')
obstacle4InitPosYSlider = slider(min = -ground.size.y/2, max = ground.size.y/2, value = obstacles[4].pos.y, bind = setObstacle4InitPosY)
scene.append_to_caption(obstacle4InitPosYSlider.min, 'to' ,obstacle4InitPosYSlider.max, '\n')

def setObstacle4InitPosY():
    #########################################################
    #                                                                                                       
    # (4-10) set obstacle 4 initial poaition y                                                    
    #                                                                                                       
    #########################################################
    pass

################################################################################
def collision(b1, b2, e):
    #########################################################
    #                                                                                                       
    # (5) collision                                                                                       
    #                                                                                                       
    #########################################################
    pass
################################################################################
start = False

g = 5
e = 1

t = 0
dt = 0.01
while True:
    if not start:
        scene.waitfor('click')
        start = True
    
    rate(1/dt)
    
    #collision
    #########################################################
    #                                                                                                       
    # (6) call collision function                                                                      
    #                                                                                                       
    #########################################################
    
    #ball
    #########################################################
    #                                                                                                       
    # (7) calculate force, acceleration, velocity, position                                     
    #                                                                                                       
    #########################################################
    
    #goal area check
    #########################################################
    #                                                                                                       
    # (8) goal area check                                                                             
    #                                                                                                       
    #########################################################
    
    #ground area check
    #########################################################
    #                                                                                                       
    # (9) ground area check                                                                         
    #                                                                                                       
    #########################################################