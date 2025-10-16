# `kisbeadando_feladat` package
ROS 2 python package.  [![Static Badge](https://img.shields.io/badge/ROS_2-Humble-34aec5)](https://docs.ros.org/en/humble/)
## Packages and build

It is assumed that the workspace is `~/ros2_ws/`.

### Clone the packages
``` r
cd ~/ros2_ws/src
```
``` r
git clone https://github.com/ImreMarkus/imr_atc_repo
```

### Build ROS 2 packages
``` r
cd ~/ros2_ws
```
``` r
colcon build --packages-select kisbeadando_feladat --symlink-install
```

<details>
<summary> Don't forget to source before ROS commands.</summary>

``` bash
source ~/ros2_ws/install/setup.bash
```
</details>

``` r
ros2 launch kisbeadando_feladat obstacle_detector_launch.py
```

``` r
A package két node-ból áll.A lidar_simulator egy LiDAR-t szimulál, véletlenszerű távolságokat generál, amiket a distance topicban hirdet (std_msgs/msg/Float32). Az obstacle_monitor egy akadályfigyelő node, ami feliratkozik a distance topicra (std_msgs/msg/Float32). Ha a távolság kisebb, mint 0.5m, akkor kiad egy alert topicot (std_msgs/msg/String) és a node konzolon figyelmezteti a felhasználót. Megvalósítás ROS2-vel.
```

```mermaid
graph LR
  subgraph Nodes
    LS[LidarSimulator]
    OM[ObstacleMonitor]
  end

  subgraph Topics
    D[/distance/]
    A[/alert/]
  end

  LS -- publishes --> D
  OM -- subscribes --> D
  OM -- publishes --> A