# Part IX   Special Processing  and Assembly  Technologies  

# Rapid Prototyping  and Additive  Manufacturing  

# Chapter Contents  

32.1 Fundamentals of Rapid Prototyping  and Additive Manufacturing  

32.2 Additive Manufacturing Processes  

32.2.1 Liquid-Based Systems 32.2.2 Powder-Based Systems 32.2.3 Molten Material Systems 32.2.4 Solid Sheet-Based Systems  

32.3 Cycle Time and Cost Analysis  

32.4 Additive Manufacturing Applications In this part of the book, a collection of processing  and assembly technologies is discussed that do not  ﬁ  t neatly into the classiﬁ  cation scheme in Figure 1.5.  They are techno  logies that have been adapted from  conventional manufacturing and assembly operations  or developed from scratch to serve special functions  or needs in design and manufacturing. Rapid proto- typing and additive manufacturing, covered in the  present chapter, are a collection of processes used to  fabricate parts directly from a computer-aided design  (CAD) model. Chapters 33 and 34 discuss technolo- gies used in electronics manufacturing, an activity of  signiﬁ  cant economic importance. Chapter 33 covers  integrated circuit processing, and Chapter 34 covers  electronics assembly and packaging. Chapters 35 and  36 survey some of the technologies used to produce  very small parts and products. Chapter 35 describes  microfabrication technologies used to produce items  measured in microns  $(10^{-6}\mathrm{~m})$ , whereas Chapter 36  discusses nano  fabrication technologies for producing  items measured in nanometers  $(10^{-9}\,\mathrm{m})$ . The pro  cesses  covered in these ﬁ  ve chapters are relatively new.  Rapid prototyping dates from about 1988. Modern  electro  nics production techniques date from around  

1960 (Historical Note 33.1), although dramatic advances have been made in elec- tronics processing since that time. The microfabrication technologies discussed in  Chapter 35 followed soon after integrated circuit processing. Finally, nanofabrica- tion represents an emerging ﬁ  eld today that dates from the 1990s.  

Rapid prototyping  (RP) is a family of technologies used to fabricate engineer- ing prototypes of parts in minimum possible lead time based on a computer-aided  design (CAD) model of the item. The traditional method of fabricating a proto- type part is machining, which can require signiﬁ  cant lead times—up to several  weeks, sometimes longer, depending on part complexity, difﬁ  culty in ordering  materials, and scheduling production equipment. A number of rapid prototyping  techniques are now available that allow a part to be produced in hours or days  rather than weeks, given that a computer model of the part has been generated  on a CAD system.  

As the RP technologies have evolved, they are increasingly being used to pro- duce parts, not just prototypes, and a more general term has emerged:  Additive  manufacturing  (AM), which refers to the same technologies used in RP. All of  these technologies work by adding layers of material to an existing part or sub- strate, so that the item is gradually built one layer at a time; hence the word “addi- tive.” One might say that rapid prototyping is a subset of additive manufac  turing  when the purpose is to fabricate a physical model of a newly designed part. Other  terms often used synonymously with AM include direct digital manufac  turing,  rapid manufacturing, layer-based manufacturing, and solid free-form fabrication.  A short history of rapid prototyping and additive manufacturing is presented in  Historical Note 32.1.  

# H istorical  N ote  32.1   Rapid Prototyping and Additive Manufacturing [4]  

It should be noted that the historical development  of rapid prototyping and additive manufacturing is  based on several enabling technologies, including  inte  grated circuits, computers, in particular computer  graphics and computer-aided design, lasers, ink-jet  and other printing technologies, and highly accurate  positioning systems, to name the most obvious.  Without these enablers, RP and AM would not be  technically feasible.  

The beginnings of rapid prototyping as an identi- ﬁ  able technical area occurred in the mid-1980s when  similar patents were ﬁ  led by researchers in Japan,  France, and the United States. What these patent  applications had in common was the idea of con- structing a three-dimensional object by adding a  seque  nce of layers, one on top of the previous. The  patent by Charles Hull is considered the most signiﬁ  - cant because it resulted in the commercial develop- ment of stereo lithography (SL) and the formation  of the company 3D Systems, Inc. SL users a laser  beam to harden liquid photopolymers in a layer by  layer construction process.  

Several additional patents followed in 1986 for  Solid Ground Curing (SGC, Section 32.2.1); Selective  Laser Sintering (SLS, Section 32.2.2); and Laminated  Object Manufacturing (LOM, Section 32.2.4). SGC  exposed photopolymers through a physical mask;  SLS used lasers to sinter or melt powder layers; and  LOM cut paper sheets in the part building procedure.  These systems were commercially introduced by  three start-up companies, respectively, Cubital, DTM,  and Helisys. DTM was the only survivor; it merged  with 3D Systems in 2001.  

In 1989, Fused Deposition Modeling (FDM, Section  32.2.3) was patented, and the Stratasys Company was  formed to commercialize the technology. FDM uses  an extrusion process to add layers of material to an  exist  ing structure. In the same year,  Three-Dimensional  Printing (3DP , Section 32.2.2), which uses ink-jets to  deposit droplets of a binder onto layers of powdered  material, was patented by researchers at MIT . They  licensed the technology to several companies for  develop  ment and commercialization. In 1994, a similar  approach based on ink-jet technology was developed,  only it deposits the material itself to form layers rather  of the RP and AM technologies used today through- than a binder on powder. out the world. Even SGC and LOM are used in altered  The collection of processes discussed here, with  forms, although the companies that originally developed  reﬁ  nements over many years, constitute the majority  them were unsuccessful.  

# Fundamentals of Rapid Prototyping and  Additive Manufacturing  

