# 40 Quality Control  and Inspection  

# Chapter Contents  

40.1 Product Quality  

40.2 Process Capability and Tolerances  

40.3 Statistical Process Control  

40.3.1 Control Charts for Variables 40.3.2 Control Charts for Attributes 40.3.3 Interpreting the Charts  

# 40.4 Quality Programs in Manufacturing  

40.4.1 Total Quality Management 40.4.2 Six Sigma 40.4.3 Taguchi Methods 40.4.4 ISO 9000  

# 40.5 Inspection Principles  

40.5.1 Manual and Automated  Inspection 40.5.2 Contact versus Noncontact  Inspection  

# 40.6 Modern Inspection Technologies  

40.6.1 Coordinate Measuring Machines 40.6.2 Measurements with Lasers 40.6.3 Machine Vision 40.6.4 Other Noncontact Inspection  Techniques  

Traditionally,  quality control  (QC) has been concerned  with detecting poor quality in manufactured products and  taking corrective action to eliminate it. QC has often been  limited to inspecting the product and its components, and  deciding whether the dimensions and other features con- formed to design speciﬁ  cations. If they did, the product  was shipped. The modern view of quality control encom- passes a broader scope of activities, including various  quality programs such as statistical process control and  Six Sigma as well as modern inspection technologies such  as coordinate measuring machines and machine vision.  This chapter discusses these and other quality and inspec- tion topics that are relevant today in modern manufac- turing operations. The coverage begins with the topic of  product quality.  

#  Product Quality  

#  

The dictionary deﬁ  nes quality as “the degree of excel- lence which a thing possesses,” or “the features that  make something what it is”—its characteristic elements  and attributes. The American Society for Quality (ASQ)  deﬁ  nes quality as “the totality of features and character- istics of a product or service that bear on its ability to  satisfy given needs” [2].  

In a manufactured product, quality has two aspects [4]:  (1) product features and (2) freedom from deﬁ  ciencies.  Product features  are the characteristics of the product  that result from design. They are the functional and aes- thetic features of the item intended to appeal to and pro- vide satisfaction to the customer. In an automobile, these  features include the size of the car, its styling, the ﬁ  nish of  the body, gas mileage, reliability, reputation of the manu- facturer, and similar aspects. They also include the avail- able options for the customer to choose. The sum of a  product’s features usually deﬁ  nes its  grade ; this relates  to the level in the market at which the product is aimed.  Cars (and most other products) come in different grades.  Some cars provide basic transportation because that is  what some customers want, while others are upscale for  consumers willing to spend more to own a “better product.” The features of a product  are decided in design, and they generally determine the inherent cost of the product.  Superior features and more of them mean higher cost.  

Freedom from deﬁ  ciencies  means that the product does what it is supposed to do  (within the limitations of its design features), that it is absent of defects and out-of- tolerance conditions, and that no parts are missing. This aspect of quality includes  components and subassemblies of the product as well as the product itself. Freedom  from deﬁ  ciencies means conforming to design speciﬁ  cations, which is accomplished  in manufacturing. Although the inherent cost to make a product is a function of its  design, minimizing the product’s cost to the lowest possible level within the limits  set by its design is largely a matter of avoiding defects, tolerance deviations, and  other errors during production. Costs of these deﬁ  ciencies make a long list indeed:  scrapped parts, larger lot sizes for scrap allowances, rework, reinspection, sortation,  customer complaints and returns, warranty costs and customer allowances, lost sales,  and lost good will in the marketplace.  

Thus, product features are the aspect of quality for which the design depart- ment is responsible. Product features determine to a large degree the price that  a company can charge for its products. Freedom from deﬁ  ciencies is the quality  aspect for which the manufacturing departments are responsible. The ability to  minimize these deﬁ  ciencies has an important inﬂ  uence on the cost of the product.  These generalities oversimplify the way things work, because the responsibility  for high quality extends well beyond the design and manufacturing functions in  an organization.  

#  Process Capability and Tolerances  

In any manufacturing operation, variability exists in the process output. In a machin- ing operation, which is one of the most accurate processes, the machined parts may  appear to be identical, but close inspection reveals dimensional differences from one  part to the next. Manufacturing variations can be divided into two types: random  and assignable.  

Random variations  are caused by many factors: human variability within each  operation cycle, variations in raw materials, machine vibration, and so on. Individually,  these factors may not amount to much, but collectively the errors can be signiﬁ  cant  enough to cause trouble unless they are within the tolerances for the part. Random  variations typically form a normal statistical distribution. The output of the process  tends to cluster about the mean value, in terms of the product’s quality characteristic  of interest (e.g., length, diameter). A large proportion of the population of parts is  centered around the mean, with fewer parts away from the mean. When the only vari- ations in the process are of this type, the process is said to be in  statistical control .  This kind of variability will continue so long as the process is operating normally. It is  when the process deviates from this normal operating condition that variations of the  second type appear.  

Assignable variations  indicate an exception from normal operating conditions.  Something has occurred in the process that is not accounted for by random vari- ations. Reasons for assignable variations include operator mistakes, defective raw  materials, tool failures, machine malfunctions, and so on. Assignable variations in  manufacturing usually betray themselves by causing the output to deviate from the  normal distribution. The process is no longer in statistical control.  

Process capability relates to the normal variations inherent in the output when the  process is in statistical control. By deﬁ  nition,  process capability  equals  $\pm3$  standard  deviations about the mean output value (a total of 6 standard deviations),  

$$
P C=\mu\pm3\,\sigma
$$  

where $P C=$  process capability; $\mu=$  process mean, which is set at the nominal value  of the product characteristic when bilateral tolerancing is used (Section 5.1.1); and 

 $\sigma=$ standard deviation of the process. Assumptions underlying this deﬁ  nition are 

 (1) steady state operation has been achieved and the process is in statistical control,  and (2) the output is normally distributed. Under these assumptions, $99.73\,\%$  of the  parts produced will have output values that fall within  $\overline{{\pm3.0\sigma}}$  of the mean.  

The process capability of a given manufacturing operation is not always known,  and experiments must be conducted to assess it. Methods are available to estimate  the natural tolerance limits based on a sampling of the process.  

The issue of tolerances is critical to product quality. Design engineers tend to assign  dimensional tolerances to components and assemblies based on their judgment of how  size variations will affect function and performance. Conventional wisdom is that closer  tolerances beget better performance. Small regard is given to the cost resulting from  tolerances that are unduly tight relative to process capability. As tolerance is reduced,  the cost of achieving the tolerance tends to increase because additional processing  steps may be needed and/or more accurate and expensive production machines may be  required. The design engineer should be aware of this relationship. Although primary  consideration must be given to function in assigning tolerances, cost is also a factor,  and any relief that can be given to the manufacturing departments in the form of wider  tolerances without sacriﬁ  cing product function is worthwhile.  

