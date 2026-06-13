# Installation Guide

## Requirements
To run this verification workspace, you will need:
- **Python 3.x**
- **NuSMV** (Version 2.7.1 or higher)

## 1. Python Setup
We recommend using a virtual environment for the Python tools.
```bash
python3 -m venv .venv
source .venv/bin/activate
```

## 2. NuSMV Installation
### For Linux and Windows:
You can download pre-compiled binaries directly from the [NuSMV Download Page](https://nusmv.fbk.eu/NuSMV/download/getting_v2.html).

### For macOS (Apple Silicon / ARM64):
Because the distributed macOS binaries are compiled for Intel (x86_64) and rely on MacPorts libraries, running them directly via Rosetta 2 often results in missing library errors (`libedit`, `libgmp`, `libxml2`). 

The most reliable solution is to compile NuSMV natively for Apple Silicon:

1. **Install Build Dependencies** (via Homebrew):
   ```bash
   brew install pkgconfig cmake flex bison gmp
   ```

2. **Download NuSMV Source**:
   Download the source tarball (e.g. `NuSMV-2.7.1.tar.gz`) from the NuSMV website and extract it.

3. **Install Meson & Ninja** (in your Python environment):
   ```bash
   pip install meson ninja
   ```

4. **Compile NuSMV**:
   Export your Homebrew paths and compile the binary:
   ```bash
   export PATH="/opt/homebrew/opt/flex/bin:/opt/homebrew/opt/bison/bin:/opt/homebrew/bin:$PATH"
   export LDFLAGS="-L/opt/homebrew/opt/flex/lib -L/opt/homebrew/opt/bison/lib"
   export CPPFLAGS="-I/opt/homebrew/opt/flex/include"
   export PKG_CONFIG_PATH="/opt/homebrew/lib/pkgconfig"
   
   cd NuSMV-2.7.1
   meson setup build
   meson compile -C build
   ```

5. **Run**:
   The native binary will be located in `NuSMV-2.7.1/build/NuSMV`. Add this to your system path or execute it directly on your generated SMV models!
