# Shark Tank: Aero Edition — AE 107 Lab Game

Nov 21, 2026 · @GeneralKC

## Student handout

Your team is an aerospace startup. In 90 minutes, build a working Python model that answers a customer's question, then pitch it to the Sharks for up to $1M in (fake) investment. The team that raises the most money wins.

### Team roles (teams of 3–4)

| Role | Job |
| --- | --- |
| CEO | Leads the pitch, keeps the team on time |
| CTO | Owns the code and drives the AI assistant |
| Chief Engineer | Checks the physics and does the hand calculation |
| CFO | Turns results into numbers, plots, and the "ask" |

Teams of 3 combine CEO and CFO. Everyone must be able to explain every line of code.

### Timeline

| Time | Phase |
| --- | --- |
| 0:00–0:10 | Form teams, draw a challenge card, open your starter template |
| 0:10–1:40 | Build phase (Market Shock card arrives at 0:55) |
| 1:40–1:50 | Finalize pitch: 3 slides max, or present straight from your plots |
| 1:50–2:30 | Pitches: 3 min pitch + 2 min Shark Q&A per team |
| 2:30 | Deals announced |

### The rules

1. **Use AI freely, but own it.** Any AI tool is allowed. During Q&A a Shark can point at any line of code and ask any team member to explain it. Can't explain it? You lose $100K.
2. **Sanity check required.** Show one hand calculation (back-of-envelope, on paper or a whiteboard) that confirms your simulation is in the right ballpark.
3. **Prompt log.** Paste the prompts you used into a text file and submit it with your code. Catch the AI making a mistake and explain it: +$100K bonus.
4. **At least one plot.** Labeled axes with units. A plot without units is not investable.
5. **Buzzword tax.** Every unexplained "AI-powered" or "revolutionary" in your pitch costs $50K.

### Your 3-minute pitch

1. **The problem** (30 s): who is the customer and what do they need?
2. **The model** (60 s): what physics did you include, and what did you assume away?
3. **The result** (60 s): your plot and the one number the customer cares about.
4. **The ask** (30 s): how much you want, for what equity, and why your model is trustworthy (hint: your sanity check).

### How the Sharks score you

| Criterion | Weight |
| --- | --- |
| Model works and makes physical sense | 30% |
| Insight: did you answer the customer's question? | 25% |
| Code understanding (line audit) | 20% |
| Pitch clarity and visuals | 15% |
| Creativity and stretch goals | 10% |

## Challenge cards

Print one card per page and have each team draw one. Each card has a matching starter template (card1\_dropzone.py … card6\_redplanet.py).

### Card 1 — DropZone Drones

**Customer:** A campus food-delivery startup.

**Problem:** "How far can our quadcopter deliver, and what payload makes us the most money per flight?"

**Your model must:** Estimate hover/cruise power from momentum theory, convert battery energy into flight time and range, and sweep payload from 0 to 3 kg.

**Key physics:** Thrust = weight; ideal induced power P = T^1.5 / sqrt(2ρA); range = speed × endurance; account for the round trip.

**Deliverable:** Plot of range vs. payload, plus expected revenue per flight vs. payload. You earn $4 per kg, but customers are spread evenly over a 15 km radius and you can only serve those within your one-way range.

**Stretch goal:** Add a headwind on the outbound leg and a tailwind on the return.

### Card 2 — BalloonBet

**Customer:** A high-school STEM program launching weather balloons.

**Problem:** "How high will our balloon get before it bursts, and how long will the ascent take?"

**Your model must:** Use a standard atmosphere model for pressure, density and temperature, grow the balloon as pressure drops, and integrate the ascent until the diameter hits the burst diameter.

**Key physics:** Ideal gas law; buoyancy = ρ\_air × V × g; drag = ½ ρ v² C\_D A; Newton's 2nd law.

**Deliverable:** Plot of altitude and balloon diameter vs. time; predicted burst altitude.

**Stretch goal:** Find how much helium gives the highest burst altitude.

### Card 3 — SoftLanding Inc.

**Customer:** A rocketry club that keeps breaking its payload bay.

