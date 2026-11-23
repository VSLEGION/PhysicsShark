"""
AE 107 Shark Tank: Aero Edition
CARD 3 -- SoftLanding Inc.                        starter template

Customer question:
    "What parachute size gets our 2 kg payload down under 5 m/s, without
     drifting off the field?"

Model idea:
    * The chute opens at 300 m. The payload is falling at 15 m/s at that moment.
    * 1D vertical motion with drag:  m dv/dt = m g - 0.5 rho v^2 Cd A
      (take v positive DOWNWARD).
    * The wind blows the payload sideways at the wind speed the whole way down,
      so drift = wind speed * descent time.

Your job: fill in every TODO, sweep the parachute diameter, and plot.
"""
import numpy as np
import matplotlib.pyplot as plt
from scipy.integrate import solve_ivp

# ----------------------------------------------------------------- givens
g = 9.81
rho = 1.225              # kg/m^3 (you may use constant density -- or isa() for bonus)
m = 2.0                  # kg
Cd = 1.5                 # round parachute, based on canopy area pi D^2 / 4
h_deploy = 300.0         # m
v_deploy = 15.0          # m/s, downward speed when the chute opens
wind = 4.0               # m/s
v_target = 5.0           # m/s, max safe landing speed


def rhs(t, y, D):
    """State y = [height h (m), downward speed v (m/s)].  D = chute diameter (m)."""
    # TODO: return [dh/dt, dv/dt]
    raise NotImplementedError("rhs()")


def ground(t, y, D):
    """Event: crosses zero when the payload hits the ground."""
    # TODO
    raise NotImplementedError("ground()")


ground.terminal = True


def simulate(D):
    """Returns (landing speed [m/s], descent time [s]) for chute diameter D."""
    sol = solve_ivp(rhs, [0, 2000], [h_deploy, v_deploy], args=(D,),
                    events=ground, max_step=0.5, rtol=1e-8)
    return sol.y[1, -1], sol.t[-1]


# ----------------------------------------------------------------- main
if __name__ == "__main__":
    try:
        diameters = np.linspace(0.4, 3.0, 131)
        v_land, drift = [], []
        for D in diameters:
            v, t = simulate(D)
            v_land.append(v)
            drift.append(wind * t)
        v_land, drift = np.array(v_land), np.array(drift)

        # TODO: find the smallest diameter with v_land < v_target and print it,
        #       along with its drift distance

        fig, ax1 = plt.subplots(figsize=(8, 4))
        ax1.plot(diameters, v_land, label="landing speed")
        ax1.axhline(v_target, ls="--", color="gray")
        ax1.set(xlabel="Parachute diameter [m]", ylabel="Landing speed [m/s]")
        ax2 = ax1.twinx()
        ax2.plot(diameters, drift, "r", label="drift")
        ax2.set_ylabel("Drift distance [m]")
        ax1.grid(True)
        fig.legend(loc="upper right")
        plt.show()
    except NotImplementedError as e:
        print(f"Not finished yet -- fill in the TODO in {e}")

# SANITY CHECK (by hand):
#   Set drag = weight and solve for the terminal velocity of your chosen chute.
#   Then estimate descent time ~ 300 m / v_terminal and the drift. Match?