The special need that motivated the development of rapid prototyping is that  product designers would like to have a physical model of a new part design rather  than a computer model or line drawing. The creation of a prototype is an integral  step in the design procedure. A  virtual prototype , which is a computer model of  the part design on a CAD system, may not be adequate for the designer to visual- ize the part. It certainly is not sufﬁ  cient to conduct real physical tests on the part,  although it is possible to perform simulated tests by ﬁ  nite element analysis or  other methods. Using one of the available RP technologies, a solid physical part  can be created in a relatively short time (hours if the company possesses the RP  equipment or days if the part fabrication must be contracted to an outside ﬁ  rm  specializing in RP). The designer can therefore visually examine and physically  feel the part and begin to perform tests and experiments to assess its merits and  shortcomings. By speeding up the process of fabricating part prototypes, the du- ration of the entire product design cycle is reduced.  

Available prototyping technologies can be divided into two basic categories:  (1) material removal processes, and (2) material addition processes. The  material  removal  $R P$  alternative involves machining, primarily milling and drilling, using  a dedicated Computer Numerical Control (CNC) machine that is available to the  design department on short notice. To use CNC, a part program must be prepared  from the CAD model (Section 37.3.3). The starting material is often a solid block  of wax, which is very easy to machine, and the part and chips can be melted and  resolidiﬁ  ed for reuse when the current prototype is no longer needed. Other start- ing materials can also be used, such as wood, plastics, or metals (e.g., a machinable  grade of aluminum or brass). The CNC machines used for rapid prototyping are  often small, and the terms  desktop milling  or  desktop machining  are sometimes  used when referring to them.  

The principal emphasis in this chapter is on  material-addition  technologies, all  of which add thin layers of material one at a time to build the physical part from  bottom to top. Advantages of these technologies over CNC machining include [4]:  (1) speed of part delivery, as has already been mentioned; (2) avoidance of the  CNC part programm  ing task, because the CAD model is the part program in RP;  and (3) complexity of part geometry is not an issue in additive manufacturing.  Considering this last point, the AM time advantage increases with the complexity  of the part geometry, because additive technologies operate the same whether the  part is simple or complex, whereas CNC planning must include decisions about  tooling, sequence, and access, and more machining is generally required for more  complex parts.  

![](images/6d1fa9b59e66c7b5e7c6c39d0e8ba4e962b204a3d3ff14dfdc6a76280cb89ef0.jpg)  
FIGURE 32.1  Conversion of a solid model of an object into layers (only one layer is shown).  

The common approach to prepare the control instructions (i.e., part program) in  all of the rapid prototyping and additive manufacturing technologies involves the  following steps [7]:  

1.  Geometric modeling . This consists of modeling the component on a CAD system  to deﬁ  ne its enclosed volume. Solid modeling is the preferred technique because  it provides a complete and unambiguous mathematical representation of the geo- metry. The important issue is to distinguish the interior (mass) of the part from its  exterior, and solid modeling provides for this distinction.

 2.  Tessellation of the geometric model .  In this step, the CAD model is converted into  a format that approximates its surfaces by triangles, with their vertices arranged to  distinguish the object’s interior from its exterior. The common tessellation format  used in rapid prototyping is STL 2 , which has become the de facto standard input  format for nearly all RP systems.

 3.  Slicing of the model into layers . In this step, the model in STL ﬁ  le format is  sliced into closely spaced parallel horizontal layers. Conversion of a solid model  into layers is illustrated in Figure 32.1. These layers are subsequently used by the  RP system to construct the physical model. By convention, the layers are formed  in the $x{-}y$  plane, and the layering procedure occurs in the $z$ -axis direction. For  each layer, a curing path is generated, called the STI ﬁ  le, which is the path that  will be followed by the RP system to cure (or otherwise solidify) the layer.  

Starting material forms in additive manufacturing include (1) liquid polymers  that are cured layer by layer into solid polymers, (2) powders that are aggregated  and bonded layer by layer, (3) molten materials that are solidiﬁ  ed layer by layer,  and (4) solid sheets that are laminated to create the solid part. Material types  include wax, polymers, metals, and ceramics.  

![](images/6d5c1c02394bdf1de12112a02f2148ec7875601de1c8a3fe536f15c7d182bd81.jpg)  
FIGURE 32.2  The  three basic layer  construction modes:  (a) point or spot mode,  (b) moving line mode,  and (c) layer mode.  

In addition to starting material, there are various layer-forming processes by  which each layer is created to build the part. These processes include (1) lasers,  (2) printing heads that operate using ink-jet technology, and (3) extruder heads.  Other processes are based on electron beams, cutting knives, ultraviolet light  systems, and so on.  

In addition to the layer forming process, several modes of operation are used,  called channel modes. The three basic channel modes are (1) a moving point or mov- ing spot; for example, a laser spot moving in an $x$ - $\cdot y$  plane to chemically solidify a layer  of liquid polymer by photo polymerization; (2) a moving line consisting of a linear  array of spots that sweeps across the entire layer in one translational motion, some- what like the way ink-jet printers work; and ﬁ  nally (3) a layer mode using a mask  projection system in which the entire layer is created all at the same time. The time to  complete each layer can be signiﬁ  cant using the moving-point mode. The moving line  mode of operation is faster, and the layer mode is theoretically the fastest. The three  channel modes are depicted in Figure 32.2.  

A summary of these combinations of starting material forms and types, layer- forming processes, and channel modes is presented in Table 32.1 together with repre- sentative AM systems.  

TABLE •  32.1  Additive Manufacturing Starting Materials, Layer-Forming Processes, and Channel Modes. 
![](images/4e8132ca1777390bfb75c101e8e058179a61c8103fbdc41885497cba361b0cf7.jpg)  
Key: $\mathrm{SL}=$  stereo lithography, $\mathrm{{MPSL}}={}$  mask projection stereo lithography, $\mathrm{SL}S=$  selective laser sintering,  $3\mathrm{D}\mathrm{P}=$  three-dimensional  printing, $\mathrm{FDM}=$  fused deposition modeling, $\mathrm{\bfDDM}=$ droplet deposition manufacturing, $\mathrm{LOM}=$ laminated object manufacturing.  

