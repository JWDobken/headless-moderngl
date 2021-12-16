# Headless-moderngl

Headless 3D rendering with Python and ModernGL.

> :grimacing: **Work in process**: not yet a working solution.

## Problem description

In an attempt to make 3D renders of the obj file `rebar.obj`; I ran into so many issues that I've decided to narrow this problem down to a single script that can run in a docker container.

## Tools

- [Moderngl](https://moderngl.readthedocs.io)

to consider
- [PyWavefront](https://github.com/pywavefront/PyWavefront): Parser of obj files
- [Moderngl-window](https://moderngl-window.readthedocs.io/en/latest/index.html#) ??

## Run the container

I am building and running containers with [`nerdctl`](https://github.com/containerd/nerdctl), you can simply replace `nerdctl` with `docker`.

Build the container:

```cmd
nerdctl build -t moderngl_obj .
```

Run container with an interactive shell with the `src` directory mounted as a volume:

```cmd
nerdctl run -w /src -v "${PWD}"/src:/src --rm -i -t moderngl_obj bash
```

and run:

```
python render.py
```

Check these libraries exist:

```cmd
# ls /usr/lib/x86_64-linux-gnu/libGL.so.1 -l
lrwxrwxrwx 1 root root 14 Aug 10  2018 /usr/lib/x86_64-linux-gnu/libGL.so.1 -> libGL.so.1.7.0
# ls /usr/lib/x86_64-linux-gnu/libX11.so.6 -l
lrwxrwxrwx 1 root root 15 Oct  9  2018 /usr/lib/x86_64-linux-gnu/libX11.so.6 -> libX11.so.6.3.0
# ls /usr/lib/x86_64-linux-gnu/libEGL.so.1 -l
lrwxrwxrwx 1 root root 15 Aug 10  2018 /usr/lib/x86_64-linux-gnu/libEGL.so.1 -> libEGL.so.1.1.0
```
