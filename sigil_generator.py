import matplotlib.pyplot as plt
import numpy as np
from collections import OrderedDict

def remove_vowels_and_duplicates(intent):
    vowels = 'aeiou'
    intent = ''.join([char for char in intent.lower() if char not in vowels])
    intent = ''.join(OrderedDict.fromkeys(intent))  # Remove duplicates, keep order
    return intent

def create_sigil(intent):
    simplified_intent = remove_vowels_and_duplicates(intent)
    return simplified_intent

def map_to_points(sigil, canvas_size=1):
    np.random.seed(0)  # For reproducibility
    points = np.random.rand(len(sigil), 2) * canvas_size  # Random points in the canvas
    return points

def bezier_curve(p0, p1, p2, t):
    """ Compute the point on a quadratic Bézier curve at parameter t """
    return (1-t)**2 * p0 + 2 * (1-t) * t * p1 + t**2 * p2

def draw_sigil(points):
    fig, ax = plt.subplots()

    # Draw the Bézier curves connecting the points
    for i in range(len(points) - 1):
        p0 = points[i]
        p2 = points[i + 1]
        p1 = (p0 + p2) / 2 + np.random.rand(2) * 0.2 - 0.1  # Random control point
        t_values = np.linspace(0, 1, 100)
        curve = np.array([bezier_curve(p0, p1, p2, t) for t in t_values])
        ax.plot(curve[:, 0], curve[:, 1], 'k-', linewidth=2)

    # Optionally close the loop by connecting the last point to the first
    p0 = points[-1]
    p2 = points[0]
    p1 = (p0 + p2) / 2 + np.random.rand(2) * 0.2 - 0.1  # Random control point
    curve = np.array([bezier_curve(p0, p1, p2, t) for t in np.linspace(0, 1, 100)])
    ax.plot(curve[:, 0], curve[:, 1], 'k-', linewidth=2)

    # Add circles at each point
    ax.scatter(points[:, 0], points[:, 1], s=100, c='red')

    ax.set_aspect('equal')
    plt.axis('off')
    plt.show()

def main():
    print("Welcome to the Sigil Generator!")
    intent = input("Enter your intent or desire: ")
    sigil = create_sigil(intent)
    print(f"Simplified intent: {sigil}")
    points = map_to_points(sigil)
    draw_sigil(points)

if __name__ == "__main__":
    main()