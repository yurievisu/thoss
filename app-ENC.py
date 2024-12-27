import base64
import os
import sys
import tempfile
import subprocess
import shutil

def execute_code():
    temp_dir = None
    original_dir = os.getcwd()
    
    try:
        temp_dir = tempfile.mkdtemp()
        
        c_file = os.path.join(temp_dir, "module.c")
        with open(c_file, "wb") as f:
            f.write(c_code)
        
        setup_content = """
from setuptools import setup, Extension

ext = Extension(
    "module",
    sources=["module.c"],
    include_dirs=["/data/data/com.termux/files/usr/include/python3.12"],
    library_dirs=["/data/data/com.termux/files/usr/lib"],
    libraries=["python3.12"]
)

setup(
    name="module",
    ext_modules=[ext]
)
"""
        
        setup_file = os.path.join(temp_dir, "setup.py")
        with open(setup_file, "w") as f:
            f.write(setup_content)
        
        os.chdir(temp_dir)
        
        subprocess.check_call([sys.executable, "setup.py", "build_ext", "--inplace"])
        
        # Copy the .so file to current directory
        so_files = [f for f in os.listdir(temp_dir) if f.endswith('.so')]
        if so_files:
            so_file = so_files[0]
            target_path = os.path.join(original_dir, so_file)
            shutil.copy2(os.path.join(temp_dir, so_file), target_path)
            
            # Add current directory to Python path
            if original_dir not in sys.path:
                sys.path.insert(0, original_dir)
            
            import module
            return module
        else:
            print("Error: No compiled module found")
            return None
            
    except Exception as e:
        print(f"Error during execution: {str(e)}")
        return None
        
    finally:
        os.chdir(original_dir)
        if temp_dir and os.path.exists(temp_dir):
            try:
                shutil.rmtree(temp_dir)
            except:
                pass

module = execute_code()

if module is None:
    print("Failed to load module. Check the above error messages.")
else:
    print("Module loaded successfully!")

del execute_code