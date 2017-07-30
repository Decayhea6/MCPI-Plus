import mcpi.minecraft as minecraft
import time
mc = minecraft.Minecraft.create()
global blockId
blockId = 0
import pickle
while True:
    #GET THE PARTICLE TYPE
    datafile = open('ParticleType.dat', 'rb')
    Database = pickle.load(datafile)
    blockId = Database['blockdata']
    #FIND YOUR LOCATION
    pos = mc.player.getPos()
    ay = pos.y - 1
    #FIND THE TYPES OF BLOCKS
    blockType = mc.getBlock(pos.x, ay, pos.z)
    playerBlock = mc.getBlock(pos.x, pos.y, pos.z)

    if blockId == 78:
        if blockType != 0 and blockType != 78:
            mc.setBlock(pos.x, pos.y, pos.z, blockId)
        
        
        
    else:
    #DROP PARTICLE
        mc.setBlock(pos.x, pos.y, pos.z, blockId)
        mc.setBlock(pos.x, ay, pos.z, 0)
        mc.setBlock(pos.x, ay, pos.z, 1)
        mc.setBlock(pos.x, ay, pos.z, blockType)
        mc.setBlock(pos.x, pos.y, pos.z, playerBlock)
    #WAIT A LITTLE if u take away hashtag
    #time.sleep(0.2)