#  Additive Manufacturing Processes  

AM processes can be classiﬁ  ed in various ways. The classiﬁ  cation system used here is  based on the form of the starting material in the process: (1) liquid-based, (2) powder- based, (3) molten material, and (4) solid sheets. These starting materials are subjected  to the various layer-forming processes and channel modes.  

# 32.2.1  LIQUID-BASED SYSTEMS  

The starting material in these processes is a liquid polymer. Stereo lithography is  the main technology in this category, although it includes several variations, one of  which is discussed here.  

Stereo lithography  This was the ﬁ  rst material addition RP technology, dating  from about 1988 and introduced by 3D Systems Inc. based on the work of inventor  Charles Hull. It is one of the most widely used additive manufacturing methods.  Stereo lithography (SL) is a process for fabricating a solid plastic part out of a  photosensitive liquid polymer using a directed laser beam to solidify the polymer.  The general setup for the process is illustrated in Figure 32.3. Part fabrication is  accomplished as a series of layers, in which one layer is added onto the previous  layer to gradually build the desired three-dimensional geometry. A part fabricated  by SL is illustrated in Figure 32.4.  

The stereo lithography apparatus consists of (1) a platform that can be moved  vertically inside a vessel containing the photosensitive polymer, and (2) a laser  whose beam can be controlled in the  $x{-}y$  direction. At the start of the process, the  platform is positioned vertically near the surface of the liquid photopolymer, and  the laser beam is directed through a curing path that comprises an area corre- sponding to the base (bottom layer) of the part. This and subsequent curing paths  are deﬁ  ned by the STI ﬁ  le (step 3 in preparing the control instructions described  earlier). The action of the laser is to harden (cure) the photosensitive polymer  where the beam strikes the liquid, forming a solid layer of plastic that adheres to  

![](images/adfaa68ebe5a38b83b135bf4880d9bd23b156c26724b34a0c90790214c002fc0.jpg)  
FIGURE 32.3  Stereo lithography:  (1) at the start of the  process, in which the  initial layer is added to  the platform; and  (2) after several layers  have been added so  that the part geometry  gradually takes form.  

![](images/225fad5f5e14b4d5fa9dc58db7f3cdbe76688266e75b2b06d76c1b0af7b4c1da.jpg)  
FIGURE 32.4  A part produced  by stereo lithography. (Photo  courtesy of 3D Systems, Inc.)  

the platform. When the initial layer is completed, the platform is lowered by a dis- tance equal to the layer thickness, and a second layer is formed on top of the ﬁ  rst  by the laser, and so on. Before each new layer is cured, a recoating blade is passed  over the viscous liquid resin to ensure that its level is the same throughout the sur- face. Each layer consists of its own area shape, so that the succession of layers, one  on top of the previous, creates the solid part shape. Typical layer thickness is 0.05 to  $0.15\;\mathrm{mm}$  (0.002–0.006 in). Thinner layers provide better resolution and allow more  intricate part shapes; but processing times are longer. Typical liquid photopolymers  include acrylic and epoxy, which are cured upon exposure to an ultraviolet laser.  After all of the layers have been formed, excess polymer is removed, and light  sanding is sometimes used to improve smoothness and appearance.  

Depending on its design and orientation, a part may contain overhanging  features that have no means of support during the bottom-up approach used in  stereo  lithography. For example, in Figure 32.1, if the lower half of the handle and  the lower handlebar were eliminated, the upper portion of the handle would be  unsupported during fabrication. In these cases, extra pillars or webs may need to be  added to the part simply for support purposes. Otherwise, the overhangs may ﬂ  oat  away or otherwise distort the desired part geometry. These extra features must be  trimmed away after the process is completed.  

Mask Projection Stereo lithography   Conventional stereo lithography described  above uses a single moving laser beam to cure the photopolymer in a given layer. As  mentioned, this can be quite time consuming. In mask projection stereo lithography  (MPSL), the entire layer of liquid photopolymer is exposed at once to an ultraviolet  light source through a mask instead of using a scanning laser beam. The hardening  process for each layer in MPSL is therefore much shorter than conventional SL.  

The key to MPSL is the use of a dynamic mask that is digitally altered for each  layer by any of several proprietary technologies such as the digital micromirror  device TM  (DMD), a product of Texas Instruments [14]. A DMD is an integrated  

![](images/b9dec91b4b7f7034d23d4c46814bb1f706cc73f1e14213a94b886ee2c9e3200c.jpg)  
FIGURE 32.5  Mask  Projected Stereo lithography  uses a layer mode.  

circuit plus additional hardware consisting of several hundred thousand alumi- num mirrors arranged in a rectangular pattern. The mirrors, which are only about  $16~\mu\mathrm{m}$  (0.00063 in) across, can be individually rotated between on and off states  corresponding to the bright and dark pixels in the dynamic mask. Light from a  UV source is focused on the DMD which reﬂ  ects the mask image corresponding  to the programmed layer pattern onto the liquid polymer.  The mask projection  stereo lithography process is depicted in Figure 32.5.  

# 32.2.2  POWDER-BASED SYSTEMS  

The common feature of the additive manufacturing processes described below is  that the starting material is powder.  These processes are sometimes referred to by  the name  Powder Bed Fusion , all of which operate on a bed of powdered material  [4]. Two important AM processes in this category are (1) selective laser sintering  and (2) three-dimensional printing.  

