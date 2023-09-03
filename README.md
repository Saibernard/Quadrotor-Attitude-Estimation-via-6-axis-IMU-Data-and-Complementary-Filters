# Quadrotor-Attitude-Estimation-via-6-axis-IMU-Data-and-Complementary-Filters
This repository offers a deep dive into quadrotor attitude determination using a 6-axis IMU. Leveraging the EuRoc dataset from ETH Zurich, the project adopts a complementary filter approach for precise attitude estimation.


## Overview

### Quadrotor Attitude Estimation using 6-axis IMU Data

This project zeroes in on determining the attitude of a quadrotor accurately through data sourced from a 6-axis Inertial Measurement Unit (IMU). The IMU is pivotal, providing crucial acceleration and angular rate readings. The foundational data for this project is extracted from the renowned EuRoc dataset by ETH Zurich.

## Code Framework
Outlined below is the code structure:

- **setup.py**: Initializes package installations.
- **project package**:
  - **util**: Hosts unit tests.
  - **dataset**: Features a subset of the EuRoc dataset, emphasizing IMU data.
  - **code**: Encompasses core code files and sandbox files integral to this initiative.

Within this structure, the **complementary filter.py** is architectured to contain the complementary filter algorithm logic. The algorithm's efficiency is reflected through a plotting mechanism that processes vast IMU readings.

## Algorithm Details and Formulas

Central to this endeavor is the complementary filter algorithm, detailed as follows:

1. **Initialization**: Start with an initial rotation estimate presented as a `scipy.spatial.transform.Rotation` object.
   
2. **Inputs**: Each update requires:
   - Two 3x1 vectors signifying the angular velocity and measured acceleration.
   - Duration of the interval.

3. **Quaternion Adjustments**: The Rotation class formats quaternions as (x, y, z, w), distinguishing it from the traditional (w, x, y, z) sequence.

4. **Gravity Alignment**: Data indicates the IMU's x-axis aligning more with gravitational force than the z-axis, necessitating a quaternion adjustment to derive the rotation correction `q_acc`.

5. **Normalization**: Given acceleration measurements in m/s^2, normalization is crucial for accurate attitude inference.

6. **Rotation Estimation**: Central to the complementary filter update function is:

\[ R_{new} = R_{old} \times q_{\omega} \times (1-\alpha) + R_{old} \times q_{acc} \times \alpha \]

Where:
   - \( R_{new} \) and \( R_{old} \) are the new and previous rotation matrices.
   - \( q_{\omega} \) is the quaternion rotation from angular velocities.
   - \( q_{acc} \) is the quaternion rotation from acceleration.
   - \( \alpha \) is the complementary filter blending element.

7. **Rodrigues Formula Connection**: The project dives into the connection between quaternions and the Rodrigues Formula. Specifically:

\[ H(u_0, u) = (u_0^2 - u^T u) I + 2 u_0 \hat{u} + 2 u u^T \]

Established as equivalent to the Rodrigues Formula, this interlinks the two rotation expressions.

## Concluding Remarks
Throughout this project, utmost care and precision were maintained, ensuring authentic outcomes and a deep-rooted grasp of quadrotor attitude estimation.

