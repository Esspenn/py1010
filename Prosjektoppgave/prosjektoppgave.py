"""
Prosjektoppgave: Support Dashboard
Programmet analyserer supportdata fra en Excel-fil.
@author: Espen Arnesen
2025 04 06
"""

import pandas as pd
import numpy as np
import matplotlib.pyplot as plt


# Del a) Innlesing av data fra Excel-fil
fil = pd.read_excel("support_uke_24.xlsx")

# Henter ut kolonner som arrays for videre analyse
u_dag = np.array(fil["Ukedag"])
kl_slett = np.array(fil["Klokkeslett"])
varighet = np.array(fil["Varighet"])
score = np.array(fil["Tilfredshet"])


# Del b) Analyse av antall hendelser per ukedag
# Teller opp antall henvendelser for hver ukedag (teller forekomster av "Mandag", "Tirsdag" osv.)
antall_mandag = 0
antall_tirsdag = 0
antall_onsdag = 0
antall_torsdag = 0
antall_fredag = 0

for dag in u_dag:
    if dag == "Mandag":
        antall_mandag += 1
    elif dag == "Tirsdag":
        antall_tirsdag += 1
    elif dag == "Onsdag":
        antall_onsdag += 1
    elif dag == "Torsdag":
        antall_torsdag += 1
    elif dag == "Fredag":
        antall_fredag += 1

# Lager søylediagram som viser fordelingen
ukedager_liste = ["Mandag", "Tirsdag", "Onsdag", "Torsdag", "Fredag"]
antall_per_dag = [antall_mandag, antall_tirsdag, antall_onsdag, antall_torsdag, antall_fredag]

plt.figure(figsize=(10, 6))  # Setter størrelse på plottet
plt.bar(ukedager_liste, antall_per_dag)
plt.ylabel("Antall hendelser")
plt.title("Antall hendelser per dag")
plt.grid(axis='y', linestyle='--', alpha=0.7)  # Legger til rutenett på y-aksen
plt.tight_layout()  # Justerer layout automatisk
plt.show()


# Del c) Korteste og lengste samtale
def tid_til_minutter(tid):
    """
    Regner om tid fra timer:minutter:sekunder til antall minutter.
    """
    tid_delt = tid.split(':')
    timer = int(tid_delt[0])
    minutter = int(tid_delt[1])
    sekunder = int(tid_delt[2])
    total_minutter = timer*60 + minutter + sekunder/60
    return total_minutter

# Lager liste med alle varigheter konvertert til minutter
varighet_minutter = []
for tid in varighet:
    minutter = tid_til_minutter(tid)
    varighet_minutter.append(minutter)  # Legger til i listen varighet_minutter

# Finner korteste og lengste samtale
min_varighet = min(varighet_minutter)
maks_varighet = max(varighet_minutter)

print(f"Den korteste varigheten er {min_varighet:.1f} minutt(er)")
print(f"Den lengste varigheten er {maks_varighet:.1f} minutt(er)")


# Del d) Beregning av gjennomsnittlig samtaletid
# Bruker listen varighet_minutter fra del c) som allerede er konvertert til minutter
snitt_varighet = sum(varighet_minutter) / len(varighet_minutter)
print(f"Gjennomsnittlig varighet er {snitt_varighet:.1f} minutt(er)")


# Del e) Analyse av henvendelser fordelt på tidspunkt
# Teller antall henvendelser i hver 2-timers periode
antall_8_10 = 0
antall_10_12 = 0
antall_12_14 = 0
antall_14_16 = 0

for tid in kl_slett:
    # Henter ut timetallet fra tidspunktet (første del før ':')
    time = int(str(tid).split(':')[0])  # f.eks. fra "09:45:00" får vi bare "09" (blir til 9 med int())
    if time >= 8 and time < 10:
        antall_8_10 += 1
    elif time >= 10 and time < 12:
        antall_10_12 += 1
    elif time >= 12 and time < 14:
        antall_12_14 += 1
    elif time >= 14 and time < 16:
        antall_14_16 += 1

# Lager sektordiagram som viser fordelingen
tidsbolker = ["08-10", "10-12", "12-14", "14-16"]
antall_per_bolk = [antall_8_10, antall_10_12, antall_12_14, antall_14_16]

plt.pie(antall_per_bolk, labels=tidsbolker, autopct='%1.1f%%')
plt.title("Fordeling av henvendelser per tidsbolk")
plt.show()


# Del f) NPS-analyse
# Kategoriserer kunder basert på tilfredshetsscore:
# Positive: score 9-10
# Nøytrale: score 7-8
# Negative: score 1-6
antall_positive = 0
antall_noytrale = 0
antall_negative = 0
antall_svar = 0

for tilfredshet in score:
    if not np.isnan(tilfredshet):  # Hopper over manglende svar (NaN)
        antall_svar += 1
        if tilfredshet >= 9:
            antall_positive += 1
        elif tilfredshet >= 7:
            antall_noytrale += 1
        else:
            antall_negative += 1

# Regner ut prosentandel i hver kategori (basert kun på de som har svart)
prosent_positive = (antall_positive / antall_svar) * 100
prosent_noytrale = (antall_noytrale / antall_svar) * 100
prosent_negative = (antall_negative / antall_svar) * 100

# Beregner NPS
nps = prosent_positive - prosent_negative

print("\nNPS Analyse:")
print(f"Positive kunder (score 9-10): {prosent_positive:.1f}%")
print(f"Nøytrale kunder (score 7-8): {prosent_noytrale:.1f}%")
print(f"Negative kunder (score 1-6): {prosent_negative:.1f}%")
print(f"NPS Score: {nps:.1f}")
