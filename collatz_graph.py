import matplotlib.pyplot as plt
import collatz as col

x_values = range(1, len(col.collatz_number_list)+1)
y_values = [x for x in col.collatz_number_list]

plt.style.use("seaborn")
fig, ax = plt.subplots()
ax.plot(x_values, y_values, c='blue', linewidth=2)
ax.set_title(f"Collatz conjecture for number {col.graph_value}", fontsize=24)

plt.show()