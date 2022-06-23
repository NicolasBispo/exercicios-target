distr_sp = 67836.43
distr_rj = 36678.66
distr_mg = 29229.88
distr_es = 27165.48
distr_outros = 19849.53

print("Percentual de vendas por estado")

valor_total = distr_sp + distr_rj + distr_mg + distr_es + distr_outros

pct_sp = (distr_sp * 100)/valor_total
pct_rj = (distr_rj * 100)/valor_total
pct_mg = (distr_rj * 100)/valor_total
pct_es = (distr_es * 100)/valor_total
pct_outros = (distr_outros * 100)/valor_total

print("Percentual São Paulo:", str(pct_sp) + " %\nPercentual Rio de Janeiro:", str(pct_rj) + "%\n")
print("Percentual Minas Gerais:", str(pct_mg) + "%\nPercentual Espirito Santo:", str(pct_es))
print("Percentual Outros:", str(pct_outros) + "%")
