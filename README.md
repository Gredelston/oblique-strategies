# Oblique Strategies

Since 1975, Brian Eno and Peter Schmidt have produced a deck of cards dubbed
"Oblique Strategies". Each card offers an unconventional way of approaching a
creative problem.

These cards have been released in a variety of editions, and more recently for a
variety of software platforms. This repository offers a command-line interface.

I grabbed the list of strategies from
https://matt-rickard.com/list-of-all-oblique-strategies. I am not positive that 
this list is canonical or endorsed by Eno and Schmidt, but it was the most
accurate-looking source I could find. Since Eno has a net worth of $60,000,000
and Peter Schmidt is long dead, I am more concerned about the authenticity of
the strategies than I am about the marginal loss to their profits. Maybe someday
I'll get my hands on a real deck to offer a more authentic option.

# Usage

`eno.py` is an executable. Run it to get a strategy.

Avoid the temptation to reroll. The only way the strategy can change your
perspective is if you treat it seriously (or playfully).

Peter Schmidt deserves credit too, but `eno` is pleasantly short to type.

# Installation

I recommend setting up a link to the `eno.py` executable somewhere on your
`PATH`:

1.  Clone this repo anywhere on your system.

```bash
% cd path/to/some/dir
% git clone git@github.com:Gredelston/oblique-strategies.git
```

2.  Create a symlink from somewhere on your `PATH` (e.g. `~/.local/bin` or
`/usr/bin`). I named mine `eno`.

WARNING: Make sure it's a symbolic link (`ln -s`), not a hard link!

```bash
% cd /usr/bin
% ln -s path/to/some/dir/oblique-strategies/eno.txt eno
```

3.  Make sure you can run the command from an arbitrary working directory.

```bash
% cd ~
% eno
Courage!
```

