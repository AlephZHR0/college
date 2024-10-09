import chi_calc

total_chi = 0
for i in range(10):
    total_chi += chi_calc.move()
print(total_chi)