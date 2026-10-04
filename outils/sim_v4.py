# Simulation v4 : architecture révisée (session metamaieutique, M7). Voir la note 19.
# Garde sim_v3.py pour comparaison. Tous les paramètres sont [C] ; les montants non sourcés sont [À vérifier].
# 2026-10-04 [opus-5.5] : la règle d'emploi par défaut devient « les droits d'abord » (décision 75) ; l'ancienne
# règle D8 (décision 54) reste calculable avec alloc='D8'. Ajout de la variante d'ouverture sur trois ans (D13.6)
# et du détail du scénario bas.
# 2026-10-04 (M9) [opus-5.5] : par défaut, l'ouverture sur trois ans (décision 78), m ramené à 2 au plus une fois
# la cible atteinte (décision 79) et l'indexation des montants (décision 80) : le socle, le besoin, la formation
# et la valeur du point de cotisation suivent le revenu médian (+ 2 % par an en nominal [Unverified]). Le socle est
# exprimé en euros de 2026 (pouvoir d'achat constant au regard du seuil de pauvreté) ; les recettes, en euros courants.
import sys

# ---------------------------------------------------------------- calendrier
START = 2028          # vote en 2027, statu quo de 3 mois (décision 62), entrée en vigueur au 1er janvier 2028
OPEN1 = 2031          # phase 1 au plus tôt après trois ans de phase 0 (D13.6, décision 73)
END = 2040
YEARS = list(range(START, END + 1))

# ---------------------------------------------------------------- marché (repris de sim_v3, base 2026)
SCEN = {
    'Bas':     (0.46, [1.5, 1.45, 1.4, 1.35, 1.3, 1.25, 1.2, 1.15, 1.1]),
    'Central': (1.32, [2.0, 1.8, 1.6, 1.45, 1.3, 1.2, 1.15, 1.1, 1.05]),
    'Haut':    (3.02, [2.5, 2.1, 1.7, 1.45, 1.3, 1.2, 1.1, 1.05, 1.05]),
}
G_LATE = 1.04         # croissance 2036-2040 [C]

def market(name):
    V0, g = SCEN[name]
    V = {2026: V0}
    for i, y in enumerate(range(2027, END + 1)):
        V[y] = V[y - 1] * (g[i] if i < len(g) else G_LATE)
    return V

# ---------------------------------------------------------------- assiette (paramètres de la section F de la note 18)
P = dict(
    EPS=0.5,          # élasticité de la demande au prix (inconnue : sensibilité 0,3 et 1,0)
    F_CHAMP=0.95,     # champ D13.1 : l'IA non générative est exclue [C]
    F_INTERNE=1.10,   # inférence sur serveurs propres, absente de v2/v3 [C, À vérifier]
    CIVISME=0.90,     # écart de recouvrement (fraude, erreurs, litiges) [C]
    ABATT=0.5,        # Md€ de dépense HT sous l'abattement (environ 500 000 groupes x 1 000 €) [C, À vérifier]
    TERM0=0.05, TERM_STEP=0.02, TERM_MAX=0.20,   # part du volume exécutée sur terminal [C]
    TERM_RED_END=2030,  # 0,25 x le tarif pendant trois ans (décision 60) ; plein tarif ensuite (maturité)
    LAG=1.0,          # effet du décalage de P_k (trimestre précédent, prix en baisse) : neutralisé par prudence
    # Les coefficients par flux (lues 0,25 ; cache 0,025) et les trois classes sont neutres au premier ordre :
    # P_k est un prix moyen par octet-équivalent pondéré, donc taxe = m x dépense en moyenne de classe (D2).
)

def revenue(V, y, m, p):
    base = V * p['F_CHAMP'] * p['F_INTERNE']
    ts = min(p['TERM_MAX'], p['TERM0'] + p['TERM_STEP'] * (y - START))
    red = 0.25 if y <= p['TERM_RED_END'] else 1.0
    cloud = base * (1 - ts) * (1 + m) ** (-p['EPS'])
    term = base * ts * (1 + red * m) ** (-p['EPS'])
    taxable_cloud = max(0.0, cloud - p['ABATT'])
    R = p['CIVISME'] * p['LAG'] * (m * taxable_cloud + red * m * term)
    return R, cloud + term   # recette, dépense HT après réaction de la demande

