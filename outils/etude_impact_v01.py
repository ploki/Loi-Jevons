# Chiffres de l'étude d'impact v0.1 (M11, 2026-10-04) [opus-5.5].
# Toutes les trajectoires viennent de sim_v4.py (règles retenues : décisions 75, 78 à 81, 85, 86, 88, 89).
# Les paramètres propres à ce script (sortie progressive, conformité, frontaliers, secteur public) sont des
# hypothèses de l'agent, [Unverified] : ce sont des ordres de grandeur à faire confirmer par l'économiste.
# Usage : python3 outils/etude_impact_v01.py
import sim_v4 as s

REF = 3.0      # trajectoire de référence du Gouvernement : m <= 3 pendant la montée en charge, puis 2 (décision 84)
ALT = 2.0      # le Parlement s'en tient au repère des deux tiers

def f1(x): return '%.1f' % x
def f2(x): return '%.2f' % x
def soc(x): return '—' if x is None else '%.0f' % x

def fund_target(r):
    return 0.5 * (r['need'] + s.C['FORM'] * r['I']) if r['s'] else None

def section(t): print('\n## ' + t)

# ------------------------------------------------------------------ 1. trajectoire de référence
section('1. Trajectoire de référence (Central, m <= 3 puis 2) — Md€ courants ; socle en € de 2026 et € courants')
print('année | m | recette | socle € 2026 | socle € courants | besoin net | baisse cotis. Md€ (pts) | fonds | cible du fonds | note')
ref = s.run('Central', REF)
for r in ref:
    tg = fund_target(r)
    print('%d | %.1f | %s | %s | %s | %s | %s (%s) | %s | %s | %s' % (
        r['y'], r['m'], f1(r['R']), soc(r['s']), soc(r['s'] * r['I'] if r['s'] else None), f1(r['need']),
        f1(r['B']), f2(max(0, r['pts'])), f1(r['fund']), '—' if tg is None else f1(tg), r['note']))

section('1 bis. Comparaison des plafonds (Central) : année de la cible, m maximal, années à m > 2, pts 2040, fonds 2040')
for cap in (1.0, 2.0, 3.0, 4.0):
    rows = s.run('Central', cap); o, f, at = s.summary(rows)
    print('m <= %.0f | ouverture %s | cible %s | m max %.1f | années à m > 2 : %d | pts 2035 %s | pts 2040 %s | fonds 2040 %s | socle 2040 %s' % (
        cap, o, f or 'non', max(r['m'] for r in rows), sum(1 for r in rows if r['m'] > 2.0),
        f2(max(0, at[2035]['pts'])), f2(max(0, at[2040]['pts'])), f1(at[2040]['fund']), soc(at[2040]['s'])))
rows = s.run('Central', REF, c={'M79_FONDS': True}); o, f, at = s.summary(rows)
print('variante M79_FONDS (m <= 3) | cible %s | m : %s | fonds 2040 %s | pts 2040 %s' % (
    f, ' '.join('%.1f' % r['m'] for r in rows), f1(at[2040]['fund']), f2(at[2040]['pts'])))
m10 = s.run('Central', REF, c={'B_SOUTENABLE': False})
print('règles de M10 (sans la décision 89), m <= 3 | pts : %s | fonds : %s' % (
    ' '.join(f2(r['pts']) for r in m10), ' '.join(f1(r['fund']) for r in m10)))
print('règles retenues (décision 89), m <= 3     | pts : %s | fonds : %s' % (
    ' '.join(f2(max(0, r['pts'])) for r in ref), ' '.join(f1(r['fund']) for r in ref)))

# ------------------------------------------------------------------ 2. scénario bas
section('2. Scénario bas : ouverture, déficit (contribution d\'équilibre), écart à la cible en 2040')
for cap in (2.0, 3.0, 4.0):
    rows = s.run('Bas', cap); o, f, at = s.summary(rows)
    defs = [(r['y'], float(r['note'].split()[1])) for r in rows if r['note'].startswith('déficit')]
    r40 = at[2040]
    gap = s.need(s.S_CIBLE, s.C) * r40['I'] - (r40['R'] - s.C['FORM'] * r40['I'])
    print('m <= %.0f | ouverture %s | socle 2040 %s | recette 2035 %s | recette 2040 %s | fonds 2040 %s | déficits %s | écart à la cible 2040 : %s Md€ courants' % (
        cap, o or 'jamais', soc(r40['s']), f1(at[2035]['R']), f1(r40['R']), f1(r40['fund']),
        ', '.join('%d : %.1f' % d for d in defs) or 'aucun', f1(gap)))

