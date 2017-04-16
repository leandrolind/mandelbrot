#Developed by Leandro Lind

from PIL import Image
import time
import colorsys
import math

start_time = time.time()

max_iterations = 100
win_max = 800
scale = 250.0
x_offset = -0.7
y_offset = 0

img = Image.new("RGB", (win_max, win_max), (0,255,255))

pc = 0
pc2 = 0

for num_y in range(win_max):

    pc = int((float(num_y) / float(win_max))*100)

    if pc > pc2:
        print pc, "%"
        pc2 = pc
    else:
        pc2 = pc

    y = ((num_y/(scale)) - ((win_max/2)/scale) + y_offset)*-1
        
    for num_x in range(win_max):
    
        count = 0
        check = 0

        x = (num_x/(scale)) - ((win_max/2)/scale) + x_offset

        c = complex(x, y)

        z = complex(0, 0)

        d = 0

        while count < max_iterations :

            z = z**2 + c

            if abs(z) > 2 :
                d = count

                mu = d + 1 - math.log10((math.log10(abs(z)))) / math.log10(2)
                ru = mu / max_iterations

            if abs(z) > 1000000000000 :

                check = count
                count = max_iterations
           
            count += 1
      
        if abs(z) <= 2:
            img.putpixel((num_x, num_y), (0, 0, 0))

        else :
      
            r1, g1, b1 = colorsys.hls_to_rgb(0.666, ru, 1)            
            r2, g2, b2 = int(r1*255), int(g1*255), int(b1*255)
            img.putpixel((num_x, num_y), (r2, g2, b2))
            

timestr = time.strftime("%Y%m%d-%H%M%S")
img.save("Img_Mandelbrot_"+timestr+".png","PNG")

elapsed_time = time.time() - start_time
print elapsed_time
