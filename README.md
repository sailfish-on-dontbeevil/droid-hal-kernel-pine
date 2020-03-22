# droid-hal-kernel
Mainline kernel packaging for the PinePhone

## Upstream kernel

Upstream kernel can be found here: https://gitlab.com/pine64-org/linux
Default branch: `pine64-kernel-5.5.y`

## Downstream kernel

We experiment with different patches here: https://github.com/sailfish-on-dontbeevil/linux
Default branch: `pine64-kernel-5.5.y-sailfishos`

## Building kernel

Execute these steps on the repo of upstreamed kernel or use the downstream version with additional patches (experimental).

1. Set arm64 as architecture: `export ARCH=arm64`
2. Enable cross-compiling: `export CROSS_COMPILE=aarch64-linux-gnu-`
3. Pick a local version name, can be anything: `export LOCALVERSION=-nemo`
4. Clean start: `make clean`
5. Create `.config` using the defconfig from this repo: `make defconfig KBUILD_DEFCONFIG=config-sailfishos-allwinner.aarch64`
6. Build the kernel Image, modules and device tree files: `make -j4 Image modules dtbs`