# ---------------------------------------------------------------- dépenses (D13.2 à D13.7)
S_RSA, S_CIBLE = 650.0, 1200.0   # €/mois [À vérifier : RSA 2026, seuil de pauvreté à 60 %]
C = dict(
    N_RSA=7.0,        # besoin net à l'ouverture au niveau du RSA : jeunes 18-24 (3,9), individualisation des couples (1,2),
                      # séjour voie b (0,5), frontaliers (0,3), sortie progressive de 12 mois (1,0) [C]
    N_CIBLE=20.0,     # besoin net au socle cible (D13.7 : 18 à 23 Md€, formation exclue) [C]
    FORM=1.0,         # coûts pédagogiques de la formation rémunérée (abondement du CPF), dès 2028 [C]
    B_MAX=44.0, PT=11.0,   # 4 points de contribution patronale, 11 Md€ le point [À vérifier]
    FUND_MONTHS=6,    # cible du fonds : six mois (décision 54), appliqués au besoin net financé par la taxe [C]
    FUND_GROSS=False, # variante : six mois des prestations brutes du socle (environ 29 Md€ au socle cible)
    ETU=False, PATR=False, INACT=False,
    OPEN_RULE='trois_ans',  # décision 78 : ouverture si la recette plus un tiers du fonds couvre le niveau du RSA
                            # (équilibre sur trois ans, D13.6) ; 'annuel' : la recette de l'année seule
    IDX=0.02,         # décision 80 : indexation nominale annuelle des montants depuis 2026 (revenu médian) [Unverified]
    M_POST=2.0,       # décision 79 : une fois la cible atteinte, m est ramené à 2 au plus (None : pas de règle)
)

def need(s, c):
    """Besoin net annuel de la branche financé par la taxe (Md€), pour un socle s (€/mois)."""
    x = (s - S_RSA) / (S_CIBLE - S_RSA)
    n = c['N_RSA'] + x * (c['N_CIBLE'] - c['N_RSA'])
    if c['ETU']:   n += 2.9 * s * 12 / 1000 - 2.3    # 2,9 M d'étudiants, bourses (2,3 Md€) reprises [À vérifier]
    if c['PATR']:  n -= 0.02 * 4.0 * 0.5 * s * 12 / 1000   # 2 % des bénéficiaires, socle réduit de moitié [C]
    if c['INACT']: n += 0.5 * s * 12 / 1000            # 0,5 M d'inactifs supplémentaires qui s'inscrivent [C]
    return n

def gross(s):
    return 4.0 * s * 12 / 1000   # prestations brutes du socle, 4 M de bénéficiaires (note 05) [À vérifier]

def s_for(target_need, c):
    lo, hi = S_RSA, S_CIBLE
    if need(hi, c) <= target_need: return hi
    if need(lo, c) >= target_need: return lo
    for _ in range(60):
        mid = (lo + hi) / 2
        if need(mid, c) < target_need: lo = mid
        else: hi = mid
    return lo

