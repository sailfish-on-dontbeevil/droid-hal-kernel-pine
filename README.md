# droid-hal-kernel
Mainline kernel packaging for the PinePhone

## Upstream kernel

Upstream kernel can be found here: https://gitlab.com/pine64-org/linux
Default branch: `pine64-kernel-5.6.y`

## Downstream kernel

We experiment with different patches here: https://github.com/sailfish-on-dontbeevil/linux
Default branch: `pine64-kernel-5.6.y-sailfishos`

## Building kernel

Execute these steps on the repo of upstreamed kernel or use the downstream version with additional patches (experimental).

1. Set arm64 as architecture: `export ARCH=arm64`.
2. Enable cross-compiling: `export CROSS_COMPILE=aarch64-linux-gnu-`.
3. Pick a local version name, can be anything: `export LOCALVERSION=-sfos`.
4. Clean start: `make clean`.
5. Copy the config file from this repo to the default config directory: `arch/arm64/configs/config-sailfishos-allwinner.aarch64`. 
6. Build a full config using: `make defconfig KBUILD_DEFCONFIG=config-sailfishos-allwinner.aarch64`.
7. Build the kernel Image, modules and device tree files: `make -j4 Image modules dtbs`.
8. Install the kernel modules to a given path which can be copied over to the `/lib/modules` directory on the device: `make modules_install INSTALL_MOD_PATH=../linux_modules/`
