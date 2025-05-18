import numpy as np
import matplotlib.pyplot as plt

# Sample years from 2011 to 2031
years = np.arange(2011, 2032, 1)

# Simulated market share growth data for different regions
us_market_share = np.exp((years - 2011) / 10) - 1
us_market_share = us_market_share / max(us_market_share) * 40

europe_market_share = np.exp((years - 2011) / 9) - 1
europe_market_share = europe_market_share / max(europe_market_share) * 50

china_market_share = np.exp((years - 2011) / 8.5) - 1
china_market_share = china_market_share / max(china_market_share) * 55

global_market_share = (us_market_share + europe_market_share + china_market_share) / 3

# Plotting the data
plt.figure(figsize=(8, 5))
plt.plot(years, us_market_share, label='US - EV market share', linestyle='-', color='blue')
plt.plot(years, europe_market_share, label='Europe - EV market share', linestyle='-', color='green')
plt.plot(years, china_market_share, label='China - EV market share', linestyle='-', color='orange')
plt.plot(years, global_market_share, label='EV Global share of sales', linestyle='-', color='black')

# Labels and title
plt.xlabel("Year")
plt.ylabel("Market Share (%)")
plt.title("Outlook for EV market share by major region")
plt.legend()
plt.grid(True, linestyle='--', alpha=0.6)

# Show the plot
plt.show()