Design tolerances must be compatible with process capability. It serves no use- ful purpose to specify a tolerance of  $\pm0.025\;\mathrm{mm}$  ( $\acute{-}0.001$  in) on a dimension if the  process capability is signiﬁ  cantly wider than  $^{\pm}0.025\ \mathrm{mm}$  ( $'\pm0.001$  in). Either the  tolerance should be opened further (if design functionality permits), or a different  manufacturing process should be selected. Ideally, the speciﬁ  ed tolerance should be  greater than the process capability. If function and available processes prevent this,  then sorting must be included in the manufacturing sequence to inspect every unit  and separate those that meet speciﬁ  cation from those that do not.  

Design tolerances can be speciﬁ  ed as being equal to process capability as deﬁ  ned in  Equation (40.1). The upper and lower boundaries of this range are known as the  natural  tolerance limits . When design tolerances are set equal to the natural tolerance limits,  then  $99.73\%$  of the parts will be within tolerance and  $0.27\%$  will be outside the limits.  Any increase in the tolerance range will reduce the percentage of defective parts.  

Tolerances are not usually set at their natural limits by product design engineers;  tolerances are speciﬁ  ed based on the allowable variability that will achieve required  function and performance. It is useful to know the ratio of the speciﬁ  ed tolerance  relative to the process capability. This is indicated by the  process capability index  

$$
P C I=\frac{T}{6\sigma}
$$  

where $P C I=$  process capability index;  $T=$  tolerance range—the difference between  upper and lower limits of the speciﬁ  ed tolerance; and  $6\sigma=$ natural tolerance limits.  The underlying assumption in this deﬁ  nition is that the process mean is set equal to  the nominal design speciﬁ  cation, so that the numerator and denominator in Equa- tion (40.2) are centered about the same value.  

TABLE  •  40.1  Defect rate when tolerance is deﬁ  ned in terms of number of standard  deviations of the process, given that the process is operating in statistical control. 
![](images/a31c146640005510814498388d58a753522150062de11009db235f8a9cf7147c.jpg)  

Table 40.1 shows the effect of various multiples of standard deviation on defect  rate (i.e., proportion of out-of-tolerance parts). The desire to achieve very-low- fraction defect rates has led to the popular notion of “six sigma” limits in quality  control. Achieving six sigma limits virtually eliminates defects in a manufactured  product, assuming the process is maintained within statistical control. As noted  later in the chapter, Six Sigma quality programs do not quite live up to their names.  Before addressing that issue, the next section discusses a quality control technique  that is widely used in industry: statistical process control.  

Statistical process control (SPC) involves the use of various statistical methods to  assess and analyze variations in a process. SPC methods include simply keeping  records of the production data, histograms, process capability analysis, and control  charts. Control charts are the most widely used SPC method, and this section will  focus on them.  

The underlying principle in control charts is that the variations in any process  divide into two types: (1) random variations, which are the only variations present  if the process is in statistical control, and (2) assignable variations that indicate a  departure from statistical control (Section 40.2). It is the objective of a control chart  to identify when the process has gone out of statistical control, thus signaling that  some corrective action should be taken.  

A  control chart  is a graphical technique in which statistics computed from meas- ured values of a certain process characteristic are plotted over time to determine  if the process remains in statistical control. The general form of the control chart  is illustrated in Figure 40.1. The chart consists of three horizontal lines that remain  constant over time: a center, a lower control limit  $(L C L)$ , and an upper control limit  ( UCL ). The center is usually set at the nominal design value. The upper and lower  control limits are generally set at $\pm3$  standard deviations of the sample means.  

It is highly unlikely that a random sample drawn from the process will lie outside  the upper or lower control limits while the process is in statistical control. Thus,  if it happens that a sample value does fall outside these limits, it is interpreted to  mean that the process is out of control. Therefore, an investigation is undertaken to  determine the reason for the out-of-control condition, with appropriate corrective  action to eliminate the condition. By similar reasoning, if the process is found to  be in statistical control, and there is no evidence of undesirable trends in the data,  

![](images/ee626f01219c480c05fc1b51b44e6a716df44a753efc1074348e87c3a7062cc8.jpg)  

then no adjustments should be made since they would introduce an assignable vari- ation to the process. The philosophy, “If it ain’t broke, don’t ﬁ  x it,” is applicable to  control charts.  

There are two basic types of control charts: (1) control charts for variables and  (2) control charts for attributes. Control charts for variables require a measurement  of the quality characteristic of interest. Control charts for attributes simply require  a determination of whether a part is defective or how many defects there are in the  sample.  

# 40.3.1  CONTROL CHARTS FOR VARIABLES  

A process that is out of statistical control manifests this condition in the form of signi- ﬁ  cant changes in process mean and/or process variability. Corresponding to these possi- bilities, there are two principal types of control charts for variables: _  chart and $R$  chart.  The _  chart  (call it “ $\cdot_{x}$  bar chart”) is used to plot the average measured value of a certain  quality characteristic for each of a series of samples taken from the production process.  It indicates how the process mean changes over time. The  $\pmb{R}$  chart  plots the range of  each sample, thus monitoring the variability of the process and indicating whether it  changes over time.  

A suitable quality characteristic of the process must be selected as the variable  to be monitored on the _  and $R$  charts. In a mechanical process, this might be a shaft  diameter or other critical dimension. Measurements of the process itself must be  used to construct the two control charts.  

With the process operating smoothly and absent of assignable variations, a series  of samples (e.g., $m=20$  or more is generally recommended) of small size (e.g., $n=4$ ,  5, or 6 parts per sample) are collected and the characteristic of interest is measured  for each part. The following procedure is used to construct the center,  $L C L$ , and  $U C L$  for each chart:  

1.  Compute the mean _  and range  $R$  for each of the  m  samples.

 2.  Compute the grand mean _  , which is the mean of the  values for the  m  samples;  this will be the center for the _  chart. __

 3.  Compute   $\overline{{R}}$ , which is the mean of the $R$  values for the  m  samples; this will be the  center for the $R$  chart.  

TABLE  •  40.2  Constants for the   $\bar{x}$   and  R  charts. 
![](images/a79b339cc3fcd7960a46ec105d89ce9299cfc0272f4b655000fd6c822bc069de.jpg)  

4.  Determine the upper and lower control limits,  UCL  and $L C L$ , for the _   and  $R$ charts. The approach is based on statistical factors tabulated in Table 40.2 that  have been derived speciﬁ  cally for these control charts. Values of the factors  depend on sample size $n$ . For the _  chart:  

$$
L C L=\overline{{{\overline{{{x}}}}}}-A_{2}\overline{{{R}}}\qquad\mathrm{and}\qquad U C L=\overline{{{\overline{{{x}}}}}}+A_{2}\overline{{{R}}}
$$  

and for the $R$  chart:  

$$
L C L=D_{3}{\overline{{{R}}}}\qquad\mathrm{and}\qquad U C L=D_{4}{\overline{{{R}}}}
$$
 R  

# Example 40.1  __ x  and  R  charts  

Eight samples  $(m=8)$  of size 4  $(n=4)$ ) have been collected from a manufactur- ing process that is in statistical control, and the dimension of interest has been  measured for each part. It is desired to determine the values of the center,  $L C L$ ,  and  $U C L$  for _  and $R$  charts. The calculated _  values (units are cm) for the eight  samples are 2.008, 1.998, 1.993, 2.002, 2.001, 1.995, 2.004, and 1.999. The calculated $R$   values (cm) are, respectively $,0.027,0.011,0.017,0.009,0.014,0.020,0.024$ , and 0.018.  

Solution  The calculation of _  and $R$  values above comprise step 1 in the  procedure. In step 2, the grand mean of the sample averages is computed:  

$$
\overline{{\overline{{x}}}}=(2.008+1.998+\cdot\cdot\cdot+1.999)/8=2.000
$$  

In step 3, the mean value of $R$  is computed:  

