import tkinter as tk
from tkinter import messagebox, filedialog
import matplotlib.pyplot as plt
import matplotlib.colors as mcolors
from erotima1 import Factory
from erotima2 import Solution
import os
import logging

logging.getLogger("matplotlib").setLevel(logging.WARNING)
logging.getLogger("PIL").setLevel(logging.WARNING)


class JobShopVisualization:
    def __init__(self, root):
        self.root = root
        self.root.title("Job Shop Scheduling")
        self.root.geometry("400x300")
        self.root.config(bg="#F2F2F2")

        self.instruction_label = tk.Label(
            root,
            text="Enter the path to the job-shop problem file (.txt):",
            font=("Arial", 12),
            bg="#F2F2F2",
        )
        self.instruction_label.pack(pady=10)

        self.path_entry = tk.Entry(root, width=40, font=("Arial", 12))
        self.path_entry.pack(pady=10)

        self.solve_button = tk.Button(
            root,
            text="ΕΠΙΛΥΣΗ",
            command=self.load_file,
            width=20,
            height=2,
            font=("Arial", 14),
            bg="#4CAF50",
            fg="white",
            relief="solid",
            bd=2,
        )
        self.solve_button.pack(pady=20)

        self.save_button = tk.Button(
            root,
            text="ΑΠΟΘΥΚΕΥΣΗ",
            command=self.save_chart,
            width=20,
            height=2,
            font=("Arial", 14),
            bg="#FF5722",
            fg="white",
            relief="solid",
            bd=2,
        )
        self.save_button.pack(pady=10)

        self.factory = None
        self.solution = None
        self.figure = None

    def load_file(self):
        file_path = self.path_entry.get().strip()

        if not os.path.isfile(file_path):
            messagebox.showerror("Error", "Couldn't make a diagram. Invalid file path.")
            return

        try:
            self.factory = Factory.from_file(file_path)
            self.solution = Solution(self.factory)
            self.solution.eet()
            self.plot_gantt_chart()
        except Exception as e:
            messagebox.showerror("Error", f"Couldn't make a diagram. Error: {e}")

    def plot_gantt_chart(self):
        fig, ax = plt.subplots(figsize=(10, 6))

        jobs = self.solution.factory.jobs
        machine_names = sorted(set(op.machine for job in jobs for op in job.operations))
        machine_index = {machine: i for i, machine in enumerate(machine_names)}

        colors = list(mcolors.TABLEAU_COLORS.values())

        for job in jobs:
            for i, op in enumerate(job.operations):
                start_time, end_time, machine = self.solution.schedule[(job.job_id, i)]
                machine_row = machine_index[machine]
                ax.barh(
                    machine_row,
                    end_time - start_time,
                    left=start_time,
                    color=colors[job.job_id % len(colors)],
                    edgecolor="black",
                    height=0.6,
                )

        ax.set_xlabel("Time", fontsize=14)
        ax.set_ylabel("Machines", fontsize=14)
        ax.set_title("Job Shop Scheduling Gnatt Chart", fontsize=16)
        ax.set_yticks(range(len(machine_names)))
        ax.set_yticklabels(machine_names, fontsize=12)
        ax.grid(True, which="both", linestyle="--", linewidth=0.5, color="#999999")

        self.figure = fig
        plt.show()

    def save_chart(self):
        if not self.figure:
            messagebox.showerror(
                "Error", "No Gantt chart to save. Please load a problem first."
            )
            return

        file_path = filedialog.asksaveasfilename(
            defaultextension=".png", filetypes=[("PNG files", "*.png")]
        )

        if not file_path:
            return

        try:
            self.figure.savefig(file_path)
            messagebox.showinfo("Success", f"Gantt chart saved as {file_path}")
        except Exception as e:
            messagebox.showerror("Error", f"Could not save the Gantt chart. Error: {e}")


if __name__ == "__main__":
    root = tk.Tk()
    app = JobShopVisualization(root)
    root.mainloop()
