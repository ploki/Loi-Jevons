# Simulation v4 : architecture révisée (session metamaieutique, M7). Voir la note 19.
# sim_v3.py est archivé (archive/sim_v3.py). Tous les paramètres sont [C] ; les montants non sourcés sont [À vérifier].
# 2026-10-04 [opus-5.5] : la règle d'emploi par défaut devient « les droits d'abord » (décision 75) ; l'ancienne
# règle D8 (décision 54) reste calculable avec alloc='D8'. Ajout de la variante d'ouverture sur trois ans (D13.6)
# et du détail du scénario bas.
# 2026-10-04 (M9) [opus-5.5] : par défaut, l'ouverture sur trois ans (décision 78), m ramené à 2 au plus une fois
# la cible atteinte (décision 79) et l'indexation des montants (décision 80) : le socle, le besoin, la formation
# et la valeur du point de cotisation suivent le revenu médian (+ 2 % par an en nominal [Unverified]). Le socle est
# exprimé en euros de 2026 (pouvoir d'achat constant au regard du seuil de pauvreté) ; les recettes, en euros courants.
# 2026-10-04 (M10) [opus-5.5] : vérification des unités (décision 85) : le marché V est le chiffre d'affaires HT
# de l'IA vendue aux professionnels en France (note 13), en euros courants ; c'est un volume × un prix, de sorte
# que la baisse de P_k y est déjà incluse, et la recette (m × dépense) est elle aussi en euros courants. Les unités
# sont cohérentes avec l'indexation nominale ; rien n'est corrigé. Ajouts : la décision 86 (hors retournement, la
# baisse des cotisations est suspendue avant de puiser dans le fonds) et l'abattement exprimé en taxe (Q44, proposition).
# 2026-10-04 (M11) [opus-5.5] : l'abattement de 1 000 € de taxe par groupe est validé (décision 88). Règle de la
# décision 89 (B_SOUTENABLE) : une baisse des cotisations n'est ENGAGÉE que si elle est soutenable avec m <= 2,
# c'est-à-dire si la recette que donnerait m = min(m, 2), cette année et l'année suivante (montants indexés), couvre
# la formation, les droits et la baisse déjà engagée augmentée de la nouvelle. Ce qui n'est pas engagé va au fonds.
# Le « cliquet » proposé en M10 (ne baisser m que si la recette couvre aussi la baisse engagée) est refusé.
# B_SOUTENABLE=False reproduit exactement la sortie de M10 (contrôle de non-régression).
# 2026-10-04 (M12) [opus-5.5] : décisions 94 (M79_FONDS par défaut), 95 (retournement sur l'assiette) et 96 (sortie
# progressive au plus favorable, puis dégressivité linéaire : SP, legacy, sp_pay, sp_cost ; le surcoût par rapport à
# l'hypothèse d'origine est ajouté au besoin). Le réglage M11 reproduit exactement la sortie de M11.
# 2026-10-04 (M14, passe de corrections) [opus-5.5] : (1) raccord du besoin et de la sortie progressive (rapport de
# relecture, A4) : N_RSA comptait 1,0 Md€ de sortie progressive « d'origine » alors que le modèle explicite la chiffre à
# - 0,52 Md€ au niveau du RSA ; le besoin est désormais une part hors sortie progressive (N_RSA - 1,0 ; N_CIBLE -
# sp_cost(1200, 'M11'), soit l'hypothèse d'origine incluse dans les 20 Md€) plus sp_cost(s, SORTIE) ; (2) la garantie
# familiale (A5, arbitrage C7 [opus-5.5 as ggim] : elle suit la revalorisation légale du RSA, pas la hausse du socle)
# est chiffrée explicitement (GF_TYPES, gf_cost) ; (3) variante du tarif réduit sur terminal prolongé à cinq ans (C2).
# Le réglage AVANT_M14 (SP_RACCORD=False, GF=None) reproduit exactement la sortie précédente ; option --avant-m14.
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

