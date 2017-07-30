#==--Simple Script To Place Blocks that are NOT in the Game Inventory--==#
import mcpi.minecraft as minecraft
mc = minecraft.Minecraft.create()
import pickle


while True:
    blockEvent = mc.events.pollBlockHits()
    for blockHit in blockEvent:
        
        #start from here to write what happens after a block is hit--
        #print('HIT')
        datafile = open('BlockID.dat', 'rb')
        Database = pickle.load(datafile)
        blockId = Database['blockdata']
        #print('Block ID: ' + str(blockId))
        
        x = blockHit.pos.x
        y = blockHit.pos.y
        z = blockHit.pos.z
        
        sideHit = blockHit.face
        #mc.postToChat(sideHit)

        if sideHit == 0: 
            y = y - 1
        elif sideHit == 1:
            y = y + 1
        elif sideHit == 2:
            z = z - 1
        elif sideHit == 3:
            z = z + 1
        elif sideHit == 4:
            x = x - 1
        elif sideHit == 5:
            x = x +1
            
        mc.setBlock(x, y, z, blockId)#<Block id here. If using gui, place 'blockId' here   
            
        
    
