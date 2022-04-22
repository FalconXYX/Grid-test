import box
black = (0,0,0)
def main(num, dementions, dis):
    tempthing = []
    for i in range(1,num):
        for l in range(1,num):
            tempthing.append(box.part(i*dementions,l*dementions,dementions,dementions,black,dis))
    
    return tempthing