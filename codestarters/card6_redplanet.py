"""
AE 107 Shark Tank: Aero Edition
CARD 6 -- RedPlanet Hoppers                       starter template

Customer question:
    "How big do the rotors need to be for a 2 kg helicopter to hover on Mars,
     and how much power does it take?"

Model idea:
    * Momentum theory: ideal hover power P_ideal = T^1.5 / sqrt(2 rho A)
    * Real rotors waste power: P_real = P_ideal / FM   (FM = figure of merit)
    * In hover, thrust = weight = m * g_planet.
    * Treat the rotor as one disk of diameter D (ignore the coaxial layout).

Your job: fill in every TODO, compare Earth and Mars, and size the rotor.
"""
import numpy as np
import matplotlib.pyplot as plt

# ----------------------------------------------------------------- givens
m = 2.0                  # kg
FM = 0.5                 # figure of merit (small rotors in thin air are inefficient)
P_budget = 350.0         # W, max power the battery can supply in hover

planets = {
    #          g [m/s^2]  rho [kg/m^3]
    "Earth": (9.81,      1.225),
    "Mars":  (3.71,      0.017),
}


def hover_power(D, g, rho):
    """Real hover power [W] for rotor diameter D [m] on a planet with g, rho."""
    # TODO
    raise NotImplementedError("hover_power()")


def min_diameter(g, rho, P_max):
    """Smallest rotor diameter [m] that hovers with P_real <= P_max.

    Try to solve this ANALYTICALLY (rearrange the power equation for A),
    then check it against the plot.
    """
    # TODO
    raise NotImplementedError("min_diameter()")


# ----------------------------------------------------------------- main
if __name__ == "__main__":
    try:
        D = np.linspace(0.3, 2.0, 341)
        plt.figure(figsize=(8, 4))
        for name, (g, rho) in planets.items():
            plt.plot(D, hover_power(D, g, rho), label=name)
        plt.axhline(P_budget, color="r", ls="--", label="power budget")
        plt.xlabel("Rotor diameter [m]")
        plt.ylabel("Hover power [W]")
        plt.ylim(0, 1500)
        plt.legend(); plt.grid(True)

        g_m, rho_m = planets["Mars"]
        print(f"Smallest Mars rotor for {P_budget:.0f} W: "
              f"{min_diameter(g_m, rho_m, P_budget):.2f} m")
        # TODO: how much power does Ingenuity's 1.2 m rotor need in your model?
        plt.show()
    except NotImplementedError as e:
        print(f"Not finished yet -- fill in the TODO in {e}")

# SANITY CHECK (by hand):
#   Mars has ~38 % of Earth's gravity but ~1.4 % of its air density.
#   Using P ~ T^1.5 / sqrt(rho), by what factor should hover power change
#   from Earth to Mars for the SAME rotor? Does your plot agree?
