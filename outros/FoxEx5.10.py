#!/usr/bin/python

#----------------------------------------------------------------------------
# Created By: Marcos Lourenço
# Created Date: 24/08/2022
# version ='1.0'
# ---------------------------------------------------------------------------
# Traçado dos perfis de velocidade para o Ex. 5.10 do livro Introdução à
#  Mecânica dos Fluidos, de Fox et. al.

import matplotlib.pyplot as plt
from numpy import linspace, concatenate

razao = 0.7
r2 = 0.2 # 20 cm
r1 = r2*razao
k2 = pow(r1/r2, 2)
w = 1 # rad/s

def v_theta(r):
    "Perfil de velocidade deduzido"
    A = w/(1 - k2)
    return A*(r - r1*r1/r)

def v_plani(r):
    "Perfil de velocidade planificado"
    return w*r2*(r - r1)/(r2 - r1)

fig = plt.figure()
ax = fig.add_subplot(projection="polar")

r = linspace(r1, r2, 128) # Campo de r

v_t = v_theta(r) # Perfil 2D deduzido em coordenadas cilíndricas
v_p = v_plani(r) # Perfil entre placas planas
dois_perfis = concatenate((v_t,v_p))

ax.plot(v_t, r, '-', color="tab:orange", lw=2, label="Deduzido")
ax.plot(v_p, r, '--', color="tab:green",  lw=2, label="Linear")
ax.fill_betweenx(r, v_t, v_p, color="tab:blue", alpha=0.5, label="Erro")
ax.set_rmin(r1)
ax.set_rmax(r2)
ax.set_rorigin(-r1)
ax.set_thetamin(0)
ax.set_thetamax(12)
ax.set_xlabel(r"$r\,$[m]", labelpad=10)
ax.set_ylabel(r"$v_{\theta}$[m/s]", labelpad=-450)
ax.grid(False)
ax.set_rticks(linspace(r.min(), r.max(), 3))
ax.set_xticks(linspace(0, dois_perfis.max(), 6),
              ['0','2','5','7','9','11'])
plt.legend()
plt.show()