$$
\overline{{R}}=(0.027+0.011+\cdot\cdot\cdot+0.018)/8=0.0175
$$  

In step 4, the values of LCL and UCL are determined based on factors in  Table 40.2. First, using Equation (40.3) for the _  chart,  

$$
\begin{array}{c}{L C L=2.000-0.729(0.0175)=1.9872}\\ {U C L=2.000+0.729(0.0175)=2.0128}\end{array}
$$  

and for the $R$  chart using Equation (40.4),  

$$
\begin{array}{l}{L C L=0(0.0175)=0}\\ {U C L=2.282(0.0175)=0.0399}\end{array}
$$  

The two control charts are constructed in Figure 40.2 with the sample data  plotted in the charts.  

![](images/16f1d8cfe7bd15bf888cf549693966b9fb17f3af08520e22b61dc6eae11a20d6.jpg)  
FIGURE 40.2  Control  charts for Example 40.2.  

# 40.3.2  CONTROL CHARTS FOR ATTRIBUTES  

Control charts for attributes do not use a measured quality variable; instead, they  monitor the number of defects present in the sample or the fraction defect rate as  the plotted statistic. Examples of these kinds of attributes include number of defects  per automobile, fraction of bad parts in a sample, existence or absence of ﬂ  ash in  plastic moldings, and number of ﬂ  aws in a roll of sheet steel. The two principal types  of control charts for attributes are the $\pmb{p}$  chart , which plots the fraction defect rate in  successive samples; and the  c chart , which plots the number of defects, ﬂ  aws, or other  nonconformities per sample.  

p  Chart  In the $p$  chart, the quality characteristic of interest is the proportion ( $\boldsymbol{\mathscr{p}}$  for  proportion) of nonconforming or defective units. For each sample, this proportion $p_{i}$ is the ratio of the number of nonconforming or defective items  $d_{i}$  over the number  of units in the sample $n$  (assume samples of equal size in constructing and using the  control chart)  

$$
p_{i}=\frac{d_{i}}{n}
$$  

where  $i$  is used to identify the sample. If the  $p_{i}$  values for a sufﬁ  cient number of  samples are averaged, the mean value   p  is a reasonable estimate of the true value  of $p$  for the process. The $p$  chart is based on the binomial distribution, where $p$  is  the probability of a nonconforming unit. The center in the  $p$  chart is the computed  __ value of p   for  $m$  samples of equal size $n$  collected while the process is operating in  statistical control.  

$$
{\overline{{p}}}={\frac{\displaystyle\sum_{i=1}^{m}p_{i}}{\displaystyle m}}
$$  

The control limits are computed as three standard deviations on either side of the  center. Thus,  

$$
L C L=\overline{{{p}}}-3\sqrt{\frac{\overline{{{p}}}(1-\overline{{{p}}})}{n}}\qquad\mathrm{and}\qquad L C L=\overline{{{p}}}+3\sqrt{\frac{\overline{{{p}}}(1-\overline{{{p}}})}{n}}
$$  

where the standard deviation of   p  in the binomial distribution is given by  

$$
\sigma_{p}={\sqrt{\frac{{\overline{{p}}}(1-{\overline{{p}}})}{n}}}
$$  

If the value of p   is relatively low and the sample size $n$  is small, then the lower control  limit computed by the ﬁ  rst of these equations is likely to be a negative value. In this  case, let $L C L=0$  (the fraction defect rate cannot be less than zero).  

c  Chart   In the $c$  chart ( $c$  for count), the number of defects in the sample are plotted  over time. The sample may be a single product such as an automobile, and $c=$  number  of quality defects found during ﬁ  nal inspection. Or the sample may be a length of  carpeting at the factory prior to cutting, and $c=$ number of imperfections discovered  in that strip. The  $c$  chart is based on the Poisson distribution, where  $c=$ parameter  representing the number of events occurring within a deﬁ  ned sample space (defects  per car, imperfections per speciﬁ  ed length of carpet). The best estimate of the true  value of $c$  is the mean value over a large number of samples drawn while the process  is in statistical control:  

$$
\displaystyle\overline{{c}}=\,\frac{\displaystyle\sum_{i=1}^{m}c_{i}}{\displaystyle m}
$$  

This value of c  is used as the center for the control chart. In the Poisson distribution,  the standard deviation is the square root of parameter  $c$ . Thus, the control limits are:  

$$
L C L=\overline{{{c}}}-3\sqrt{{\overline{{{c}}}}}\qquad\mathrm{and}\qquad U C L=\overline{{{c}}}+3\sqrt{{\overline{{{c}}}}}
$$  

# 40.3.3  INTERPRETING THE CHARTS  

When control charts are used to monitor production quality, random samples are  drawn from the process of the same size $n$  used to construct the charts. For  _  and  $R$   charts, the _  and $R$  values of the measured characteristic are plotted on the control  chart. By convention, the points are usually connected, as in the ﬁ  gures. To interpret  the data, one looks for signs that indicate the process is not in statistical control. The  most obvious sign is when _  or $R$  (or both) lie outside the  $L C L$  or  $U C L$  limits. This  indicates an assignable cause such as bad starting materials, new operator, broken  tooling, or similar factors. An out-of-limit _  indicates a shift in the process mean. An  out-of-limit $R$  shows that the variability of the process has changed. The usual effect  is that $R$  increases, indicating variability has risen. Less-obvious conditions may reveal  process problems, even though the sample points lie within the  $\pm3\sigma$  limits. These  conditions include (1) trends or cyclical patterns in the data, which may mean wear or  other factors that occur as a function of time; (2) sudden changes in average level of  the data; and (3) points consistently near the upper or lower limits.  

The same kinds of interpretations that apply to the $x$  chart and  $R$  chart are also  applicable to the $p$  chart and  $c$  chart.  

#  Quality Programs in Manufacturing  

Statistical process control is widely used for monitoring the quality of manufactured  parts and products. Several additional quality programs are also used in industry,  and this section brieﬂ  y describes four of them: (1) total quality management, (2) six  sigma, (3) Taguchi methods, and (4) ISO 9000. These programs are not alternatives  to statistical process control; in fact, the tools used in SPC are included within the  methodologies of total quality management and six sigma.  

# 40.4.1  TOTAL QUALITY MANAGEMENT  

Total quality management (TQM) is a management approach to quality that pursues  three main goals: (1) achieving customer satisfaction, (2) encouraging the involvement  of the entire workforce, and (3) continuous improvement.  

The customer and customer satisfaction are a central focus of TQM, and products  are designed and manufactured with this focus in mind. The product must be designed  with the features that customers want, and it must be manufactured free of deﬁ  ciencies.  Within the scope of customer satisfaction is the recognition that there are two categories  of customers: (1) external customers and (2) internal customers. External customers are  those who purchase the company’s products and services. Internal customers are inside  the company, such as the company’s ﬁ  nal assembly department that is the customer of  the parts production departments. For the total organization to be effective and efﬁ  cient,  satisfaction must be achieved in both categories of customers.  

In TQM, worker involvement in the quality efforts of the organization extends  from the top executives through all levels beneath. There is recognition of the  important inﬂ  uence that product design has on product quality and how decisions  made during design affect the quality that can be achieved in manufacturing. In  addition, production workers are made responsible for the quality of their own  output, rather than rely on inspectors to uncover defects after the parts are already  produced. TQM training, including use of the tools of statistical process control, is  provided to all workers. The pursuit of high quality is embraced by every member  of the organization.  

