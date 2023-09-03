# Quadrotor-Attitude-Estimation-via-6-axis-IMU-Data-and-Complementary-Filters
This repository offers a deep dive into quadrotor attitude determination using a 6-axis IMU. Leveraging the EuRoc dataset from ETH Zurich, the project adopts a complementary filter approach for precise attitude estimation.


## Overview

### Quadrotor Attitude Estimation using 6-axis IMU Data

This project centers on determining the attitude of a quadrotor accurately through data sourced from a 6-axis Inertial Measurement Unit (IMU). The IMU is pivotal, providing essential acceleration and angular rate readings. The foundational data for this project is a subset of the renowned EuRoc dataset by ETH Zurich.

## Code Framework
Outlined below is the code structure:
- **setup.py**: Initializes package installations.
- **proj2 1 package**:
  - **util**: Houses unit tests.
  - **dataset**: Contains a snippet of the EuRoc dataset, majorly focusing on IMU data.
  - **code**: Houses core code files and sandbox files vital to this project.

The **complementary filter.py** is crafted to contain the logic for the complementary filter algorithm. The algorithm's efficiency is evident through a plotting procedure that processes extensive IMU readings.

## Algorithm Details and Formulas
At the core of this endeavor is the complementary filter algorithm:

1. **Initialization**: Kickstart with an initial rotation estimate, which is a `scipy.spatial.transform.Rotation` object.
2. **Inputs**: For every update, the filter needs:
   - Two 3x1 vectors that showcase angular velocity and the measured acceleration.
   - The time duration of that specific interval.
3. **Quaternion Adjustments**: The Rotation class details quaternions as (x, y, z, w) which is a change from the traditional (w, x, y, z) sequence.
4. **Gravity Alignment**: The data denotes the IMU's x-axis is more aligned with gravitational force than the z-axis. This demands a tweak in the quaternion build to get the rotation correction termed as `q_acc`.
5. **Normalization**: Acceleration measurements being in m/s^2, normalization becomes a vital step for precise attitude estimation.
6. **Rotation Estimation**: The main formula for the complementary filter update function is:
   
   R_new = R_old * q_w * (1-alpha) + R_old * q_acc * alpha

Where:
   - R_new and R_old signify the new and previous rotation matrices respectively.
   - q_w is the quaternion rotation derived from angular velocities.
   - q_acc is the quaternion rotation courtesy of acceleration.
   - alpha stands for the complementary filter blending element.
7. **Rodrigues Formula Link**: The project ventures into the tie-up between quaternions and the Rodrigues Formula. Explicitly, the formula given is:

   H(u_0, u) = (u_0^2 - uT * u)I + 2u_0 * u_hat + 2u * uT

This has been derived to equate the Rodrigues Formula, thus connecting the two rotation representations.

## Final Remarks
Throughout the project's duration, undivided attention and precision were the norms, ensuring genuine results and a comprehensive understanding of quadrotor attitude estimation.