Selective Laser Sintering   Selective laser sintering (SLS) uses a moving laser  beam to fuse powders in areas corresponding to the CAD geometric model one  layer at a time to build the solid part. After each layer is completed, a new layer  of loose powders is spread across the surface and leveled using a counter-rotating  roller. The powders are preheated to just below their melting point  to facilitate  bonding and reduce distortion of the ﬁ  nished product. Preheating also serves to  reduce power requirements of the laser. Layer by layer, the powders are gradually  bonded into a solid mass that forms the three-dimensional part geometry. In areas  not sintered by the laser beam, the powders remain loose so they can be poured  out of the completed part. Meanwhile, they serve to support the solid regions of the  part as fabrication proceeds. Layer thickness is 0.075 to $0.50\:\mathrm{mm}$  (0.003–0.020 in).  The SLS process is usually accomplished in an enclosure that is ﬁ  lled with nitro- gen to minimize degradation of powders that might be susceptible to oxidation  (e.g., metals).  

SLS was developed by Carl Deckard at the University of Texas (Austin) as an  alternative to stereo lithography, and SLS machines were originally marketed by  DTM Corporation, a company founded by Deckard and two partners [9].  It is a  more versatile process than stereo lithography in terms of possible work materials.  Whereas SL is limited to liquid photopolymers, selective laser sintering materials  include polymers, metals, and ceramics, which are generally less expensive than  photosensitive resins.  

As mentioned, SLS is a Powder Bed Fusion (PBF) process. Other PBF technologies  differ from SLS in the following ways: (1) heating or fusion techniques, (2) methods  for handling the powders, and (3) mechanisms by which the powders are bonded into  solid objects. For example, one alternative process uses an electron beam as the heat- ing source to melt the powders; it is called electron beam melting (EBM). Other varia- tions include the use of line-wise and layer-wise processes as opposed to the point-wise  process in selective laser sintering.  

Three-Dimensional Printing   This technology (3DP) builds the part using an ink- jet printer to eject adhesive bonding material onto successive layers of powders.  The binder is deposited in areas corresponding to the cross sections of the solid  part, as determined by slicing the CAD geometric model into layers. The binder  holds the powders together to form the solid part, whereas the unbonded powders  remain loose to be removed later. While the loose powders are in place during the  build process, they serve to support overhanging and fragile features of the part.  When the build process is complete, the loose powders are removed. To further  strengthen the part, a sintering step can be applied to bond the individual powders.  

The part is built on a platform whose level is controlled by a piston. Consider the  process for one cross section with reference to Figure 32.6: (1) A layer of powder  is spread on the existing part-in-process. (2) An ink-jet printing head moves across  the surface using a line-wise channel mode, ejecting droplets of binder on those  regions that are to become the solid part. (3) When the printing of the current layer  is completed, the piston lowers the platform for the next layer.  

Starting materials in 3DP are powders of ceramic, metal, or cermet, and binders  that are polymeric or colloidal silica or silicon carbide [12], [19]. Typical layer thick- ness ranges from about 0.10 to  $0.20~\mathrm{mm}$  (0.004–0.008 in). The ink-jet printing head  moves across the layer at a speed of about $1.5\,\mathrm{m/sec}$  (59 in/sec), with ejection of liquid  binder determined during the sweep by raster scanning. The sweep time, together with  the spreading of the powders, permits a cycle time per layer of about 2 seconds [19].  Allowing for repositioning and recoating delays, this permits the machine to operate  at a rate of two to four layers per minute [4].  

![](images/4a8c868c827d7645789b25b76411a0c0555aeb6b7a6fa656f54843e1cc2a7822.jpg)  
FIGURE 32.6  Three-dimensional printing: (1) powder layer is deposited, (2) ink-jet printing of areas that will become  the part, and (3) piston is lowered for next layer (key:  $V=$  motion).  

# 32.2.3  MOLTEN MATERIAL SYSTEMS  

These additive technologies work by depositing material onto the layer at close to  the material’s melting point. Although the material is molten just before deposi- tion, it must be in a solid or semisolid state immediately after it is deposited  to  maintain the desired shape. As a practical matter, the melting requirement limits  the materials that can be used with these systems to thermoplastic polymers or  wax. Two representative systems are described below: (1) fused deposition model- ing, which uses an extrusion head to dispense the material; and (2) droplet deposi- tion manufacturing, which uses a multichannel printing head.  

Fused-Deposition Modeling  Fused-deposition modeling (FDM) is an RP process  in which a ﬁ  lament of wax and/or thermoplastic polymer is extruded onto the  exist  ing part surface from a work head to complete each new layer. The work head  is controlled in the $x{-}y$  plane during each layer and then moved up by a distance  equal to one layer in the $z$ -direction. The starting material is a solid ﬁ  lament with  typical diameter $=1.25\:\mathrm{mm}$  (0.050 in) fed from a spool into the work head, which  heats the material to about $0.5^{\circ}\mathrm{C}\left(\sim\!1^{\circ}\mathrm{F}\right)$  above its melting point before extruding it  onto the part surface. The extrudate is solidiﬁ  ed and cold welded to the cooler part  surface in about 0.1 sec. If a support structure is needed, that material is usually  extruded by a second extrusion head using a different material that can be readily  separated from the main part. The part is fabricated from the base up, using a  layer-by-layer procedure similar to other RP systems. A disadvantage of FDM is its  relatively slow speed, because the deposited material is applied in a moving-point  channel mode, and the work head cannot be moved with the high speed of a laser  spot. Also, the use of an extruder, with its circular nozzle oriﬁ  ce, makes it difﬁ  cult  to form sharp corners [4].  

FDM was developed by Stratasys Inc., which sold its ﬁ  rst machine in 1990. Today,  there are more FDM machines throughout the world than any other type of AM  machine [4]. The starting data is a CAD geometric model that is processed by  Stratasys’s software modules QuickSlice ® ; and SupportWork ™ . QuickSlice ®  is used  to slice the model into layers, and SupportWork ™  is used to generate any support  

![](images/3f987c1e1461bbfd86186586b21b75baa90b64f639d0896691e5799bc661be59.jpg)  
FIGURE 32.7  Collection  of parts produced by  fused deposition  modeling. (Courtesy  of George E. Kane  Manufacturing  Technology Laboratory,  Lehigh University.)  

