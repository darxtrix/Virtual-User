from SimpleCV import *
import numpy as np
from SimpleCV.Display import Display
cam=Camera()
import time
from mouse_api import *
m = Mouse()
nf = 2
h = 0
fl=[]
reset = 0

while h<nf:
	h = h + 1
	snap = cam.getImage()                
	d = Display(snap.size())
	snap.save(d)
	col = Color.RED
	start_time = time.time()
	i=0
	while d.isNotDone():
	    elapsed_time = time.time() - start_time
	    if d.mouseLeft:
	        txt = "coord: (" + str(d.mouseX) + "," + str(d.mouseY) + ")"
	        snap.dl().text(txt, (10,snap.height / 2), color=col)
	        txt = "color: " + str(snap.getPixel(d.mouseX,d.mouseY))
	        snap.dl().text(txt, (10,(snap.height / 2) + 10), color=col)
	        print "coord: (" + str(d.mouseX) + "," + str(d.mouseY) + "), color: " + str(snap.getPixel(d.mouseX,d.mouseY))
	        if i==1:    
	            x2=d.mouseX
	            y2=d.mouseY
	            time.sleep(1)      
	    if d.mouseLeft:
	        if i==0:
	            x1=d.mouseX
	            y1=d.mouseY
	            time.sleep(1)
	            i=i+1
	    snap.save(d)
	    if d.mouseRight:
	        print "Closing Window"
	        d.done = True
	pg.quit()
	print ( str(x1) + "," + str(x2)+ "," +str(y1) + "," + str(y2))  
	cropsnap = snap.crop(x1,y1,abs(x2-x1),abs(y2-y1))
	f = np.array(cropsnap.getMatrix())
	r = list(f[:,:,0])
	g = list(f[:,:,1])
	b = list(f[:,:,2])
	rmin = min(r[0])
	rmax = max(r[0])
	gmin = min(g[0])
	gmax = max(g[0])
	bmin = min(b[0])
	bmax = max(b[0])
	for i in list(r):
	    if min(i)<rmin:    
	        rmin=min(i)
	    if max(i)>rmax:
	        rmax = max(i)
	for i in list(g):
	    if min(i)<gmin:
	        gmin=min(i)
	    if max(i)>gmax:
	        gmax = max(i)
	for i in list(b):
	    if min(i)<bmin:
	        bmin=min(i)
	    if max(i)>bmax:
	        bmax = max(i)
	l = [bmin,bmax,gmin,gmax,rmin,rmax]
	fl.append(l)
par = 0
c1 = 0
###### par = 2 # blue
def check(f,lt,c1,xc):
	global reset,list1
	par = 0
	x11 = f[:,:,0]>=lt[4]
	x12 = f[:,:,0]<=lt[5]
	x21 = f[:,:,1]>=lt[2]
	x22 = f[:,:,1]<=lt[3]
	x31 = f[:,:,2]>=lt[0]
	x32 = f[:,:,2]<=lt[1]
	x1 = x11*x12
	x2 = x21*x22
	x3 = x31*x32
	x = x1*x2*x3
	if np.sum(x)>200:
		if c1==0:
		   par = 1
		if c1==1:
		   par = 2
		if c1==2:
		   par = 3
		if c1==3:
		   par = 4
		#print par, np.sum(x)
	
	
	
	if par == 1:
	    cord(x,xc)
	    reset = 0
	 
	if par == 2 and reset == 0:
	    time.sleep(0.7)
	    m.mouseEvent(LEFT)
	    reset = 1
	if par == 3 and reset == 0:
	    time.sleep(0.7)
	    m.mouseEvent(DOUBLE)
	    reset = 1
	if par == 4 and reset == 0:
	    time.sleep(0.7)
	    m.mouseEvent(RIGHT)
	    reset = 1

def cord(x,xc):
	yc=0
        t=0
	sum1 = 0
	count = 0
	for el in x:
	    factor = np.sum(el)
     	    t = t + factor*yc
     	    yc = yc + 1
	p = np.sum(x)
	reqy = int(t/p)
	lg = x[reqy]
	#print lg
	for k in range(xc):
		if lg[k]==True:
		    sum1 = sum1 + k
		    count = count + 1
	if count!=0:
	    reqx = int(sum1/count)
	    
	    #print reqx,"%%%", reqy
	###############
	    try:
	        m.mouseMove(int((xc-reqx)*1366/640),int(reqy*768/480))
	    except Exception:
		    pass
		

while 1:
	c1 = 0
	i = cam.getImage()
	#print i.size()
	(xc,yc) = i.size()
	f = np.array(i.getMatrix())
	while c1<nf:
		check(f,fl[c1],c1,xc)
		c1 = c1 +1
		

	













	


