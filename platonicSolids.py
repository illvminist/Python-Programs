import tkinter as tk
from matplotlib.backends.backend_tkagg import FigureCanvasTkAgg
import matplotlib.pyplot as plt
from mpl_toolkits.mplot3d.art3d import Poly3DCollection
import numpy as np

# Function to create a checkerboard background
def create_checkerboard(ax):
    ax.set_facecolor('lightgray')
    ax.grid(False)
    checkerboard_size = 10
    x_ticks = np.arange(-checkerboard_size, checkerboard_size + 1, 1)
    y_ticks = np.arange(-checkerboard_size, checkerboard_size + 1, 1)
    ax.set_xticks(x_ticks)
    ax.set_yticks(y_ticks)
    ax.set_xticklabels([])
    ax.set_yticklabels([])
    ax.set_xticks(np.arange(-checkerboard_size, checkerboard_size + 1, 2), minor=True)
    ax.set_yticks(np.arange(-checkerboard_size, checkerboard_size + 1, 2), minor=True)
    ax.grid(which='minor', color='black', linestyle='-', linewidth=1)

# Function to plot a Platonic solid
def plot_platonic_solid(vertices, faces, solid_name, ax, color):
    ax.set_title(solid_name, fontsize=10)
    ax.view_init(elev=30, azim=30)

    # Create the 3D faces of the Platonic solid
    poly3d = Poly3DCollection(faces, facecolors=color, linewidths=1, edgecolors='k', alpha=.25)
    ax.add_collection3d(poly3d)

    # Set limits for the plot
    ax.set_xlim([-2, 2])
    ax.set_ylim([-2, 2])
    ax.set_zlim([-2, 2])

# Define Platonic solids' vertices and faces
# Tetrahedron
tetrahedron_vertices = np.array([[1, 1, 1], [-1, -1, 1], [-1, 1, -1], [1, -1, -1]])
tetrahedron_faces = [[tetrahedron_vertices[0], tetrahedron_vertices[1], tetrahedron_vertices[2]],
                     [tetrahedron_vertices[0], tetrahedron_vertices[1], tetrahedron_vertices[3]],
                     [tetrahedron_vertices[0], tetrahedron_vertices[2], tetrahedron_vertices[3]],
                     [tetrahedron_vertices[1], tetrahedron_vertices[2], tetrahedron_vertices[3]]]

# Cube
cube_vertices = np.array([[1, 1, 1], [1, 1, -1], [1, -1, 1], [1, -1, -1],
                          [-1, 1, 1], [-1, 1, -1], [-1, -1, 1], [-1, -1, -1]])
cube_faces = [[cube_vertices[0], cube_vertices[1], cube_vertices[2], cube_vertices[3]],
              [cube_vertices[4], cube_vertices[5], cube_vertices[6], cube_vertices[7]],
              [cube_vertices[0], cube_vertices[1], cube_vertices[5], cube_vertices[4]],
              [cube_vertices[2], cube_vertices[3], cube_vertices[7], cube_vertices[6]],
              [cube_vertices[0], cube_vertices[3], cube_vertices[7], cube_vertices[4]],
              [cube_vertices[1], cube_vertices[2], cube_vertices[6], cube_vertices[5]]]

# Octahedron
octahedron_vertices = np.array([[0, 0, 1], [0, 0, -1], [1, 0, 0], [-1, 0, 0], [0, 1, 0], [0, -1, 0]])
octahedron_faces = [[octahedron_vertices[0], octahedron_vertices[2], octahedron_vertices[4]],
                    [octahedron_vertices[0], octahedron_vertices[4], octahedron_vertices[3]],
                    [octahedron_vertices[0], octahedron_vertices[3], octahedron_vertices[5]],
                    [octahedron_vertices[0], octahedron_vertices[5], octahedron_vertices[2]],
                    [octahedron_vertices[1], octahedron_vertices[2], octahedron_vertices[4]],
                    [octahedron_vertices[1], octahedron_vertices[4], octahedron_vertices[3]],
                    [octahedron_vertices[1], octahedron_vertices[3], octahedron_vertices[5]],
                    [octahedron_vertices[1], octahedron_vertices[5], octahedron_vertices[2]]]

# Dodecahedron (12 faces, regular pentagons)
# Define the dodecahedron with correct vertices and faces
dodecahedron_vertices = np.array([
    [1, 1, 1], [-1, 1, 1], [1, -1, 1], [-1, -1, 1],
    [1, 1, -1], [-1, 1, -1], [1, -1, -1], [-1, -1, -1],
    [0, 1.618, 1.618], [0, -1.618, 1.618], [0, 1.618, -1.618], [0, -1.618, -1.618],
    [1.618, 1.618, 0], [-1.618, 1.618, 0], [1.618, -1.618, 0], [-1.618, -1.618, 0],
    [1.618, 0, 1.618], [-1.618, 0, 1.618], [1.618, 0, -1.618], [-1.618, 0, -1.618]
])