The third goal of TQM is continuous improvement; that is, adopting the attitude  that it is always possible to make something better, whether it is a product or a  process. Continuous improvement in an organization is generally implemented  using worker teams that have been organized to solve speciﬁ  c problems that are  identiﬁ  ed in production. The problems are not limited to quality issues. They may  include productivity, cost, safety, or any other area of interest to the organization.  Team members are selected on the basis of their knowledge and expertise in the  problem area. They are drawn from various departments and serve part-time on  the team, meeting several times per month until they are able to make recommen- dations and/or solve the problem. Then the team is disbanded.  

The Six Sigma quality program originated and was ﬁ  rst used at Motorola Corpora- tion in the 1980s. It has been adopted by many other companies in the United States  and was brieﬂ  y discussed in Section 1.6 as one of the recent developments in manu- facturing. Six Sigma is quite similar to total quality management in its emphasis on  management involvement, worker teams to solve speciﬁ  c problems, and the use of  SPC tools such as control charts. The major difference between Six Sigma and TQM  is that Six Sigma establishes measurable targets for quality based on the number  of standard deviations (sigma  $\sigma$ ) away from the mean in the normal distribution.  Six sigma implies near perfection in the process in the normal distribution. A proc- ess operating at the  $6\sigma$  level in a Six Sigma program produces no more than 3.4  defects per million, where a defect is anything that might result in lack of customer  satisfaction.  

As in TQM, worker teams participate in problem-solving projects. A project  requires the Six Sigma team to (1) deﬁ  ne the problem, (2) measure the process  and assess current performance, (3) analyze the process, (4) recommend improve- ments, and (5) develop a control plan to implement and sustain the improvements.  The responsibility of management in Six Sigma is to identify important problems  in their operations and sponsor the teams to address those problems.  

Statistical Basis of Six Sigma  An underlying assumption in Six Sigma is that the  defects in any process can be measured and quantiﬁ  ed. Once quantiﬁ  ed, the causes of  the defects can be identiﬁ  ed, and improvements can be made to eliminate or reduce  the defects. The effects of any improvements can be assessed using the same measure- ments in a before-and-after comparison. The comparison is often summarized as a  sigma level; for example, the process is now operating at the 4.8-Sigma level whereas  before it was only operating at the 2.6-Sigma level. The relationship between sigma  level and defects per million (DPM) is listed in Table 40.3 for a Six Sigma program.  Accordingly, the DPM was previously at 135,666 defects per 1,000,000 in this example,  whereas it has now been reduced to 483 DPM.  

TABLE  •  40.3  Sigma Levels and Corresponding Defects Per Million in a Six Sigma  Program. 
![](images/2fd33844080bb7b44a93798dc9f87cc7dcae4987c0795e4cf0e58e21887d1d19.jpg)  

A traditional measure for good process quality is  $\pm3\sigma$  (three sigma level).  It implies that the process is stable and in statistical control, and the variable  represen  ting the output of the process is normally distributed. Under these condi- tions, $99.73\,\%$  of the output will be within the $\pm3\sigma$  range, and  $0.27\,\%$  or 2700 parts  per million will lie outside these limits  $(0.135\%$  or 1350 parts per million beyond  the upper limit and the same number beyond the lower limit). But wait a minute,  if one looks up 3.0 sigma in Table 40.3, there are 66,807 defects per million. Why  is there a difference between the standard normal distribution value (2700 DPM)  and the value given in Table 40.3 (66,807 DPM)? There are two reasons for this  discrepancy. First, the values in Table 40.3 refer to only one tail of the distribution,  so that an appropriate comparison with the standard normal tables would only  use one tail of the distribution (1350 DPM). Second, and much more signiﬁ  cant,  is that when Motorola devised the Six Sigma program, they considered the opera- tion of processes over long periods of time, and processes over long periods tend  to experience shifts from their original process means. To compensate for these  shifts, Motorola decided to adjust the standard normal values by  $1.5\sigma$ . To sum- marize, Table 40.3 includes only one tail of the normal distribution, and it shifts  the distribution by 1.5 sigma relative to the standard normal distribution. These  effects can be seen in Figure 40.3.  

Measuring the Sigma Level  In a Six Sigma project, the performance level of  the process of interest is reduced to a sigma level. This is done at two points during  the project: (1) after measurements have been taken of the process as it is currently  operating and (2) after process improvements have been made to assess the effect of  the improvements. This provides a before-and-after comparison. High sigma values  represent good performance; low sigma values mean poor performance.  

To ﬁ  nd the sigma level, the number of defects per million must ﬁ  rst be deter- mined. There are three measures of defects per million used in Six Sigma. The ﬁ  rst  and most important is the defects per million opportunities ( DPMO ), which con- siders that there may be more than one type of defect that can occur in each unit  (product or service). More complex products are likely to have more opportunities  

![](images/5088bdee5236c6841f2b0f48827690b82b600d534a40a870272a50194a95dd6d.jpg)  
FIGURE 40.3  Normal distribution shift by  $1.5\sigma$  from original mean and consideration of only one tail of the distribution  (at right). Key: $\mu_{1}=$  mean of original distribution, $\mu_{2}=$  mean of shifted distribution, $\sigma=$  standard distribution.  

for defects, while simple products have fewer opportunities. Thus,  DPMO  accounts  for the complexity of the product and allows entirely different kinds of products or  services to be compared. Defects per million opportunities is calculated using the  following equation:  

$$
D P M O=1,\!000,\!000\frac{N_{d}}{N_{u}N_{o}}
$$  

where  $N_{d}=$  total number of defects found,  $N_{u}=$  number of units in the population  of interest, and  $N_{o}=$  number of opportunities for a defect per unit. The constant  1,000,000 converts the ratio into defects per million.  

Other measures besides  DPMO  are defects per million ( DPM ), which measures  all of the defects found in the population, and defective units per million ( DUPM ),  which counts the number of defective units in the population and recognizes that  there may be more than one type of defect in any defective unit. The following two  equations can be used to compute $D P M$  and  DUPM :  

$$
D P M=1,\!000,\!000\frac{N_{d}}{N_{u}}
$$  

$$
D U P M=1,\!000,\!000\frac{N_{d u}}{N_{u}}
$$  

where $N_{d u}=$  number of defective units in the population, and the other terms are the  same as for Equation (40.10). Once the values of  DPMO ,  $D P M$ , and  DUPM  have  been determined, Table 40.3 can be used to convert these values to their correspond- ing sigma levels.  

# Example 40.2  Determining the  sigma level of a  process  

A ﬁ  nal assembly plant that makes dishwashers inspects for 23 features that  are considered important for overall quality. During the previous month,  9,056 dishwashers were produced. During inspection, 479 defects among  the 23 features were found, and 226 dishwashers had one or more defect.  Determine $D P M O,D P M$ , and  $D U P M$  for these data and convert each to its  corresponding sigma level.  

Solution:   Summarizing the data, $N_{u}=9056,N_{o}=23,N_{d}=479$ , and  $N_{d u}=226$ Thus,  

$$
D P M O=1{,}000{,}000{\frac{479}{9056(23)}}=2300
$$  

The corresponding sigma level is about 4.3 from Table 40.3.  

$$
D P M=1{,}000{,}000{\frac{479}{9056}}=52{,}893
$$  