# ---------------------------------------------------------------- assiette (paramètres de la section F de la note 18, archivée)
P = dict(
    EPS=0.5,          # élasticité de la demande au prix (inconnue : sensibilité 0,3 et 1,0)
    F_CHAMP=0.95,     # champ D13.1 : l'IA non générative est exclue [C]
    F_INTERNE=1.10,   # inférence sur serveurs propres, absente de v2/v3 [C, À vérifier]
    CIVISME=0.90,     # écart de recouvrement (fraude, erreurs, litiges) [C]
    ABATT=0.5,        # Md€ de TAXE abattue : 1 000 € de taxe par groupe et par an (proposition Q44, opus-5.5),
                      # environ 500 000 groupes utilisateurs [Unverified] ; avant M10 : 0,5 Md€ de dépense
    ABATT_EN_TAXE=True,
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
    if p['ABATT_EN_TAXE']:
        R = max(0.0, p['CIVISME'] * p['LAG'] * (m * cloud + red * m * term) - p['ABATT'])
    else:
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
    B_AVANT_FONDS=True,  # décision 86 (False : l'ordre de la décision 54, le fonds d'abord)
    M_POST=2.0,       # décision 79 : une fois la cible atteinte, m est ramené à 2 au plus (None : pas de règle)
    B_SOUTENABLE=True,  # décision 89 : la baisse des cotisations n'est engagée que si elle est soutenable avec m <= 2
    M79_FONDS=True,   # décision 94 (proposition opus-5.5 de M11, adoptée en M12) : pour ramener m vers 2 (décision 79),
                      # compter aussi un tiers de l'excédent du fonds sur sa cible (l'équilibre sur trois ans de l'article 10)
    RETOURNEMENT='assiette',  # décision 95 : retournement = baisse de l'assiette (dépense taxable, à multiple constant),
                              # et non du produit ; 'produit' : la définition de M11 (une baisse votée de m la déclenchait)
    SORTIE='degressif',  # décision 96 : sortie progressive au plus favorable (socle résiduel ou droit actuel), puis
                         # dégressivité linéaire sur les D derniers mois ; 'M11' : socle - f x salaire, sans plancher
                         # (l'hypothèse N_RSA d'origine) ; 'plus_favorable' : le plancher sans dégressivité ;
                         # 'prolonge' : 12 mois pleins au plus favorable, puis D mois dégressifs en plus
    SP_RACCORD=True,  # M14 (A4) : le besoin = part hors sortie progressive + sp_cost(s, SORTIE) ; False : la formule
                      # précédente, N(s) + sp_cost(s, SORTIE) - sp_cost(s, 'M11'), qui comptait 1,52 Md€ au niveau du RSA
    SP_ORIG_RSA=1.0,  # la sortie progressive « d'origine » comprise dans N_RSA (note 19, § 1.3)
    GF='rsa',         # M14 (A5, C7) : garantie familiale revalorisée comme le RSA ; 'socle' : revalorisée comme le socle
                      # (rédaction de l'art. 9 avant M14) ; None : non chiffrée (avant M14)
)

# ---------------------------------------------------------------- sortie progressive (décision 96) [Unverified]
SP = dict(
    ENTREES=0.6,      # millions de reprises d'emploi par an chez les bénéficiaires du socle [Unverified]
    F=0.5,            # fraction des revenus d'activité déduite du socle (plafond légal, décision 91)
    D=6,              # nombre de mois de dégressivité linéaire, fixé par décret [opus-5.5]
    SMIC=1430.0,      # SMIC net mensuel à temps plein, € de 2026 [Unverified]
    W=(0.25, 0.5, 0.75, 1.0),   # salaires de reprise, en fraction du SMIC, à parts égales [Unverified]
    LF=640.0, LT=0.39,  # droit actuel simplifié (RSA + prime d'activité, personne seule) : max(0, LF - LT x w) [Unverified]
)

def legacy(w, sp=SP):
    """Ce que procure la législation actuelle (RSA et prime d'activité, simplifiés) à un salaire net w."""
    return max(0.0, sp['LF'] - sp['LT'] * w)

def sp_pay(S, w, t, mode, sp=SP):
    """Versement du mois t (1 = premier mois de reprise) pour un socle S et un salaire w."""
    res = max(0.0, S - sp['F'] * w); L = legacy(w, sp); D = sp['D']
    if mode == 'M11':
        return res if t <= 12 else L
    if mode == 'plus_favorable':
        return max(res, L) if t <= 12 else L
    if mode == 'degressif':          # les D derniers des 12 mois : k décroît linéairement
        k = 1.0 if t <= 12 - D else (12 - t + 1) / (D + 1)
        return max(k * res, L) if t <= 12 else L
    if mode == 'prolonge':           # 12 mois pleins, puis D mois dégressifs en plus
        k = 1.0 if t <= 12 else max(0.0, (12 + D - t + 1) / (D + 1))
        return max(k * res, L) if t <= 12 + D else L
    raise ValueError(mode)

def sp_cost(S, mode, sp=SP):
    """Coût net annuel (Md€ de 2026) de la sortie progressive par rapport à la législation actuelle."""
    per = sum(sum(sp_pay(S, x * sp['SMIC'], t, mode, sp) - legacy(x * sp['SMIC'], sp) for t in range(1, 25))
              for x in sp['W']) / len(sp['W'])
    return sp['ENTREES'] * per / 1000.0


