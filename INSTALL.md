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

### Option A: Pre-compiled Binaries (Recommended for Windows / x86_64 Linux)
You can download pre-compiled binaries directly from the [NuSMV Download Page](https://nusmv.fbk.eu/NuSMV/download/getting_v2.html). Simply extract the archive and add the `bin/` directory to your system path.

### Option B: Compiling from Source (Required for Apple Silicon / Custom Environments)
If the pre-compiled binaries are incompatible with your system architecture (such as macOS Apple Silicon), you will need to compile NuSMV natively from source.

1. **Install Build Dependencies**:
   You must install the following C/C++ build tools using your system's package manager (e.g., `apt`, `brew`, `pacman`):
   - `pkg-config`, `cmake`, `flex`, `bison`, `gmp`

   *Example for macOS (Homebrew):* `brew install pkgconfig cmake flex bison gmp`
   *Example for Ubuntu/Debian:* `sudo apt-get install pkg-config cmake flex bison libgmp-dev`

2. **Install Meson & Ninja**:
   NuSMV utilizes the Meson build system. Install it within your Python environment:
   ```bash
   pip install meson ninja
   ```

3. **Download NuSMV Source**:
   Download the source tarball (e.g., `NuSMV-2.7.1.tar.gz`) from the NuSMV website and extract it:
   ```bash
   tar -xzf NuSMV-2.7.1.tar.gz
   cd NuSMV-2.7.1
   ```

4. **Compile NuSMV**:
   *Note: If your system installs packages in non-standard directories (like Homebrew on Apple Silicon in `/opt/homebrew`), ensure you export the necessary `PATH`, `LDFLAGS`, `CPPFLAGS`, and `PKG_CONFIG_PATH` variables before running the build commands.*

   ```bash
   meson setup build
   meson compile -C build
   ```

5. **Run**:
   Upon a successful build, the native executable will be generated at `build/NuSMV`. Add this to your system path or execute it directly against your generated `.smv` models!