The corresponding sigma level is about 3.1.  

$$
D U P M=1,\!000,\!000\frac{226}{9056}=24,\!956
$$  

The corresponding sigma level is about 3.4.  

# 40.4.3  TAGUCHI METHODS  

Genichi Taguchi has had an important inﬂ  uence on the development of quality engi- neering, especially in the design area—both product design and process design. This  section reviews two of the Taguchi methods: (1) the loss function and (2) robust design.  More complete coverage can be found among the references [5], [10].  

The Loss Function  Taguchi deﬁ  nes quality as “the loss a product costs society from  the time the product is released for shipment” [10]. Loss includes costs to operate,  failure to function, maintenance and repair costs, customer dissatisfaction, injuries  caused by poor design, and similar costs. Some of these losses are difﬁ  cult to quan- tify in monetary terms, but they are nevertheless real. Defective products (or their  components) that are exposed before shipment are not considered part of this loss.  Instead, any expense to the company resulting from scrap or rework of defective  product is a manufacturing cost rather than a quality loss.  

Loss occurs when a product’s functional characteristic differs from its nominal or  target value. Although functional characteristics do not translate directly into dimen- sional features, the loss relationship is most readily understood in terms of dimensions.  When the dimension of a component deviates from its nominal value, the component’s  function is adversely affected. No matter how small the deviation, there is some loss in  function. The loss increases at an accelerating rate as the deviation grows, according to  Taguchi. Let $x=$  the quality characteristic of interest and $N=$  its nominal value, then  the loss function is a U-shaped curve as in Figure 40.4(a). A quadratic equation can be  used to describe this curve:  

$$
L(x)=k(x-N)^{2}
$$  

where $L(x)=\log$  function; $k=$  constant of proportionality; and $x$  and $N$ are deﬁ  ned  above. At some level of deviation  $(x_{2}-N)=-(x_{1}-N)$ , the loss will be prohibitive,  and it is necessary to scrap or rework the product. This level identiﬁ  es one possible  way of specifying the tolerance limit for the dimension.  

In the traditional approach to quality control, tolerance limits are deﬁ  ned and any  product within those limits is acceptable. Whether the quality characteristic (e.g., the  dimension) is close to the nominal value or close to one of the tolerance limits, it is  acceptable. Trying to visualize this approach in terms analogous to the preceding  relation, the discontinuous loss function in Figure 40.4(b) is obtained. The reality is  that products closer to the nominal speciﬁ  cation are better quality and will provide  

![](images/826e0807b8ff71bbc4ff3de4b3ea6cbf3e7925b0525a3f1294dd956542a29814.jpg)  
FIGURE 40.4  (a) The  quadratic quality loss  function. (b) Loss function  implicit in traditional  tolerance speciﬁ  cation.  

greater customer satisfaction. In order to improve quality and customer satisfaction,  one must attempt to reduce the loss by designing the product and process to be as  close as possible to the target value.  

![](images/7d73ae7382c5e05e10bc4348e4f65b1c9b7e7cc60f866accc882f269fca25c91.jpg)  

A certain product has a critical dimension that is speciﬁ  ed as  $20.00\pm0.04\;\mathrm{cm}.$ .  Repair records indicate that if the tolerance is exceeded, there is a $75\%$  prob- ability that the product will be returned to the manufacturer at a cost of  $\S80$   for replacement and shipping. (a) Estimate the constant $k$  in the Taguchi loss  function, Equation (40.13). (b) Using the loss function constant determined in  (a), what would be the value of the loss function if the company could maintain  a tolerance of  $\pm0.01$  cm instead of  $\pm0.04\,\mathrm{cm}?$  

Solution:   In Equation (40.13), the value of  $(x-N)$  is the tolerance  $0.04\;\mathrm{cm}$ .  The loss is the expected cost of replacement and shipping, which is calculated  as follows:  

$$
E\{L(x)\}=0.75(\S80)+0.25(0)=\S60
$$  

Using this expected cost in the loss function, the value of $k$  can be determined  as follows:  

$$
\begin{array}{c l l}{60=k(0.04)^{2}=0.0016k}\\ {\ }\\ {k=60/0.0016=\S37{,}500}\end{array}
$$  

Accordingly, the Taguchi loss function is $L(x)=37{,}500(x-N)$  

(b) For a tolerance of $\pm0.01\;\mathrm{cm}$ , the loss function is determined as follows:  

$$
L(x)=37{,}500(0{.}01)^{2}=37{,}500(0{.}0001)=\S\mathbf{3.75}
$$  

This is a signiﬁ  cant reduction from the $\S60.00$  using a tolerance of  $\pm0.04\,\mathrm{cm}$ .  

Robust Design  A basic purpose of quality control is to minimize variations. Taguchi  calls the variations noise factors. A  noise factor  is a source of variation that is impossi- ble or difﬁ  cult to control and that affects the functional characteristics of the product.  Three types of noise factors can be distinguished: (1) unit-to-unit, (2) internal, and  (3) external.  

Unit-to-unit noise factors  consist of inherent random variations in the process or  product caused by variability in raw materials, machinery, and human participation.  These are noise factors that were previously called random variations in the process.  They are associated with a production process that is in statistical control.  

Internal noise factors  are sources of variation that are internal to the product or  process. They include time-dependent factors such as wear of mechanical components,  spoilage of raw materials, and fatigue of metal parts; and operational errors, such as  improper settings on the product or machine tool. An  external noise factor  is a source  of variation that is external to the product or process, such as outside temperature,  humidity, raw material supply, and input voltage. Internal and external noise factors  constitute what were previously called assignable variations.  

A  robust design  is one in which the product’s function and performance are rela- tively insensitive to variations in design and manufacturing parameters. It involves  the design of both the product and process so that the manufactured product will  be relatively unaffected by all noise factors. An example of a robust product design  is an automobile whose ignition starter works as well in Minneapolis, Minnesota in  winter as in Meridian, Mississippi in summer. An example of robust process design is  a metal extrusion operation that produces good product despite temperature varia- tions in the starting billet.  

ISO 9000 is a set of international standards that relate to the quality of the products  (and services, if applicable) delivered by a given facility. The standards were devel- oped by the International Organization for Standardization (ISO), based in Geneva,  Switzerland. ISO 9000 establishes standards for the systems and procedures used by  the facility that determine the quality of its products. ISO 9000 is not a standard for  the products themselves. Its focus is on systems and procedures, which include the  facility’s organizational structure, responsibilities, methods, and resources needed  to manage quality. ISO 9000 is concerned with the activities used by the facility to  ensure that its products achieve customer satisfaction.  

ISO 9000 can be implemented in two ways, formally and informally. Formal imple- mentation means that the facility becomes registered, which certiﬁ  es that the facility  meets the requirements of the standard. Registration is obtained through a third-party  agency that conducts on-site inspections and reviews the facility’s quality systems  and procedures. A beneﬁ  t of registration is that it qualiﬁ  es the facility to do business  with companies that require ISO 9000 registration, which is common in the European  Economic Community where certain products are regulated and ISO 9000 registra- tion is required for companies making these products.  

Informal implementation of ISO 9000 means that the facility practices the stand- ards or portions thereof simply to improve its quality systems. Such improvements  are worthwhile, even without formal certiﬁ  cation, for companies desiring to deliver  high quality products.  

#  Inspection Principles  