# ---------------------------------------------------------------- simulation
def run(name, mcap=1.0, alloc='droits', p=None, c=None):
    """alloc='droits' : décision 75 (les droits d'abord jusqu'au socle cible, puis le surplus va au partage ;
    les droits étant alors au plafond, il va à la baisse des cotisations). alloc='D8' : l'ordre de la décision 54."""
    p = dict(P, **(p or {})); c = dict(C, **(c or {}))
    V = market(name)
    m = 1.0; s = None; B = 0.0; fund = 0.0; rows = []
    for y in YEARS:
        R, spend = revenue(V[y], y, m, p)
        I = (1 + c['IDX']) ** (y - 2026)    # indice des montants (euros courants / euros 2026)
        nd = lambda x: need(x, c) * I       # besoin en euros courants
        BMAX = c['B_MAX'] * I
        form = min(R, c['FORM'] * I); avail = R - form
        note = ''
        reserve = fund / 3 if c['OPEN_RULE'] == 'trois_ans' else 0.0
        if s is None and y >= OPEN1 and avail + reserve >= nd(S_RSA):
            s = S_RSA; note = 'ouverture'
        if s is None:
            fund += avail          # phase 0 : RSA et ASS repris à l'identique (neutre), tout va au fonds
        else:
            commit = nd(s) + B
            surplus = avail - commit
            tgt = (c['FUND_MONTHS'] / 12) * (gross(s) * I if c['FUND_GROSS'] else nd(s) + c['FORM'] * I)
            if surplus < 0:
                draw = min(fund, -surplus); fund -= draw; gap = -surplus - draw
                if gap > 0:        # les droits priment : on suspend d'abord la baisse des cotisations
                    cut = min(B, gap); B -= cut; gap -= cut
                if gap > 0:
                    note = 'déficit %.1f (contribution d\'équilibre)' % gap
            else:
                top = min(surplus, max(0.0, tgt - fund)); fund += top; surplus -= top
                if surplus > 0:
                    if alloc == 'D8':
                        half = surplus / 2
                        newA = min(nd(S_CIBLE), nd(s) + half); usedA = newA - nd(s)
                        usedB = min(max(0.0, BMAX - B), surplus - usedA)
                        rest = surplus - usedA - usedB
                        if rest > 0:   # ce que B ne peut absorber revient aux droits
                            newA2 = min(nd(S_CIBLE), newA + rest); rest -= newA2 - newA; newA = newA2
                    else:              # décision 75 : droits d'abord, puis cotisations
                        newA = min(nd(S_CIBLE), nd(s) + surplus); rest = surplus - (newA - nd(s))
                        usedB = min(max(0.0, BMAX - B), rest); rest -= usedB
                    s = s_for(newA / I, c); B += usedB; fund += max(0.0, rest)
        rows.append(dict(y=y, V=V[y], m=m, R=R, spend=spend, s=s, need=(nd(s) if s else 0.0),
                         B=B, pts=B / (c['PT'] * I), fund=fund, note=note, I=I))
        # vote de m pour l'année suivante (LFSS), lissé à ± 0,5 par an [C]
        complete = s is not None and s >= S_CIBLE - 0.5
        if y >= OPEN1 - 1:   # m reste à 1 pendant la phase 0 ; la LFSS pour l'année d'ouverture peut le relever
            if not complete and m < mcap: m = min(mcap, m + 0.5)
            elif complete and c['M_POST'] is not None and m > c['M_POST']:
                # décision 79 : ramener m vers 2 si la recette attendue couvre encore les droits (hors baisse des cotisations)
                R2, _ = revenue(V[y + 1] if y < END else V[y], y + 1, max(c['M_POST'], m - 0.5), p)
                I2 = I * (1 + c['IDX'])
                if R2 - c['FORM'] * I2 >= need(s, c) * I2: m = max(c['M_POST'], m - 0.5)
            elif complete and B >= BMAX - 0.01 and m > 1:
                # baisse de m seulement si la recette attendue à m - 0,5 couvre encore les engagements
                R2, _ = revenue(V[y + 1] if y < END else V[y], y + 1, m - 0.5, p)
                if R2 - c['FORM'] * I * (1 + c['IDX']) >= need(s, c) * I * (1 + c['IDX']) + B: m = max(1.0, m - 0.5)
    return rows

def summary(rows):
    full = next((r['y'] for r in rows if r['s'] and r['s'] >= S_CIBLE - 0.5), None)
    opened = next((r['y'] for r in rows if r['s']), None)
    at = {r['y']: r for r in rows}
    return opened, full, at

def fmt_s(s): return '—' if s is None else '%4.0f' % s

def table(rows):
    print('année | marché HT | m | recette | socle €/mois | besoin net | baisse cotis. (pts) | fonds | note')
    for r in rows:
        print('%d | %5.1f | %3.1f | %5.1f | %s | %5.1f | %5.1f (%.2f) | %5.1f | %s' % (
            r['y'], r['V'], r['m'], r['R'], fmt_s(r['s']), r['need'], r['B'], r['pts'], r['fund'], r['note']))

