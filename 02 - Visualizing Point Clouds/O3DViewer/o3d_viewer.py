import numpy as np
import argparse
import os
import open3d as o3d

def save_view_point(vis, filename):
    parms = vis.get_view_control().convert_to_pinhole_camera_parameters()
    o3d.io.write_pinhole_camera_parameters(filename, parms)

def load_view_point(vis, filename):
    ctr = vis.get_view_control()
    parms = o3d.io.read_pinhole_camera_parameters(filename)
    ctr.convert_from_pinhole_camera_parameters(parms)

if __name__ == '__main__':
    """
    Main function for executing the .py script.
    Command:
        -p <filename>.ply
    """
    # construct the argument parser and parse the arguments
    ap = argparse.ArgumentParser()
    ap.add_argument("-p", "--path", type=str,
                    help="absolute path to .ply or .pcd files") # can someone make it work with relative paths?
    args = vars(ap.parse_args())

    # Initialize the visualizer
    vis = o3d.visualization.Visualizer()
    vis.create_window(window_name="Press 'h' for help, 'q' to terminate")
    vis.get_render_option().load_from_json("renderoption.json")

    # Load a point cloud
    cloud = o3d.io.read_point_cloud(args["path"])

    vis.add_geometry(cloud)
    load_view_point(vis, "o3d_viewpoint.json")
    vis.run()

    # Save things
    save_view_point(vis, "o3d_viewpoint.json")

    # convert to pcd
    #pcd_filename = "{}.pcd".format(args["path"].split(".")[0])
    #o3d.io.write_point_cloud(pcd_filename, cloud)

    vis.destroy_window()
