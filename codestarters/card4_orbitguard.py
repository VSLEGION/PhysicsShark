"""
AE 107 Shark Tank: Aero Edition
CARD 4 -- OrbitGuard                              starter template

Customer question:
    "Will this debris come within 5 km of our satellite in the next 24 hours,
     and when?"

Model idea:
    * Two-body gravity only:  r_ddot = -mu * r / |r|^3   (for each object)
    * Integrate both objects together (12 states) for 24 hours.
    * Compute the distance between them at every second and find the minimum.

Your job: fill in every TODO, propagate, and plot the separation.
"""
import numpy as np
import matplotlib.pyplot as plt
from scipy.integrate import solve_ivp

# ----------------------------------------------------------------- givens
mu = 3.986004418e14      # m^3/s^2, Earth's gravitational parameter
R_E = 6378.137e3         # m
threshold_km = 5.0

# Initial states in an Earth-centered inertial frame: [x, y, z] (m), [vx, vy, vz] (m/s)
sat_r0 = np.array([-6691645.3, 988123.3, 1246701.3])
sat_v0 = np.array([-1760.6736, -4600.3461, -5804.1922])
deb_r0 = np.array([-4569328.5, -4309909.8, 2806300.0])
deb_v0 = np.array([-2972.8915, -1328.0615, -6880.2134])


def rhs(t, y):
    """y = [r_sat (3), v_sat (3), r_deb (3), v_deb (3)].  Return dy/dt (12 values)."""
    # TODO: two-body acceleration for each object
    raise NotImplementedError("rhs()")


# ----------------------------------------------------------------- main
if __name__ == "__main__":
    try:
        # Quick checks before the main event:
        # TODO: print each object's altitude (km) and orbital period (min)

        y0 = np.concatenate([sat_r0, sat_v0, deb_r0, deb_v0])
        t_eval = np.arange(0, 24 * 3600 + 1, 1.0)     # every second
        sol = solve_ivp(rhs, [0, t_eval[-1]], y0, t_eval=t_eval,
                        method="DOP853", rtol=1e-11, atol=1e-6)

        # TODO: separation distance in km at each time step
        sep_km = None

        # TODO: find and print the time (hours) and distance of the closest approach
        # TODO: list every pass that comes inside threshold_km

        plt.figure(figsize=(9, 4))
        plt.semilogy(sol.t / 3600, sep_km)
        plt.axhline(threshold_km, color="r", ls="--", label="5 km alert")
        plt.xlabel("Time [h]")
        plt.ylabel("Separation [km]")
        plt.legend()
        plt.grid(True, which="both")
        plt.show()
    except NotImplementedError as e:
        print(f"Not finished yet -- fill in the TODO in {e}")

# SANITY CHECK (by hand):
#   From |r| compute each object's altitude and its circular-orbit period
#   T = 2 pi sqrt(r^3 / mu). Does your plot's repeating pattern match?
#   Try method="RK45" with rtol=1e-6. Why does the answer change?
