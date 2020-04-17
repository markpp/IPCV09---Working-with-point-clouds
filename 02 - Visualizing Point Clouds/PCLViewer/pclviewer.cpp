/**
pclviewer.cpp
Purpose: Visualize point cloud.

@author Mark Philip Philipsen
@version 1.0 12/6/17
*/
#include <boost/thread/thread.hpp>
#include <string>
#include <iostream>
#include <fstream>

#include <pcl/common/common_headers.h>
#include <pcl/io/pcd_io.h>
#include <pcl/io/ply_io.h>
#include <pcl/point_types.h>
#include <pcl/visualization/pcl_visualizer.h>

#include "libs/cxxopts.hpp"

typedef pcl::PointXYZ PointT;
//typedef pcl::PointXYZRGB PointT;

/**
Main function.

Example:
./pclviewer -p ../input/test.pcd

@param argc the number of commandline arguments. argv, the commandline arguments
@terminates when "q" is pressed.
*/
int main( int argc, char** argv )
{
  cxxopts::Options options("pclviewer", "Shows point cloud");
  options.add_options()
    ("p,path", ".pcd file", cxxopts::value<std::string>());
  options.parse(argc, argv);

  // Get path and load the current point cloud
  std::string path_cloud = options["path"].as<std::string>();
  pcl::PointCloud<PointT>::Ptr input_cloud(new pcl::PointCloud<PointT>);
  if(pcl::io::loadPCDFile<PointT>(path_cloud, *input_cloud) == -1)
  {
    PCL_ERROR("Couldn't read .pcd file \n");
    return (-1);
  }

  // Initialize viewer
  std::size_t filename_location = path_cloud.find_last_of("/\\");
  std::stringstream label_stream;
  label_stream << path_cloud.substr(filename_location+1);
  boost::shared_ptr<pcl::visualization::PCLVisualizer> viewer (new pcl::visualization::PCLVisualizer("Showing '" + label_stream.str() + "'. Press 'q' to quit"));

  while(!viewer->wasStopped())
  {
    if (!viewer->updatePointCloud<PointT>(input_cloud, "cloud"))
    {
      viewer->addPointCloud<PointT>(input_cloud, "cloud");
    }
    viewer->spinOnce(1);
  }
  return 0;
}