Inspection  involves the use of measurement and gaging techniques to determine  whether a product, its components, subassemblies, or starting materials conform to  design speciﬁ  cations. The design speciﬁ  cations are established by the product de- signer, and for mechanical products they refer to dimensions, tolerances, surface ﬁ  n- ish, and similar features. Dimensions, tolerances, and surface ﬁ  nish were deﬁ  ned in  Chapter 5, and many of the measuring instruments and gages for assessing these  speciﬁ  cations were described in that chapter.  

Inspection is performed before, during, and after manufacturing. The incoming  materials and starting parts are inspected upon receipt from suppliers; work units  are inspected at various stages during their production; and the ﬁ  nal product should  be inspected prior to shipment to the customer.  

There is a difference between inspection and testing, which is a closely related  topic. Whereas inspection determines the quality of the product relative to design  speciﬁ  cations, testing generally refers to the functional aspects of the product. Does  the product operate the way it is supposed to operate? Will it continue to operate for  a reasonable period of time? Will it operate in environments of extreme temperature  and humidity? In quality control,  testing  is a procedure in which the product, sub- assembly, part, or material is observed under conditions that might be encountered  during service. For example, a product might be tested by operating it for a certain  period of time to determine whether it functions properly. If it passes the test, it is  approved for shipment to the customer.  

Testing of a component or material is sometimes damaging or destructive. In  these cases, the items must be tested on a sampling basis. The expense of destruc- tive testing is signiﬁ  cant, and great efforts are made to develop methods that do  not destroy the item. These methods are referred to as  nondestructive testing  or  nondestructive evaluation .  

Inspections divide into two types: (1)  inspection by variables , in which the product  or part dimensions of interest are measured by the appropriate measuring instru- ments; and (2)  inspection by attributes , in which the parts are gaged to determine  whether they are within tolerance limits. The advantage of measuring a part dimen- sion is that data are obtained about its actual value. The data might be recorded over  time and used to analyze trends in the manufacturing process. Adjustments in the  process can be made based on the data so that future parts are produced closer to  the nominal design value. When a part dimension is simply gaged, all that is known is  whether it is within tolerance or too big or too small. On the positive side, gaging can  be done quickly and at low cost.  

# 40.5.1  MANUAL AND AUTOMATED INSPECTION  

Inspection procedures are often performed manually. The work is usually boring  and monotonous, yet the need for precision and accuracy is high. Hours are some- times required to measure the important dimensions of only one part. Because of  the time and cost of manual inspection, statistical sampling procedures are generally  used to reduce the need to inspect every part.  

Sampling versus 1 $100\%$  Inspection   When sampling inspection is used, the  number of parts in the sample is generally small compared to the quantity of parts  produced. The sample size may be only $1\%$  of the production run. Because not all of  the items in the population are measured, there is a risk in any sampling procedure  that defective parts will slip through. One of the goals in statistical sampling is to  deﬁ  ne the expected risk; that is, to determine the average defect rate that will pass  through the sampling procedure. The risk can be reduced by increasing the sample  size and the frequency with which samples are collected. But the fact remains that  $100\%$  good quality cannot be guaranteed in a sampling inspection procedure.  

Theoretically, the only way to achieve  $100\%$  good quality is by  $100\%$  inspection;  thus, all defects are screened and only good parts pass through the inspection proce- dure. However, when $100\%$  inspection is done manually, two problems are encoun- tered. The ﬁ  rst is the expense involved. Instead of dividing the cost of inspecting  the sample over the number of parts in the production run, the unit inspection cost  is applied to every part in the batch. Inspection cost sometimes exceeds the cost  of making the part. Second, in  $100\%$  manual inspection, there are almost always  errors associated with the procedure. The error rate depends on the complexity and  difﬁ  culty of the inspection task and how much judgment is required by the human  inspector. These factors are compounded by operator fatigue. Errors mean that a  certain number of poor quality parts will be accepted and a certain number of good  quality parts will be rejected. Therefore,  $100\%$  inspection using manual methods is  no guarantee of $100\%$  good quality product.  

Automated  $100\%$  Inspection   Automation of the inspection process offers a  possible way to overcome the problems associated with  $100\%$  manual inspection.  Automated inspection  is deﬁ  ned as automation of one or more steps in the inspec- tion procedure, such as (1) automated presentation of parts by an automated handl- ing system, with a human operator still performing the actual inspection process  (e.g., visually examining parts for ﬂ  aws); (2) manual loading of parts into an auto- matic inspection machine; and (3) fully automated inspection cell in which parts  are both presented and inspected automatically. Inspection automation can also  include (4) computerized data collection from electronic measuring instruments.  

Automated  $100\%$  inspection can be integrated with the manufacturing process  to accomplish some action relative to the process. The actions can be one or both of  the following: (1) parts sortation, and/or (2) feedback of data to the process.  Parts  sortation  means separating parts into two or more quality levels. The basic sortation  includes two levels: acceptable and unacceptable. Some situations require more than  two levels, such as acceptable, reworkable, and scrap. Sortation and inspection may  be combined in the same station. An alternative approach is to locate one or more  inspections along the processing line, and instructions are sent to a sortation station  at the end of the line indicating what action is required for each part.  

Feedback  of inspection data to the upstream manufacturing operation allows  compensating adjustments to be made in the process to reduce variability and  improve quality. If inspection measurements indicate that the output is drifting  toward one of the tolerance limits (e.g., due to tool wear), corrections can be made  to process parameters to move the output toward the nominal value. The output is  thereby maintained within a smaller variability range than possible with sampling  inspection methods.  

# 40.5.2  CONTACT VERSUS NONCONTACT INSPECTION  

There are a variety of measurement and gaging technologies available for inspec  tion.  The possibilities can be divided into contact and noncontact inspection methods.  Contact inspection  involves the use of a mechanical probe or other device that  makes contact with the object being inspected. By its nature, contact inspection is  usually concerned with measuring or gaging some physical dimension of the part.  It is accomplished manually or automatically. Most of the traditional measuring  and gaging devices described in Chapter 5 relate to contact inspection. An example  of an automated contact measuring system is the coordinate measuring machine  (Section 40.6.1).  

Noncontact inspection  methods utilize a sensor located a certain distance from the  object to measure or gage the desired feature(s). Typical advantages of noncontact  inspection are (1) faster inspection cycles, and (2) avoidance of damage to the part  that might result from contact. Noncontact methods can often be accomplished on the  production line without any special handling. By contrast, contact inspection usually  requires special positioning of the part, necessitating its removal from the production  line. Also, noncontact inspection methods are inherently faster because they employ a  stationary probe that does not require positioning for every part. By contrast, contact  inspection requires positioning of the contact probe against the part, which takes time. Noncontact inspection technologies can be classiﬁ  ed as optical or nonoptical.  Prominent among the optical methods are lasers (Section 40.6.2) and machine vision  (Section 40.6.3). Nonoptical inspection sensors include electrical ﬁ  eld techniques,  radiation techniques, and ultrasonics (Section 40.6.4).  

#  Modern Inspection Technologies  

Advanced technologies are substituting for manual measuring and gaging tech- niques in modern manufacturing plants. They include contact and noncontact sens- ing methods. The coverage begins with an important contact inspection technology:  coordinate measuring machines.  

# 40.6.1  COORDINATE MEASURING MACHINES  

