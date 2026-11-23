"""
AE 107 Shark Tank: Aero Edition
CARD 1 -- DropZone Drones                         starter template

Customer question:
    "How far can our quadcopter deliver, and what payload makes us the
     most money per flight?"

Business model (given):
    * You earn $4 for every kg you deliver.
    * Customers are spread evenly over a disk of radius 15 km around the hub.
    * You can only serve a customer if they are within your ONE-WAY range
      (the drone flies out loaded and comes back empty).
    * So expected revenue per flight = $4 * payload * (fraction of customers
      in range), and fraction in range = (range / 15 km)^2, capped at 1.

Your job: fill in every TODO, then make the two plots.
Use AI if you like -- but every team member must be able to explain every line.
"""
import numpy as np
import matplotlib.pyplot as plt

# ----------------------------------------------------------------- givens
g = 9.81                 # m/s^2
rho = 1.225              # kg/m^3, sea-level air density
m_empty = 2.0            # kg, airframe + battery
battery_Wh = 222.0       # Wh  (6S 10 Ah pack)
usable = 0.80            # only use 80 % of the pack
D_rotor = 0.38           # m, rotor diameter (15 inch props)
n_rotors = 4
FM = 0.65                # rotor figure of merit (ideal power / real power)
eta_motor = 0.85         # motor + ESC efficiency
v_cruise = 12.0          # m/s
CdA = 0.05               # m^2, drag area of the airframe
T_max = 70.0             # N, max total thrust of all 4 motors
thrust_margin = 1.3      # need thrust >= 1.3 * weight to fly safely
price_per_kg = 4.0       # $
R_city = 15.0            # km


def electrical_power(m_total):
    """Electrical power [W] to fly at v_cruise with total mass m_total [kg].

    Model it as:
        induced power  = ideal momentum-theory hover power / (FM * eta_motor)
                         ideal hover power P = T^1.5 / sqrt(2 * rho * A)
        parasite power = 0.5 * rho * v^3 * CdA / eta_motor
    where T = weight and A = total disk area of all rotors.
    """
    # TODO: compute the total rotor disk area A
    # TODO: compute induced power and parasite power, return their sum
    raise NotImplementedError("electrical_power()")


def one_way_range_km(payload):
    """One-way delivery distance [km] for a given payload [kg].

    Hint: energy used = P_loaded * (d / v) + P_empty * (d / v) for the
    out-and-back trip. Solve for d.
    """
    # TODO
    raise NotImplementedError("one_way_range_km()")


def revenue_per_flight(payload):
    """Expected $ per flight (see the business model at the top)."""
    # TODO: remember the thrust limit -- return np.nan if the drone can't lift it
    raise NotImplementedError("revenue_per_flight()")


# ----------------------------------------------------------------- main
if __name__ == "__main__":
    try:
        payloads = np.linspace(0, 3, 301)
        ranges = np.array([one_way_range_km(p) for p in payloads])
        revenue = np.array([revenue_per_flight(p) for p in payloads])

        i_best = np.nanargmax(revenue)
        print(f"Best payload: {payloads[i_best]:.2f} kg, "
              f"range {ranges[i_best]:.1f} km, ${revenue[i_best]:.2f} per flight")

        fig, (ax1, ax2) = plt.subplots(1, 2, figsize=(11, 4))
        ax1.plot(payloads, ranges)
        ax1.set(xlabel="Payload [kg]", ylabel="One-way range [km]",
                title="Range vs payload")
        ax2.plot(payloads, revenue)
        ax2.set(xlabel="Payload [kg]", ylabel="Expected revenue [$ / flight]",
                title="Revenue vs payload")
        for ax in (ax1, ax2):
            ax.grid(True)
        fig.tight_layout()
        plt.show()
    except NotImplementedError as e:
        print(f"Not finished yet -- fill in the TODO in {e}")

# SANITY CHECK (do this by hand, not in code!):
#   What is the hover power of the EMPTY drone? Roughly how many minutes
#   can it hover on 80 % of a 222 Wh battery? Does your code agree?