structures that are required during the build process. The slice (layer) thickness is  typically set from 0.25 to $0.33\,\mathrm{mm}$  (0.01–0.013 in), but for ﬁ  ner details, layer thickness  can be set to a minimum of $0.076\:\mathrm{mm}\:(0.003\:\mathrm{in})$ [4]. Up to about  $400\,\mathrm{mm}$  of ﬁ  lament  can be deposited per second by the extrusion work head. Starting materials are wax  and several polymers, including ABS and polycarbonate. These materials are non- toxic, allowing the FDM machine to be set up in an ofﬁ  ce environment. A collection  of plastic parts made by fused deposition modeling is shown in Figure 32.7, and the  FDM machine that made these parts is shown in Figure 32.8.  

Droplet Deposition Manufacturing   This process, also known as ballistic-particle  manufacturing, operates by melting the starting material and shooting small droplets  onto a previously formed layer. The term droplet deposition manufacturing (DDM)  refers to the fact that small particles of work material are deposited as projectile  droplets from the work head nozzle. The liquid droplets cold weld to the surface  to form a new layer. The deposition of droplets for each new layer is controlled by  a moving $x$ - y  work head that operates in a point-wise manner, in which the path is  based on a cross section of a CAD geometric model that has been sliced into layers.  For geometries that require a support structure, two work heads are used, one to  dispense the polymer to make the object itself, and the second to deposit another  material for the support. After each layer has been applied, the platform supporting  the part is lowered a certain distance corresponding to the layer thickness, in prepa- ration for the next layer.  

Several commercial additive manufacturing machines are based on this general  operating principle, the differences being in the type of material that is deposited  

![](images/e16ff65db1254ee339a95453e83d7f638443fed33836af433b1eba36c8d6d269.jpg)  
FIGURE 32.8  Fused  deposition modeling  machine. (Courtesy of  George E. Kane  Manufacturing  Technology Laboratory,  Lehigh University.)  

and the corresponding technique by which the work head operates to melt and  apply the material. An important criterion that must be satisﬁ  ed by the starting  material is that it be readily melted and solidiﬁ  ed. Work materials used in DDM  include wax and thermoplastics. Metals with low melting point, such as tin and  aluminum, have also been tested. Improvements in the channel modes include the  use of moving line printing heads that operate much like ink-jet printers.  

# 32.2.4  SOLID SHEET–BASED SYSTEMS  

The common feature in these additive manufacturing systems is that the starting  material is a solid sheet. In this section a solid-sheet system called laminated- object manufacturing is discussed. Differences among commercial products in  this category include materials out of which the sheets are made and methods of  assembling the sheets.  

Laminated-Object Manufacturing   Laminated-object manufacturing (LOM)  produces a solid physical model by stacking layers of sheet stock that are each  cut to an outline corresponding to the cross-sectional shape of a CAD model that  has been sliced into layers. The layers are sequentially stacked and bonded one  on top of the previous one to build the part. After cutting, the excess material in  each layer remains in place to support the part during building. Starting materials  in LOM include paper, cardboard, and plastic in sheet stock form. Stock thickness  is 0.05 to $0.50\;\mathrm{mm}$  (0.002–0.020 in). In LOM, the sheet material is usually supplied  with adhesive backing as rolls that are spooled between two reels, as in Figure 32.9.  Otherwise, the LOM process must include an adhesive coating step for each layer.  

The data preparation phase in LOM consists of slicing the geometric model using  the STL ﬁ  le for the given part. With reference to Figure 32.9, the LOM process for  each layer can be described as follows, picking up the action with a sheet of stock in  place and bonded to the previous stack: (1) The cross-sectional perimeter of the STL  model is computed based on the measured height of the physical part at the current  layer of completion. The slicing function in LOM is performed after each layer has  been physically added and the vertical height of the part has been measured. This  provides a feedback correction to account for the actual thickness of the sheet stock  being used, a feature unavailable on most other RP systems. (2) A laser beam is used  to cut along the perimeter, as well as to crosshatch the surplus portions of the sheet  for subsequent removal. The cutting trajectory is controlled by means of an  $x{-}y$   positioning system, and cutting depth is controlled so that only the top layer is cut.  (3) The platform holding the stack is lowered, and the sheet stock is advanced bet- ween supply roll and take-up spool for the next layer. The platform is then raised  to a height consistent with the stock thickness, and a heated roller moves across  the new layer to bond it to the previous layer. The height of the physical stack is  measured in preparation for the next slicing computation.  

