"""
AE 107 Shark Tank: Aero Edition
CARD 5 -- Paper Jet Labs                          starter template

Customer question:
    "What launch angle and speed give the longest glide, and does the real
     plane match the model?"

Model idea:
    * 2D point-mass glider with constant C_L and C_D.
    * Lift acts PERPENDICULAR to the velocity, drag acts OPPOSITE to it.
    * Launch from shoulder height, sweep the launch angle, record distance.
    * Then fold a real plane, throw it 3 times, and compare!

Your job: fill in every TODO, run the sweep, and plot flight paths.
"""
import numpy as np
import matplotlib.pyplot as plt
from scipy.integrate import solve_ivp

# ----------------------------------------------------------------- givens
g = 9.81
rho = 1.225
m = 0.005                # kg, one sheet of printer paper
S = 0.015                # m^2, wing area (measure yours for the bonus!)
CL = 0.6
CD = 0.10
h0 = 1.8                 # m, launch height
v0 = 8.0                 # m/s, launch speed

# Fill in after you throw the real plane:
measured_distances_m = []      # TODO, e.g. [7.2, 8.1, 6.5]
measured_angle_deg = None      # TODO, roughly what angle did you throw at?


def rhs(t, y):
    """State y = [x, z, vx, vz].  Return [dx/dt, dz/dt, dvx/dt, dvz/dt].

    Hint: with V = |velocity|, the unit vector along the velocity is
    (vx, vz)/V and the unit vector perpendicular to it (pointing "up") is
    (-vz, vx)/V.
    """
    # TODO
    raise NotImplementedError("rhs()")


def ground(t, y):
    """Event: crosses zero when the glider hits the floor."""
    # TODO
    raise NotImplementedError("ground()")


ground.terminal = True
ground.direction = -1


def fly(angle_deg, speed=v0):
    th = np.radians(angle_deg)
    return solve_ivp(rhs, [0, 60], [0, h0, speed * np.cos(th), speed * np.sin(th)],
                     events=ground, max_step=0.01, rtol=1e-8)


# ----------------------------------------------------------------- main
if __name__ == "__main__":
    try:
        angles = np.arange(-20, 41, 2)
        distances = np.array([fly(a).y[0, -1] for a in angles])
        # TODO: print the best angle and its distance

        fig, (ax1, ax2) = plt.subplots(1, 2, figsize=(12, 4))
        for a in (-10, 0, 10, 20):
            s = fly(a)
            ax1.plot(s.y[0], s.y[1], label=f"{a} deg")
        ax1.set(xlabel="x [m]", ylabel="height [m]", title="Flight paths")
        ax1.legend(); ax1.grid(True)

        ax2.plot(angles, distances, "o-", label="model")
        # TODO: add your measured throws to this plot
        ax2.set(xlabel="Launch angle [deg]", ylabel="Distance [m]",
                title="Model vs. measured")
        ax2.legend(); ax2.grid(True)
        fig.tight_layout()
        plt.show()
    except NotImplementedError as e:
        print(f"Not finished yet -- fill in the TODO in {e}")

# SANITY CHECK (by hand):
#   In a steady glide, distance = height * (L/D) = h0 * CL / CD.
#   And the steady glide speed comes from lift = weight. Compute both.
#   Why can the simulated glider beat the steady-glide distance?
