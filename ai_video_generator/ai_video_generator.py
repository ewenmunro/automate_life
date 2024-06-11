import cv2
import numpy as np

# Video properties
frame_width = 1920
frame_height = 1080
fps = 24
duration = 15

# Cube properties
cube_size = 5
num_cubes = 1000000

# Create a VideoWriter object
output_file = 'video.mp4'
fourcc = cv2.VideoWriter_fourcc(*'XVID')
out = cv2.VideoWriter(output_file, fourcc, fps, (frame_width, frame_height))

# Generate random starting positions for the cubes
x_positions = np.random.randint(0, frame_width, num_cubes)
y_positions = np.random.randint(0, frame_height, num_cubes)

# Generate random velocities for the cubes
x_velocities = np.random.randint(1, 5, num_cubes)
y_velocities = np.random.randint(-2, 3, num_cubes)

# Generate random shades of blue for the cubes (dark shade)
cube_colors = np.zeros((num_cubes, 3), dtype=np.uint8)
cube_colors[:, 2] = np.random.randint(0, 100, num_cubes, dtype=np.uint8)
cube_colors[:, 0:2] = np.random.randint(
    170, 256, (num_cubes, 2), dtype=np.uint8)

# Create a blank frame
frame = np.zeros((frame_height, frame_width, 3), dtype=np.uint8)

# Main animation loop
num_frames = int(fps * duration)
for i in range(num_frames):
    # Update cube positions
    x_positions += x_velocities
    y_positions += y_velocities

    # Reset positions that go beyond frame boundaries
    x_positions = np.where((x_positions >= frame_width), 0, x_positions)
    x_positions = np.where((x_positions < 0), frame_width - 1, x_positions)
    y_positions = np.where((y_positions >= frame_height), 0, y_positions)
    y_positions = np.where((y_positions < 0), frame_height - 1, y_positions)

    # Draw cubes on the frame
    frame.fill(0)
    for j in range(num_cubes):
        x = x_positions[j]
        y = y_positions[j]
        color = tuple(map(int, cube_colors[j]))
        cv2.rectangle(frame, (x, y), (x + cube_size, y + cube_size), color, -1)

    # Write the frame to the video file
    out.write(frame)

    # Display the current frame
    cv2.imshow('AI Video', frame)
    cv2.waitKey(1)

# Release the VideoWriter and close windows
out.release()
cv2.destroyAllWindows()
