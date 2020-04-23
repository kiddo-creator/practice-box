x,y,w,h = map(int,input().split())

dis_x=abs(w-x)
dis_y=abs(h-y)

def dis(disx,dis_y):
    if dis_x>dis_y:
        return dis_y
    else:
        return dis_x

print(dis(dis_x,dis_y))
