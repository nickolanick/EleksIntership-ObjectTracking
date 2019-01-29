import time
class Circle:
    def __init__(self,x,y,r,id,time_created):
        self.id = id
        self.x = x
        self.y = y
        self.r = r
        self.timeStart = time_created
        self.time_created = time_created


    def update(self,x,y,r):
        is_close =self.is_close(x,y,r)
        if is_close:
            self.set_new(x,y,is_close)
            print(self.timeStart,"time start")
            print(self.id,"ID")
            return True
        print("NEW CREATED NEW CREATED NEW CREATED")
        print(self.id,"ID")
        return False
    def is_close(self,x,y,r):
        new_x= abs(self.x-x)
        new_y = abs(self.y - y)
        new_r = abs(self.r - r)
        print(new_x,new_y,new_r,"IS CLOSE")

        if new_x < 50 and new_y <50 and new_r < 40:
            return (self.r+r)//2
        return False

    def set_new(self,x,y,r):
        self.x = x
        self.y = y
        self.r = r
        self.time_created = time.time()

    def __str__(self):
        return "x{} y{} r{}".format(self.x,self.y,self.r)