import matplotlib.pyplot as plt
import matplotlib.patches as patches

# Dimensiones de la casa
house_length = 20  # metros
house_width = 6    # metros

# Crear figura
fig, ax = plt.subplots(figsize=(12, 4))
ax.set_xlim(0, house_length)
ax.set_ylim(0, house_width)

# Dibujar habitaciones
# Espacio abierto (sala/comedor/cocina)
ax.add_patch(patches.Rectangle((0, 0), 8, 6, edgecolor='black', facecolor='lightgray'))
ax.text(1, 5.5, "Sala / Comedor / Cocina", fontsize=8)

# Dormitorio principal
ax.add_patch(patches.Rectangle((8, 3), 4, 3, edgecolor='black', facecolor='lightblue'))
ax.text(8.2, 5.5, "Dormitorio Ppal", fontsize=8)

# Baño en suite
ax.add_patch(patches.Rectangle((12, 4), 2, 2, edgecolor='black', facecolor='lightgreen'))
ax.text(12.1, 5.2, "Baño Ppal", fontsize=7)

# Dormitorios secundarios
ax.add_patch(patches.Rectangle((8, 0), 3, 3, edgecolor='black', facecolor='lightyellow'))
ax.text(8.2, 2.5, "Dormitorio 2", fontsize=8)

ax.add_patch(patches.Rectangle((11, 0), 3, 3, edgecolor='black', facecolor='lightyellow'))
ax.text(11.2, 2.5, "Dormitorio 3", fontsize=8)

# Baño común
ax.add_patch(patches.Rectangle((14, 2), 2, 2, edgecolor='black', facecolor='lightgreen'))
ax.text(14.1, 3.5, "Baño", fontsize=8)

# Lavandería
ax.add_patch(patches.Rectangle((16, 0), 2, 2, edgecolor='black', facecolor='pink'))
ax.text(16.1, 1.5, "Lavandería", fontsize=8)

# Patio trasero
ax.add_patch(patches.Rectangle((18, 0), 2, 6, edgecolor='black', facecolor='white', linestyle='dotted'))
ax.text(18.1, 5.5, "Patio", fontsize=8)

# Etiquetas generales
ax.set_title("Plano esquemático - Casa tipo 'Lange' (20m x 6m)", fontsize=12)
ax.set_aspect('equal')
ax.axis('off')

plt.tight_layout()
plt.show()
