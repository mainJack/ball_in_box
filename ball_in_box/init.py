import math
import ballinbox as ballinbox
import validate as validate
import area_sum as area_sum

def get_blockers(m,blockers):
    print "The case you want"
    m = input("Please input the number of circles")
    n = input("Please input the number of blockers")
    i = 0
    while i<n:
        str1 = "Please input the x of blocker[" + str(i) + "]"
        x = input(str1)
        str2 = "Please input the y of blocker" + str(i) + "]"
        y = input(str2)
        blockers.append((x,y,0))
        i += 1
    return m

blockers = []
num = 0
num = get_blockers(num,blockers)
circles = ballinbox.ball_in_box(num,blockers)
t = 0
while t<100000:
    circles1 = ballinbox.ball_in_box(num,blockers)
    if area_sum.area_sum(circles)<area_sum.area_sum(circles1):
        circles = circles1
    t += 1

if validate.validate(circles, blockers):
    area = area_sum.area_sum(circles)
    print("Total area: {}".format(area))
    for circle in circles:
        print "(", circle[0], circle[1], circle[2], ")"
else:
    print("Error: no good circles.")