def grid(alloc='D8', c=None, p=None, label=''):
    print('\n#### Synthèse %s (allocation %s)' % (label, alloc))
    print('scénario | plafond de m | ouverture | socle cible atteint | socle 2035 | socle 2040 | pts 2035 | pts 2040 | m max')
    for k in SCEN:
        for cap in (1.0, 2.0, 4.0):
            rows = run(k, cap, alloc, p, c); o, f, at = summary(rows)
            print('%s | %.0f | %s | %s | %s | %s | %.2f | %.2f | %.1f' % (
                k, cap, o or 'jamais', f or 'non (2040)', fmt_s(at[2035]['s']), fmt_s(at[2040]['s']),
                at[2035]['pts'], at[2040]['pts'], max(r['m'] for r in rows)))

SANS_IDX = {'IDX': 0.0}
AVANT_M9 = {'IDX': 0.0, 'OPEN_RULE': 'annuel', 'M_POST': None}   # les hypothèses de M7, pour comparaison

def grid2(c=None, alloc='droits', label='', caps=(1.0, 2.0, 3.0, 4.0)):
    print('\n#### Synthèse %s (allocation %s)' % (label, alloc))
    print('scénario | plafond de m | ouverture | socle cible atteint | socle 2035 (€ 2026) | socle 2040 | pts 2035 | pts 2040 | m max | m 2040 | fonds 2040 | déficit max')
    for k in SCEN:
        for cap in caps:
            rows = run(k, cap, alloc, None, c); o, f, at = summary(rows)
            dmax = max([float(r['note'].split()[1]) for r in rows if r['note'].startswith('déficit')] or [0.0])
            print('%s | %.0f | %s | %s | %s | %s | %.2f | %.2f | %.1f | %.1f | %.1f | %.1f' % (
                k, cap, o or 'jamais', f or 'non', fmt_s(at[2035]['s']), fmt_s(at[2040]['s']),
                max(0.0, at[2035]['pts']), max(0.0, at[2040]['pts']), max(r['m'] for r in rows), at[2040]['m'], at[2040]['fund'], dmax))

if __name__ == '__main__':
    print('# Règles retenues : droits d\'abord (75), ouverture sur trois ans (78), m <= 2 après la cible (79), indexation (80)')
    for cap in (2.0, 3.0, 4.0):
        print('\n## Central, m plafonné à %.0f (règles retenues ; socle en euros 2026)' % cap); table(run('Central', cap))
    print('\n## Bas, m plafonné à 4 (règles retenues)'); table(run('Bas', 4.0))
    grid2(label='règles retenues')
    grid2(SANS_IDX, label='sans indexation')
    grid2(AVANT_M9, label='hypothèses de M7 (sans indexation, ouverture annuelle, sans règle 79)')
    grid2(AVANT_M9, 'D8', label='ancienne règle D8 (décision 54), hypothèses de M7')
    print('\n## Variantes et sensibilités (Central, règles retenues)')
    print('variante | plafond | socle cible atteint | socle 2035 | socle 2040 | pts 2040')
    VAR = [('base', {}, {}), ('étudiants inclus', {'ETU': True}, {}), ('réduction patrimoine', {'PATR': True}, {}),
           ('inscription de 0,5 M inactifs', {'INACT': True}, {}), ('fonds = 6 mois bruts', {'FUND_GROSS': True}, {}),
           ('indexation 1 %', {'IDX': 0.01}, {}), ('indexation 3 %', {'IDX': 0.03}, {}),
           ('élasticité 0,3', {}, {'EPS': 0.3}), ('élasticité 1,0', {}, {'EPS': 1.0}),
           ('décalage de P_k (x1,09)', {}, {'LAG': 1.09}), ('sans serveurs propres ni recouvrement', {}, {'F_INTERNE': 1.0, 'CIVISME': 1.0})]
    for lab, cc, pp in VAR:
        for cap in (2.0, 3.0, 4.0):
            rows = run('Central', cap, 'droits', pp, cc); o, f, at = summary(rows)
            print('%s | %.0f | %s | %s | %s | %.2f' % (lab, cap, f or 'non', fmt_s(at[2035]['s']), fmt_s(at[2040]['s']), max(0.0, at[2040]['pts'])))
    print('\n## Étudiants inclus, Haut, m <= 4 (règles retenues)'); table(run('Haut', 4.0, 'droits', None, {'ETU': True}))