# ------------------------------------------------------------------ 3. variantes ouvertes
section('3. Variantes réservées à l\'auteur (Central) : cible, socle 2040, surcoût au socle cible (Md€ de 2026)')
base_n = s.need(s.S_CIBLE, s.C)
for lab, cc in (('base', {}), ('étudiants inclus', {'ETU': True}), ('réduction patrimoine', {'PATR': True})):
    c = dict(s.C, **cc)
    d_cible = s.need(s.S_CIBLE, c) - base_n
    d_rsa = s.need(s.S_RSA, c) - s.need(s.S_RSA, s.C)
    out = []
    for cap in (2.0, 3.0, 4.0):
        rows = s.run('Central', cap, c=cc); o, f, at = s.summary(rows)
        out.append('m <= %.0f : ouverture %s, cible %s, socle 2040 %s' % (cap, o or 'jamais', f or 'non', soc(at[2040]['s'])))
    print('%s | surcoût au RSA %+.1f ; au socle cible %+.1f | %s' % (lab, d_rsa, d_cible, ' ; '.join(out)))
rows = s.run('Haut', 4.0, c={'ETU': True}); o, f, at = s.summary(rows)
print('étudiants, scénario haut, m <= 4 : cible %s, m max %.1f' % (f, max(r['m'] for r in rows)))

# ------------------------------------------------------------------ 4. sensibilités
section('4. Sensibilité (Central) : indexation et élasticité ; m <= 2 / m <= 3')
for lab, cc, pp in (('indexation 1 %', {'IDX': 0.01}, {}), ('indexation 2 % (centrale)', {}, {}), ('indexation 3 %', {'IDX': 0.03}, {}),
                    ('élasticité 0,3', {}, {'EPS': 0.3}), ('élasticité 0,5 (centrale)', {}, {}), ('élasticité 1,0', {}, {'EPS': 1.0})):
    out = []
    for cap in (ALT, REF):
        rows = s.run('Central', cap, 'droits', pp, cc); o, f, at = s.summary(rows)
        out.append('m <= %.0f : cible %s, socle 2040 %s, pts 2040 %s, recette 2035 %s' % (
            cap, f or 'non', soc(at[2040]['s']), f2(max(0, at[2040]['pts'])), f1(at[2035]['R'])))
    print('%s | %s' % (lab, ' | '.join(out)))

section('4 bis. Effet prix sur la dépense hors taxe : facteur (1 + m)^-ε (Q74) ; prix TTC = (1 + m) × prix HT')
print('ε | m = 1 (prix × 2) | m = 2 (× 3) | m = 3 (× 4) | m = 4 (× 5)')
for eps in (0.3, 0.5, 1.0):
    print('%.1f | %s' % (eps, ' | '.join('%.0f %%' % (100 * ((1 + m) ** (-eps) - 1)) for m in (1, 2, 3, 4))))

# ------------------------------------------------------------------ 5. abattement
section('5. Abattement (décision 88) : 1 000 € de taxe par groupe, 0,5 Md€ [Unverified] ; part de la recette brute (trajectoire de référence)')
for r in ref:
    if r['y'] in (2028, 2031, 2035, 2040):
        print('%d | m %.1f | abattement / (recette + abattement) : %.0f %%' % (r['y'], r['m'], 100 * s.P['ABATT'] / (r['R'] + s.P['ABATT'])))
print('Dépense HT annuelle en deçà de laquelle un groupe ne paie rien : m = 1 : 1 000 € ; m = 2 : 500 € ; m = 3 : 333 € (1 000 / m)')

