# Simulation v3 : trajectoire avec partage 50/50 et règle de taux (plancher P, moteur, plafond 4P)
EPS=0.5            # élasticité de la demande au prix
A_TARGET=10.0      # Md€ : extension des droits (chômage universel complet ≈ 50, dont ≈ 40 déjà financés)
PT=11.0            # Md€ par point de cotisation
B_TARGET=44.0      # Md€ : 4 points de cotisation remplacés
years=list(range(2026,2036))
scen={
 'Bas':     (0.46,[1.5,1.45,1.4,1.35,1.3,1.25,1.2,1.15,1.1]),
 'Central': (1.32,[2.0,1.8,1.6,1.45,1.3,1.2,1.15,1.1,1.05]),
 'Haut':    (3.02,[2.5,2.1,1.7,1.45,1.3,1.2,1.1,1.05,1.05]),
}
def rev(V,m): return m*V*(1+m)**(-EPS)
def run(name,V0,g,engine=False,deadline=2032):
    V=V0; A=0.0; B=0.0; fund=0.0; rows=[]
    for i,y in enumerate(years):
        if i>0: V*=g[i-1]
        m=1.0
        if engine and y>=2029:
            need=(A_TARGET-A)+(B_TARGET-B)
            yrs=max(1,deadline-y+1)
            target=need/yrs + (A+B)   # flux annuel nécessaire pour finir à l'échéance (en plus du stock déjà financé)
            lo,hi=1.0,4.0
            if rev(V,hi)<=target: m=hi
            elif rev(V,lo)>=target: m=lo
            else:
                for _ in range(60):
                    mid=(lo+hi)/2
                    if rev(V,mid)<target: lo=mid
                    else: hi=mid
                m=hi
        R=rev(V,m)
        if y<=2028:
            fund+=R; alloc='réserve + formation'
        else:
            # le flux annuel finance d'abord le maintien des mesures déjà prises (A+B), puis le surplus se partage 50/50
            surplus=R-(A+B)
            if surplus>0:
                a=min(surplus/2,A_TARGET-A); b=min(surplus-a,B_TARGET-B)
                if a<surplus/2: b=min(surplus-a,B_TARGET-B)
                A+=a; B+=b
                left=surplus-a-b; fund+=left
            else:
                fund+=surplus  # le fonds absorbe un éventuel déficit
            alloc=''
        rows.append((y,V,m,R,A,B,B/PT,fund,alloc))
    return rows
import sys
for engine in (False,True):
    print('\n######## ', 'MOTEUR (objectifs atteints en 2032, plafond 4P)' if engine else 'PLANCHER SEUL (50/50, m=1)')
    for k,(V0,g) in scen.items():
        print('\n==',k)
        print('année | marché HT | multiple m | recettes | droits A | cotis B | points | fonds')
        for (y,V,m,R,A,B,pts,f,al) in run(k,V0,g,engine):
            print(f"{y} | {V:6.1f} | {m:4.2f} | {R:6.1f} | {A:5.1f} | {B:5.1f} | {pts:4.2f} | {f:6.1f}")