dodecahedron_faces = [
    [dodecahedron_vertices[0], dodecahedron_vertices[8], dodecahedron_vertices[12], dodecahedron_vertices[16], dodecahedron_vertices[4]],
    [dodecahedron_vertices[1], dodecahedron_vertices[9], dodecahedron_vertices[13], dodecahedron_vertices[17], dodecahedron_vertices[5]],
    [dodecahedron_vertices[2], dodecahedron_vertices[10], dodecahedron_vertices[14], dodecahedron_vertices[18], dodecahedron_vertices[6]],
    [dodecahedron_vertices[3], dodecahedron_vertices[11], dodecahedron_vertices[15], dodecahedron_vertices[19], dodecahedron_vertices[7]],
    [dodecahedron_vertices[0], dodecahedron_vertices[1], dodecahedron_vertices[5], dodecahedron_vertices[4], dodecahedron_vertices[8]],
    [dodecahedron_vertices[1], dodecahedron_vertices[2], dodecahedron_vertices[6], dodecahedron_vertices[5], dodecahedron_vertices[9]],
    [dodecahedron_vertices[2], dodecahedron_vertices[3], dodecahedron_vertices[7], dodecahedron_vertices[6], dodecahedron_vertices[10]],
    [dodecahedron_vertices[3], dodecahedron_vertices[0], dodecahedron_vertices[4], dodecahedron_vertices[7], dodecahedron_vertices[11]],
    [dodecahedron_vertices[4], dodecahedron_vertices[5], dodecahedron_vertices[9], dodecahedron_vertices[8], dodecahedron_vertices[12]],
    [dodecahedron_vertices[5], dodecahedron_vertices[6], dodecahedron_vertices[10], dodecahedron_vertices[9], dodecahedron_vertices[13]],
    [dodecahedron_vertices[6], dodecahedron_vertices[7], dodecahedron_vertices[11], dodecahedron_vertices[10], dodecahedron_vertices[14]],
    [dodecahedron_vertices[7], dodecahedron_vertices[8], dodecahedron_vertices[12], dodecahedron_vertices[11], dodecahedron_vertices[15]],
    [dodecahedron_vertices[8], dodecahedron_vertices[9], dodecahedron_vertices[13], dodecahedron_vertices[12], dodecahedron_vertices[16]]
]

# Icosahedron (20 faces, equilateral triangles)
icosahedron_vertices = np.array([
    [0, 1, 1.618], [0, -1, 1.618], [0, 1, -1.618], [0, -1, -1.618],
    [1.618, 0, 1], [-1.618, 0, 1], [1.618, 0, -1], [-1.618, 0, -1],
    [1, 1.618, 0], [-1, 1.618, 0], [1, -1.618, 0], [-1, -1.618, 0]
])

icosahedron_faces = [
    [icosahedron_vertices[0], icosahedron_vertices[8], icosahedron_vertices[4]],
    [icosahedron_vertices[0], icosahedron_vertices[5], icosahedron_vertices[9]],
    [icosahedron_vertices[0], icosahedron_vertices[1], icosahedron_vertices[6]],
    [icosahedron_vertices[0], icosahedron_vertices[7], icosahedron_vertices[8]],
    [icosahedron_vertices[0], icosahedron_vertices[9], icosahedron_vertices[5]],
    [icosahedron_vertices[1], icosahedron_vertices[0], icosahedron_vertices[2]],
    [icosahedron_vertices[2], icosahedron_vertices[1], icosahedron_vertices[3]],
    [icosahedron_vertices[3], icosahedron_vertices[2], icosahedron_vertices[6]],
    [icosahedron_vertices[7], icosahedron_vertices[6], icosahedron_vertices[2]],
    [icosahedron_vertices[6], icosahedron_vertices[7], icosahedron_vertices[8]]
]

# Set up the main Tkinter window
root = tk.Tk()
root.title("Platonic Solids")

frame = tk.Frame(root)
frame.pack(fill=tk.BOTH, expand=True)

# Create a figure for plotting
fig = plt.figure(figsize=(16, 12))

# Create subplots for all five Platonic solids
ax1 = fig.add_subplot(231, projection='3d')
create_checkerboard(ax1)
plot_platonic_solid(tetrahedron_vertices, tetrahedron_faces, "Tetrahedron", ax1, 'red')

ax2 = fig.add_subplot(232, projection='3d')
create_checkerboard(ax2)
plot_platonic_solid(cube_vertices, cube_faces, "Cube", ax2, 'blue')

ax3 = fig.add_subplot(233, projection='3d')
create_checkerboard(ax3)
plot_platonic_solid(octahedron_vertices, octahedron_faces, "Octahedron", ax3, 'green')

ax4 = fig.add_subplot(234, projection='3d')
create_checkerboard(ax4)
plot_platonic_solid(dodecahedron_vertices, dodecahedron_faces, "Dodecahedron", ax4, 'orange')

ax5 = fig.add_subplot(235, projection='3d')
create_checkerboard(ax5)
plot_platonic_solid(icosahedron_vertices, icosahedron_faces, "Icosahedron", ax5, 'purple')

# Embed the plot in the Tkinter window
canvas = FigureCanvasTkAgg(fig, master=frame)
canvas.draw()
canvas.get_tk_widget().pack(fill=tk.BOTH, expand=True)

# Start the Tkinter event loop
root.mainloop()
