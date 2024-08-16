# Action potential models

This is a list of published action potential models.
Specifically, detailed models (not reduced or propagation focussed) without stochastics (no release units).

### Key
Models are listed as year, followed by first author (or multiple if shared first authorship).
Model names / nicknames (e.g. LR1) are provided separately under "known as".
Ordering is year, then first author alphabetically.

**Type**
- A Atrial
- V Ventricular
- P Purkinje
- S SA node
- N AV node
- e embryonic stem cell
- i induced pluripotent stem cell
- d Developing cardiomyocyte, neonatal, embryonic

**Species**
- C Canine
- F Frog
- G Guinea pig
- H Human
- K chicken
- L Rat
- M Mouse
- P Pig
- R Rabbit
- m Mammal

**Preparation**
- f recordings in fibres or other multicellular preparations, instead of isolated cells

**Base**
A tentative "base" model is indicated.
This can be a clear ancestor - with many equations and parameters inherited - but also a more vague "inspiration".

**Code**
Where possible, indicate whether code is
- "Original": used by the authors when writing the publication
- "Official": an author-sanctioned translation to code, e.g. a CellML created during publishing
- "Updated": created by authors or others, with slight modifications or fixes to original code

### Inclusion criteria
Models are included if they represent the dynamics of a single cell or, for early models, of a small, space-clamped, multicellular preparation.
Models are omitted if they contain spatial propagation, either in larger tissues or by dividing the cell into a multitude of "calcium release units".

Whether or not a modification counts as a "model" is entirely subjective.
No strict criteria are used here, just try to make it useful.

