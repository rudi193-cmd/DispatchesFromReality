# LEDGER: SOIL-PHYS-001 // THE ARBITRARY SEED AND THE BOUNDED VOID

Revision 2, tidied 2026-11-06. Coordinates: relational, 1-indexed lines.

Every entry now carries one of three marks:

- **SOURCE**: what the cited work shows, as near its own terms as a line allows.
- **READING**: this ledger's interpretation. It may be good; no source above it derives it.
- **CHANGED**: what revision 1 said that this one doesn't, and why.

The header's "Willow/Kernel-1.0 Compatible" and "SHA256-GENESIS-INTENT" are
names, not anything Willow defines; they're kept as names. What the kernel
actually does is in Section 06.

## RECORD: GENESIS_STATE

| Line | Mark | Statement |
|---|---|---|
| 0001 | READING | True nullity is never observed: every physical "zero" turns out to be a ground state with something in it (Section 05). |
| 0002 | READING | The minimal non-trivial existence condition is the singleton container {0}. |
| 0003 | SOURCE | In von Neumann's construction the number 1 *is* {0} = {∅}: the set whose only member is the empty set. Its cardinality is 1 (von Neumann 1923). |
| 0004 | READING | The boundary makes the first bit; the container is the state. (Spencer-Brown 1969 takes "draw a distinction" as the primitive act, which is this line's nearest source.) |

## SECTION 01: THE CONSTANTS AND THE ARENA

**[01.01] Fundamental constants**

- SOURCE: The defining constants are c, ħ (via h), k_B and e, fixed exactly in the 2019 SI; G is measured (CODATA 2022). Dimensionless couplings such as α ≈ 1/137.036 are pure numbers no choice of units changes.
- SOURCE: Planck's radiation law, Verh. Dtsch. Phys. Ges. 2 (1900) 237, with the fuller paper in Ann. Phys. 4 (1901) 553. Planck units follow from c, ħ, G and k_B.
- SOURCE: Dirac, "The Cosmological Constants", Nature 139 (1937) 323: the large-number coincidences.
- READING: Natural units show only ratios carry physical meaning, so law has no external origin.
- CHANGED: Planck's 1900 result is in the Physical Society's proceedings; the Annalen paper is 1901.

**[01.02] Why 3 + 1**

- SOURCE: Einstein's field equations, Sitzungsber. Preuss. Akad. Wiss. (1915) 844.
- SOURCE: Ehrenfest, Proc. KNAW Amsterdam 20 (1917) 200: in n space dimensions, stable planetary orbits and stable atoms occur only for n = 3.
- SOURCE: Clean (sharp) wave propagation holds in odd spatial dimensions of at least 3 (Hadamard). Tegmark, Class. Quantum Grav. 14 (1997) L69, combines the arguments for 3 + 1.
- SOURCE: Kaluza, Sitzungsber. Preuss. Akad. Wiss. (1921) 966; Klein, Z. Phys. 37 (1926) 895: a fifth, compact dimension.
- CHANGED: "require exactly 3" becomes "single out 3, by stability": it's an argument from stability, not a derivation. Tegmark (1997) added as the source that makes the 3 + 1 case.

## SECTION 02: THE SEED AND ITS ANCHOR (N)

**[02.01] A non-zero offset**

- SOURCE: The universe holds more matter than antimatter: baryon-to-photon ratio η ≈ 6 × 10⁻¹⁰ (Planck collaboration 2018; Big Bang nucleosynthesis).
- SOURCE: Sakharov, JETP Lett. 5 (1967) 24: such an asymmetry can *arise* from symmetric beginnings if baryon number is violated, C and CP are violated, and there is a departure from thermal equilibrium.
- READING: A non-trivial offset N seeds the dynamics; reality doesn't sum to cancellation.
- CHANGED: Revision 1 called N "conserved" and cited Sakharov. Sakharov's first condition is that baryon number is *not* conserved: his paper is how the offset is made, not a conserved one. The 10⁻¹⁰ is the observed value, not Sakharov's.
- CHANGED: Wilson (1971, renormalization-group fixed points) removed here: it is about how theories change with scale, not about asymmetry. It is used at [03.02].

**[02.02] The origin is arbitrary**

- SOURCE: Leibniz-Clarke correspondence (1715-16): Leibniz argues space is relations among things, so a shift of the whole universe is no real change.
- SOURCE: Mach, *Die Mechanik in ihrer Entwickelung* (1883): inertia relative to the distant masses.
- SOURCE: Einstein's hole argument (1913-14) and its resolution (1915): in general relativity only coincidences between events are physical; coordinates are not.
- SOURCE: Weyl, Sitzungsber. Preuss. Akad. Wiss. (1918) 465, and Z. Phys. 56 (1929) 330: gauge invariance, the freedom to re-choose a local reference.
- READING: The axis N sits on is unobservable; only relational differences and holonomies are physical.

**[02.03] Choosing a vacuum**

- SOURCE: Nambu, Phys. Rev. 117 (1960) 648; Goldstone, Nuovo Cimento 19 (1961) 154; Anderson, Phys. Rev. 130 (1963) 439; Englert and Brout, Phys. Rev. Lett. 13 (1964) 321; Higgs, Phys. Rev. Lett. 13 (1964) 508; Guralnik, Hagen and Kibble (1964).
- SOURCE: A symmetric law can have many equivalent ground states; the system settling into one breaks the symmetry, and in gauge theories this gives the gauge bosons mass.
- READING: Selecting an arbitrary point N is that choice, and form follows from it.
- CHANGED: Anderson's paper is 1963. Nambu's symmetry-breaking paper is the 1960 Physical Review one on superconductivity. Guralnik, Hagen and Kibble added: they are the third 1964 paper.

## SECTION 03: RECURSIVE UNFOLDING

**[03.01] Rich structure from simple iteration**

- SOURCE: Julia, J. Math. Pures Appl. (1918); Fatou, Bull. Soc. Math. France (1919-20): iterating a rational map z ↦ f(z).
- SOURCE: Mandelbrot, *Les objets fractals* (1975) and *The Fractal Geometry of Nature* (1982). The Mandelbrot set is the set of c for which z ↦ z² + c stays bounded from z = 0.
- SOURCE: Feigenbaum, J. Stat. Phys. 19 (1978) 25: period-doubling routes to chaos share universal constants δ ≈ 4.669 and α ≈ 2.503.
- READING: A fixed local rule applied again and again from a minimal seed generates self-similar structure.
- CHANGED: *The Fractal Geometry of Nature* is 1982; 1975 is the French book.

**[03.02] Scale and dimension**

- SOURCE: Ambjørn, Jurkiewicz and Loll, Phys. Rev. Lett. 95 (2005) 171301: in causal dynamical triangulations, the spectral dimension (as a diffusing walker sees it) runs from about 4 at large scales to about 2 at the shortest.
- SOURCE: Wilson, Phys. Rev. B 4 (1971) 3174, 3184: the renormalization group and its fixed points.
- SOURCE: Wolfram, Rev. Mod. Phys. 55 (1983) 601: elementary cellular automata; Cook, Complex Systems 15 (2004) 1: Rule 110 is computationally universal.
- READING: Spacetime may be smooth and four-dimensional only at large scales.
- CHANGED: "a 2D fractal at Planck scale" becomes "spectral dimension near 2 at the shortest scales" (the paper measures the first). Rule 110's universality credited to Cook (2004).

## SECTION 04: GRAVITY AND ENTANGLEMENT

**[04.01] Gravity from thermodynamics**

- SOURCE: Jacobson, Phys. Rev. Lett. 75 (1995) 1260: Einstein's equation follows from δQ = T dS applied to local horizons, entropy proportional to area.
- SOURCE: Verlinde, JHEP 04 (2011) 029: gravity as an entropic force (a proposal, much debated).
- READING: Gravity is the large-scale statistics of underlying quantum degrees of freedom, not a separate medium.

**[04.02] Geometry and entanglement**

- SOURCE: Ryu and Takayanagi, Phys. Rev. Lett. 96 (2006) 181602: in holographic theories, the entanglement entropy of a boundary region equals the area of a minimal surface in the bulk, over 4G.
- SOURCE: Van Raamsdonk, Gen. Rel. Grav. 42 (2010) 2323: removing entanglement between two regions pulls the spacetime connecting them apart.
- SOURCE: Maldacena and Susskind, Fortschr. Phys. 61 (2013) 781: ER = EPR, a conjecture that entangled pairs are connected by (non-traversable) wormholes.
- READING: Connectivity of space is built from entanglement; tearing information tears space.
- CHANGED: "g_μν is directly proportional to entanglement" becomes "areas in the geometry measure entanglement entropy, in holographic settings". No source claims the metric is proportional to entanglement, and ER = EPR is marked a conjecture.

## SECTION 05: WHY NOT ABSOLUTE ZERO

**[05.01] Nature's zeros are never empty**

- SOURCE: A quantum oscillator's lowest energy is E₀ = ½ħω, not zero (quantum mechanics, 1925-26; Planck's 1911 second theory first had it).
- SOURCE: Casimir, Proc. KNAW 51 (1948) 793: two uncharged plates attract, a measurable effect of vacuum modes.
- SOURCE: Nernst's heat theorem (1906), and its unattainability form (1912): no finite process reaches T = 0.
- SOURCE: Penrose, Phys. Rev. Lett. 14 (1965) 57: under general conditions, gravitational collapse ends in a singularity; general relativity's predictions fail there.
- READING: Each of these is a place where "zero" is a ground state or a breakdown, never an observed emptiness.

