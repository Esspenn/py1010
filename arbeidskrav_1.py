"""
Program som beregner de årlige kostnadene for elbil og bensinbil, samt årlig 
kostnadsdifferanse mellom disse
@author: Espen Arnesen
2024 10 29
"""

#%% Felles variabler for elbil og bensinbil
trafikkforsikring_avgift = float(8.38*365)  # årlig avgift (kr)
kjoerelengde = float(10000)  # kjørelengde (km)

#%% Variabler for elbil
forsikring_elbil = float(5000)  # årlig forsikring (kr)
drivstoffbruk_elbil = float(0.2)  # strømforbruk (kWh/km)
strompris = float(2)  # strømpris (kr/kWh)
bomavgift_elbil = float(0.1)  # bomavgift (kr/km)

#%% Beregner totalt strømforbuk og kostnad for elbil
total_stroemforbruk = kjoerelengde * drivstoffbruk_elbil  # (kWh)
total_kostnad_elbil = (
    (total_stroemforbruk * strompris)
    + (bomavgift_elbil * kjoerelengde)
    + forsikring_elbil
    + trafikkforsikring_avgift
)

#%% Variabler for bensinbil
forsikring_bensinbil = float(7500)  # årlig forsikring (kr)
drivstoffbruk_bensinbil = float(1)  # drivstoffbruk (kr/km)
bomavgift_bensinbil = float(0.3)  # bomavgift (kr/km)

#%% Beregner totale kostnader for bensinbil
total_kostnad_bensinbil = (
    (kjoerelengde*drivstoffbruk_bensinbil)
    + (bomavgift_bensinbil*kjoerelengde)
    + forsikring_bensinbil + trafikkforsikring_avgift
)

#%% Beregner kostnadsdifferanse mellom elbil og bensinbil
 #  Bruker abs() for å få positiv differanse uavhengig av hvilken bil som er dyrest
kostnadsdifferanse = abs(total_kostnad_elbil - total_kostnad_bensinbil)  # (kr/år)

#%% Utskrifter for totale kostnader og kostnadsdifferanse
print(f"De totale kostnadene for elbil er {total_kostnad_elbil:.0f} kr, "
    f"og de totale kostnadene for bensinbil er {total_kostnad_bensinbil:.0f} kr."
)
print(f"Kostnadsdifferansen er {kostnadsdifferanse:.0f} kr"
)
