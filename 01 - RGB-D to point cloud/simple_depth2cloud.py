#!/usr/bin/env python
import numpy as np
import cv2
import os
import open3d as o3d

# accuracy can be improved. How?
def create_point_cloud(depth,rgb):
    height, width = depth.shape
    points = []
    for j in range(height):
        for i in range(width):
            # 3D
            d = depth[j,i]
            z = d
            x = (i-width/2)*d*(1/572.4114) # inverse focal length fx
            y = (j-height/2)*d*(1/573.57043) # inverse focal length fy
            # color
            r = rgb[j,i,0]
            g = rgb[j,i,1]
            b = rgb[j,i,2]
            points.append([x,y,z,r,g,b])

    return np.array(points)


if __name__ == '__main__':
    rgb = (cv2.cvtColor(cv2.imread("rgb.png"), cv2.COLOR_BGR2RGB)/255.0).astype('float32')
    depth = cv2.imread("depth.png",-1)/1000.0 # convert to meters

    color_points = create_point_cloud(depth,rgb)

    cloud = o3d.geometry.PointCloud()
    cloud.points = o3d.utility.Vector3dVector(color_points[:,:3])
    cloud.colors = o3d.utility.Vector3dVector(color_points[:,3:])
    o3d.io.write_point_cloud("simple_cloud.ply", cloud)
