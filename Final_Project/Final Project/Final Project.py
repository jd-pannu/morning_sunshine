import math
import open3d as o3d
import numpy as np



import serial

s = serial.Serial('COM4', baudrate = 115200, timeout = 10)
                            
print("Opening: " + s.name)


s.reset_output_buffer()
s.reset_input_buffer()


input("Press Enter to start communication...")

s.write('s'.encode())

f = open("tof_radar.xyz", "w")


count = 0
distancex = 0
x = s.readline()
while x.decode() != "s":
    angle = 0
    x = s.readline()
    try:
        integer = int(x.decode())
        for i in range(32):
            x = s.readline()
            integer = int(x.decode())
            print(integer)
            distancey = integer*math.cos(angle)
            distancez = integer*math.sin(angle)
            f.write('{} {} {}\n'.format(distancex, distancey, distancez))

            angle += math.pi / 16

        count += 1
        print("Continue to read more values or stop reading")
            
    except ValueError:
        if x.decode() != '':
            print(x.decode())
        continue
    

    distancex += 3000


    
       

f.close()
   
        
print("Read in the prism point cloud data (pcd)")
pcd = o3d.io.read_point_cloud("tof_radar.xyz", format="xyz")

     
print("The PCD array:")
print(np.asarray(pcd.points))

     
print("Lets visualize the PCD: (spawns seperate interactive window)")
o3d.visualization.draw_geometries([pcd])


yz_slice_vertex = []
for x in range(0, 32*count):
    yz_slice_vertex.append([x])

       
lines = []
for x in range(0, 32*count, 32): 
    lines.append([yz_slice_vertex[x], yz_slice_vertex[x+1]])
    lines.append([yz_slice_vertex[x+1], yz_slice_vertex[x+2]])
    lines.append([yz_slice_vertex[x+2], yz_slice_vertex[x+3]])
    lines.append([yz_slice_vertex[x+3], yz_slice_vertex[x+4]])
    lines.append([yz_slice_vertex[x+4], yz_slice_vertex[x+5]])
    lines.append([yz_slice_vertex[x+5], yz_slice_vertex[x+6]])
    lines.append([yz_slice_vertex[x+6], yz_slice_vertex[x+7]])
    lines.append([yz_slice_vertex[x+7], yz_slice_vertex[x+8]])
    lines.append([yz_slice_vertex[x+8], yz_slice_vertex[x+9]])
    lines.append([yz_slice_vertex[x+9], yz_slice_vertex[x+10]])
    lines.append([yz_slice_vertex[x+10], yz_slice_vertex[x+11]])
    lines.append([yz_slice_vertex[x+11], yz_slice_vertex[x+12]])
    lines.append([yz_slice_vertex[x+12], yz_slice_vertex[x+13]])
    lines.append([yz_slice_vertex[x+13], yz_slice_vertex[x+14]])
    lines.append([yz_slice_vertex[x+14], yz_slice_vertex[x+15]])
    lines.append([yz_slice_vertex[x+15], yz_slice_vertex[x+16]])
    lines.append([yz_slice_vertex[x+16], yz_slice_vertex[x+17]])
    lines.append([yz_slice_vertex[x+17], yz_slice_vertex[x+18]])
    lines.append([yz_slice_vertex[x+18], yz_slice_vertex[x+19]])
    lines.append([yz_slice_vertex[x+19], yz_slice_vertex[x+20]])
    lines.append([yz_slice_vertex[x+20], yz_slice_vertex[x+21]])
    lines.append([yz_slice_vertex[x+21], yz_slice_vertex[x+22]])
    lines.append([yz_slice_vertex[x+22], yz_slice_vertex[x+23]])
    lines.append([yz_slice_vertex[x+23], yz_slice_vertex[x+24]])
    lines.append([yz_slice_vertex[x+24], yz_slice_vertex[x+25]])
    lines.append([yz_slice_vertex[x+25], yz_slice_vertex[x+26]])
    lines.append([yz_slice_vertex[x+26], yz_slice_vertex[x+27]])
    lines.append([yz_slice_vertex[x+27], yz_slice_vertex[x+28]])
    lines.append([yz_slice_vertex[x+28], yz_slice_vertex[x+29]])
    lines.append([yz_slice_vertex[x+29], yz_slice_vertex[x+30]])
    lines.append([yz_slice_vertex[x+30], yz_slice_vertex[x+31]])
    lines.append([yz_slice_vertex[x+31], yz_slice_vertex[x]])

if count > 1:
    for x in range(0, 32*count - 32, 32): 
        lines.append([yz_slice_vertex[x], yz_slice_vertex[x+32]])
        lines.append([yz_slice_vertex[x+1], yz_slice_vertex[x+33]])
        lines.append([yz_slice_vertex[x+2], yz_slice_vertex[x+34]])
        lines.append([yz_slice_vertex[x+3], yz_slice_vertex[x+35]])
        lines.append([yz_slice_vertex[x+4], yz_slice_vertex[x+36]])
        lines.append([yz_slice_vertex[x+5], yz_slice_vertex[x+37]])
        lines.append([yz_slice_vertex[x+6], yz_slice_vertex[x+38]])
        lines.append([yz_slice_vertex[x+7], yz_slice_vertex[x+39]])
        lines.append([yz_slice_vertex[x+8], yz_slice_vertex[x+40]])
        lines.append([yz_slice_vertex[x+9], yz_slice_vertex[x+41]])
        lines.append([yz_slice_vertex[x+10], yz_slice_vertex[x+42]])
        lines.append([yz_slice_vertex[x+11], yz_slice_vertex[x+43]])
        lines.append([yz_slice_vertex[x+12], yz_slice_vertex[x+44]])
        lines.append([yz_slice_vertex[x+13], yz_slice_vertex[x+45]])
        lines.append([yz_slice_vertex[x+14], yz_slice_vertex[x+46]])
        lines.append([yz_slice_vertex[x+15], yz_slice_vertex[x+47]])
        lines.append([yz_slice_vertex[x+16], yz_slice_vertex[x+48]])
        lines.append([yz_slice_vertex[x+17], yz_slice_vertex[x+49]])
        lines.append([yz_slice_vertex[x+18], yz_slice_vertex[x+50]])
        lines.append([yz_slice_vertex[x+19], yz_slice_vertex[x+51]])
        lines.append([yz_slice_vertex[x+20], yz_slice_vertex[x+52]])
        lines.append([yz_slice_vertex[x+21], yz_slice_vertex[x+53]])
        lines.append([yz_slice_vertex[x+22], yz_slice_vertex[x+54]])
        lines.append([yz_slice_vertex[x+23], yz_slice_vertex[x+55]])
        lines.append([yz_slice_vertex[x+24], yz_slice_vertex[x+56]])
        lines.append([yz_slice_vertex[x+25], yz_slice_vertex[x+57]])
        lines.append([yz_slice_vertex[x+26], yz_slice_vertex[x+58]])
        lines.append([yz_slice_vertex[x+27], yz_slice_vertex[x+59]])
        lines.append([yz_slice_vertex[x+28], yz_slice_vertex[x+60]])
        lines.append([yz_slice_vertex[x+29], yz_slice_vertex[x+61]])
        lines.append([yz_slice_vertex[x+30], yz_slice_vertex[x+62]])
        lines.append([yz_slice_vertex[x+31], yz_slice_vertex[x+63]])

    


line_set = o3d.geometry.LineSet(points=o3d.utility.Vector3dVector(np.asarray(pcd.points)),lines=o3d.utility.Vector2iVector(lines))

      
o3d.visualization.draw_geometries([line_set])

    
#close the port
print("Closing: " + s.name)
s.close()
