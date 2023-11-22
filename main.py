import os
import tkinter as tk

# ----------------------!VARIABLES!----------------------
CANVAS_WIDTH = 320
CANVAS_HEIGHT = 240


# ----------------------!FUNCTIONS!----------------------
def run_script():
    # Update map
    update_sbm(0)

    # Run scenario
    os.system("python scenario.py")


def update_sbm(value):
    # Write values to file
    with open("map.sbm", "w") as file:
        file.write(str(scale_ground_height.get()) + "\n")  # Ground height
        file.write(str(scale_ceiling_height.get()) + "\n")  # Ceiling height
        file.write(str(scale_wall_left_width.get()) + "\n")  # Wall left width
        file.write(str(scale_wall_right_width.get()) + "\n")  # Wall right width
        file.write(str(scale_bouncer_x.get()) + "\n")  # Bouncer x
        file.write(str(scale_bouncer_y.get()) + "\n")  # Bouncer y
        file.write(str(scale_bouncer_width.get()) + "\n")  # Bouncer width
        file.write(str(scale_bouncer_height.get()) + "\n")  # Bouncer height
        file.write(str(scale_bouncer_speed_x.get()) + "\n")  # Bouncer speed x
        file.write(str(scale_bouncer_speed_y.get()) + "\n")  # Bouncer speed y

    update_canvas()


def update_canvas():
    # Clear the canvas
    canvas_blueprint.delete("all")

    # Draw ground
    canvas_blueprint.create_rectangle(0,
                                      CANVAS_HEIGHT - scale_ground_height.get() / 2,
                                      CANVAS_WIDTH,
                                      CANVAS_HEIGHT,
                                      fill="grey",
                                      outline="grey")

    # Draw ceiling
    canvas_blueprint.create_rectangle(0,
                                      0,
                                      CANVAS_WIDTH,
                                      scale_ceiling_height.get() / 2,
                                      fill="grey",
                                      outline="grey")

    # Draw left wall
    canvas_blueprint.create_rectangle(0,
                                      0,
                                      scale_wall_left_width.get() / 2,
                                      CANVAS_HEIGHT,
                                      fill="grey",
                                      outline="grey")

    # Draw right wall
    canvas_blueprint.create_rectangle(CANVAS_WIDTH - scale_wall_right_width.get() / 2,
                                      0,
                                      CANVAS_WIDTH,
                                      CANVAS_HEIGHT,
                                      fill="grey",
                                      outline="grey")

    # Draw bouncer
    canvas_blueprint.create_rectangle(scale_bouncer_x.get() / 2,
                                      scale_bouncer_y.get() / 2,
                                      (scale_bouncer_x.get() / 2) + (scale_bouncer_width.get() / 2),
                                      (scale_bouncer_y.get() / 2) + (scale_bouncer_height.get() / 2),
                                      fill="green",
                                      outline="green")


# ----------------------!WINDOW AND GUI!----------------------

# Main window
win_root = tk.Tk()
win_root.geometry("320x700")
win_root.resizable(False, False)
win_root.title("Square Bouncer")

# Configure the grid
win_root.rowconfigure(0, weight=1)
win_root.columnconfigure(0, weight=1)

# Canvas
canvas_blueprint = tk.Canvas(win_root, width=320, height=240, background="black")

# Label
label_ground_height = tk.Label(win_root, text="Ground height: ")
label_ceiling_height = tk.Label(win_root, text="Ceiling height: ")
label_wall_left_width = tk.Label(win_root, text="Wall left width: ")
label_wall_right_width = tk.Label(win_root, text="Wall right width: ")
label_bouncer_x = tk.Label(win_root, text="Bouncer X")
label_bouncer_y = tk.Label(win_root, text="Bouncer Y")
label_bouncer_width = tk.Label(win_root, text="Bouncer width")
label_bouncer_height = tk.Label(win_root, text="Bouncer height")
label_bouncer_speed_x = tk.Label(win_root, text="Bouncer speed x")
label_bouncer_speed_y = tk.Label(win_root, text="Bouncer speed y")

# Scale
scale_ground_height = tk.Scale(win_root, from_=1, to=240, orient=tk.HORIZONTAL, command=update_sbm)
scale_ceiling_height = tk.Scale(win_root, from_=1, to=240, orient=tk.HORIZONTAL, command=update_sbm)
scale_wall_left_width = tk.Scale(win_root, from_=1, to=320, orient=tk.HORIZONTAL, command=update_sbm)
scale_wall_right_width = tk.Scale(win_root, from_=1, to=320, orient=tk.HORIZONTAL, command=update_sbm)

scale_bouncer_x = tk.Scale(win_root, from_=1, to=640, orient=tk.HORIZONTAL, command=update_sbm)
scale_bouncer_x.set(50)
scale_bouncer_y = tk.Scale(win_root, from_=1, to=480, orient=tk.HORIZONTAL, command=update_sbm)
scale_bouncer_y.set(50)
scale_bouncer_width = tk.Scale(win_root, from_=1, to=640, orient=tk.HORIZONTAL, command=update_sbm)
scale_bouncer_width.set(50)
scale_bouncer_height = tk.Scale(win_root, from_=1, to=480, orient=tk.HORIZONTAL, command=update_sbm)
scale_bouncer_height.set(50)
scale_bouncer_speed_x = tk.Scale(win_root, from_=-50, to=50, orient=tk.HORIZONTAL, command=update_sbm)
scale_bouncer_speed_x.set(0)
scale_bouncer_speed_y = tk.Scale(win_root, from_=-50, to=50, orient=tk.HORIZONTAL, command=update_sbm)
scale_bouncer_speed_y.set(0)

# Button
button_run_scenario = tk.Button(win_root, text="Run Scenario", command=run_script)

# Pack everything together
canvas_blueprint.grid(row=0, column=0, sticky="n")

label_ground_height.grid(row=1, column=0, sticky="nw")
scale_ground_height.grid(row=1, column=0, sticky="ne")

label_ceiling_height.grid(row=2, column=0, sticky="nw")
scale_ceiling_height.grid(row=2, column=0, sticky="ne")

label_wall_left_width.grid(row=3, column=0, sticky="nw")
scale_wall_left_width.grid(row=3, column=0, sticky="ne")

label_wall_right_width.grid(row=4, column=0, sticky="nw")
scale_wall_right_width.grid(row=4, column=0, sticky="ne")

label_bouncer_x.grid(row=5, column=0, sticky="nw")
scale_bouncer_x.grid(row=5, column=0, sticky="ne")

label_bouncer_y.grid(row=6, column=0, sticky="nw")
scale_bouncer_y.grid(row=6, column=0, sticky="ne")

label_bouncer_width.grid(row=7, column=0, sticky="nw")
scale_bouncer_width.grid(row=7, column=0, sticky="ne")

label_bouncer_height.grid(row=8, column=0, sticky="nw")
scale_bouncer_height.grid(row=8, column=0, sticky="ne")

label_bouncer_speed_x.grid(row=9, column=0, sticky="nw")
scale_bouncer_speed_x.grid(row=9, column=0, sticky="ne")

label_bouncer_speed_y.grid(row=10, column=0, sticky="nw")
scale_bouncer_speed_y.grid(row=10, column=0, sticky="ne")


button_run_scenario.grid(row=11, column=0, sticky="ne", padx=5, pady=5)

# Start the main window
win_root.mainloop()
