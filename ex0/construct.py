import os
import sys


def check_virtual_environment() -> None:
    venv_path = os.environ.get("VIRTUAL_ENV")
    is_in_venv = venv_path is not None or sys.prefix != sys.base_prefix

    current_python: str = sys.executable

    if not is_in_venv:
        print("MATRIX STATUS: You're still plugged in")
        print(f"Current Python: {current_python}")
        print("Virtual Environment: None detected")
        print("WARNING: You're in the global environment!")
        print("The machines can see everything you install.")
        print("To enter the construct, run:")
        print("python -m venv matrix_env")
        print("source matrix_env/bin/activate # On Unix")
        print(r"matrix_env\Scripts\activate # On Windows")
        print("Then run this program again.")
    else:
        env_path: str = venv_path if venv_path else sys.prefix
        env_name: str = os.path.basename(env_path)
        site_packages: str = (
            f"{env_path}/lib/python{sys.version_info.major}."
            f"{sys.version_info.minor}/site-packages"
        )

        print("MATRIX STATUS: Welcome to the construct")
        print(f"Current Python: {current_python}")
        print(f"Virtual Environment: {env_name}")
        print(f"Environment Path: {env_path}")
        print("SUCCESS: You're in an isolated environment!")
        print("Safe to install packages without affecting")
        print("the global system.")
        print("Package installation path:")
        print(site_packages)


def main() -> None:
    check_virtual_environment()


if __name__ == "__main__":
    main()