A coordinate measuring machine (CMM) consists of a contact probe and a mechanism  to position the probe in three dimensions relative to surfaces and features of a work  part. See Figure 40.5. The location coordinates of the probe can be accurately recorded  as it contacts the part surface to obtain part geometry data.  

In a CMM, the probe is fastened to a structure that allows movement of the probe  relative to the part, which is ﬁ  xtured on a worktable connected to the structure. The  structure must be rigid to minimize deﬂ  ections that contribute to measurement errors.  The machine in Figure 40.5 has a bridge structure, one of the most common designs.  Special features are used in CMM structures to build high accuracy and precision into  the measuring machine, including use of low-friction air-bearings and mechanical iso- lation of the CMM to reduce vibrations. An important aspect in a CMM is the contact  probe and its operation. Modern “touch-trigger” probes have a sensitive electrical  contact that emits a signal when the probe is deﬂ  ected from its neutral position in  the slightest amount. On contact, the coordinate positions are recorded by the CMM  controller, adjusting for overtravel and probe size.  

Positioning of the probe relative to the part can be accomplished either manually or  under computer control. Methods of operating a CMM can be classiﬁ  ed as (1) manual  control, (2) manual computer-assisted, (3) motorized computer-assisted, and (4) direct  computer control.  

In  manual control , a human operator physically moves the probe along the axes  to contact the part and record the measurements. The probe is free-ﬂ  oating for easy  movement. Measurements are indicated by digital read-out, and the operator can  record the measurement manually or automatically (paper print-out). Any trigono- metric calculations must be made by the operator. The  manual computer-assisted CMM is capable of computer data processing to perform these calculations. Types  of computations include simple conversions from U.S. customary units to SI, deter- mining the angle between two planes, and determining hole-center locations. The  probe is still free-ﬂ  oating to permit the operator to bring it into contact with part  surfaces.  

Motorized computer-assisted  CMMs power drive the probe along the machine axes  under operator guidance. A joystick or similar device is used to control the motion.  Low-power stepping motors and friction clutches are used to reduce the effects of  collisions between probe and part. The  direct computer-control  CMM operates like  

![](images/48446d911eb3a1dcc10002d23cdaf3bc79b3dfeb3b4d9ef98ea6371134a4a2cb.jpg)  
FIGURE 40.5  Coordinate measuring  machine. (Courtesy of  Hexagon Metrology.)  

a CNC machine tool. It is a computerized inspection machine that operates under  program control. The basic capability of a CMM is to determine coordinate values  where its probe contacts the surface of a part. Computer control permits the CMM to  accomplish more sophisticated measurements and inspections, such as (1) determin- ing center location of a hole or cylinder, (2) deﬁ  nition of a plane, (3) measurement of  ﬂ  atness of a surface or parallelism between two surfaces, and (4) measurement of an  angle between two planes.  

Advantages of using coordinate measuring machines over manual inspection  methods include (1) higher productivity—a CMM can perform complex inspection  procedures in much less time than traditional manual methods; (2) greater inherent  accuracy and precision than conventional methods; and (3) reduced human error  through automation of the inspection procedure and associated computations [8].  A CMM is a general-purpose machine that can be used to inspect a variety of part  conﬁ  gurations.  

# 40.6.2  MEASUREMENTS WITH LASERS  

Recall that laser stands for light ampliﬁ  cation by stimulated emission of radiation.  Applications of lasers include cutting (Section 25.3.3) and welding (Section 29.4).  These applications involve the use of solid-state lasers capable of focusing sufﬁ  cient  power to melt or sublimate the work material. Lasers for measurement applications  are low-power gas lasers such as helium-neon, which emits light in the visible range.  The light beam from a laser is (1) highly monochromatic, which means the light has a  single wave length, and (2) highly collimated, which means the light rays are parallel.  These properties have motivated a growing list of laser applications in measurement  and inspection. Two are described here.  

Scanning Laser Systems   The scanning laser uses a laser beam deﬂ  ected by a rotat- ing mirror to produce a beam of light that sweeps past an object, as in Figure 40.6.  A photodetector on the far side of the object senses the light beam during its sweep  except for the short time when it is interrupted by the object. This time period can be  measured quickly with great accuracy. A microprocessor system measures the time  interruption that is related to the size of the object in the path of the laser beam, and  converts the time to a linear dimension. Scanning laser beams can be applied in high  production on-line inspection and gaging. Signals can be sent to production equip- ment to make adjustments in the process and/or activate a sortation device on the  production line. Applications of scanning laser systems include rolling-mill operations,  wire extrusion, machining, and grinding.  

Laser Triangulation   Triangulation is used to determine the distance of an object  from two known locations by means of trigonometric relationships of a right triangle.  The principle can be applied in dimensional measurements using a laser system, as in  Figure 40.7. The laser beam is focused on an object to form a light spot on the surface.  A position-sensitive optical detector is used to determine the location of the spot. The  angle $A$  of the beam directed at the object and the distance $H$  are ﬁ  xed and known.  

![](images/d37ff4768f44d2a016d2b11f7fa9b3ac6e866e115baf6e33c04b1f341048defd.jpg)  
FIGURE 40.6  Scan- ning laser system for  measuring diameter of  cylindrical work part;  time of interruption of  light beam is propor- tional to diameter $D$ .  

![](images/9a12393eb6aa11a0fa487b6695c607d911bf11d69744d3975ac601990ab5c271.jpg)  
FIGURE 40.7  Laser  triangulation to measure  part dimension $D$ .  

Given that the photodetector is located a ﬁ  xed distance above the worktable, the part  depth $D$  in the setup of Figure 40.7 is determined from  

$$
D=H-R=H-L\cot A
$$  

where  $L$  is determined by the position of the light spot on the work part.  

# 40.6.3  MACHINE VISION  

Machine vision involves the acquisition, processing, and interpretation of image data  by computer for some useful application. Vision systems can be classiﬁ  ed as two  dimensional or three dimensional. Two-dimensional systems view the scene as a 2-D  image, which is quite adequate for applications involving a planar object. Examples  include dimensional measuring and gaging, verifying the presence of components,  and checking for features on a ﬂ  at (or almost ﬂ  at) surface. Three-dimensional vision  systems are required for applications requiring a 3-D analysis of the scene, where  contours or shapes are involved. The majority of current applications are 2-D, and  the discussion will focus (excuse the pun) on this technology.  

Operation of Machine Vision Systems   Operation of a machine vision system  consists of three steps, depicted in Figure 40.8: (1) Image acquisition and digitization,  (2) image processing and analysis, and (3) interpretation.  

Image acquisition and digitizing is accomplished by a video camera connected to a  digitizing system to store the image data for subsequent processing. With the camera  focused on the subject, an image is obtained by dividing the viewing area into a matrix  of discrete picture elements (called  pixels ), in which each element assumes a value  proportional to the light intensity of that portion of the scene. The intensity value for  each pixel is converted to its equivalent digital value by analog-to-digital conversion.  Image acquisition and digitizing is depicted in Figure 40.9 for a  binary vision  system,  in which the light intensity is reduced to either of two values (black or white $=0$  or 1),  as in Table 40.4. The pixel matrix in the illustration is only $12\times12$ ; a real vision system  would have many more pixels for better resolution. Each set of pixel values is a  frame ,  which consists of the set of digitized pixel values. The frame is stored in computer  memory. The process of reading all the pixel values in a frame is performed 30 times  per second in United States, 25 cycle/s in European systems.  