When all of the layers are completed, the new part is separated from the excess  external material. The part can then be sanded to smooth and blend the layered  edges. A sealing application is recommended, at least for paper and cardboard  stock to prevent moisture absorption and damage, using a urethane, epoxy, or other  polymer spray. LOM part sizes can be relatively large among AM processes, with  work volumes up to  $800\;\mathrm{mm}\times500\;\mathrm{mm}$  by $550\;\mathrm{mm}$  ( $(32\;\mathrm{in}\times20$  in $\times\;22$  in). More  common work volumes are  $380\:\mathrm{mm}\times250\:\mathrm{mm}\times350\:\mathrm{mm}$  ( $(15\;\mathrm{in}\times10\;\mathrm{in}\times14\;\mathrm{in})$ .  

![](images/fbccb2789dec80d8715eb290f4b7826f1c527c6945bebdb290ab5d617dba55a7.jpg)  
FIGURE 32.9  Laminated- object manufacturing.  

Thus, one of the advantages of LOM compared to other RP and AM technologies  is the capability to build parts that are quite large.  

The original company offering LOM systems was Helisys, Inc. Its machine proc- essed paper sheet stock backed with adhesive and used a sequence in which the most  recently added sheet was bonded to the existing structure before cutting the outline  in that layer. A heated roller was used to melt the thermoplastic adhesive in the  bonding operation. Subsequent modiﬁ  cations in LOM introduced by other compa- nies have included (1) the use of a cutting blade rather than a laser to perform the  cutting, (2) polymeric sheet stock rather than paper as the material, and (3) changing  the process sequence to cut the layer outline before bonding rather than bonding  before cutting. The advantage of this last modiﬁ  cation is that it facilitates the fabrica- tion of objects that possess internal features [4].  

#  Cycle Time and Cost Analysis  

All of the additive manufacturing technologies described above work in a similar  way, which is to build a part or prototype by adding layers one layer at a time. The  purpose of this section is to develop mathematical models of this layer-by-layer  approach to determine cycle time and part cost.  

Cycle Time Analysis  The cycle time to build a part by the layering processes in  additive manufacturing depends on the size of the part (volume of material in the  part) and the number of parts produced in one build cycle. It also depends on the  layer formation processes (e.g., lasers, droplet-based, extruder) and the associated  channel mode (moving spot, moving line, or layer). Associated process parameters  include layer thickness (thinner layers mean more layers and slower cycle time for  the same part size), the speed with which the moving spot or moving line travels, and  any delays that are inherent in the process, such as repositioning and recoating. The  modeling approach used here for estimating build time is to determine the time to  complete each layer and then sum up the layer times to obtain the overall cycle time.  An alternative and more detailed approach is described in Gibson et al [4].  

First, the time to complete a single layer in processes that use a moving-spot  channel mode is given by the following equation:  

$$
T_{i}=\frac{A_{i}}{\nu D}+\,T_{r}
$$  

where $T_{i}=$  time to complete layer  i , s (sec), where the subscript  $i$  is used to identify the  layer; $A_{i}=$  area of layer $i,\mathsf{m}\mathrm{m}^{2}\,(\mathrm{in}^{2});\nu=$ speed of the moving spot on the surface, $\mathrm{mm/s}$   (in/sec); $D=$  diameter of the spot (assumed circular), mm (in); and  $T_{r}=$  repositioning  and recoating time between layers, s (sec). Repositioning time involves lowering the  worktable to prepare for the next layer to be fabricated. It also includes repositioning  of the work head at the beginning and end of a layer if that is not performed in parallel  with table repositioning. Recoating time is the time to spread material for the new layer;  for example, to spread the next layer of powders. Recoating time is not applicable in  all AM processes.  $T_{r}$  may also include built-in delays associated with each layer, such as  cooling or heating delays, and nozzle cleaning.  

Once the $T_{i}$  values have been determined for all layers, then the build cycle time can  be determined as the sum of these times plus any setup or start-up time required for  the process. For example, the machine may require a warm-up period during which the  chamber is brought up to a speciﬁ  ed temperature. It may also be desirable to include  the time for the operator to load the starting material and perform any setup tasks that  are associated with the production run. The total cycle time is given by the following:  

$$
T_{c}=\ensuremath{T_{s u}}+\sum_{i=1}^{n_{l}}\ensuremath{T_{i}}
$$  

where  $T_{c}=$  build cycle time, s (sec);  $T_{s u}=$ setup time, s (sec); and $n_{l}=$  number of  layers used to approximate the part.  

# Example 32.1  Build cycle  time in stereo- lithography  

The square cup-shaped part shown in Figure 32.10 is to be fabricated using  stereo lithography. The base of the cup is  $40\,\mathrm{mm}$  on each side and is $5\,\mathrm{mm}$   thick. The walls are $4\:\mathrm{mm}$  thick, and the total height of the cu $\mathsf{p}=52\,\mathsf{m}\mathsf{m}$ . The  SL machine used for the job uses a spot diameter $=0.25\:\mathrm{mm}$ , and the beam is  moved at a speed $=950\,\mathrm{mm/s}.$ . Layer thickness $,=0.10\,\mathrm{mm}$ . Repositioning and  recoating time for each layer $=21$  s. Compute an estimate of the cycle time to  build the part if the setup time $=20\:\mathrm{min}$ .  

Solution:  The geometry of the part can be divided into two sections: (1) base  and (2) walls. The cross-sectional area of the base  $A_{1}=40^{2}=1600\:\mathrm{mm}^{2}$  and its  thickness is given as $5\,\mathrm{mm}$ . The cross-sectional area of the walls $A_{2}=40^{2}-32^{2}=$ $576\,\mathrm{mm}^{2}$  and its height $=52-5=47\,\mathrm{mm}.$  With a layer thickness $=0.10\,\mathrm{mm}$ ,  there will be $5.0/0.10=50\$  layers to build the base and $47/0.10=470$  layers to  fabricate the walls, a total of $470+50=520\$  layers.  

The time per layer for the base  

$$
T_{i}={\frac{A}{\nu D E_{p}}}+\,T_{r}={\frac{1600}{950(0.25)}}+21=6.737+21=27.737\ \mathrm{s}
$$  

The time per layer for the walls  

$$
T_{i}={\frac{576}{950(0.25)}}+21=2.425+21=23.425\:\mathrm{{s}}
$$  

Total build cycle time  

$T_{\mathrm{{c}}}=20(60)+50(27.737)+470(23.425)=\mathbf{13.597\,\mathrm{s}}=226.6\,\mathbf{min}=3.777\,\mathbf{h}\mathbf{r}$  

If a separate support structure must be constructed for the part, some RP  machines require a second scan to accomplish this in each layer. For example,  fused deposition modeling uses a second extruder if the support material is of  a different type than the part material (e.g., lower melting point wax to support  a plastic part). In this case, the time taken by the secondary work head must be  added if the extruder heads operate sequentially, so Equation (32.1) becomes:  

$$
T_{i}=\frac{A_{i}}{\nu D}+\frac{A_{s i}}{\nu D}+\;T_{r}
$$  

where  $A_{s i}=$  support area in layer  $i,\,\mathrm{mm}^{2}\,\,(\mathrm{in}^{2})$ . A separate term is used to allow  for the possibility that the spot speed and diameter used for the support may be  different than those used for the part itself. In some cases, the extruder heads can  be operated simultaneously rather than sequentially, so the layering time depends  

![](images/8e0cc7c02251f4382072aa6498d0d0b8457cb60e94d4026381367db119f770fb.jpg)  
FIGURE 32.10  Sample part  used in Example 32.1.  

on whichever work head takes longer (usually the part work head because more  material is deposited).  

For processes that use a moving-line channel mode, the time to complete a layer is  the time required for the moving line to sweep across the worktable plus reposition- ing and recoating time:  

$$
T_{i}=\nu_{s}L_{s}+\,T_{r}
$$  

where  $\nu_{s}=$  velocity of the moving line as it sweeps across the layer,  $\mathrm{mm/s\(in/sec)}$ ;  and $L_{s}=$  length of the sweep, mm (in). These values of  $\nu_{s}$  and $L_{s}$  should be the same  for all layers.  

Finally, for processes using the layer channel mode, the time to complete one  layer is given by  

$$
T_{i}=\,T_{e x}+\,T_{r}
$$  

where  $T_{e x}=$  exposure time to form the layer, s (sec). This should be the same for  all layers.  

The task of determining $A_{i}$  for each layer can be tedious for a part of even modest  geometric complexity. In these cases, it may be easier to determine the total volume  of the part and divide this volume by the number of layers to determine the average  volume per layer. Then, dividing this average volume by the layer thickness provides  the average area per layer. Summarizing, the average layer area is given by  

$$
\overline{{A}}_{i}=\frac{V}{n_{l}t}
$$  

where  $V=$  total volume of the part,  $\mathsf{m}\mathsf{m}^{3}\;(\mathrm{i}\mathsf{n}^{3});n_{l}=$ number of layers; and  $t=\mathrm{layer}$ thickness, mm (in). Time to complete the layer then becomes  

$$
T_{i}=\frac{\overline{{A}}_{i}}{\nu D}+\mathrm{\Delta}T_{r}=\frac{V}{n_{l}t\nu D}+\mathrm{\Delta}T_{r}
$$  

where   $\overline{{A}}_{i}=$  average area per layer, $\mathrm{mm}^{2}\left(\mathrm{in}^{2}\right)$ , and the other terms are the same as in  Equation (32.1). The total cycle time equation, Equation (32.2), can then be reduced  to the following forms:  

$$
T_{c}=T_{s u}+n_{l}T_{i}=T_{s u}+{\frac{V}{t\nu D}}+n_{l}T_{r}
$$  

where the terms on the far right-hand side are obtained by combining Equations  (32.6) and (32.7) and expanding the  $T_{i}$  term.  

Cost Analysis  The cost per piece  $C_{p c}$  fabricated by any of the additive manufac- turing technologies is the sum of material, labor, and machine operating cost. The  following terminology and units will be used to develop equations to compute cost  per piece:  $C_{m}=$  material cost,  $\S/\mathrm{{pc}}$ ;  $C_{L}\,=$  labor cost,  $\S/\mathrm{hr}$ ;  $C_{e q}\,=$ equipment cost,  $\S/\mathrm{hr}$ . The build cycle time  $T_{c}$  has already been deﬁ  ned in Equations (32.2) and (32.8),  but units of hours will be used here for convenience; that is  $T_{c}=$  cycle time, hr/cycle.  Owing to the automated operation of the AM machine, a utilization factor  $U_{L}$  should  be applied to the labor rate during the build cycle. Finally, a post-processing time per  piece  $T_{p p}$  is the time following the build cycle that is required for support removal  (if supports have been added to the part), cleaning, and ﬁ  nishing. Combining these  terms, the piece cost can be computed from the following equation:  

$$
C_{p c}=C_{m}+\left(C_{L}U_{L}+C_{e q}\right)T_{c}+C_{L}\;T_{p p}
$$  

Equipment cost per hour can be based on the original installed cost of the equip- ment divided by the total number of hours of operation the machine is expected to  be used during its life, as explained in Section 1.5.2 and Example 1.1.  

# Example 32.2  Cost per piece  in additive  manufacturing  

The cost of the stereo lithography machine in Example $32.1=\S100{,}000$  installed.  It operates 5 days per week, 8 hours per day, 50 weeks per year, and is expected  to last 4 years. Material cost for the photopolymer $=\S120,$ /liter. Assume that all  of the photopolymer in the container that is not used for the part can be reused.  Labor rate $=\S24.00/\mathrm{hr}$ , but labor will be used for only $=25\%$  of the build cycle,  mostly for setup. The post-processing time $=6.0\,\mathrm{min/part}$ . Using the cycle time  of 3.777 hr from Example 32.1, determine the part cost.  

Solution:  The number of hours of operation per year  $H=50(5)(8)=2000\,\mathrm{hr/yr}$ The hourly equipment cost is calculated as follows:  

$$
C_{e q}=\frac{100{,}000}{4(2000)}=\S}12{.}50/\mathrm{hr}
$$  

Material  $\mathrm{cos}\,\mathrm{=}\,\S120/\mathrm{L}$   $(1\;\mathrm{L}=1\;\mathrm{d}\mathrm{m}^{3}=1(10^{6})\;\mathrm{mm}^{3})$ . The part in Example 32.1  has a volume composed of the square base where  $V_{1}=5(1600)=8000\;\mathrm{mm}^{3}$   plus the walls, where $V_{2}=47(576)=27{,}072\:\mathrm{mm}^{3}.$  Total volume  $=35{,}072\:\mathrm{mm}^{3}$ .  

$C_{m}=(\S120\;(10^{-6})/\mathrm{mm}^{3})(35,\!072\;\mathrm{mm}^{3})=\S4.21/\mathrm{pc}$  

Cost per piece  $C_{p c}=4.21+(24.00(0.25)+12.50)(3.777)+24.00(6/60)=$   ${\mathfrak{S76.48/p c}}$  

In many additive manufacturing applications used for production, more than  one part is made in the build cycle. Let $n_{b}$  denote the batch size (number of parts  built during the production cycle). Equation (32.9) can be amended as follows to  account for batch size:  

$$
C_{p c}=C_{m}+\frac{\left(C_{L}U_{L}+C_{e q}\right)T_{c}}{n_{b}}+\,C_{L}T_{p p}
$$  

#  Additive Manufacturing Applications  

Applications of additive manufacturing can be classiﬁ  ed into four categories: (1) design,  (2) engineering analysis and planning, (3) tooling, and (4) parts production. These appli- cations are discussed in the following paragraphs. The chapter concludes with a brief  discussion of the problems encountered in additive manufacturing.  

Design  This was the initial application area for rapid prototyping systems. Designers  are able to conﬁ  rm their design by building a real physical model in minimum time  using rapid prototyping. The features and functions of the part can be communicated  to others more easily using a physical model than by a paper drawing or displaying it  on a CAD system monitor. Design beneﬁ  ts attributed to rapid prototyping include [2]:  (1) reduced lead times to produce prototype components, (2) improved ability to  visu  alize the part geometry because of its physical existence, (3) earlier detection and  reduc  tion of design errors, and (4) increased capability to compute mass properties of  components and assemblies.  

Engineering Analysis and Planning  The existence of an RP-fabricated part allows  for certain types of engineering analysis and planning activities to be accom  plished  that would be more difﬁ  cult without the physical entity. Some of the possibilities are 

 (1) comparison of different shapes and styles to optimize aesthetic appeal of the part; 

 (2) analysis of ﬂ  uid ﬂ  ow through different oriﬁ  ce designs in valves fabri  cated by RP; 

 (3) wind tunnel testing of different streamline shapes using physical models created  by RP; (4) stress analysis of a physical model; (5) fabrication of preproduction parts as  an aid in process planning and tool design; and (6) combining medical imaging techno- logies, such as magnetic resonance imaging, with RP to create models for doctors in  planning surgical procedures or fabricating prostheses or implants.  

Tooling  When AM is adopted to fabricate production tooling, the term  rapid tool  making  (RTM) is often used. RTM applications divide into two approaches [5]:  indirect RTM method, in which a pattern is created by RP and the pattern is used to fabricate  the tool, and  direct  RTM method, in which RP is used to make the tool itself. Examples  of indirect RTM include the following [7], [12]: (1) use of an RP-fabricated part as the  master in making a silicon rubber mold that is subsequently used as a production mold;  (2) RP patterns to make the sand molds in sand casting (Section 11.1); (3) fabrication of  patterns of low-melting point materials (e.g., wax) in limited quantities for investment  casting (Section 11.2.4); and (4) making electrodes for EDM (Section 25.3.1).  

Examples of direct RTM include [5], [7], [12]: (1) RP-fabricated mold cavity inserts  that can be sprayed with metal to produce injection molds for a limited quantity of pro- duction plastic parts (Section 13.6) and (2) 3-D printing to create a die geometry in me- tallic powders followed by sintering and inﬁ  ltration to complete the fabrication of the die.  

Parts Production  Additive manufacturing is increasingly being used to produce  parts and products, and the term  direct digital manufacturing  is sometimes used for  these applications. Parts production examples include [4], [12]: (1) plastic parts in small  batch sizes that cannot be economically produced by injection molding because of  high mold cost; (2) parts with intricate and/or complex geometries, especially internal  geometric features, that cannot be made by conventional processes without assembly;  (3) spare parts in circumstances where it is more feasible to fabricate a part when it  is needed than to maintain an inventory; and (4) customized one-of-a-kind parts that  must be made to correct size for each individual application. Examples of customized  parts are found in medical applications such as bone replacements, hearing aid shells  that must be ﬁ  tted to an individual’s ear, dental aligners (clear dental braces that  gradually correct a patient’s bite), and custom soccer shoes for professional athletes.  

As the preceding examples illustrate, direct digital manufacturing is not a substi- tute for mass production. Instead, it is appropriate for low-volume production and  mass customization, in which products are made in large numbers but each product is  somehow unique. To generalize, the characteristics of production situations suited to  additive manufacturing include the following [4]: (1) unique geometries, (2) complex  shapes, (3) low quantities, even quantities of one, (4) quick turnaround, and (5) it is  desirable to avoid the fabrication of special hard tooling. The requirement is that a  CAD model of the item must be available.  

Problems with Additive Manufacturing  The principal problems with current AM  processes include (1) part accuracy, (2) limited variety of materials, and (3) mechanical  performance of the fabricated parts.  

Several sources of error limit part accuracy in AM systems: (1) mathematical,  (2) process related, or (3) material related [19]. Mathematical errors include approxi- mations of part surfaces used in RP data preparation and differences between the slic- ing thicknesses and actual layer thicknesses in the physical part. The latter differences  result in  $z$ -axis dimensional errors. An inherent limitation in the physical part is the  steps between layers, especially as layer thickness is increased, resulting in a staircase  appearance for sloping part surfaces. Process-related errors sometimes result from  the particular part building technology used in the AM system. These errors degrade  the shape of each layer as well as the registration between adjacent layers. Process  errors can also affect the  $z$ -axis dimension. Finally, material-related errors include  shrinkage and distortion. An allowance for shrinkage can be made by enlarging the  CAD model of the part based on previous experience with the process and materials.  

Current rapid prototyping systems are limited in the variety of materials they  can process. For example, stereo lithography is limited to photosensitive polymers.  In general, the materials used in AM systems are not as strong as the production  part materials that will be used in the actual product. This limits the mechanical  performance of the prototypes and the amount of realistic testing that can be done  to verify the design during product development.  