# ---------------------------------------------------------------- garantie familiale (art. 9, I ; D9 ; C7) [Unverified]
# Foyers allocataires du RSA que le socle individuel désavantagerait : (libellé, millions de foyers, RSA du foyer en
# € de 2026 par mois, avant forfait logement (note 18, D9), nombre d'adultes). Les effectifs sont des hypothèses de
# l'agent [opus-5.5, Unverified], calées pour retrouver l'ordre de grandeur de D13.7 (0,5 à 1 Md€ au socle cible).
GF_TYPES = [
    ('parent isolé, 1 enfant (RSA majoré)', 0.10, 1110.0, 1),
    ('parent isolé, 2 enfants (RSA majoré)', 0.10, 1390.0, 1),
    ('parent isolé, 3 enfants ou plus (RSA majoré)', 0.05, 1670.0, 1),
    ('couple, 2 enfants', 0.15, 1365.0, 2),
    ('couple, 6 enfants ou plus', 0.01, 2700.0, 2),
]

def gf_cost(s, rule):
    """Versements du complément familial (Md€ de 2026 par an) pour un socle s : l'écart entre le montant garanti et la
    somme des socles du foyer. rule='rsa' (C7) : le montant garanti suit la revalorisation légale du RSA, supposée égale,
    par prudence, à l'indexation du modèle (montant constant en € de 2026) ; rule='socle' : il suit le socle (× s/650)."""
    tot = 0.0
    for _, n, G, a in GF_TYPES:
        g = G if rule == 'rsa' else G * s / S_RSA
        tot += n * max(0.0, g - a * s) * 12 / 1000
    return tot

def need(s, c):
    """Besoin net annuel de la branche financé par la taxe (Md€), pour un socle s (€/mois)."""
    x = (s - S_RSA) / (S_CIBLE - S_RSA)
    if c.get('SP_RACCORD'):   # M14 (A4) : la sortie progressive est retirée des deux points de calage, puis chiffrée
        lo = c['N_RSA'] - c['SP_ORIG_RSA']; hi = c['N_CIBLE'] - sp_cost(S_CIBLE, 'M11')
        n = lo + x * (hi - lo) + sp_cost(s, c['SORTIE'])
    else:
        n = c['N_RSA'] + x * (c['N_CIBLE'] - c['N_RSA'])
        if c['SORTIE'] != 'M11':   # décision 96 : surcoût de la correction par rapport à l'hypothèse d'origine (N_RSA)
            n += sp_cost(s, c['SORTIE']) - sp_cost(s, 'M11')
    if c.get('GF'):   # M14 (A5) : N_RSA reprend les foyers à l'identique (le complément y est implicite, financé par le
        # RSA repris) ; N_CIBLE (note 05) déduit leur RSA entier et ne le contient pas : on remplace la part implicite
        # interpolée, (1 - x) × gf(650), par le versement effectif gf(s)
        n += gf_cost(s, c['GF']) - (1 - x) * gf_cost(S_RSA, c['GF'])
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

# ---------------------------------------------------------------- décision 89
def capB(V, y, m, needA, B, I, p, c):
    """Marge disponible pour ENGAGER une baisse des cotisations supplémentaire (Md€ courants) : ce que la recette
    à m' = min(m, M_POST) couvrirait au-delà de la formation, des droits (needA) et de la baisse déjà engagée (B),
    l'année y et l'année y + 1 (montants indexés ; la baisse engagée reste en euros courants)."""
    m2 = min(m, c['M_POST']) if c['M_POST'] is not None else m
    out = []
    for k in (0, 1):
        yy = min(y + k, END)
        R2, _ = revenue(V[yy], y + k, m2, p)
        g = (1 + c['IDX']) ** k
        out.append(R2 - min(R2, c['FORM'] * I * g) - needA * g - B)
    return max(0.0, min(out))

