import subprocess
import sys

def install_ansible():
    """Install Ansible using pip."""
    try:
        subprocess.check_call([sys.executable, "-m", "pip", "install", "ansible"])
        print("Ansible installed successfully.")
    except subprocess.CalledProcessError as e:
        print(f"Failed to install Ansible: {e}")
        sys.exit(1)

def check_ansible_version():
    """Check the installed version of Ansible."""
    try:
        result = subprocess.run(["ansible", "--version"], capture_output=True, text=True)
        print("Ansible Version:")
        print(result.stdout)
    except FileNotFoundError:
        print("Ansible is not installed.")
        sys.exit(1)

def print_ansible_info():
    """Print basic information about Ansible."""
    info = """
    🌟 Ansible - Simple, Powerful IT Automation

    Ansible is an open-source, radically simple IT automation system. It helps manage configuration, application deployment, cloud provisioning, network automation, and orchestrates multi-node environments. With Ansible, complex changes like zero-downtime rolling updates become easy!

    Explore more about Ansible on the Official Website: https://ansible.com
    """
    print(info)

if __name__ == "__main__":
    install_ansible()
    check_ansible_version()
    print_ansible_info()