### Sources
Some papers with model lists or model comparison:
- [Noble, Garny, Noble (2012) How the Hodgkin-Huxley equations inspired the Cardiac Physiome Project](https://doi.org/10.1113/jphysiol.2011.224238)
- [Amuzescu, Airini et al., Radu (2021) Evolution of mathematical models of cardiomyocyte electrophysiology](https://doi.org/10.1016/j.mbs.2021.108567)
- [Wilders (2007) Computer modelling of the sinoatrial node](https://doi.org/10.1007/s11517-006-0127-0)
- [Davies, Wang et al., Polonchuk (2016) Recent developments in using mechanistic cardiac modelling for drug safety evaluation](https://doi.org/10.1016/j.drudis.2016.02.003)
- [Ricci, Bartolucci, Severi (2022) The virtual sinoatrial node: What did computational models tell us about cardiac pacemaking?](https://doi.org/10.1016/j.pbiomolbio.2022.10.008)

Online model lists:
- [InSilicoCardiotox  Human Action Potential Models Repository](https://www.cs.ox.ac.uk/insilicocardiotox/model-repository)
- [Physiome model repository category "Electrophysiology"](https://models.physiomeproject.org/electrophysiology)

A number of software packages are referenced, because they contain models.
- Oxsoft Heart (1984-1999) was a DOS program released by Denis Noble and his group, and contained Noble-group models in that period. It was succeded by COR (and then OpenCOR) and CellML. The Oxsoft models were all converted to CellML.
- LabHEART (2001-2022) was a Windows program built around Bers et al. models. It is archived at https://web.archive.org/web/20220615151709/http://www.labheart.org/
- simBio (2005-2008) was a Windows program released by Sarai et al., and contained the "Kyoto model" family. It can still be downloaded from https://sourceforge.net/projects/simbio/files/simBio. It was succeded (I think) by e-Heart.
- e-Heart (2014-present) is a Windows (visual basic) program released by Noma's group(?) it can be downloaded from http://www.eheartsim.com.

### Not included in the main list
Some reductions and propagation models:
- Fitzugh 1961 reduces HH to a "Bonhoeffer-Van der Pol" model
- Nagumo 1962 makes Fitzhugh 1961 suitable for propagation
- Morris & Lecar 1981 create a reduced HH-like model of a Ca-driven AP
- Winfree 1991 provides a great overview of spiral wave models, including Belousov-Zhabotinsky
- Varghese 1993 reduces DiFrancesco 1985
- Karma 1993 reduces Noble 1962 and adapts for propagation
- Aliev & Panfilov 1996
- Endresen 1997 adapts Morris-Lecar for rabbit SAN
- Fenton & Karma 1998 derive an FN-like model
- Bernus 2002 reduces Priebe 1998
- Fenton 2002 builds on Fenton 1998
- Garny et al. 2003 implemented "a variety" of one-dimensional SAN models
- Mitchell & Schaeffer 2003
- Biktasheva 2006 reduces Courtemanche 1998
- Cherry 2006 uses Fenton 2002
- Simitev 2006 adapted Biktasheva 2006
- Ten Tusscher 2006b reduces Ten Tusscher 2006
- Bueno-Orovio 2008 adds an equation to Fenton 1998
- Tran 2009 reduces Luo 1991
- Aslanidi 2012 applied the Courtemanche and Nygren models on realistic anatomy
- Balakrishnan 2015 develop a reduced whole heart model
- Gray & Pathmanathan 2016 create a minimal but fully parametrisable AP model
- Corrado 2017, Carrado & Niederer 2016, Corrado 2018
- ...

Some CaRU stochastic/spatial models:
- Rice et al 1999 used stochastic CaRUs (called FRUs in the paper)
- Greenstein 2002 builds on Rice 1999 and Winslow 1999
- Lovell et al 2004 created a SAN model with a spatial gradient of heterogeneity
- Tanskanen 2005 builds on Greenstein 2002
- Greenstein 2006 builds on Greenstein 2002
- Flaim et al 2006 modified Greenstein 2006
- Stern 2014 built a sparking SAN model based on Maltsev 2009
- Voigt 2014 built a CaRU model based on Voigt 2013
- Sutanto 2018 adapted the Voigt 2014 model
- Maltsev 2022 build on Stern 2014

## 1962 Noble mPf
Base: HH1952
| [Paper](https://doi.org/10.1113/jphysiol.1962.sp006849) Noble (1962) A Modification of the Hodgkin-Huxley Equations Applicable to Purkinje Fibre Action and Pacemaker Potentials

## 1966 Krause mVf
Krause, Antoni, Fleckenstein (1966) An electronic model for the formation of local and transmitted stimuli on the myocardium fibers based upon variable current-voltage characteristics for potassium and sodium ions

Note: In german. Can't find it online

## 1975 McAllister mPf
Base: [Noble 1962](#1962-noble-mpf)
| [Paper](https://doi.org/10.1113/jphysiol.1975.sp011080) McAllister, Noble, Tsien (1975) Reconstruction of the electrical activity of cardiac Purkinje fibres

Known as: McAllister-Noble-Tsien (MNT)

## 1977 Beeler mVf
Base: [McAllister 1975](#1975-mcallister-hpf)
| [In Myokit repo](https://github.com/myokit/models/blob/main/c/beeler-1977.mmt)
| [Paper](https://doi.org/10.1113/jphysiol.1977.sp011853) Beeler, Reuter (1977) Reconstruction of the action potential of ventricular myocardial fibres

Known as: Beeler-Reuter (BR)

Modifications:
- Adds INa j gate based on work w. Haas
- ...

## 1980 Yanagihara RSf
Base: Mixed
| [Paper](https://doi.org/10.2170/jjphysiol.30.841) Yanagihara, Noma, Irisawa (1980) Reconstruction of sino-atrial node pacemaker potential based on the voltage clamp experiments

## 1982 Bristow RSf
Base: [McAllister 1975](#1975-mcallister-hpf)
| [Paper](https://doi.org/10.1152/ajpheart.1982.243.2.h207) Bristow, Clark (1982) A mathematical model of primary pacemaking cell in SA node of the heart

Known as: Bristow-Clark

## 1982 Irisawa RSf
Base: [Yanagihara 1980](#1980-yanagihara-msf)
| [Chapter](https://doi.org/10.1007/978-94-009-7535-4_4) Irisawa, Noma (1982) Pacemaker mechanisms of rabbit sinoatrial node cells, in: Bouman, Jongsma (Eds.), Cardiac Rate and Rhythm: Physiological, Morphological, and Developmental Aspects

Known as: Irisawa-Noma

## 1984 Noble mSf
Base: [DiFrancesco 1985](#1985-difrancesco-mpf)
| [Paper](https://doi.org/10.1098/rspb.1984.0065) Noble, Noble (1984) A model of sino-atrial node electrical activity based on a modification of the DiFrancesco-Noble 1984 equations

Known as: Noble-Noble model

Note: This is an adaptation of the DiFrancesco 1985 model, but was published earlier. It cites DiFrancesco 1985 as "1984 (in the press)".

## 1985 DiFrancesco mPf
Base: [McAllister 1975](#1975-mcallister-hpf)
| [Paper](https://doi.org/10.1098/rstb.1985.0001) DiFrancesco, Noble (1985) A Model of the Cardiac Electrical Activity Incorporating Ionic Pumps and Concentration Changes

Known as: DiFrancesco-Noble model

Bits:
- INaK new formulation

## 1985 Reiner RSf
Base: [Bristow 1982](#1982-bristow-rsf)
| | [Paper](https://doi.org/10.1152/ajpheart.1985.249.6.h1143) Reiner, Antzelevitch (1985) Phase resetting and annihilation in a mathematical model of sinus node

Known as: Reiner-Antzelevitch

## 1987 Drouhard mV
Base: [Beeler 1977](#1977-beeler-mvf)
| [Paper](https://doi.org/10.1016/0010-4809(87)90048-6) Drouhard, Roberge (1987) Revised formulation of the Hodgkin-Huxley representation of the sodium current in cardiac cells

Known as: Drouhard-Roberge, BRDR

Modifications:
- Remove INa j gate again

## 1987 Hilgemann RAf
Base: [DiFrancesco 1985](#1985-difrancesco-mpf)
| [Paper](https://doi.org/10.1098/rspb.1987.0015) Hilgemann, Noble (1987) Excitation-contraction coupling and extracellular calcium transients in rabbit atrium; reconstruction of basic cellular mechanisms

## 1987 Murphey RSf
Chapter: Murphey, Clark (1987) Parasympathetic control of the SA node cell in rabbit heart; a model. In: Activation, Metabolism and Perfusion of the Heart, eds Sideman, Beyar

## 1989 Noble mS
Base: [Noble 1984](#1984-noble-mSf)
| Chapter: "DiFrancesco, Noble, Denyer (1989) Ionic Mechanisms in Normal and Abnormal Cardiac Pacemaker Activity", in "Jacklet (Ed, 1989) Neuronal and Cellular Oscillators".

Known as: Noble-DiFrancesco-Denyer

## 1981 Fischmeister FPf
Base: [McAllister 1975](#1975-mcallister-hpf)
| [Abstract](https://pubmed.ncbi.nlm.nih.gov/7288663/) Fischmeister, Vassort (1981) The electrogenic NaCa exchange and the cardiac electrical activity; I Simulation on Purkinje fibre action potential

Abstract only.

## 1990 Earm RA
Base: [Hilgemann 1987](#1987-hilgemann-raf)
| Code for this paper is inside "Oxsoft Heart"
| [Paper](https://doi.org/10.1098/rspb.1990.0028) Earm, Noble (1990) A model of the single atrial cell; relation between calcium current and calcium release

## 1990a Rasmusson FS
Base: [DiFrancesco 1985](#1985-difrancesco-mpf), but mostly new
| [Paper](https://doi.org/10.1152/ajpheart.1990.259.2.h352) Rasmusson, Clark et al., Campbell (1990) A mathematical model of a bullfrog cardiac pacemaker cell

Novelties:
- Single cell data, improved modelling of extracellular cleft
- Calcium buffering

## 1990b Rasmusson FA
Base: [Rasmusson 1990a](#1990a-rasmusson-fs)
| [Paper](https://doi.org/10.1152/ajpheart.1990.259.2.h370) Rasmusson, Clark et al., Campbell (1990) A mathematical model of electrophysiological activity in a bullfrog atrial cell

## 1991 Luo GV
Base: [Beeler 1977](#1977-beeler-mvf)
| [Updated matlab code](https://rudylab.wustl.edu/code-downloads/)
| [Paper](https://doi.org/10.1161/01.res.68.6.1501) Luo, Rudy (1991) A model of the ventricular cardiac action potential. Depolarization, repolarization, and their interaction.

Known as: Luo-Rudy model, LR1, Luo-Rudy phase 1 model

Bits:
- INa based on Ebihara 1980, but with a j gate added back in

## 1991 Noble GV
Base: [Earm 1990](#1990-earm-ra)
| Code for this paper is inside "Oxsoft Heart"
| [Paper]() Noble, Noble et al., So (1991) The Role of Sodium-Calcium Exchange During the Cardiac Action Potential

## 1991 Wilders mS
Base: [Noble 1984](#1984-noble-msf)
| [Paper](https://doi.org/10.1016/s0006-3495(91)82155-5) Wilders, Jongsma, Van Ginneken (1991) Pacemaker activity of the rabbit sinoatrial node; A comparison of mathematical models

## 1993 Nordin GV
Base: [DiFrancesco 1985](#1985-difrancesco-mpf)
| [Paper](https://doi.org/10.1152/ajpheart.1993.265.6.H2117) Nordin (1993) Computer model of membrane current and intracellular Ca2 flux in the isolated guinea pig ventricular myocyte
**Has erratum**

Bits:
- INaK new formulation

## 1994 Demir RS
Base: [Rasmusson 1990](#1990b-rasmusson-fa)
| [Paper](Demir, Clark, Murphey, Giles (1994) A mathematical model of a rabbit sinoatrial node cell)

## 1994 Luo GV
Base: [Luo 1991](#1991-luo-gv)
| [Paper](https://doi.org/10.1161/01.res.74.6.1071) Luo, Rudy (1994) A dynamic model of the cardiac ventricular action potential I; Simulations of ionic currents and concentration changes

Known as: LRd, LR2, Luo-Rudy phase 2 model

Modifications:
- INaK new formulation
- Rescaled gK1
- ...
- CICR

## 1995 Zeng GV
Base: [1994 Luo GV](#1994-luo-gv)
| [Paper](https://doi.org/10.1161/01.res.77.1.140) Zeng, Laurita, Rosenbaum, Rudy (1995) Two Components of the Delayed Rectifier K Current in Ventricular Myocytes of the Guinea Pig Type

Modifications:
- Splits IK into IKr and IKs
- Calcium buffering, with an analytical solution to a higher-order problem that ends up involving arccos and cos.
- ...

## 1996a Dokos RS
Base: [Noble 1989](#1989-noble-ms), [Wilders 1991](#1991-wilders-ms)
| [Paper](https://doi.org/10.1006/jtbi.1996.0129) Dokos, Celler, Lovell (1996) Ion Currents Underlying Sinoatrial Node Pacemaker Activity; A New Single Cell Mathematical Model

## 1996b Dokos RS
Base: [Dokos 1996a](#1996a-dokos-rs)
| [Paper](https://doi.org/10.1006/jtbi.1996.0141) Dokos, Celler, Lovell (1996) Vagal Control of Sinoatrial Rhythm; a Mathematical Model

Modifications:
- Contains ACh storage and interaction

## 1996 Lindblad RA
Base: [Demir 1994](#1994-demir-rs)
| [Paper](https://doi.org/10.1152/ajpheart.1996.271.4.h1666) Lindblad, Murphey, Clark Giles (1996) A model of the action potential and underlying membrane currents in a rabbit atrial cell

## 1998 Courtemanche HA
Base: [Luo 1994](#1994-luo-gv)
| [In Myokit repo](https://github.com/myokit/models/blob/main/c/courtemanche-1998.mmt)
| [Paper](https://doi.org/10.1152/ajpheart.1998.275.1.h301) Courtemanche, Ramirez, Nattel (1998) Ionic mechanisms underlying human atrial action potential properties; insights from a mathematical model

## 1998 Jafri GV
Base: [Luo 1994](#1994-luo-gv)
| [Paper](https://doi.org/10.1016/s0006-3495(98)77832-4) Jafri, Rice, Winslow (1998) Cardiac Ca2 Dynamics; The Roles of Ryanodine Receptor Adaptation and Sarcoplasmic Reticulum Load

Modifications:
- Elements of Keizer & Levine 1996 Ca-induced Ca release model

## 1998 Noble GV
Base: [Noble 1991](#1991-noble-gv)
| Code for this paper is inside "Oxsoft Heart"
| [Paper (not online)](https://pubmed.ncbi.nlm.nih.gov/9487284/) Noble, Varghese, Kohl, Noble (1998) Improved guinea-pig ventricular cell model incorporating a diadic space, IKr and IKs, and length- and tension-dependent processes
| [Correction (not online)](https://www.dpag.ox.ac.uk/publications/1249778)

## 1998 Nygren HA
Base: [Lindblad 1996](#1996-lindblad-ra)
| [In Myokit repo](https://github.com/myokit/models/blob/main/c/nygren-1998.mmt)
| [Paper](https://doi.org/10.1161/01.res.82.1.63) Nygren, Fiset et al., Giles (1998) Mathematical model of an adult human atrial cell; the role of K-currents in repolarization

## 1998 Priebe HV
Base: [Luo 1994](#1994-luo-gv)
| [In Myokit repo](https://github.com/myokit/models/blob/main/c/priebe-1998.mmt)
| [Paper](https://doi.org/10.1161/01.res.82.11.1206) Priebe, Beuckelmann (1998) Simulation study of cellular electric properties in heart failure

## 1998 Riemer GV
Base: [Luo 1994](#1994-luo-gv)
| [Paper](https://doi.org/10.1152/ajpheart.1998.275.2.h431) Riemer, Sobie, Tung (1998) Stretch-induced changes in arrhythmogenesis and excitability in experimentally based heart cell models

Modifications:
- Added stretch channel

## 1999 Chudin GV
Base: [Zeng 1995](#1995-zeng-gv)
| [Paper](https://doi.org/10.1016/S0006-3495(99)77126-2) Chudin, Goldhaber et al., Kogan (1999) Intracellular Ca dynamics and the stability of ventricular tachycardia

Modifications:
- New calcium handling

## 1999 Clancy GV
Base: [Zeng 1995](#1995-zeng-gv)
| [Paper](https://doi.org/10.1038/23034) Clancy, Rudy (1999) Linking a genetic defect to its cellular phenotype in a cardiac arrhythmia

Modifications:
- New (baseline and mutated) INa model

## 1999 Demir RS
Base: [Demir 1994](#1994-demir-rs)
| [Paper](https://doi.org/10.1152/ajpheart.1999.276.6.H2221) Demir, Clark, Giles (1999) Parasympathetic modulation of sinoatrial node pacemaker activity in rabbit heart; a unifying model

Modifications:
- Added cAMP and ACh response

## 1999 Dumaine GV
Base: [Luo 1994](#1994-luo-gv)
| [Paper](https://doi.org/10.1161/01.res.85.9.803) Dumaine, Towbin et al., Antzelevitch (1999) Ionic mechanisms responsible for the electrocardiographic phenotype of the Brugada syndrome are temperature dependent

## 1999 Viswanathan GV
Base: [Zeng 1995](#1995-zeng-gv)
| [Paper](https://doi.org/10.1161/01.CIR.99.18.2466) Viswanathan, Shaw, Rudy (1999) Effects of IKr and IKs Heterogeneity on Action Potential Duration and Its Rate Dependence; A Simulation Study

## 1999 Winslow CV
Base: [Jafri 1998](#1998-jafri-gv)
| [Paper](https://doi.org/10.1161/01.res.84.5.571) Winslow, Rice et al., O'Rourke (1999) Mechanisms of Altered Excitation-Contraction Coupling in Canine Tachycardia-Induced Heart Failure, II Model Studies

## 2000 Endresen RS
Base: Rederive everything
| [Paper](https://doi.org/10.1007/s002490050254) Endresen, Hall, Hoye, Myrheim (2000) A theory for the membrane potential of living cells

Novelties:
- The paper contains nice derivations of e.g. gating and transport equations
- The paper uses an analytical V equation

## 2000 Faber GV
Base: [Viswanathan 1999](#1999-viswanathan-gv)
| [Original C++ code](https://rudylab.wustl.edu/code-downloads/)
| [Paper](https://doi.org/10.1016/s0006-3495(00)76783-x) Faber, Rudy (2000) Action Potential and Contractility in [Na+]i Overloaded Cardiac Myocytes

## 2000 Greenstein CV
Base: [Winslow 1999](#1999-winslow-cv)
| [Paper](https://doi.org/10.1161/01.res.87.11.1026) Greenstein, Wu et al., Winslow (2000) Role of the calcium-independent transient outward current Ito1 in shaping action potential morphology and duration

## 2000 Ramirez CA
Base: [Courtemanche 1998](#1998-courtemanche-ha)
| [Paper](https://doi.org/10.1152/ajpheart.2000.279.4.h1767) Ramirez, Nattel, Courtemanche (2000) Mathematical analysis of canine atrial action potentials; rate, regional factors, and electrical remodeling

## 2000 Rice GV
Base: [Jafri 1998](#1998-jafri-gv)
| [Paper](https://doi.org/10.1152/ajpheart.2000.278.3.h913) Rice, Jafri, Winslow (2000) Modeling short-term interval-force relations in cardiac muscle

## 2000 Zhang RS
Base: Mostly new?
| [Paper](https://doi.org/10.1152/ajpheart.2000.279.1.h397) Zhang, Holden et al., Boyett (2000) Mathematical models of action potentials in the periphery and center of the rabbit sinoatrial node

## 2001 Boyett RS
Base: [Zhang 2000](#2000-zhang-rs)
| [Paper](https://doi.org/10.1098/rsta.2001.0818) Boyett, Zhang, Garny, Holden (2001) Control of the pacemaker activity of the sinoatrial node by intracellular Ca; Experiments and modelling

## 2001 Hund GV
Base: [Faber 2000](#2000-faber-gv)
| [Paper](https://doi.org/10.1016/s0006-3495(01)75965-6) Hund, Kucera, Otani, Rudy (2001) Ionic Charge Conservation and Long-Term Steady State in the Luo-Rudy Dynamic Cell Model

Modifications:
- Algebraic V (usually not inherited by next models!)
- Stimulus current assigned to K+ in concentration updates

## 2001 Mazhari CV
Base: [Winslow 1999](#1999-winslow-cv)
| [Paper](https://doi.org/10.1161/hh1301.093633) Mazhari, Greenstein et al., Nuss (2001) Molecular interactions between two long-QT syndrome gene products, HERG and KCNE2, rationalized by in vitro and in silico analysis

## 2001 Michailova CV
Base: [Winslow 1999](#1999-winslow-cv)
| [Paper](https://doi.org/10.1016/s0006-3495(01)75727-x) Michailova, McCulloch (2001) Model Study of ATP and ADP Buffering, Transport of Ca2 and Mg2, and Regulation of Ion Pumps in Ventricular Myocyte

## 2001 Noble GP
Base: [Noble 1998](#1998-noble-gv)
| Paper not online: Noble, Noble (2001) Remodelling of calcium dynamics in guinea-pig ventricular cells

## 2001 Pandit LV
Base: [Demir 1999](#1999-demir-rs), [Winslow 1999](#1999-winslow-cv)
| [Paper](https://doi.org/10.1016/s0006-3495(01)75943-7) Pandit, Clark, Giles, Demir (2001) A Mathematical Model of Action Potential Heterogeneity in Adult Rat Left Ventricular Myocytes

## 2001 Puglisi GV
Base: [Luo 1994](#1994-luo-gv)
| [Paper](https://doi.org/10.1152/ajpcell.2001.281.6.c2049) Puglisi, Bers (2001) LabHEART; an interactive computer model of rabbit ventricular myocyte ion channels and Ca transport

Known as: Puglisi-Bers, LabHEART

Modifications:
- Rescaled gK1
- ... see Table 1

## 2002 Clancy GV
Base: [Clancy 1999](#1999-clancy-gv), [Viswanathan 1999](#1999-viswanathan-gv) 
| [Paper](https://doi.org/10.1038/23034) Clancy, Rudy (1999) Linking a genetic defect to its cellular phenotype in a cardiac arrhythmia

Modifications:
- New (baseline and mutated) INa model

## 2002 Fox CV
Base: [Chudin 1999](#1999-chudin-gv)
| [Paper](https://doi.org/10.1152/ajpheart.00612.2001) Fox, McHarg, Gilmour (2002) Ionic mechanism of electrical alternans

## 2002 Kneller CA
Base: [Ramirez 2000](#2000-ramirez-ca)
| [Paper](https://doi.org/10.1152/ajpheart.00489.2001) Kneller, Ramirez et al., Nattel (2002) Time-dependent transients in an ionically based mathematical model of the canine atrial action potential

## 2002 Kurata RS
Base: [Wilders 1991](#1991-wilders-ms), [Demir 1994](#1994-demir-rs), [Dokos 1996](#1996-dokos-rs), [Zhang 2000](#2000-zhang-rs)
| [Paper](https://doi.org/10.1152/ajpheart.00900.2001) Kurata, Hisatome, Imanishi, Shibamoto (2002) Dynamical description of sinoatrial node pacemaking; improved mathematical model for primary pacemaker cell

## 2003 Cabo CV
Base: [Luo 1994](#1994-luo-gv)
| [Paper](https://doi.org/10.1152/ajpheart.00512.2002) Cabo, Boyden (2003) Electrical remodeling of the epicardial border zone in the canine infracted heart; a computational analysis

## 2003 Matsuoka GV
Base: [Luo 1991](#1991-luo-gv), but lots of new things
| [Original Delphi code](https://web.archive.org/web/20070819084149/http://www.card.med.kyoto-u.ac.jp/simulation/)
| [Reimplementation in simBio](http://www.sim-bio.org/model/index.html#Kyoto+model)
| [Paper](https://doi.org/10.2170/jjphysiol.53.105) Matsuoka, Sarai et al., Noma (2003) Role of individual ionic current systems in ventricular cells hypothesized by a model study

Known as: Kyoto model

Bits:
- Contraction from Negroni 1996
- INaK novel reduced formulation, based on INaCa
- ...

## 2003 Pandit LV
Base: [Pandit 2001](#2001-pandit-lv)
| [Paper](https://doi.org/10.1016/s0006-3495(03)74902-9) Pandit, Giles, Demir (2003) A Mathematical Model of the Electrophysiological Alterations in Rat Ventricular Myocytes in Type-I Diabetes

## 2003 Sarai mS
Base: [Matsuoka 2003](#2003-matsuoka-mV)
| [Original Delphi code](https://web.archive.org/web/20070819084149/http://www.card.med.kyoto-u.ac.jp/simulation/)
| [Reimplementation in simBio](http://www.sim-bio.org/model/index.html#Kyoto+model)
| [Paper](https://doi.org/10.2170/jjphysiol.53.125) Sarai, Matsuoka et al., Noma (2003) Role of individual ionic current systems in the SA node hypothesized by a model study

Based mostly on Rabbit and Guinea pig data.
The Delphi and C++ code for this model is the same as that for Matsuoka 2003, but it has a mode switch.

## 2003 Saucerman LV
Base: [Puglisi 2001](#2001-puglisi-gv)
| [Original matlab code](https://github.com/saucermanlab/model-archive)
| [Paper](https://doi.org/10.1074/jbc.M308362200) Saucerman, Brunton, Michailova, McCulloc (2003) Modeling beta-adrenergic control of cardiac myocyte contractility in silico

## 2003 Seemann HV
Base: [Priebe 1998](#1998-priebe-hv)
| [Paper](https://doi.org/10.1046/j.1540.8167.90314.x) Seemann, Sachse, Weiss, Doessel (2003) Quantitative reconstruction of cardiac electromechanics in human myocardium; regional heterogeneity

Modifications:
- Added force development model

## 2003 Solovyova GV
Base: [Noble 1998](#1998-noble-gv)
| [Paper](https://doi.org/10.1142/S0218127403008983) Solovyova, Vikulova et al., Noble (2003) Mechanical interaction of heterogeneous cardiac muscle segments in silico; effects on Ca handling and action potential

Known as: Ekaterinburg-Oxford (EO) model

## 2004 Bassani-Altamirano mV
Base: [Puglisi 2001](#2001-puglisi-gv)
| [Paper](https://doi.org/10.1113/jphysiol.2004.067959) Bassani*, Altamirano*, Puglisi, Bers (2004) Action potential duration determines sarcoplasmic reticulum Ca reloading in mammalian ventricular myocytes (*contributed equally)

Note: Ferret, rabbit, and rat.

## 2004 Bondarenko MV
Base: [Luo 1994](#1994-luo-gv), but many new formulations
| [Paper](https://doi.org/10.1152/ajpheart.00185.2003) Bondarenko, Szigeti et al., Rasmusson (2004) Computer model of action potential of mouse ventricular myocytes

## 2004 Hund CV
Base: [Hund 2001](#2001-hund-gv) (arguably, most of the formulations are new, but the supplement is written in a way that strongly suggests this model was based on LRd2).
| [Updated matlab and C++ code](https://rudylab.wustl.edu/code-downloads/)
| [Paper](https://doi.org/10.1161/01.cir.0000147231.69595.d3) Hund, Rudy (2004) Rate Dependence and Regulation of Action Potential and Calcium Transient in a Canine Cardiac Ventricular Cell Model

Known as: HRd

Bits:
- CaMKII from Hanson et al 1994
- INaCa from Weber et al 2001
- INa from Luo 1994
- INaL from Luo 1994 and Maltsev et al 2001
- Cl regulation from Baumgarten et al [28]
- Iup, Ileak, Itr from Luo 1994
- INaK, IKp, IK1, IpCa from Luo 1994

## 2004 Iyer HV
Base: [Winslow 1999](#1999-winslow-cv) and others
| [In Myokit repo](https://github.com/myokit/models/blob/main/c/iyer-2004.mmt)
| [Paper](https://doi.org/10.1529/biophysj.104.043299) Iyer, Mazhari, Winslow (2004) A computational model of the human left-ventricular epicardial myocyte

Known as: Iyer-Mazhari-Winslow

## 2004 Katsnelson RV
Base: [Solovyova 2003](#2003-solovyova-gv)
| [Paper](https://doi.org/10.1016/j.jtbi.2004.05.007) Katsnelson, Nikitina et al., Markhasin (2004) Influence of viscosity on myocardium mechanical activity; a mathematical model

## 2004 Matsuoka GV
Base: [Matsuoka 2003](#2003-matsuoka-gv)
| [Reimplementation in simBio](http://www.sim-bio.org/model/index.html#Kyoto+model)
| [Paper](https://doi.org/10.1016/j.pbiomolbio.2004.01.006) Matsuoka, Sarai, Jo, Noma (2004) Simulation of ATP metabolism in cardiac excitation-contraction coupling

Modifications:
- Added mitochondrial model

## 2004 Saucerman LV
Base: [Saucerman 2003](#2003-saucerman-lv)
| [Original matlab code](https://github.com/saucermanlab/model-archive)
| [Paper](https://doi.org/10.1016/j.pbiomolbio.2004.01.005) Saucerman, McCulloch (2004) Mechanistic systems models of cell signaling networks; a case study of myocyte adrenergic regulation

## 2004 Saucerman RV
Base: [Puglisi 2001](#2001-puglisi-gv)
| [Original matlab code](https://github.com/saucermanlab/model-archive)
| [Paper](https://doi.org/10.1161/01.RES.0000150055.06226.4e) Saucerman, Healy et al., McCulloch (2004) Proarrhythmic consequences of a KCNQ1 AKAP-binding domain mutation; computational models of whole cells and heterogeneous tissue

## 2004 Shannon RV
Base: [Puglisi 2001](#2001-puglisi-gv)
| [Original C code](https://web.archive.org/web/20060425184747/http://www.luhs.org/depts/physio/personal_pages/bers_d/index.html)
| [Grandi's matlab](https://github.com/drgrandilab/Shannon-et-al-2004-Rabbit-Ventricular-Model)
| [Another matlab](https://somapp.ucdmc.ucdavis.edu/pharmacology/bers/)
| [Fink's CellML](http://models.cellml.org/exposure/d72a36fe0b7e121068c96bcb1ff6044a/shannon_wang_puglisi_weber_bers_2004_a.cellml/view)
| [Paper](https://doi.org/10.1529/biophysj.104.047449) Shannon, Wang et al., Bers (2004) A mathematical treatment of integrated Ca dynamics within the ventricular myocyte

Known as: Chicago model

Modifications:
- Rescaled gK1
- ...

## 2004 Ten Tusscher HV
Base: Mostly new?
| [Original C code](https://tbb.bio.uu.nl/khwjtuss/SourceCodes/HVM)
| [In Myokit repo](https://github.com/myokit/models/blob/main/c/tentusscher-2004.mmt)
| [Paper](https://doi.org/10.1152/ajpheart.00794.2003) Ten Tusscher, Noble, Noble, Panfilov (2004) A Model for Human Ventricular Tissue

Known as: TNNP 2004

Bits:
- INa with 3 gates, ref given to Beeler 1977
- ICaL adapted from Luo 1994
- INaK adapted from DiFrancesco 1985

## 2005 Krogh-Madsen Cdf
Base: Mostly new?
| [Paper](https://doi.org/10.1152/ajpheart.00683.2004) Krogh-Madsen, Schaffer et al., Guevara  (2005) An ionic model for rhythmic activity in small clusters of embryonic chick ventricular cells

## 2005 Kurata HV
Base: [Priebe 1998](#1998-priebe-hv)
| [Original simBio code](http://www.sim-bio.org/model/index.html#Kurata+model)
| [Paper](https://doi.org/10.1529/biophysj.105.060830) Kurata, Hisatome, Matsuda, Shibamoto (2005) Dynamical Mechanisms of Pacemaker Generation in IK1-Downregulated Human Ventricular Myocytes; Insights from Bifurcation Analyses of a Mathematical Model

## 2005 Michailova CV
Base: [Michailova 2001](#2001-michailova-cv)
| [Paper](https://doi.org/10.1529/biophysj.104.046284) Michailova, Saucerman, Belik, McCulloch (2005) Modeling Regulation of Cardiac KATP and L-type Ca2 Currents by ATP, ADP, and Mg2

## 2006 Cortassa GV
Base: [Rice 2000](#2000-rice-gv)

Modifications:
- Cortassa 2003 metabolism model

## 2006 Greenstein CV
Base: [Greenstein 2000](#2000-greenstein-cv) (via Greenstein 2002 local control model)
| [Paper](https://doi.org/10.1529/biophysj.105.065169) Greenstein, Hinch, Winslow (2006) Mechanisms of Excitation-Contraction Coupling in an Integrative Model of the Cardiac Ventricular Myocyte

Modifications:
- Ensemble behaviour of CaRUs using Hinch 2004 approximation

## 2006 Iribe GV
Base: [Noble 1998](#1998-noble-gv)
| [Paper](https://doi.org/10.1098/rsta.2006.1758) Iribe, Kohl, Noble (2006) Modulatory effect of calmodulin-dependent kinase II (CaMKII) on sarcoplasmic reticulum Ca2 handling and interval-force relations; a modelling study

Modification:
- Added Rice 1999 mechanics

## 2006 Mangoni MS
Base: [Zhang 2000](#2000-zhang-rs)
| [Paper](https://doi.org/10.1161/01.RES.0000225862.14314.49) Mangoni, Traboulsie et al., Lory (2006) Bradycardia and Slowing of the Atrioventricular Conduction in Mice Lacking CaV31 alpha-1g T-Type Calcium Channels

## 2006 Pasek LV
Base: [Pandit 2001](#2001-pandit-lv)
| [Paper](https://doi.org/10.1098/rsta.2006.1764) Pasek, Simurda, Christe (2006) The functional role of cardiac T-tubules explored in a model of rat ventricular myocytes
 
 Modifications:
- Inclusion of a restricted "tubular" space.
 
## 2006 Sato CV
Base: [Fox 2002](#2002-fox-cv)
| [Paper](https://doi.org/10.1161/01.RES.0000240542.03986.e7) Sato, Shiferaw et al., Karma (2006) Spatially Discordant Alternans in Cardiac Tissue; Role of Calcium Cycling

## 2006 Ten Tusscher HV
Base: [Ten Tusscher 2004](#2004-ten-tusscher-hv)
| [Original C code](https://tbb.bio.uu.nl/khwjtuss/SourceCodes/HVM2)
| [In Myokit repo](https://github.com/myokit/models/blob/main/c/tentusscher-2006.mmt)
| [Paper](https://doi.org/10.1152/ajpheart.00109.2006) Ten Tusscher, Panfilov (2006) Alternans and spiral breakup in a human ventricular tissue model

Known as: TP 2006

Modifications:
- Added dyadic subspace
- Changed IKr conductance
- Changed IKs conductance and rates
- Changed ICaL conductance and rates, added gate
- Changed INaK conductance
- Changed IpCa conductance
- New Irel formulation
- Changed Ileak and Iup rate
- Added transfer equations for new subspace

## 2006 Takeuchi GV
Base: [Terashima 2006](#2006-terashima-gv)
| [Original simBio code](http://www.sim-bio.org/model/takeuchi_et_al_2006.html)
| [Paper](https://doi.org/10.1085/jgp.200609646) Takeuchi, Tatsumi et al., Noma (2006) Ionic Mechanisms of Cardiac Cell Swelling Induced by Blocking NaK Pump As Revealed by Experiments and Simulation

## 2006 Terashima GV
Base: [Matsuoka 2004](#2004-matsuoka-gv)
| [Original simBio code](http://www.sim-bio.org/model/index.html#Kyoto+model)
| [Paper](https://doi.org/10.1098/rsta.2006.1767) Terashima, Takeuchi et al., Noma (2006) Modelling Cl homeostasis and volume regulation of the cardiac cell

Modifications:
- Chloride dynamics
- Cell volume dynamics

## 2007 Faber GV
Base: [Hund 2001](#2001-hund-gv)
|[Original matlab and C++ code](https://rudylab.wustl.edu/code-downloads/)
| [Paper](https://doi.org/10.1529/biophysj.106.088807) Faber, Silva, Livshitz, Rudy (2007) Kinetic Properties of the Cardiac L-Type Ca Channel and Its Role in Myocyte Electrophysiology; A Theoretical Investigation

Known as: Faber-Rudy

## 2007 Grandi RV
Base: [Shannon 2004](#2004-shannon-rv)
| [Paper](https://doi.org/10.1529/biophysj.107.114868) Grandi, Puglisi et al., Bers (2007) Simulation of Ca-calmodulin-dependent protein kinase II on rabbit ventricular myocyte ion currents and action potentials

## 2007 Iyer HV
Base: [Iyer 2004](#2004-iyer-hv)
| [Paper](https://doi.org/10.1161/01.res.0000258468.31815.42) Iyer, Hajjar, Armoundas (2007) Mechanisms of Abnormal Calcium Homeostasis in Mutations Responsible for Catecholaminergic Polymorphic Ventricular Tachycardia

## 2007 Kuzumoto GV
Base: [Takeuchi 2006](#2006-takeuchi-gv)
| [Original simBio code](http://www.sim-bio.org/model/kuzumoto_et_al_2007.html)
| [Paper](https://doi.org/10.1016/j.pbiomolbio.2007.07.005) Kuzumoto, Takeuchi et al., Matsuoka (2008) Simulation analysis of intracellular Na and Cl homeostasis during beta1-adrenergic stimulation of cardiac myocyte

Modifications: 
- Beta-adrenergic signalling
- ...

## 2007 Livshitz CV
Base: [Hund 2004](#2004-hund-cv)
| [Original matlab code](https://rudylab.wustl.edu/code-downloads/)
| [In Myokit repo](https://github.com/myokit/models/blob/main/c/livshitz-2007.mmt)
| [Paper](https://doi.org/10.1152/ajpheart.01347.2006) Livshitz, Rudy (2007) Regulation of Ca and electrical alternans in cardiac myocytes; role of CAMKII and repolarizing currents

## 2007 Niederer LV
Base: [Pandit 2001](#2001-pandit-lv)
| [Paper](https://doi.org/10.1529/biophysj.106.095463) Niederer, Smith (2007) A Mathematical Model of the Slow Force Response to Stretch in Rat Ventricular Myocytes

Modifications:
- Added Hinch Ca model
- Added Niederer 2006 contraction

## 2007 Terkildsen GV
Base: [Hund 2001](#2001-hund-gv)
| [Paper](https://doi.org/10.1152/ajpheart.00771.2007) 

Modifications:
- INaK from Smith 2004, updated by same authors
- IKATP from Michailova
- Cell volume regulation and water flux
- Metabolite concentrations

## 2008 Benson CV
Base: [Hund 2004](#2004-hund-cv)
| [Paper](https://doi.org/10.1016/j.pbiomolbio.2007.08.002) Benson, Aslanidi, Zhang, Holden (2008) The canine virtual ventricular wall; A platform for dissecting pharmacological effects on propagation and arrhythmogenesis

## 2008 Fink HV
Base: [Ten Tusscher 2006](#2006-ten-tusscher-hv)
| [In Myokit repo](https://github.com/myokit/models/blob/main/c/fink-2008.mmt)
| [Paper](https://doi.org/10.1016/j.pbiomolbio.2007.07.011) Fink, Noble et al., Giles (2008) Contributions of HERG K current to repolarization of the human ventricular action potential

Modifications:
- New IK1 formulation, based on Yan & Ishihara 2005
- New IKr formulation
- Rescaled IKs

## 2008 Himeno GS
Base: [Sarai 2003](#2003-sarai-ms), [Kuzumoto 2007](#2007-kuzumoto-gv)
| [Original simBio code](http://www.sim-bio.org/model)
| [Paper](https://doi.org/10.2170/physiolsci.RP015207) Himeno, Sarai, Matsuoka, Noma (2008) Ionic mechanisms underlying the positive chronotropy induced by beta1-adrenergic stimulation in guinea pig sinoatrial node cells

## 2008 Hund CV
Base: [Livshitz 2007](#2007-livshitz-cv)
| [Original C++ code](https://rudylab.wustl.edu/code-downloads/)

## 2008 Korhonen Md
Base: [Dokos 1996](#1996-dokos-rs), [Bondarenko 2004](#2004-bondarenko-mv)
| [Paper](https://doi.org/10.1085/jgp.200809961) Korhonen, Rapila, Tavi (2008) Mathematical model of mouse embryonic cardiomyocyte excitation-contraction coupling

## 2008 Kurata RS
Base: [Kurata 2002](#2002-kurata-rs)
| [Paper](https://doi.org/10.1529/biophysj.107.112854) Kurata, Matsuda, Hisatome, Shibamoto (2008) Regional difference in dynamical property of sinoatrial node pacemaking; role of Na channel current

## 2008 Mahajan RV
Base: [Shannon 2004](#2004-shannon-rv)
| [Paper](https://doi.org/10.1529/biophysj.106.98160) Mahajan, Shiferaw et al., Weiss (2008) A Rabbit Ventricular Action Potential Model Replicating Cardiac Dynamics at Rapid Heart Rates

## 2008 Pasek GV
Base: [Hund 2001](#2001-hund-gv) with many changes
| [Paper](https://doi.org/10.1016/j.pbiomolbio.2007.07.022) Pasek, Simurda, Orchard, Christe (2008) A model of the guinea-pig ventricular cardiac myocyte incorporating a transverse-axial tubular system

## 2008 Ten Tusscher HP
Base: [Ten Tusscher 2006](#2006-ten-tusscher-hv)
| [Paper](https://doi.org/10.1016/j.pbiomolbio.2007.07.026) Ten Tusscher, Panfilov (2008) Modelling of the ventricular conduction system

Modifications:
- Scaled GKs by 0.35, GNa by 2.94. No other changes.

## 2008 Terkildsen LV
Base: [Pandit 2001](#2001-pandit-lv), 
| [Paper](https://doi.org/10.1113/expphysiol.2007.041871) Terkildsen, Niederer et al., Smith (2008) Using Physiome standards to couple cellular functions for rat cardiac excitation-contraction

Known as: PHN

Modifications:
- Niederer 2006 contraction model
- Hinch calcium dynamics

## 2008 Saucerman RV
Base: [Shannon 2004](#2004-shannon-rv)
| [Original matlab code](https://github.com/saucermanlab/model-archive)
| [Paper](https://doi.org/10.1529/biophysj.108.128728) Saucerman, Bers (2008) Calmodulin mediates differential sensitivity of CaMKII and calcineurin to local Ca2 in cardiac myocytes

## 2008 Sulman GV
Base: [Solovyova 2003](#2003-solovyova-gv)
| [Paper](https://doi.org/10.1007/s11538-007-9285-y) Sulman, Katsnelson, Solovyova, Markhasin (2008) Mathematical modeling of mechanically modulated rhythm disturbances in homogeneous and heterogeneous myocardium with attenuated activity of Na-K pump

## 2008 Wang Md
Base: [Bondarenko 2004](#2004-bondarenko-mv)
| [Paper](https://doi.org/10.1152/ajpheart.01376.2007) Wang, Sobie (2008) Mathematical model of the neonatal mouse ventricular action potential

## 2009a Aslanidi RA
Base: [Lindblad 1996](#1996-lindblad-ra)
| [Paper](https://doi.org/10.1016/j.bpj.2008.09.057) Aslanidi, Boyett et al., Zhang (2009) Mechanisms of transition from normal to reentrant electrical activity in a model of rabbit atrial tissue; interaction of tissue heterogeneity and anisotropy

## 2009b Aslanidi CP
Base: [Benson 2008](#2008-benson-cv)
| [Paper](https://doi.org/10.1016/j.bpj.2009.03.061) Aslanidi, Stewart, Boyett, Zhang (2009) Optimal Velocity and Safety of Discontinuous Conduction through the Heterogeneous Purkinje-Ventricular Junction

## 2009 Decker CV
Base: [Hund 2008](#2008-hund-cv)
| [Original matlab and C++ code](https://rudylab.wustl.edu/code-downloads/)
| [In Myokit repo](https://github.com/myokit/models/blob/main/c/decker-2009.mmt)
| [Paper](https://doi.org/10.1152/ajpheart.01216.2008) Decker, Heijman et al., Rudy (2009) Properties and ionic mechanisms of action potential adaptation, restitution, and accommodation in canine epicardium

## 2009 Grandi HV
Base: [Ten Tusscher 2004](#2004-ten-tusscher-hv)
| [Paper](https://doi.org/10.1016/j.yjmcc.2008.12.002) Grandi, Pasqualini et al., Severi (2009) Theoretical investigation of action potential duration dependence on extracellular Ca in human cardiomyocytes

## 2009 Inada mA
Base: [Lindblad 1996](#1996-lindblad-ra), [Kurata 2002](#2002-kurata-rs)
| [Paper](https://doi.org/10.1016/j.bpj.2009.06.056) Inada, Hancox, Zhang, Boyett (2009) One-Dimensional Mathematical Model of the Atrioventricular Node Including Atrio-Nodal, Nodal, and Nodal-His Cells

## 2009 Korhonen Ld
Base: [Pandit 2001](#2001-pandit-lv), [Bondarenko 2004](#2004-bondarenko-mv)
| [Paper](https://doi.org/10.1016/j.bpj.2008.10.026) Korhonen, Hanninen, Tavi (2009) Model of excitation-contraction coupling of rat neonatal ventricular myocytes

## 2009 Koivumaki MV
Base: [Bondarenko 2004](#2004-bondarenko-mv)
| [Paper](https://doi.org/10.1186/1472-6793-9-16) Koivumaki, Korhonen et al., Tavi (2009) Regulation of excitation-contraction coupling in mouse cardiac myocytes; integrative analysis with mathematical modelling

## 2009 Livshitz GV
Base: [Faber 2007](#2007-faber-gv)
| [Original matlab code](https://rudylab.wustl.edu/code-downloads/)
| [Paper](https://doi.org/10.1016/j.bpj.2009.05.062) Livshitz, Rudy (2009) Uniqueness and Stability of Action Potential Models during Rest, Pacing, and Conduction Using Problem-Solving Environment

## 2009 Livshitz CV
Base: [Hund 2004](#2004-hund-cv)
| [Original matlab code](https://rudylab.wustl.edu/code-downloads/)
| [Paper](https://doi.org/10.1016/j.bpj.2009.05.062) Livshitz, Rudy (2009) Uniqueness and Stability of Action Potential Models during Rest, Pacing, and Conduction Using Problem-Solving Environment

## 2009 Maleckar HA
Base: [Nygren 1998](#1998-nygren-ha)
| [In Myokit repo](https://github.com/myokit/models/blob/main/c/maleckar-2009.mmt)
| [Paper](https://doi.org/10.1152/ajpheart.00411.2009) Maleckar, Greenstein, Giles, Trayanova (2009) K current changes account for the rate dependence of the action potential in the human atrial myocyte

## 2009 Maltsev RS
Base: [Kurata 2002](#2002-kurata-rs), [Shannon 2004](#2004-shannon-rv)
| [Paper](https://doi.org/10.1152/ajpheart.01118.2008) Maltsev, Lakatta (2009) Synergism of coupled subsarcolemmal Ca2 clocks and sarcolemmal voltage clocks confers robust and flexible pacemaker function in a novel pacemaker cell model

## 2009 Stewart HP
Base: [Ten Tusscher 2006](#2006-ten-tusscher-hv)
| [Original CellML code](https://models.cellml.org/workspace/stewart_aslanidi_noble_noble_boyett_zhang_2009)
| [In Myokit repo](https://github.com/myokit/models/blob/main/c/stewart-2009.mmt)
| [Paper](https://doi.org/10.1098/rsta.2008.0283) Stewart, Aslanidi et al., Zhang (2009) Mathematical model of the electrical action potential of Purkinje fibre cells

## 2010 Grandi HV
Base: [Shannon 2004](#2004-shannon-rv)
| [Original matlab code](https://github.com/drgrandilab/Grandi-et-al-2010-Human-Ventricular-Model)
| [In Myokit repo](https://github.com/myokit/models/blob/main/c/grandi-2010.mmt)
| [Paper](https://doi.org/10.1016/j.yjmcc.2009.09.019) Grandi, Pasqualini, Bers (2010) A novel computational model of the human ventricular action potential and Ca transient

Known as: Grandi-Pasqualini-Bers human ventricular model, GPB

Note: Also credited as 2009 due to publication date being listed as 2009 and date of issue it appeared in listed as 2010.

Modifications:
- Scaled gK1
- ...

## 2010 Imtiaz RS
Base: [Kurata 2002](#2002-kurata-rs)
| [Paper](https://doi.org/10.1016/j.yjmcc.2010.03.015) Imtiaz, von der Weid, Laver, van Helden (2010) SR Ca store refill; a key factor in cardiac pacemaking

## 2010 Korhonen Md
Base: [Korhonen 2008](#2008-korhonen-md)
| [Paper](https://doi.org/10.1113/jphysiol.2009.185173) Korhonen, Rapila et al., Tavi (2010) Local Ca releases enable rapid heart rates in developing cardiomyocytes

## 2010 Li MV
Base: [Bondarenko 2004](#2004-bondarenko-mv)
| [Official CellML](https://models.cellml.org/workspace/li_smith_2009)
| [Paper](https://doi.org/10.1152/ajpheart.00219.2010) Li, Niederer et al., Smith (2010) A mathematical model of the murine ventricular myocyte; a data-driven biophysically based approach applied to mice overexpressing the canine NCX isoform

## 2010 Maltsev RS
Base: [Maltsev 2009](#2009-maltsev-rs)
| [Paper](https://doi.org/10.1152/ajpheart.00783.2009) Maltsev, Lakatta (2010) A novel quantitative explanation for the autonomic modulation of cardiac pacemaker cell automaticity via a dynamic system of sarcolemmal and intracellular proteins

## 2010 Sampson-Iyer HP
Base: [Iyer 2004](#2004-iyer-hv)
| [Original fortran code](https://physoc.onlinelibrary.wiley.com/doi/suppl/10.1113/jphysiol.2010.187328#support-information-section)
| [In Myokit repo](https://github.com/myokit/models/blob/main/c/sampson-2010.mmt)
| [Paper](https://doi.org/10.1113/jphysiol.2010.187328) Sampson, Iyer, Marks, Kass (2010). A computational model of Purkinje fibre single cell electrophysiology: implications for the long QT syndrome

## 2010 Soltis RV
Base: [Saucerman 2008](#2008-saucerman-rv)
| [Original matlab code](https://github.com/saucermanlab/model-archive)
| [Paper](https://doi.org/10.1016/j.bpj.2010.08.016) Soltis, Saucerman (2010) Synergy between CaMKII Substrates and beta-Adrenergic Signaling in Regulation of Cardiac Myocyte Ca2+ Handling

## 2011 Carro HV
Base: [Grandi 2010](#2010-grandi-hv)
| [Paper](https://doi.org/10.1098/rsta.2011.0127) Carro, Rodriguez, Laguna, Pueyo (2011) A human ventricular cell model for investigation of cardiac arrhythmias under hyperkalaemic conditions

Known as: CRLP

## 2011 Corrias RP
Base: [DiFrancesco 1985](#1985-difrancesco-mpf), but many new parts
| [Official CellML](https://models.cellml.org/w/alberto/CorriasPurkinje)
| [Paper](https://doi.org/10.1152/ajpheart.01170.2010) Corrias, Giles, Rodriguez (2011) Ionic mechanisms of electrophysiological properties and repolarization abnormalities in rabbit Purkinje fibers

## 2011 Grandi-Pandit-Voigt HA
Base: [Grandi 2010](#2010-grandi-hv)
| [Original matlab code](https://github.com/drgrandilab/Grandi-et-al-2011-Human-Atrial-Model)
| [In Myokit repo](https://github.com/myokit/models/blob/main/c/grandi-2011.mmt)
| [Paper](https://doi.org/10.1161/CIRCRESAHA.111.253955) Grandi*, Pandit*, Voigt* et al., Bers (2011) Human atrial action potential and Ca model; sinus rhythm and chronic atrial fibrillation (*shared first authorship)

Modifications:
- Scaled gK1
- ...

## 2011 Heijman CV
Base: [Decker 2009](#2009-decker-cv)
| [Original matlab code](https://rudylab.wustl.edu/code-downloads/)
| [In Myokit repo](https://github.com/myokit/models/blob/main/c/heijman-2011.mmt)
| [Paper](https://doi.org/10.1016/j.yjmcc.2011.02.007) Heijman, Volders, Westra, Rudy (2011) Local control of beta-adrenergic stimulation; effects on ventricular myocyte electrophysiology and Ca transient

## 2011 Kharche MS
Base: [Zhang 2000](#2000-zhang-rs), [Kurata 2002](#2002-kurata-rs)
| [Paper](https://doi.org/10.1152/ajpheart.00143.2010) Kharche, Yu, Lei, Zhang (2011) A mathematical model of action potentials of mouse sinoatrial node cells with molecular bases

## 2011 Koivumaki HA
Base: [Nygren 1998](#1998-nygren-ha)
| [Paper](https://doi.org/10.1371/journal.pcbi.1001067) Koivumaki, Korhonen, Tavi (2011) Impact of Sarcoplasmic Reticulum Calcium Release on Calcium Dynamics and Action Potential Morphology in Human Atrial Myocytes; A Computational Study
| [In Myokit repo](https://github.com/myokit/models/blob/main/c/koivumaki-2011.mmt)

## 2011 Li CP
Base: [Decker 2009](#2009-decker-cv)
| [Original C++ code](https://rudylab.wustl.edu/code-downloads/)
| [Paper](https://doi.org/10.1161/CIRCRESAHA.111.246512) Li, Rudy (2011) A model of canine purkinje cell electrophysiology and Ca2 cycling; rate dependence, triggered activity, and comparison to ventricular myocytes

Known as: PRd

## 2011 Moreno HV
Base: [Ten Tusscher 2006](#2006-ten-tusscher-hv)
| [Paper](https://doi.org/10.1126/scitranslmed.3002588) Moreno, Zhu et al., Clancy (2011) A computational model to predict the effects of class I anti-arrhythmic drugs on ventricular rhythms

Modifications:
- New INa model (new WT and drug-bound)

## 2011 O'Hara HV
Base: [Livshitz 2009](#2009-livshitz-cv)
| [Original matlab and C++ code](https://rudylab.wustl.edu/code-downloads/)
| [In Myokit repo](https://github.com/myokit/models/blob/main/c/ohara-2011.mmt)
| [Paper](https://doi.org/10.1371/journal.pcbi.1002061) O'Hara, Virag, Varro, Rudy (2011) Simulation of the Undiseased Human Cardiac Ventricular Action Potential; Model Formulation and Experimental Validation

Bits:
- INaK from Smith 2004, with reparametrisation

## 2011 Tao LS
Base: [Zhang 2000](#2000-zhang-rs), [Kurata 2002](#2002-kurata-rs)
| [Paper](https://doi.org/10.1016/j.bpj.2011.05.069) Tao, Paterson, Smith (2011) A model of cellular cardiac-neural coupling that captures the sympathetic control of sinoatrial node excitability in normotensive and hypertensive rats

## 2012 Christel MS
Base: [Mangoni 2006](#2006-mangoni-ms)
| [Paper](https://doi.org/10.1113/jphysiol.2012.239954) Christel, Cardona et al., Lee (2012) Distinct localization and modulation of Cav12 and Cav13 L-type Ca channels in mouse sinoatrial node

## 2012 Davies CV
Base: [Benson 2008](#2008-benson-cv)
| [Original matlab code](https://journals.physiology.org/doi/suppl/10.1152/ajpheart.00808.2011)
| [Paper](https://doi.org/10.1152/ajpheart.00808.2011) Davies, Mistry et al., Abi-gerges (2012) An in silico canine cardiac midmyocardial action potential duration model as a tool for early drug safety assessment

## 2012 Morotti RV
Base: [Shannon 2004](#2004-shannon-rv)
| [Original matlab code](https://github.com/drgrandilab/Morotti-et-al-2012-Rabbit-Ventricular-Model-with-Updated-ICaL)
| [Paper](https://doi.org/10.1113/jphysiol.2012.231886) Morotti, Grandi et al., Bers (2012) Theoretical Study of L-type Ca2+ Current Inactivation Kinetics during Action Potential Repolarization and Early Afterdepolarizations

Modifications:
- ICaL model adapted and modified from Mahajan

## 2012 Paci He
Base: [Grandi 2009](#2009-grandi-hv)
| [Paper](https://doi.org/10.1186/1475-925x-11-61) Paci, Sartiani et al., Severi (2012) Mathematical modelling of the action potential of human embryonic stem cell derived cardiomyocytes

## 2012 Severi RS
Base: [Maltsev 2009](#2009-maltsev-hs)
| [Paper](https://doi.org/10.1113/jphysiol.2012.229435) Severi, Fantini, Charawi, DiFrancesco (2012) An updated computational model of rabbit sinoatrial action potential to investigate the mechanisms of heart rate modulation

Known as: SDiF

## 2012 Yaniv RS
Base: [Maltsev 2010](#2010-maltsev-rs)
| [Paper](https://doi.org/10.1371/journal.pone.0037582) Yaniv, Spurgeon et al., Lakatta (2012) Crosstalk between mitochondrial and sarcoplasmic reticulum Ca cycling modulates cardiac pacemaker cell automaticity

## 2012 Yang HV
Base: [O'Hara 2011](#2011-ohara-hv)
| [Updated C++ code](https://github.com/drgrandilab/Fogli-Iseppe-et-al-2021-TdP-prediction)
| [Paper](https://doi.org/10.3389/fphys.2012.00360) Yang, Clancy (2012) In silico Prediction of Sex-Based Differences in Human Susceptibility to Cardiac Ventricular Tachyarrhythmias

## 2012 Yang MV
Base: [Bondarenko 2004](#2004-bondarenko-mv)
| [Original matlab code](https://github.com/saucermanlab/model-archive)
| [Paper](https://doi.org/10.1016/j.yjmcc.2011.12.015) Yang, Saucerman (2012) Phospholemman is a negative feed-forward regulator of Ca in beta-adrenergic signaling, accelerating beta-adrenergic inotropy

## 2013 Colman HA
Base: [Courtemanche 1998](#1998-courtemanche-ha)
| [Paper](https://doi.org/10.1113/jphysiol.2013.254987) Colman, Aslanidi et al., Zhang (2013) Pro-arrhythmogenic effects of atrial fibrillation-induced electrical remodelling: insights from the three-dimensional virtual human atria

## 2013 Paci Hi
Base: [Paci 2012](#2012-paci-he)
| [In Myokit repo](https://github.com/myokit/models/blob/main/c/paci-2013.mmt)
| [Paper](https://doi.org/10.1007/s10439-013-0833-3) Paci, Hyttinen, Aalto-Setala, Severi (2013) Computational Models of Ventricular and Atrial-Like Human Induced Pluripotent Stem Cell Derived Cardiomyocytes

## 2013 Voigt-Heijman HA
Base: [Grandi 2011](#2011-grandi-pandit-voigt-ha)
| [In Myokit repo](https://github.com/myokit/models/blob/main/c/voigt-2013.mmt)
| [Paper](https://doi.org/10.1016/j.yjmcc.2013.03.011) Voigt, Heijman et al., Dobrev (2013) Impaired Na-dependent regulation of acetylcholine-activated inward-rectifier K current modulates AP rate dependence in cAF

Modifications:
- Added IKAch (Kneller et al. 2002)
- Replaced INa with Courtemanche 1998 one
- Modified IK1 (changed gK1 and a)

## 2013a Yaniv RS
Base: [Yaniv 2012](#2012-yaniv-rs)
| [Paper](https://doi.org/10.1016/j.yjmcc.2013.04.026) Yaniv, Sirenko et al., Lakatta (2013) New evidence for coupled clock regulation of the normal automaticity of sinoatrial nodal pacemaker cells; bradycardic effects of ivabradine are linked to suppression of intracellular Ca cycling

## 2013b Yaniv RS
Base: [Maltsev 2009](#2009-maltsev-rs)
| [Paper](https://doi.org/10.1016/j.bpj.2013.08.024) Yaniv, Stern, Lakatta, Maltsev (2013) Mechanisms of beat-to-beat regulation of cardiac pacemaker cell function by Ca cycling dynamics

## 2014 Asakura HV
Base: [Grandi 2010](#2010-grandi-hv), CaRU reduction used by [Greenstein 2006](#2006-greenstein-cv)
| [Original visual basic code](http://www.eheartsim.com/?wpdmdl=244)
| [Paper](https://doi.org/10.1016/j.pbiomolbio.2014.08.008) Asakura, Cha et al., Noma (2014) EAD and DAD mechanisms analyzed by developing a new human ventricular cell model

Known as: HuVECI (this terminology starts with Himeno 2015)

Note: This and subsequent huvec models use an iterative procedure to implement calcium buffering, which makes it difficult to replicate in modelling frameworks.

Modifications:
- Contraction from Negroni and Lascano, 2008
- Hinch 2004 approximation for LCC-RyR coupling
- INa and INaL: mode-switching causes fixed fractions INa and INaL "mode"
- IK1 from Ishihara & Yan 2007 and Yan & Ishihara 2005
- ...

## 2014 Bondarenko MV
Base: [Bondarenko 2004](#2004-bondarenko-mv)
| [Paper](https://doi.org/10.1371/journal.pone.0089113) Bondarenko (2014) A compartmentalized mathematical model of the beta1-adrenergic signaling system in mouse ventricular myocytes

Modifications:
- Adds extensive beta1-adrenergic signalling

## 2014 Chang HA
Base: [Grandi 2011](#2011-grandi-pandit-voigt-ha)
| [Original OpenCARP code](https://doi.org/10.6084/m9.figshare.1201512)
| [Paper](https://doi.org/10.1371/journal.pcbi.1004011) Chang, Bayer, Trayanova (2014) Disrupted calcium release as a mechanism for atrial alternans associated with human atrial fibrillation

## 2014 Davies MA
Base: [Bondarenko 2004](#2004-bondarenko-mv)
| [Paper](https://doi.org/10.1161/JAHA.113.000340) Davies, Jin et al., Lei (2014) Mkk4 is a negative regulator of the transforming growth factor beta 1 signaling associated with atrial remodeling and arrhythmogenesis with age

## 2014 Morotti MV
Base: [Soltis 2010](#2010-soltis-rv)
| [Original matlab code](https://github.com/drgrandilab/Morotti-et-al-2014-Mouse-Ventricular-Model)
| [Paper](https://doi.org/10.1113/jphysiol.2013.266676) Morotti, Edwards et al., Grandi (2014) A novel computational model of mouse myocyte electrophysiology to assess the synergy between Na+ loading and CaMKII

## 2014 Yang MV
Base: [Yang 2012 mouse](#2012-yang-mv)
| [Original matlab code](https://github.com/saucermanlab/model-archive)
| [Paper](https://doi.org/10.1016/j.yjmcc.2013.11.001) Yang, Polanowska-Grabowska et al., Saucerman (2014) PKA catalytic subunit compartmentation regulates contractile and hypertrophic responses to beta-adrenergic signaling

## 2015 Himeno HV
Base: [Asakura 2014](#2014-asakura-hv)
| [Original (HuVECII) visual basic code](http://www.eheartsim.com/?wpdmdl=280)
| [Official C](http://www.eheartsim.com/?wpdmdl=442)
| [Updated (HuVECIII, 2017) visual basic](http://www.eheartsim.com/?wpdmdl=500)
| [Paper](https://doi.org/10.1016/j.bpj.2015.06.017) Himeno, Asakura et al., Noma (2015) A human ventricular myocyte model with a refined representation of excitation-contraction coupling

Known as: HuVEC, or HuVECII

## 2015 Negroni RV
Base: [Shannon 2004](#2004-shannon-rv), [Soltis 2010](#2010-soltis-rv)
| [Original matlab code](https://github.com/drgrandilab/Negroni-et-al-2015-Rabbit-Ventricular-Model-with-Myofilament-Contraction)
| [Paper](https://doi.org/10.1016/j.yjmcc.2015.02.014) Negroni, Morotti et al., Bers (2015) Beta-adrenergic effects on cardiac myofilaments and contraction in an integrated rabbit ventricular myocyte model

Bits:
- New myofilament contraction
- Currents, Ca-handling, Na-handling: Shannon 2004
- CaMKII, PKA: Soltis 2010

## 2015 Paci Hi
Base: [Paci 2013](#2013-paci-hi)
| [Paper](https://doi.org/10.1111/bph.13282) Paci, Hyttinen, Rodriguez, Severi (2015) Human induced pluripotent stem cell-derived versus adult cardiomyocytes; an in silico electrophysiological study on ionic current block effects

## 2015 Schmidt HA
Base: [Voigt-Heijman 2013](#2013-voigt-heijman-ha)
| [Paper](https://doi.org/10.1161/CIRCULATIONAHA.114.012657) 

Modifications:
- Added K2p3.1 current

## 2015 Yaniv RS
Base: Probably [Yaniv 2013a](#2013a-yaniv-rs)
| [Paper](https://doi.org/10.1016/j.yjmcc.2015.07.024) Yaniv, Ganesan et al., Lakatta (2015) Real-time relationship between PKA biochemical signal network dynamics and increased action potential firing rate in heart pacemaker cells

## 2016 Behar RS
Base: [Yaniv 2015](#2015-yaniv-rs)
| [Paper](https://doi.org/10.3389/fphys.2016.00419) Behar, Ganesan, Zhang, Yaniv (2016) The autonomic nervous system regulates the heart rate through cAMP-PKA dependent and independent coupled-clock pacemaker cell mechanisms

## 2016 Gattoni LV
Base: [Pandit 2001](#2001-pandit-lv)
| [Paper]() Gattoni, Roe et al., Smith (2016) The calcium-frequency response in the rat ventricular myocyte; an experimental and modelling study

Modifications:
- Hinch 2004 Ca dynamics
- Lewalle et al. 2014 INaK model (despite Smith as co-author?)

## 2016 Majumder RAd
Base: [Korhonen 2009](#2009-korhonen-ld)
| [Paper](https://doi.org/10.1371/journal.pcbi.1004946) Majumder et al., Pijnappels, Panfilov (2016) A Mathematical Model of Neonatal Rat Atrial Monolayers with Constitutively Active Acetylcholine-Mediated K Current

## 2016 Morotti HA
Base: [Grandi 2011](#2011-grandi-pandit-voigt-ha)
| [Original matlab code](https://github.com/drgrandilab/Morotti-et-al-2016-Human-Atrial-Model-with-Updated-INa)
| [Paper](https://doi.org/10.1016/j.yjmcc.2015.07.030) Morotti, McCulloch et al., Grandi (2016) Atrial-selective targeting of arrhythmogenic phase-3 earlyafterdepolarizations in human myocytes

Modifications:
- Markov model of INa with drug block adapted from Grandi 2007 and Wagner 2009 & Moreno 2013

## 2016 Passini HV
Base: [O'Hara 2011](#2011-ohara-hv)
| [Paper](https://doi.org/10.1016/j.yjmcc.2015.09.003) Passini, Minchole et al. Bueno-Orovio (2016 ) Mechanisms of Pro-Arrhythmic Abnormalities in Ventricular Repolarisation and Anti-Arrhythmic Therapies in Human Hypertrophic Cardiomyopathy

Modifications:
- Rescaled Ito
- Changed concentrations
- Constant EK
- Shifted act/inact curves INa, INaL, IK1
- Modified INa steady states

## 2016 Pohl HS
Base: [Dokos 1996a](#1996a-dokos-rs)
| [Paper](https://doi.org/10.1088/2057-1976/2/3/035006) Pohl, Wachter, Hatam, Leonhardt (2016) A computational model of a human single sinoatrial node cell

## 2016 Varela CA
Base: [Ramirez 2000](#2000-ramirez-ca)
| [Paper](https://doi.org/10.1371/journal.pcbi.1005245) Varela, Colman, Hancox, Aslanidi (2016) Atrial Heterogeneity Generates Re-entrant Substrate during Atrial Fibrillation and Anti-arrhythmic Drug Action

## 2017 Aguilar HA
Base: [Courtemanche 1998](#1998-courtemanche-ha)
| [Paper](https://doi.org/10.1016/j.bpj.2017.03.022) Aguilar, Feng et al., Nattel (2017) Rate-dependent role of IKur in human atrial repolarization and atrial fibrillation maintenance

## 2017 Bartos RV
Base: [Negroni 2015](#2015-negroni-rv)
| [Original matlab code](https://github.com/drgrandilab/Bartos-et-al-2017-Rabbit-Ventricular-Model-with-Updated-IKs)
| [Paper](https://doi.org/10.1113/JP273676) Bartos, Morotti et al., Bers (2017) Quantitative analysis of the Ca2+-dependent regulation of delayed rectifier K+ current IKs in rabbit ventricular myocytes

Bits:
- New IKs with Ca regulation

## 2017 Behar MS
Base: [Kharche 2011](#2011-kharche-ms)
| [Paper](https://doi.org/10.1085/jgp.201711792) Behar, Yaniv (2017) Age-related pacemaker deterioration is due to impaired intracellular and membrane mechanisms; insights from numerical modeling

## 2017 Colman HA
Base: [Colman 2013](#2013-colman-ha)
| [Paper](https://doi.org/10.1371/journal.pcbi.1005587) Colman, Ni et al., Zhang (2017) In silico assessment of genetic variation in KCNA5 reveals multiple mechanisms of human atrial arrhythmogenesis

## 2017 Dutta HV
Base: [Li 2017](#2017-li-hv)
| [Original code](https://github.com/FDA/CiPA/blob/master/AP_simulation/models/newordherg_qNet.c)
| [Official CellML](https://models.cellml.org/e/4e8/ohara_rudy_cipa_v1_2017.cellml/view)
| [In Myokit repo](https://github.com/myokit/models/blob/main/c/ohara-cipa-v1-2017.mmt)
| [Paper](https://doi.org/10.3389/fphys.2017.00616) Dutta, Chang et al., Li (2017) Optimization of an in-silico cardiac cell model for proarrhythmia risk assessment

Known as: ORd-cipa-v1

Modifications:
- Rescaling of conductances to better predict drug effects

## 2017 Ellinwood HA
Base: [Morotti 2016](#2016-morotti-ha)
| [Original matlab code](https://github.com/drgrandilab/Ellinwood-et-al-2017-Human-Atrial-Model-with-Updated-IKur)
| [In Myokit repo](https://github.com/myokit/models/blob/main/c/ellinwood-2017.mmt)
| [Paper](https://doi.org/10.1063/1.5000226) Ellinwood, Dobrev, Morotti, Grandi (2017) Revealing kinetics and state-dependent binding properties of IKur-targeting drugs that maximize atrial fibrillation selectivity [Erratum](https://doi.org/10.1063/1.5007051)

Modifications:
- Markov model of IKur with drug block adapted from Zhou et al. (PLoS ONE 2012; e42295)

## 2017 Fabbri HS
Base: [Severi 2012](#2012-severi-rs)
| [Official CellML](https://www.mcbeng.it/en/downloads/software/hap-san.html)
| [Physiome reproduction paper](https://doi.org/10.36903/physiome.16550526)
| [In Myokit repo](https://github.com/myokit/models/blob/main/c/fabbri-2017.mmt)
| [Paper](https://doi.org/10.1113/JP273259) Fabbri, Fantini, Wilders, Severi (2017) Computational analysis of the human sinus node action potential; model development and effects of mutations

Known as: FWS

## 2017 Li HV
Base: [O'Hara 2011](#2011-ohara-hv)
| [Paper](https://doi.org/10.1161/CIRCEP.116.004628) Li, Dutta et al., Colatsky (2017) Improving the in silico assessment of proarrhythmia risk by combining hERG channel-drug binding kinetics and multichannel pharmacology
Known as: IKr-dynamic ORd model, original IKr-dyn ORd model

Modifications:
- New IKr model with drug trapping

## 2017 Ni HA
Base: [Colman 2017](#2017-colman-ha)
| [In Myokit repo](https://github.com/myokit/models/blob/main/c/ni-2017.mmt)
| [Paper](https://doi.org/10.3389/fphys.2017.00946) Ni, Whittaker et al., Zhang (2017) Synergistic Anti-arrhythmic Effects in Human Atria with Combined Use of Sodium Blockers and Acacetin

Bits:
- Calcium subspaces based on Koivumaki 2011

## 2017 Paci Hi
Base: [Paci 2015](#2015-paci-hi)
| [Paper](https://doi.org/10.1016/j.hrthm.2017.07.026) Paci, Passini et al., Rodriguez (2017) Phenotypic Variability in LQT3 Human induced pluripotent stem cell-derived cardiomyocytes and their response to antiarrhythmic pharmacologic therapy; an in silico approach

## 2017 Surdo MV
Base: [Morotti 2014](#2014-morotti-mv) 
| [Original matlab code](https://github.com/drgrandilab/Surdo-et-al-2017-Mouse-Ventricular-Model-with-Myofilament-Contraction)
| [Paper](https://doi.org/10.1038/ncomms15031) Surdo, Berrera et al., Zaccolo (2017) FRET biosensor uncovers cAMP nano-domains at beta-adrenergic targets that dictate precise tuning of cardiac contractility

Bits:
- Myofilament contraction from Negroni 2015

## 2018 Bai HA
Base: [Ten Tusscher 2006](#2006-ten-tusscher-hv)
| [Official CellML](https://models.cellml.org/workspace/520)
| [In Myokit repo](https://github.com/myokit/models/blob/main/c/bai-2018.mmt)
| [Paper](https://doi.org/10.1038/s41598-018-33958-y) Bai, Gladding et al., Zhao (2018) Ionic and cellular mechanisms underlying TBX5-PITX2 insufficiency-induced atrial fibrillation; Insights from mathematical models of human atrial cells

Known as: TPA

## 2018 Colman HA
Base: [Courtemanche 1998](#1998-courtemanche-ha), [Nygren 1998](#1998-nygren-ha), [Chang 2014](#2014-chang-ha)
| [Original C++ code](https://github.com/michaelcolman/hAM_WL)
| [Paper](https://doi.org/10.3389/fphys.2018.01211) Colman, Saxena, Kettlewell, Workman (2018) Description of the Human Atrial Action Potential Derived From a Single, Congruent Data Source; Novel Computational Models for Integrated Experimental-Numerical Study of Atrial Arrhythmia Mechanisms

## 2018 Koivumaki Hi
Base: [Korhonen 2010](#2010-korhonen-md), [Paci 2015](#2015-paci-hi)
| [Original matlab code](https://www.researchgate.net/publication/323308198_hiPSC-CM_model)
| [Paper](https://doi.org/10.3389/fphys.2018.00080) Koivumaki, Naumenko et al., Tavi (2018) Structural Immaturity of Human iPSC-Derived Cardiomyocytes; In Silico Investigation of Effects on Function and Disease Modeling

## 2018 Paci Hi
Base: [Paci 2017](#2017-paci-hi)
| [In Myokit repo](https://github.com/myokit/models/blob/main/c/paci-2018.mmt)
| [Paper](https://doi.org/10.3389/fphys.2018.00709) Paci, Polonen et al., Hyttinen (2018) Automatic optimization of an in silico model of human iPSC derived cardiomyocytes recapitulating calcium handling abnormalities

## 2019 Loewe HS
Base: [Fabbri 2017](#2017-fabbri-hs)
| [Official CellML](https://models.physiomeproject.org/workspace/58f)
| [Paper](https://doi.org/10.1016/j.bpj.2019.07.037) Loewe, Lutz et al., Severi (2019) Hypocalcemia-Induced Slowing of Human Sinus Node Pacemaking

## 2019 Kernik Hi
Base: [Shannon 2004](#2004-shannon-rv), [Ten Tusscher 2004](#2004-ten-tusscher-hv), [Maltsev 2009](#2009-maltsev-hs)
| [In Myokit repo](https://github.com/myokit/models/blob/main/c/kernik-2019.mmt)
| [Paper](https://doi.org/10.1113/jp277724) Kernik, Morotti et al., Clancy (2019) A computational model of induced pluripotent stem‐cell derived cardiomyocytes incorporating experimental variability from multiple data sources

## 2019 Tomek HV
Base: [O'Hara 2011](#2011-ohara-hv)
| [Original Matlab and official CellML code](https://github.com/jtmff/torord/commit/4ffab13b48f0923d38b0315f26be466a6fad8b70)
| [Paper](https://doi.org/10.7554/elife.48890) Tomek, Bueno-Orovio et al., Rodriguez (2019) Development, calibration, and validation of a novel human ventricular myocyte model in health, disease, and drug block

## 2020 Alghamdi LS
Base: [Tao 2011](#2011-tao-ls)
| [Paper](https://doi.org/10.3389/fphys.2020.546508) Alghamdi, Boyett, Hancox, Zhang (2020) Cardiac pacemaker dysfunction arising from different studies of ion channel remodeling in the aging rat heart

## 2020 Asfaw MA
Base: [Bondarenko 2014](#2014-bondarenko-mv)
| [Original fortran code](https://figshare.com/articles/code/FORTRAN_code_for_mouse_atrial_myocytes/11628549)
| [Paper](https://doi.org/10.1152/ajpheart.00460.2019) Asfaw, Tyan, Glukhov, Bondarenko (2020) A compartmentalized mathematical model of mouse atrial myocytes

Modifications:
- Converted from ventricular model

## 2020 Balakina-Vikulova HV
Base: [Ten Tusscher 2006](#2006-ten-tusscher-hv), [Sulman 2008](#2008-sulman-gv)
| [Paper](https://doi.org/10.1186/s12576-020-00741-6) Balakina-Vikulova, Panfilov, Solovyova, Katsnelson (2020) Mechano-calcium and mechano-electric feedbacks in the human cardiomyocyte analyzed in a mathematical model

## 2020 Bartolucci HV
Base: [Dutta 2017](#2017-dutta-hv)
| [Original matlab code](https://www.mcbeng.it/en/downloads/software/16-bps2020-model.html)
| [Official CellML](https://models.physiomeproject.org/workspace/5fd)
| [In Myokit repo](https://github.com/myokit/models/blob/main/c/bartolucci-2020.mmt)
| [Paper](https://doi.org/10.3389/fphys.2020.00314) Bartolucci, Passini et al., Severi (2020) Simulation of the effects of extracellular calcium changes leads to a novel computational model of human ventricular action potential with a revised calcium handling

Known as: BPS2020

Modifications:
- New ICaL formulation (from Passini 2012 CINC)
- ...

## 2020 Paci Hi
Base: [Paci 2018](#2018-paci-hi)
| [In Myokit repo](https://github.com/myokit/models/blob/main/c/paci-2020.mmt)
| [Paper](https://doi.org/10.1016/j.bpj.2020.03.018) Paci, Passini et al., Entcheva (2020) All-Optical Electrophysiology Refines Populations of In Silico Human iPSC-CMs for Drug Evaluation

## 2020 Sengul Ayan LV
Base: [Jafri 1998](#1998-jafri-gv) but mostly new
| [Paper]() Sengul Ayan, Sircan et al., Yaras (2020) Mathematical model of the ventricular action potential and effects of isoproterenol-induced cardiac hypertrophy in rats

Modifications:
- 5 parameter reformulation of most currents

## 2020 Tomek HV
Base: [Tomek 2019](#2019-tomek-hv)
| [Original Matlab and official CellML code](https://github.com/jtmff/torord)
| [In Myokit repo](https://github.com/myokit/models/blob/main/c/tomek-2020.mmt)
| [Paper 1](https://doi.org/10.7554/elife.48890) Tomek, Bueno-Orovio et al., Rodriguez (2019) Development, calibration, and validation of a novel human ventricular myocyte model in health, disease, and drug block
| [Paper 2](https://doi.org/10.1101/2020.06.01.127043) Tomek, Bueno-Orovio, Rodriguez (2020) ToR-ORd-dynCl; an update of the ToR-ORd model of human ventricular cardiomyocyte with dynamic intracellular chloride
Known as: ToR-ORd-dynCl

Modifications:
- Chloride homeostasis

## 2020 Trovato HP
Base: [O'Hara 2011](#2011-ohara-hv), [Li 2011](#2011-li-cp)
| [Original Matlab and official CellML code](https://www.cs.ox.ac.uk/insilicocardiotox/purkinje-models)
| [In Myokit repo](https://github.com/myokit/models/blob/main/c/trovato-2020.mmt)
| [Paper](https://doi.org/10.1016/j.yjmcc.2020.04.001) Trovato, Passini et al., Rodriguez (2020) Human Purkinje in silico model enables mechanistic investigations into automaticity and pro-arrhythmic abnormalities

Modifications:
- INa from Passini 2016
- ...

## 2021 Akwaboah Hi
Base: [Kurata 2002](#2002-kurata-rs) and [Courtemanche 1998](#1998-courtemanche-ha)
| [In Myokit repo](https://github.com/myokit/models/blob/main/c/akwaboah-2021-corrected.mmt)
| [Paper](https://doi.org/10.3389/fphys.2021.675867) Akwaboah, Tsevi et al., Deo (2021) An in silico hiPSC-Derived Cardiomyocyte Model Built With Genetic Algorithm

Modifications:
- INa from Luo 1991, with partial reparameterisation
- Ito from Grandi 2010, with partial reparametrisation
- IKr from Kurata 2002, with partial reparametrisation
- If from Stewart 2009, with partial reperametrisation
- ICaL from Kurata 2002, with partial reparametrisation
- IKs from Courtemanche 1998
- IKur from Courtemanche 1998
- INaK from Courtemanche 1998
- INaCa from Courtemanche 1998
- IKACh from Kurata 2002
- IK1 from Grandi 2010
- IbCa from Courtemanche 1998
- IbNa from Courtemanche 1998
- IpCa from Courtemanche 1998
- Calcium handling from Kurata 2002

## 2021 Fogli Iseppe HV
Base: [Yang 2012](#2012-yang-hv)
| [Original C++ code](https://github.com/drgrandilab/Fogli-Iseppe-et-al-2021-TdP-prediction)
| [Paper](https://doi.org/10.1002/cpt.2240) Fogli Iseppe, Ni et al., Grandi (2021) Sex-specific classification of drug-induced Torsade de Pointes susceptibility using cardiac simulations and machine learning

## 2021 Gaur PV
Base: [O'Hara 2011](#2011-ohara-hv), but many new parts
| [Original openCARP code](https://journals.plos.org/ploscompbiol/article?id=10.1371/journal.pcbi.1009137#sec022) and official Myokit, and CellML code
| [Paper](https://doi.org/10.1371/journal.pcbi.1009137) Gaur, Qi et al., Vigmond (2021) A computational model of pig ventricular cardiomyocyte electrophysiology and calcium handling; Translation from pig to human electrophysiology

## 2021 Hoekstra HS
Base: [Fabbri 2017](#2017-fabbri-hs)
| [Paper](https://doi.org/10.1016/j.pbiomolbio.2021.05.006) Hoekstra, van Ginneken, Wilders, Verkerk (2021) HCN4 current during human sinoatrial node-like action potentials

## Morotti 2021 HV
Base: [Grandi 2010](#2010-grandi-hv)
| [Original code](https://github.com/drgrandilab/Morotti-et-al-2021-Cross-species-translators-of-electrophysiological-response)
| [Paper](https://www.science.org/doi/10.1126/sciadv.abg0927) Morotti, Liu et al., Grandi (2024) Quantitative cross-species translators of cardiac myocyte electrophysiology; Model training, experimental validation, and applications

Modifications:
- Included (and adapted) PKA and CaMKII signaling from Soltis-Saucerman

## 2021 Morotti MS
Base: [Kharche 2011](#2011-kharche-ms)
| [Original matlab code](https://github.com/drgrandilab/Morotti-et-al-2021-mouse-sinoatrial-model)
| [Paper](https://doi.org/10.3390/ijms22115645) Morotti, Ni et al., Grandi (2021) Intracellular Na+ Modulates Pacemaking Activity in Murine Sinoatrial Node Myocytes: An In Silico Analysis

## 2021 Morotti MV
Base: [Surdo 2017](#2017-surdo-mv) 
| [Original code](https://github.com/drgrandilab/Morotti-et-al-2021-Cross-species-translators-of-electrophysiological-response)
| [Paper](https://www.science.org/doi/10.1126/sciadv.abg0927) Morotti, Liu et al., Grandi (2024) Quantitative cross-species translators of cardiac myocyte electrophysiology; Model training, experimental validation, and applications

Modifications:
- Updated PKA signaling
- Improved implementation of ODE calculation

## Morotti 2021 RV
Base: [Bartos 2017](#2017-bartos-rv)
| [Original code](https://github.com/drgrandilab/Morotti-et-al-2021-Cross-species-translators-of-electrophysiological-response)
| [Paper](https://www.science.org/doi/10.1126/sciadv.abg0927) Morotti, Liu et al., Grandi (2024) Quantitative cross-species translators of cardiac myocyte electrophysiology; Model training, experimental validation, and applications

Modifications:
- Updated PKA signaling
- Improved implementation of ODE calculation

## 2022 Bartolucci HV
Base: [Bartoluci 2020](#2020-bartolucci-hv)
| [Paper](https://doi.org/10.3389/fphys.2022.906146) Bartolucci, Forouzandemehr, Severi, Paci (2022) A Novel In Silico Electromechanical Model of Human Ventricular Cardiomyocyte

Known as: BPSLand

Modifications:
- Added Land 2017 contraction model
- ...

## 2022 Doste HV
Base: [Tomek 2020](#2020-tomek-hv), [Heijman 2011](#2011-heijman-cv)
| [Original matlab code](https://github.com/rdoste/ToR-ORd-BARS)
| [Paper](https://doi.org/10.1016/j.yjmcc.2022.08.361) Doste, Coppini, Bueno-Orovio (2022) Remodelling of potassium currents underlies arrhythmic action potential prolongation under beta-adrenergic stimulation in hypertrophic cardiomyopathy

Modifications:
- Added beta-adrenergic signalling

## 2022 Kohjitani Hi
Base: [Himeno 2015](#2015-himeno-hv)
| Code not quite available, point to e-Heart
| [Paper](https://doi.org/10.1038/s41598-022-23398-0) Kohjitani, Koda et al., Kimura (2022) Gradient-based parameter optimization method to determine membrane ionic current composition in human induced pluripotent stem cell-derived cardiomyocytes

## 2022 Mahzar HA
Base: [Koivumaki 2011](#2011-koivumaki-ha), Regazzoni 2020
| [Paper](https://doi.org/10.1113/JP283974) Mazhar, Bartolucci et al., Severi (2023) A detailed mathematical model of the human atrial cardiomyocyte: integration of electrophysiology and cardiomechanics

Known as: MBS2023

## 2022 Moise RS
Base: [Severi 2012](#2012-severi-rs)
| [Original matlab code](https://github.com/SHWeinberg/SAN_FeedbackModel)
| [Paper](https://doi.org/10.1016/j.bpj.2023.03.024) Moise, Weinberg (2022) Emergent Electrical Activity, Tissue Heterogeneity, and Robustness in a Calcium Feedback Regulatory Model of the Sinoatrial Node

## 2023 Heijman HA
Base: [Grandi 2011](#2011-grandi-pandit-voigt-ha)
| [Original matlab code](https://github.com/drgrandilab/Heijman-et-al-2023-Human-Atrial-Model)
| [Paper](https://doi.org/10.1161/CIRCRESAHA.122.321858) Heijman, Zhou et al., Dobrev (2023) Enhanced Ca-Dependent SK-Channel Gating and Membrane Trafficking in Human Atrial Fibrillation

## 2023 Herrera HA
Base: [Ellinwood 2017](#2017-ellinwood-ha)
| [Original matlab code](https://github.com/drgrandilab/Herrera-et-al-2023-Human-Atrial-Model)
| [Paper](https://doi.org/10.1152/ajpheart.00362.2023) Herrera, Zhang et al., Morotti (2023) Dual effects of the small-conductance Ca-activated K current on human atrial electrophysiology and Ca-driven arrhythmogenesis; an in silico study

Also cites a 2020 Ni paper, but that refers to Ellinwood.

## 2023 Ni HA
Base: [Morotti 2017](#2016-morotti-ha)
| [Original C++ code](https://github.com/drgrandilab/Ni-et-al-2023-Human-Atrial-Signaling-Model)
| [Paper](https://doi.org/10.1093/cvr/cvad118) Ni, Morotti et al., Grandi (2023) Integrative human atrial modelling unravels interactive PKA and CaMKII signalling as key determinants of atrial arrhythmogenesis

## 2024 Botti Hi
Base: [Paci 2020](#2020-paci-hi)
| [Original matlab code](https://github.com/bottiso/AL_hiPSC_ionic_model)
| [Paper](https://doi.org/10.1016/j.compbiomed.2024.108899) Botti, Bartolucci et al., Severi (2024) A novel ionic model for matured and paced atrial-like human iPSC-CMs integrating IKur and IKCa currents

Modifications:
- Added IKur and IKCa
- Rescaled parameters to match atrial data