**Problem:** "What parachute size gets our 2 kg payload down under 5 m/s, without drifting off the field?"

**Your model must:** Simulate descent with drag from deployment altitude to the ground, sweep parachute diameter, and compute landing speed and wind drift.

**Key physics:** m dv/dt = mg − ½ ρ v² C\_D A; terminal velocity v\_t = sqrt(2mg / ρ C\_D A); drift ≈ wind speed × descent time.

**Deliverable:** Plot of landing speed and drift distance vs. parachute diameter; your recommended size.

**Stretch goal:** Add a small drogue chute at apogee and a main chute at 150 m. Does it reduce drift?

### Card 4 — OrbitGuard

**Customer:** A CubeSat operator worried about a nearby piece of debris.

**Problem:** "Will this debris come within 5 km of our satellite in the next 24 hours, and when?"

**Your model must:** Propagate two objects in Earth orbit using two-body gravity, track the distance between them, and flag every close approach.

**Key physics:** a = −μr / |r|³; circular orbit speed v = sqrt(μ/r); numerical integration with solve\_ivp.

**Deliverable:** Plot of separation distance vs. time with the 5 km threshold marked; time and distance of the closest approach.

**Stretch goal:** Recommend a small velocity change (Δv) that keeps the satellite outside 5 km.

### Card 5 — Paper Jet Labs

**Customer:** A toy company designing a paper-glider kit.

**Problem:** "What launch angle and speed give the longest glide, and does the real plane match the model?"

**Your model must:** Simulate a 2D glider with lift and drag (point mass), sweep launch angle, and find the best one. Then fold and throw a real plane three times and compare.

**Key physics:** L = ½ ρ v² S C\_L, D = ½ ρ v² S C\_D; lift acts perpendicular to velocity, drag opposite; best glide ratio = C\_L / C\_D.

**Deliverable:** Flight path plot (x vs. y) for several launch angles, plus model vs. measured distance.

**Stretch goal:** Estimate the real plane's C\_L/C\_D from your measurements.

### Card 6 — RedPlanet Hoppers

**Customer:** A Mars mission team planning a scout helicopter.

**Problem:** "How big do the rotors need to be for a 2 kg helicopter to hover on Mars, and how much power does it take?"

**Your model must:** Compare hover power on Earth vs. Mars for a range of rotor diameters, and find the smallest rotor that hovers within a 350 W power budget.

**Key physics:** Mars: g = 3.71 m/s², ρ ≈ 0.017 kg/m³; ideal hover power P = T^1.5 / sqrt(2ρA); real power ≈ P\_ideal / figure of merit.

**Deliverable:** Plot of hover power vs. rotor diameter for Earth and Mars, with the power budget marked.

**Stretch goal:** Ingenuity's rotors are 1.2 m across. Does your model say that's enough? Explain the gap.

## Market shock cards

Hand each team its shock at the 0:55 mark. Teams must show the before/after result in their pitch.

| Card | Market shock |
| --- | --- |
| 1 — DropZone Drones | "Regulators cap drone mass at 4 kg total, payload included. What's your new best payload?" |
| 2 — BalloonBet | "Helium prices spiked. You can only afford 25% less gas. How much altitude do you lose, and how much longer is the ascent?" |
| 3 — SoftLanding Inc. | "The field shrank. Drift must stay under 150 m in a 6 m/s wind. Can you still land under 5 m/s?" |
| 4 — OrbitGuard | "Tracking says the debris orbit is 2 km higher than reported. Re-run the conjunction check." |
| 5 — Paper Jet Labs | "The toy must work indoors: max launch speed is now 4 m/s. What changes?" |
| 6 — RedPlanet Hoppers | "Your battery supplier cut the power budget to 250 W. How big must the rotor be now?" |

**Wild card (any team):** "Your lead investor wants one extra feature by pitch time. The Sharks choose it."

## Shark scoresheet

Score each criterion 1–5, then invest. Each Shark has $1,000,000 to spread across teams; uninvested money is lost.

