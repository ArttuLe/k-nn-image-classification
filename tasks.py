from invoke import task
import os

source_dir = os.path.join(os.path.dirname(os.path.realpath(__file__)), "src")


@task
def start(c):

    main_path = os.path.join(source_dir, "main.py")
    c.run(f"python {main_path}")