# ------------------------------------------------------------------ 6. sortie progressive (Q56)
section('6. Sortie progressive (art. 6 ; décision 91) : taux marginal effectif sur le revenu net d\'activité [Unverified]')
SMIC_NET = 1430.0          # SMIC mensuel net à temps plein, 2026 [Unverified]
PA_FORFAIT, PA_TAUX = 640.0, 0.61   # prime d'activité simplifiée, personne seule, sans bonification [Unverified]
def pa(w): return max(0.0, PA_FORFAIT + PA_TAUX * w - w) if w > 0 else 0.0
for socle in (s.S_RSA, s.S_CIBLE):
    for f in (0.3, 0.4, 0.5):
        sortie = socle / f
        rows = []
        for w in (0.5 * SMIC_NET, SMIC_NET):
            during = w + max(0.0, socle - f * w)
            after = w + pa(w)
            rows.append('salaire %.0f : revenu pendant %.0f, au 13e mois %.0f (marche %.0f)' % (w, during, after, during - after))
        print('socle %.0f € | taux %.0f %% | TME %.0f %% jusqu\'à %.0f € de salaire net | %s' % (
            socle, 100 * f, 100 * f, sortie, ' ; '.join(rows)))
print('Repère : prime d\'activité seule, TME dans la zone dégressive = %.0f %% (1 - %.2f) [Unverified]' % (100 * (1 - PA_TAUX), PA_TAUX))

# ------------------------------------------------------------------ 7. coût de conformité (Q43, Q75)
section('7. Coût de conformité annuel, en régime de croisière [Unverified : hypothèses de l\'agent]')
CONF = [  # (catégorie, nombre, coût de mise en place par entité (k€), coût annuel par entité (k€))
    ('fournisseurs enregistrés (collecte, déclaration par SIREN)', 200, 150.0, 60.0),
    ('autoliquidants (fournisseur non enregistré)', 5000, 2.0, 1.5),
    ('déclarants pour usage propre (serveurs propres)', 2000, 20.0, 8.0),
    ('revendeurs agréés (attestations, registre)', 1000, 5.0, 3.0),
    ('TPE et PME clientes d\'un fournisseur enregistré (SIREN, relevé prérempli)', 500000, 0.0, 0.02),
]
tot_set = tot_an = 0.0
for lab, n, setup, an in CONF:
    tot_set += n * setup / 1e6; tot_an += n * an / 1e6
    print('%s | %d | mise en place %.0f M€ | annuel %.0f M€' % (lab, n, n * setup / 1e3, n * an / 1e3))
print('TOTAL | mise en place %.2f Md€ | annuel %.2f Md€' % (tot_set, tot_an))
ADMIN_ETP, COUT_ETP = 600, 0.08   # agents (DGFiP, douane, caisse) et coût complet en M€ [Unverified]
print('Administration : %d ETP × %.0f k€ = %.0f M€ par an ; SDK et systèmes : 30 M€ de mise en place [Unverified]' % (ADMIN_ETP, COUT_ETP * 1e3, ADMIN_ETP * COUT_ETP))
for r in ref:
    if r['y'] in (2028, 2035):
        print('%d : coûts annuels (entreprises + administration) / recette = %.1f %%' % (r['y'], 100 * (tot_an + ADMIN_ETP * COUT_ETP / 1e3) / r['R']))

# ------------------------------------------------------------------ 8. frontaliers (D6)
section('8. Frontaliers résidant en France : bornes du surcoût du socle (Md€ de 2026) [Unverified]')
N_FRONT = 470000           # résidents en France travaillant dans un pays voisin [Unverified]
for lab, chom, sans_are, socle in (('borne basse', 0.04, 0.3, s.S_RSA), ('centrale', 0.06, 0.4, (s.S_RSA + s.S_CIBLE) / 2),
                                    ('borne haute', 0.08, 0.5, s.S_CIBLE)):
    n = N_FRONT * chom * sans_are
    print('%s | chômage %.0f %% | sans ARE %.0f %% | %d personnes | socle %.0f € | %.2f Md€' % (
        lab, 100 * chom, 100 * sans_are, n, socle, n * socle * 12 / 1e9))
print('Hypothèse du script (N_RSA) : 0,3 Md€')

# ------------------------------------------------------------------ 9. effet circulaire (D5)
section('9. Effet circulaire : part payée par les administrations publiques (10 % de la recette [Unverified])')
PUB = 0.10
for r in ref:
    if r['y'] in (2028, 2031, 2035, 2040):
        print('%d | recette %.1f | payé par les APU %.1f | apport net aux APU (hors APU) %.1f' % (r['y'], r['R'], PUB * r['R'], (1 - PUB) * r['R']))
