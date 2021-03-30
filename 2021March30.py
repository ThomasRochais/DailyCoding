import math

def dist(p1, p2):
    return math.sqrt( (p1[0]-p2[0])**2 + (p1[1]-p2[1])**2 )

def nearest_pts(points, central, k):
    if k >= len(points):
        return points
    else:
        closest_pts = [None]*k
        for i in range(k):
            distance = dist(central, points[i])
            closest_pts[i] = (points[i], distance)
        closest_pts = sorted(closest_pts, key = lambda pts: pts[1])
        for i in range(k, len(points)):
            distance = dist(central, points[i])
            if distance < closest_pts[-1][1]:
                j = -1
                while j >= -k and distance < closest_pts[j][1]:
                    j -= 1
                closest_pts.insert(j+1, (points[i], distance))
                closest_pts.pop(-1)
        return closest_pts

L = [(9, 2), (1, 1), (1, 1.5), (0, 0), (5, 4), (3, 1)]
print(nearest_pts(L, (1,2), 4))