| Team / Card | Physics (30%) | Insight (25%) | Line audit (20%) | Pitch (15%) | Creativity (10%) | Weighted score | Bonuses / penalties | Investment ($) |
| --- | --- | --- | --- | --- | --- | --- | --- | --- |
|  |  |  |  |  |  |  |  |  |
|  |  |  |  |  |  |  |  |  |
|  |  |  |  |  |  |  |  |  |
|  |  |  |  |  |  |  |  |  |
|  |  |  |  |  |  |  |  |  |
|  |  |  |  |  |  |  |  |  |

**Bonuses and penalties:** −$100K per failed line audit · −$50K per unexplained buzzword · +$100K for catching and explaining an AI mistake · +$50K for a working stretch goal.

**Final raise** = total Shark investment + bonuses − penalties. Highest raise wins; tie goes to the higher weighted score.

## Instructor notes (do not hand out)

### Setup checklist

- [ ] Print the handout (one per student) and the six challenge cards (one per page)
- [ ] Cut out the market shock cards; set a timer for 0:55
- [ ] Put the starter templates (card1\_dropzone.py … card6\_redplanet.py) on the course page or a shared drive
- [ ] Check lab machines have numpy, scipy and matplotlib
- [ ] Card 5 teams: a stack of printer paper and a tape measure
- [ ] Print one shark scoresheet per Shark, plus fake money if you want props

Every template runs as handed out and prints which TODO to fill next. Answer key: instructor\_reference.py (do not post), which reproduces every number below and saves a check plot per card.

### Answer key

Values use the givens in each template. Student answers within about 10–15% are fine; bigger gaps usually mean a units or sign error.

| Card | Baseline answer | Market shock answer | Watch for |
| --- | --- | --- | --- |
| 1 — DropZone | Empty range 18.1 km. Best payload 2.26 kg, range 10.4 km, $4.35 per flight | 4 kg cap → 2.0 kg payload, $4.32: the cap barely hurts, since the optimum was near 2 kg anyway | Forgetting the empty return leg; using one rotor's area instead of four |
| 2 — BalloonBet | Burst at 32.1 km after 72 min | 25% less helium → bursts higher (33.9 km) but takes 107 min | Surprise result: less gas means more room to expand. Too little gas and it never lifts off |
| 3 — SoftLanding | 1.06 m chute → 4.9 m/s landing, 241 m drift | 6 m/s wind → 361 m drift. Under 150 m needs a descent under 25 s, so only a small drogue (about 0.3 m) with the main opened low (about 50 m) works | Sign errors on drag when v is negative; using terminal velocity at sea level only |
| 4 — OrbitGuard | Closest approach 1.50 km at t = 15.25 h. Only one pass under 5 km | Debris 2 km higher → still a 4.3 km conjunction, now at t = 6.58 h | Default RK45 with rtol=1e-6 gives 2.03 km (DOP853 still gets 1.51 km): a great "trust your integrator?" question |
| 5 — Paper Jet | Trim speed 3.0 m/s; steady glide from 1.8 m = 10.8 m. At 8 m/s the best angle is about −8° → 14.4 m (the plane loops first) | 4 m/s launch → best about +4°, 12.6 m | Lift pointed straight up instead of perpendicular to velocity |
| 6 — RedPlanet | Smallest Mars rotor 0.71 m for 350 W. A 1.2 m rotor needs about 206 W on Mars vs 104 W on Earth | 250 W budget → 0.99 m rotor | Using Earth g on Mars; forgetting the figure of merit |

### Line-audit questions that work well

- "What units is this variable in?" (point at any variable without a comment)
- "Why is there an absolute value in the drag term?"
- "What does `terminal = True` do, and what happens if you delete it?"
- "What would happen if you halved `max_step`? Why did you pick this tolerance?"
- "Which line would you change to run this on Mars / in a headwind / at altitude?"

### Teaching points to pull out during deals

- **Every model is a bet on its assumptions.** Ask each team: "What did you leave out, and would it make your number better or worse?"
- **The hand check is the trust signal.** Teams whose sanity check matched their simulation should get more money. That's the point of the exercise.
- **AI is a tool, not an author.** Celebrate the team that caught an AI mistake. Ask the class what kind of mistakes they saw (units, wrong sign, plausible but wrong constants).
