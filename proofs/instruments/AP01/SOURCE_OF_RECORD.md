# AP01 — DIVERGED, no source of record

**Checked 7 September 2026** by the paragraph-level test of record. The closest
candidate is `AP01_The_Actualization_State.docx` (found in Formatted), and it is **not** the published
text: 72 paragraph(s) in the source are absent from the
published PDF, and 2 published sentence(s) are absent from
the source.

**Until a matching source is produced, the published PDF's text is the source for
AP01, and the AP30 republish procedure is not available to it.** No file is
copied into this folder, so nothing here can be harvested by mistake.

| | |
|---|---|
| Published PDF | `/AP01_The_Actualization_State.pdf` |
| sha256 | `39c86fb7863b63b7accd987c79526ef95d1f9a9c7d473a8441311dde61326505` |
| Closest candidate | `AP01_The_Actualization_State.docx` (Formatted) — NOT of record |

## In the source, absent from the published paper

- A qubit S with pointer basis O = {|0⟩⟨0|, |1⟩⟨1|} is prepared in the pure pointer state |0⟩. The environment consists of N = 1000 fragments, each independently recording that the system is in sector |0⟩.
- A four-level system S with pointer basis O = {Π1, Π2, Π3, Π4} is prepared in an equal superposition and then fully dephased by coupling to a single environmental fragment E.
- Definition D1. A physically realizable coarse-graining O is a finite set of mutually orthogonal projectors O = {Πi} satisfying all of the following:
- The critical point: O is not your choice. It is nature's choice. The physics of the interaction determines what gets measured. You do not pick the basis. The coupling picks it for you.
- Definition D2. Given a density matrix ρ on Hs, the dephasing map relative to O is
- ΔO does not measure ignorance. It enforces projection onto the record algebra, isolating entropy attributable to irreversible branching rather than lack of knowledge.
- Define the dephasing map relative to this record algebra: ΔO(ρ) ≡ Σi Πi ρ Πi.
- where Seff is the effective record entropy defined below and dO is the total record-algebra dimension.
- where H is the Shannon entropy and N = |O| is the number of record sectors.
- Let O = {Πi} be the physically realizable record algebra, with total record-algebra dimension dO ≡ Σi rank(Πi).
- The maximum effective entropy achievable for a state confined to O is Seff^max = log dO (uniform distribution over the record algebra). Therefore AS(ρ; O) ∈ [0, 1] for all admissible ρ.
- The denominator log dO is fixed by the record algebra, not by ρ. The normalization is independent of the state. AS values for different states are directly comparable when computed against the same O.
- When O changes, you change the denominator. The kill switch F0 (D5) is what enforces consistency across choices of O.
- AS is well defined whenever O is identified by D1. Where O is ambiguous - where two co-admissible coarse-grainings exist and yield different AS values beyond tolerance - Kill Switch F0 (D5) fires. The framework dies cleanly.
- Two qubits S1, S2. Pointer basis O = {|00⟩⟨00|, |01⟩⟨01|, |10⟩⟨10|, |11⟩⟨11|}. Initial state |ψ⟩ = (|00⟩ + |11⟩)/√2 (Bell state). Reduced state on the joint system: ρ = |ψ⟩⟨ψ|.
- After dephasing in O: ΔO(ρ) = 1⁄2|00⟩⟨00| + 1⁄2|11⟩⟨11|. Sector weights: p00 = 1⁄2, p01 = 0, p10 = 0, p11 = 1⁄2.
- Let O1 and O2 be two physically realizable coarse-grainings selected by the same system-environment coupling. Both must satisfy D1.
- for all admissible pairs (Ok, Ok′), where δexp is the experimental tolerance set by the precision of the apparatus.
- where CO is any coherence monotone that vanishes on ΔO(ρ). Equivalently, off-diagonal terms in the O-basis decay monotonically.
- Proof. By condition (2), ΔO ∘ Et = Et ∘ ΔO, so the evolution commutes with dephasing. Therefore the diagonal elements evolve autonomously: there exists a linear map M(t) such that p(t) = M(t) p(0).
- The map is stochastic because Et is trace-preserving: Σi pi(t) = 1 for all t.
- Unitality (condition 3) means Et(I/d) = I/d. Applying ΔO to both sides and using condition (2):
- Let the total Hilbert space factor as H = Hs ⊗ He, with joint state evolving unitarily under Hse.
- for some state ρcoh satisfying ΔO(ρcoh) ≠ ρcoh, and for fixed operational tolerance ε > 0.
- Kε(O) is the viability kernel of coherence under admissible control. States outside Kε(O) are operationally irreversible with respect to O.
- State space X: the convex set of density operators on Hs, equipped with the trace-norm topology.
- Viability kernel Viab(R): exactly Kε(O) - the set of states for which there exists an admissible control strategy that maintains coherence-recoverability indefinitely.
- No-return surface Σh: the boundary ∂Kε(O), separating recoverable from irreversibly decohered states.
- The operational no-return surface relative to O is the boundary ∂Kε(O).
- Linear CPTP evolution preserves convex mixtures: E(Σi pi ρi) = Σi pi E(ρi). Any linear CPTP map that acts identically on each component preserves the mixture structure and cannot yield single-outcome definiteness in individual realizations.
- where DO is the standard pointer-dephasing channel and AO is a selection channel responsible for definiteness.
- (S0) Activation Condition. AO ≈ 0 until the decoherence condition (D13) holds within tolerance ε. Selection activates only after branches are operationally distinct.
- (S1) Record-algebra locality. AO(ρs) = AO(ΔO(ρs)). Selection never creates interference.
- (S2) Sector fixed points. AO(Πi ρs Πi) = 0 for all i. Once a branch is realized, dynamics cease.
- Setup. Let the system be a qubit with pointer basis O = {|0⟩⟨0|, |1⟩⟨1|}. After decoherence is complete, the reduced state is ρs = diag(p, 1-p), with p ∈ [0, 1]. The selection channel acts on the single free parameter p via the Itô stochastic differential equation
- The selection postulate instead acts on whatever record algebra O is selected by the system-environment coupling.
- Prepare a system with two physically realizable coarse-grainings O1 and O2. Compute AS(ρ; O1) and AS(ρ; O2).
- Setup. Systems where the environment-selected pointer algebra O is not position. Concrete examples: superconducting qubits (e.g., flux-tunable transmons), cavity QED (e.g., circuit QED, Schuster et al. 2007), collective spin ensembles.
- Dephasing map, ΔO. The map ΔO(ρ) ≡ Σi Πi ρ Πi that removes quantum interference between record sectors while preserving classical probabilities. Defined in D2 (A2.2).
- In these regimes, AS(ρ; O) remains well-defined. ASh(D) ceases to be a faithful representation.

## In the published paper, absent from the source

- The map is stochastic because t is trace-preserving: Σi pi(t) = 1 for all t.
- Linear CPTP evolution preserves convex mixtures: (Σi pi ρi) = Σi pi (ρi).

*Each item is either a pre-publication draft difference, which is nothing, or a paragraph G edited after publication, which becomes a dated note. That is G's reading to make.*
