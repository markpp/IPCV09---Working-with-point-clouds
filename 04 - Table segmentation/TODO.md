# 04 - Table segmentation

The segmentation method is based on RANdom SAmple Consensus (RANSAC). If you are unfamiliar with the method, it is explained well here RANSAC - Random Sample Consensus I](https://www.coursera.org/lecture/robotics-perception/ransac-random-sample-consensus-i-z0GWq "RANSAC for line fitting") for fitting a line.

1. Follow PCL's [tutorial on planar segmentation](https://pcl.readthedocs.io/projects/tutorials/en/latest/planar_segmentation.html "PCL tutorials").
2. Instead of the generated point cloud load "table_scene_lms400.pcd"
3. Visualize the plane (hint: [addPlane](http://docs.pointclouds.org/trunk/classpcl_1_1visualization_1_1_p_c_l_visualizer.html#a27a459da46f56faed4b44ef1c57bbbca))