**[05.02] Zero in mathematics**

- SOURCE: von Neumann, Acta Sci. Math. (Szeged) 1 (1923) 199: 0 = ∅, 1 = {∅} = {0}, 2 = {0, 1}, and on.
- SOURCE: Spencer-Brown, *Laws of Form* (1969): the calculus starts from one act, drawing a distinction.

**[05.03] The synthesis: {(0)}** (all READING)

- { }, the boundary: horizon, causal patch, container.
- (0), the arbitrary ground coordinate, the relational origin.
- {(0)}, the unit, 1: in von Neumann's terms literally so, and here the non-zero root everything else is built from.

## SECTION 06: THE SAME SHAPE IN MODELS AND IN WILLOW

**[06.01] Representations converge**

- SOURCE: Shannon, Bell Syst. Tech. J. 27 (1948) 379; Solomonoff, Information and Control 7 (1964) 1: information and induction as compression.
- SOURCE: Huh, Cheung, Wang and Isola, ICML (2024), "The Platonic Representation Hypothesis": evidence that larger models' representations grow more alike across architectures and data types, and the hypothesis that they converge on a shared model of reality.
- CHANGED: "converge onto the same geometric representation of physics" becomes the paper's own claim, a convergence of representations, stated as a hypothesis. Named products (Grok, Gemini, GPT) dropped: the paper doesn't test them by name.

**[06.02] What Willow's kernel does** (checked against `kernel.py`, 2026-11-06)

- SOURCE: Every passage the kernel serves carries its file and line. It serves a passage only when the passage holds half a question's content words; when none does, it serves nothing and says so. An empty answer is a refusal, not an invented one.
- SOURCE: Its record is a hash chain: each row holds the hash of the one before, `kernel.py verify` checks the whole chain, and rows are only ever appended.
- SOURCE: The chain's root is a zero: `GENESIS = "0" * 64` (`kernel.py`, line 79), the `prev` of the first row. The first real row is the box's boot, and it is numbered 0 (`"n": len(rows)`): the record counts rows from zero, while the passages it serves cite their files' lines from 1, as this ledger's coordinates do.
- READING: That is {(0)} in code: a literal zero that is never itself a row, held inside the first boundary the record draws.
- CHANGED: Revision 1 said "an immutable, non-zero root node" and "deletion is an appended tombstone". The root is the zero hash, and the kernel has no delete and no tombstone: nothing in its record is ever removed, rather than removed by an appended row.
