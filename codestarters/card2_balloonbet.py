"""
AE 107 Shark Tank: Aero Edition
CARD 2 -- BalloonBet                              starter template

Customer question:
    "How high will our weather balloon get before it bursts, and how long
     will the ascent take?"

Model idea:
    * The helium is at the same temperature and pressure as the air around
      it, so its volume grows as the air pressure drops: V = m_He R_He T / p
    * The balloon bursts when its diameter reaches D_burst.
    * Forces on the system: buoyancy (up), weight (down), drag (opposes v).

Your job: fill in every TODO, integrate the ascent with solve_ivp, and plot.
"""
import numpy as np
import matplotlib.pyplot as plt
from scipy.integrate import solve_ivp

# ----------------------------------------------------------------- givens
g = 9.81
R_air = 287.05           # J/(kg K)
R_he = 2077.1            # J/(kg K)
m_balloon = 1.2          # kg, latex envelope (a "1200 g" balloon)
m_payload = 1.0          # kg
m_he = 0.60              # kg of helium
D_burst = 8.6            # m, burst diameter from the manufacturer
Cd = 0.30                # drag coefficient of a sphere-ish balloon


def isa(h):
    """1976 Standard Atmosphere, valid 0-47 km.  (Provided -- no TODO.)
    Returns temperature [K], pressure [Pa], density [kg/m^3]."""
    h = np.clip(h, 0.0, 47000.0)
    if h <= 11000:
        T = 288.15 - 0.0065 * h
        p = 101325 * (T / 288.15) ** (g / (0.0065 * R_air))
    elif h <= 20000:
        T = 216.65
        p = 22632.1 * np.exp(-g * (h - 11000) / (R_air * T))
    elif h <= 32000:
        T = 216.65 + 0.001 * (h - 20000)
        p = 5474.89 * (T / 216.65) ** (-g / (0.001 * R_air))
    else:
        T = 228.65 + 0.0028 * (h - 32000)
        p = 868.019 * (T / 228.65) ** (-g / (0.0028 * R_air))
    return T, p, p / (R_air * T)


def balloon_volume(h):
    """Helium volume [m^3] at altitude h [m] (ideal gas law)."""
    # TODO
    raise NotImplementedError("balloon_volume()")


def balloon_diameter(h):
    """Diameter [m] of a sphere with the volume above."""
    # TODO
    raise NotImplementedError("balloon_diameter()")


def rhs(t, y):
    """State y = [altitude h (m), vertical speed v (m/s)].  Return [dh/dt, dv/dt].

    Net force = buoyancy - total weight - drag, with
        buoyancy = rho_air * V * g
        drag     = 0.5 * rho_air * v * |v| * Cd * A     (A = frontal area)
    """
    # TODO
    raise NotImplementedError("rhs()")


def burst_event(t, y):
    """Should cross zero when the balloon reaches D_burst."""
    # TODO
    raise NotImplementedError("burst_event()")


burst_event.terminal = True     # stop the integration at burst


# ----------------------------------------------------------------- main
if __name__ == "__main__":
    try:
        sol = solve_ivp(rhs, [0, 6 * 3600], [0.0, 0.0], events=burst_event,
                        max_step=5.0, rtol=1e-8)
        t, h = sol.t, sol.y[0]
        D = np.array([balloon_diameter(x) for x in h])
        print(f"Burst at {h[-1] / 1000:.1f} km after {t[-1] / 60:.0f} minutes")

        fig, ax1 = plt.subplots(figsize=(8, 4))
        ax1.plot(t / 60, h / 1000, label="altitude")
        ax1.set(xlabel="Time [min]", ylabel="Altitude [km]")
        ax2 = ax1.twinx()
        ax2.plot(t / 60, D, "r--", label="diameter")
        ax2.set_ylabel("Balloon diameter [m]")
        ax1.grid(True)
        fig.legend(loc="upper left")
        plt.show()
    except NotImplementedError as e:
        print(f"Not finished yet -- fill in the TODO in {e}")

# SANITY CHECK (by hand):
#   Volume at sea level vs volume at burst. Using p ~ 1/V (ignore T),
#   what pressure does the balloon burst at? Look that pressure up in an
#   atmosphere table -- what altitude is it? Does your simulation agree?