# ---------------------------------------------------------------- simulation
def run(name, mcap=1.0, alloc='droits', p=None, c=None):
    """alloc='droits' : décision 75 (les droits d'abord jusqu'au socle cible, puis le surplus va au partage ;
    les droits étant alors au plafond, il va à la baisse des cotisations). alloc='D8' : l'ordre de la décision 54."""
    p = dict(P, **(p or {})); c = dict(C, **(c or {}))
    V = market(name)
    m = 1.0; s = None; B = 0.0; fund = 0.0; rows = []; prevR = None; prev = None
    for y in YEARS:
        R, spend = revenue(V[y], y, m, p)
        if c['RETOURNEMENT'] == 'produit':
            retournement = prevR is not None and R < prevR
        else:   # décision 95 : l'assiette de l'année, au multiple de l'année précédente, baisse
            retournement = prev is not None and revenue(V[y], y, prev[0], p)[1] < prev[1]
        prevR = R; prev = (m, spend)
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
                gap = -surplus
                if c['B_AVANT_FONDS'] and not retournement:   # décision 86 : la baisse des cotisations d'abord
                    cut = min(B, gap); B -= cut; gap -= cut
                draw = min(fund, gap); fund -= draw; gap -= draw
                if gap > 0:        # les droits priment : on suspend la baisse des cotisations
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
                        usedB = min(max(0.0, BMAX - B), rest)
                        if c['B_SOUTENABLE']:   # décision 89 : soutenable avec m <= 2, cette année et la suivante
                            usedB = min(usedB, capB(V, y, m, newA, B, I, p, c))
                        rest -= usedB
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
                xs = 0.0
                if c['M79_FONDS']:   # variante : un tiers de l'excédent du fonds sur sa cible
                    xs = max(0.0, fund - (c['FUND_MONTHS'] / 12) * (need(s, c) + c['FORM']) * I2) / 3
                if R2 - c['FORM'] * I2 + xs >= need(s, c) * I2: m = max(c['M_POST'], m - 0.5)
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
AVANT_M14 = {'SP_RACCORD': False, 'GF': None}   # les règles d'avant la passe de corrections (non-régression)
if '--avant-m14' in sys.argv: C.update(AVANT_M14)
M11 = dict(AVANT_M14, M79_FONDS=False, RETOURNEMENT='produit', SORTIE='M11')   # les règles de M11 (non-régression)
M10 = dict(M11, B_SOUTENABLE=False)   # les règles de M10, sans la décision 89 (contrôle de non-régression)
AVANT_M9 = dict(M11, IDX=0.0, OPEN_RULE='annuel', M_POST=None, B_AVANT_FONDS=False, B_SOUTENABLE=False)   # les hypothèses de M7, pour comparaison

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
    print('# Règles retenues : droits d\'abord (75), ouverture sur trois ans (78), m <= 2 après la cible (79), indexation (80), baisse des cotisations soutenable à m <= 2 (89), excédent du fonds (94), retournement sur l\'assiette (95), sortie progressive corrigée (96)' + ('' if '--avant-m14' in sys.argv else ' ; M14 : besoin raccordé à la sortie progressive (A4), garantie familiale chiffrée (C7)'))
    for cap in (2.0, 3.0, 4.0):
        print('\n## Central, m plafonné à %.0f (règles retenues ; socle en euros 2026)' % cap); table(run('Central', cap))
    print('\n## Bas, m plafonné à 4 (règles retenues)'); table(run('Bas', 4.0))
    grid2(label='règles retenues')
    grid2(SANS_IDX, label='sans indexation')
    grid2(M11, label='règles de M11 (contrôle de non-régression)')
    grid2(M10, label='règles de M10, sans la décision 89 (contrôle de non-régression)')
    grid2(AVANT_M9, label='hypothèses de M7 (sans indexation, ouverture annuelle, sans règle 79)')
    grid2(AVANT_M9, 'D8', label='ancienne règle D8 (décision 54), hypothèses de M7')
    print('\n## Variantes et sensibilités (Central, règles retenues)')
    print('variante | plafond | socle cible atteint | socle 2035 | socle 2040 | pts 2040')
    VAR = [('base', {}, {}), ('étudiants inclus', {'ETU': True}, {}), ('réduction patrimoine', {'PATR': True}, {}),
           ('inscription de 0,5 M inactifs', {'INACT': True}, {}), ('fonds = 6 mois bruts', {'FUND_GROSS': True}, {}),
           ('sans l\'excédent du fonds (règle de M11)', {'M79_FONDS': False}, {}), ('sortie : plancher sans dégressivité', {'SORTIE': 'plus_favorable'}, {}), ('sortie : 12 mois + 6 mois dégressifs', {'SORTIE': 'prolonge'}, {}), ('sortie : hypothèse d\'origine (M11)', {'SORTIE': 'M11'}, {}), ('indexation 1 %', {'IDX': 0.01}, {}), ('indexation 3 %', {'IDX': 0.03}, {}),
           ('élasticité 0,3', {}, {'EPS': 0.3}), ('élasticité 1,0', {}, {'EPS': 1.0}),
           ('terminal réduit prolongé à cinq ans (C2)', {}, {'TERM_RED_END': 2032}),
           ('garantie familiale revalorisée comme le socle', {'GF': 'socle'}, {}),
           ('décalage de P_k (x1,09)', {}, {'LAG': 1.09}), ('sans serveurs propres ni recouvrement', {}, {'F_INTERNE': 1.0, 'CIVISME': 1.0})]
    for lab, cc, pp in VAR:
        for cap in (2.0, 3.0, 4.0):
            rows = run('Central', cap, 'droits', pp, cc); o, f, at = summary(rows)
            print('%s | %.0f | %s | %s | %s | %.2f' % (lab, cap, f or 'non', fmt_s(at[2035]['s']), fmt_s(at[2040]['s']), max(0.0, at[2040]['pts'])))
    print('\n## Étudiants inclus, Haut, m <= 4 (règles retenues)'); table(run('Haut', 4.0, 'droits', None, {'ETU': True}))