![](images/3a4dff08d80f8856504e2df17126f0be3dd1b8554ed8f5604f5dca56f79168cf.jpg)  
FIGURE 40.8  Operation of a machine  vision system.  

The  resolution  of a vision system is its ability to sense ﬁ  ne details and features in  the image. This depends on the number of pixels used. Common pixel arrays include  640 (horizontal) $\times\,480$  (vertical),  $1024\times768$ , or  $1040\times1392$  picture elements. The  more pixels in the vision system, the higher its resolution. However, system cost  increases as pixel count increases. Also, time required to read the picture elements  and process the data increases with number of pixels. In addition to binary vision  systems, more sophisticated vision systems distinguish various gray levels in the  image that permit them to determine surface characteristics such as texture. Called  gray-scale vision , these systems typically use four, six, or eight bits of memory. Other  vision systems can recognize colors.  

The second function in machine vision is  image processing and analysis . The data  for each frame must be analyzed within the time required to complete one scan (1/30 s  or 1/25 s). Several techniques have been developed to analyze image data, including  edge detection and feature extraction.  Edge detection  involves determining the loca- tions of boundaries between an object and its surroundings. This is accomplished by  identifying contrast in light intensity between adjacent pixels at the borders of the  object.  Feature extraction  is concerned with determining feature values of an image.  

![](images/3c8809ae50594d47a745d2a6b672f9e52520f3e464eea6eb5166421efccc6382.jpg)  

TABLE  •  40.4  Pixel values in a binary vision system for the image in Figure 40.8. 
![](images/7884b788ba26ace2672c7f7b743e078216b61eef9412a5a7d967f185c0a4704e.jpg)  

Many machine vision systems identify an object in the image by means of its features.  Features of an object include area, length, width, or dia  meter of the object, peri- meter, center of gravity, and aspect ratio. Feature extraction algorithms are designed  to deter  mine these features based on the object’s area and boundaries. Area of an  object can be determined by counting the number of pixels that make up the object.  Length can be found by measuring the distance (in pixels) between two opposite  edges of the part.  

Interpretation  of the image is the third function. It is accomplished by extracted  features. Interpretation is usually concerned with recognizing the object—identifying  the object in the image by comparing it to predeﬁ  ned models or standard values. One  common interpretation technique is  template matching , which refers to methods that  compare one or more features of an image with corresponding features of a model  (template) stored in computer memory.  

Machine Vision Applications   The interpretation function in machine vision is  generally related to applications, which divide into four categories: (1) inspection,  (2) part identiﬁ  cation, (3) visual guidance and control, and (4) safety monitoring.  

Inspection  is the most important category, accounting for about  $90\%$  of all in- dustrial applications. The applications are in mass production, where the time to  program and install the system can be divided by many thousands of units. Typical  inspection tasks include: (1)  dimensional measurement or gaging , which involves  measuring or gaging certain dimensions of parts or products moving along a con- veyor; (2)  veriﬁ  cation functions , which include verifying presence of components  in an assembled product, presence of a hole in a work part, and similar tasks; and  (3)  identiﬁ  cation of ﬂ  aws and defects , such as identifying ﬂ  aws in a printed label  in the form of mislocation, poorly printed text, numbering, or graphics on the label.  

Part identiﬁ  cation  applications include counting different parts ﬂ  owing past on  a conveyor, part sorting, and character recognition.  Visual guidance and control involves a vision system interfaced with a robot or similar machine to control the  movement of the machine. Examples include seam tracking in continuous arc weld- ing, part positioning, part reorientation, and picking parts from a bin. In  safety moni- toring  applications, the vision system monitors the production operation to detect  irregularities that might indicate a hazardous condition to equipment or humans.  

# 40.6.4  OTHER NONCONTACT INSPECTION TECHNIQUES  

In addition to optical inspection methods, there are various nonoptical techniques  used in inspection. These include sensor techniques based on electrical ﬁ  elds, radia- tion, and ultrasonics.  

Under certain conditions,  electrical ﬁ  elds  created by an electrical probe can be  used for inspection. The ﬁ  elds include reluctance, capacitance, and inductance; they  are affected by an object in the vicinity of the probe. In a typical application, the work  part is positioned in a ﬁ  xed relationship to the probe. By measuring the effect of the  object on the electrical ﬁ  eld, an indirect measurement of certain part characteristics  can be made, such as dimensional features, thickness of sheet material, and ﬂ  aws  (cracks and voids below the surface) in the material.  

Radiation techniques  use X-ray radiation to inspect metals and weldments. The  amount of radiation absorbed by the metal object indicates thickness and presence of  ﬂ  aws in the part or welded section. For example, X-ray inspection is used to measure  thickness of sheet metal in rolling (Section 18.1). Data from the inspection is used to  adjust the gap between rolls in the rolling mill.  

Ultrasonic techniques  use high-frequency sound  $\left(>20{,}000\:\mathrm{Hz}\right)$  to perform various  inspection tasks. One of the techniques analyses the ultrasonic waves emitted by a  probe and reﬂ  ected off the object. During the setup for the inspection procedure, an  ideal test part is positioned in front of the probe to obtain a reﬂ  ected sound pattern.  This sound pattern is used as the standard against which production parts are sub- sequently compared. If the reﬂ  ected pattern from a given part matches the standard,  the part is accepted. If a match is not obtained, the part is rejected.  

# References  

[1] DeFeo, J. A., Gryna, F. M., and Chua, R. C. H.  Juran’s Quality Planning and Analysis for  Enterprise Quality , 5th ed. McGraw-Hill,  New York, 2006.

  [2] Evans, J. R., and Lindsay, W. M.  The Management  and Control of Quality , 6th ed. Thomson/South- Western College Publishing Company, Mason,  Ohio, 2005.

  [3] Groover, M. P .  Automation, Production Sys- tems, and Computer Integrated Manufactur- ing , 3rd ed. Prentice Hall, Upper Saddle River,  New Jersey, 2008.

  [4] Juran, J. M., and Gryna, F. M.  Quality Planning  and Analysis , 3rd ed. McGraw-Hill, New York,  1993.

  [5] Lochner, R. H., and Matar, J. E.  Designing for  Quality . ASQC Quality Press, Milwaukee,  Wisconsin, 1990.

  [6] Montgomery, D. C.  Introduction to Statistical  Quality Control , 6th ed. John Wiley & Sons,  Hoboken, New Jersey, 2008.  

[7] Pyzdek, T., and Keller, P .  Quality Engineering  Handbook . 2nd ed. CRC Taylor & Francis, Boca  Raton, Florida, 2003.

  [8] Schaffer, G. H. “Taking the Measure of CMMs.”  Special Report 749,  American Machinist ,  October 1982, pp. 145–160.

  [9] Schaffer, G. H. “Machine Vision: A Sense for  CIM.” Special Report 767,  American Machinist ,  June 1984, pp. 101–120.

 [10] Taguchi, G., Elsayed, E. A., and Hsiang, T. C.  Quality Engineering in Production Systems .  McGraw-Hill, New York, 1989.

[11] Wick, C., and Veilleux, R. F.  Tool and Manu- facturing Engineers Handbook , 4th ed. Vol.  IV,  Quality Control and Assembly . Society of  Manufac  turing Engineers, Dearborn, Michigan,  1987.  