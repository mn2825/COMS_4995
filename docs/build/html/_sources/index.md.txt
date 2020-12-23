# Welcome to Community Health's Documentation

```eval_rst
.. toctree::
   :maxdepth: 4
   :caption: Contents:
   
   modules
```

## Kernelized K-Means Details

```eval_rst

--------------------
Dataset Information
--------------------

Below are the columns found in the dataset, and the questions they correspond to. For further information, please visit the `CHS 2017 Codebook <https://www1.nyc.gov/assets/doh/downloads/pdf/episrv/chs2017-codebook.pdf>`_. This info is provided by the previous link.

**Insurance**

:insuredgateway17: `Do you have any kind of health insurance coverage, including private health insurance or government plans such as Medicare or Medicaid?`
:insure17: `What type of health insurance do you use to pay for your doctor or hospital bills? Is it insurance through...`
:insured: `Any type of health insurance?`
:insure5: `Type of health insurance coverage`
:pcp17: `Do you have one person or more than one person you think of as your personal doctor or health care provider?`
:didntgetcare17: `Was there a time in the past 12 months when you needed medical care but did NOT get it? Medical care includes doctor’s visits, tests, procedures, prescription medication and hospitalizations.`
**Discrimination**

:discriminationtreatment: `Now, thinking of your experiences trying to get health care in the past 12 months, have you felt you were hassled, made to feel inferior, or discriminated against for any reason?`
:discrimreasonracenew: `Felt any discrimination because of race /ethnicity, or skin color while trying to get health care treatment (in the past 12 months)`
:toldhighbp17: `Have you ever been told by a doctor, nurse or other health professional that you have hypertension, also called high blood pressure?`
:toldprescription17: `Have you ever been told by a doctor, nurse or other health professional that you need to take medicine for your high blood pressure?`
:takingmeds17: `Are you currently taking medication for your high blood pressure? AMONG THOSE TOLD HBP AND TOLD TO TAKE MEDS`
:checkedbp: `During the past 30 days, have you checked your blood pressure at home or another place in your community like a pharmacy?`
:diabetes17: `Have you ever been told by a doctor, nurse or other health professional that you have diabetes?`

**Asthma**

:imputed_everasthma: `Have you ever been told by a doctor, nurse or other health professional that you had asthma?`
:imputed_currentasthma17: `In the last 12 months, have you had an episode of asthma or an asthma attack? (Asked of those ever told asthma)`

**Mental Health**

:mood63: `Over the last 2 weeks, how often have you been bothered by: little interest or pleasure in doing things?`
:mood64: `Over the last 2 weeks, how often have you been bothered by: feeling down, depressed or hopeless?`
:mood54: `Over the last 2 weeks, how often have you been bothered by: trouble falling or staying asleep, or sleeping too much?`
:mood55: `Over the last 2 weeks, how often have you been bothered by: feeling tired or having little energy?`
:mood56: `Over the last 2 weeks, how often have you been bothered by: poor appetite or overeating?`
:mood57: `Over the last 2 weeks, how often have you been bothered by: feeling bad about yourself – or that you are a failure or have let yourself or your family down?`
:mood58: `Over the last 2 weeks, how often have you been bothered by: trouble concentrating on things, such as reading the newspaper or watching TV?`
:mood59: `Over the last 2 weeks, how often have you been bothered by: moving or speaking so slowly that other people could have noticed? Or the opposite – being so fidgety or restless that you have been moving around a lot more than usual?`
:phq8score: `Patient Health Questionnaire depression scale – based on last 2 weeks`
:currdepress: `Current depression (last 2 weeks)`
:mood61: `In the past 12 months, have you taken a prescription medication for a mental health problem? Among those with current depression.`
:mood62: `In the past 12 months, have you received any counseling for a mental health problem? Among those with current depression.`
:mhtreat17: `Received counseling or prescription medication for a mental health problem in last 12 months. Among adults with current depression.`
:mood11: `Was there a time in the past 12 months when you needed treatment for a mental health problem but did not get it?`

**Nutrition**

:nutrition46: `About how many cups of fruit did you eat yesterday? One cup of fruit would equal one large orange, 8 large strawberries, or 1 medium pear.`
:nutrition47: `About how many cups of vegetables did you eat yesterday? One cup of vegetables would equal 12 baby carrots, 1 large raw tomato, or 1 large ear of corn.`
:fruitveg17: `Total servings of fruit and/or vegetables eaten yesterday did you eat yesterday?`
:nsodaperday17: `How often do you drink sugar sweetened soda? Do not include diet soda or seltzer. Standardized to per day (continuous)`
:avgsodaperday17: `Average number of sodas per day`
:twoplussoda: `Drink two or more sodas per day`
:nsugardrinkperday17: `How often do you drink other sweetened drinks like sweetened iced tea, sports drinks, fruit punch or other fruit-flavored drinks? Do not include diet soda, sugar free drinks, or 100% juice. Standardized to per day (continuous):
:avgsugarperday17: `Average number of other sugar-sweetened beverages per day`
:nsodasugarperday17: `Number of soda and other sugar sweetened beverages consumed. Standardized to per day (continuous)`
:avgsodasugarperday17: `Average number of sodas plus sweetened drinks per day (categorical)`
:ssb: `Consumes one or more sugar sweetened beverages (soda + other sweetened drinks) on average per day`
:drinkwater: `How many glasses of plain water did you drink yesterday? Plain water includes tap water, bottled plain water, plain seltzer water, and water from a drinking fountain or water cooler?`

**Food Insecurity**

:imputed_ foodinsecure: `In last the last six months, which of the following best describes the food eaten in your household – 1) you had enough of the kinds of food you wanted to eat, 2) you had enough but not always the kinds of food you wanted to eat, 3) sometimes there was not enough to eat, or 4) often there was not enough to eat.`

**Physical Activity**

:exercise17: ``During the past 30 days, other than your regular job, did you participate in any physical activities or exercises such as running, calisthenics, golf, gardening, or walking for exercise?`
:cyclingfreq: `In the past 12 months, how often have you ridden a bicycle in one of the five boroughs of New York City? Would you say once a week or more, several times a month, at least once a month, a few times a year, or never?`
:cycling17: `In the past 12 months, how often have you ridden a bicycle in one of the five boroughs of New York City? Would you say once a week or more, several times a month, at least once a month, a few times a year, or never?`
:PA083Rq1: `Meets national physical activity guidelines – 150 minutes of moderate or equivalent exercise per week- 3 levels. Asked in Version 1 only`

**Tobacco and Second Hand Smoking**

:smoker: `Have you smoked at least 100 cigarettes in your entire life? Do you now smoke cigarettes: everyday, some days, or not at all?`
:everyday: `Smoke every day vs some days`
:numberperdaya: `# cigs smoked/day every & someday smokers, continuous (imputed for missing & adjusted for days smoked)`
:cpd17a: `# cigs smoked/day every & someday smokers, categorical (imputed for missing & adjusted for days smoked)`
:everydaycpda: `# cigs smoked/day among every day smokers ONLY (imputed for missing)`
:heavysmoker17a: `Heavy smoker(>10 cig/day)(imputed for missing cigs & adjusted for days smoked)`
:smokecat: `Type of smoker`
:smoke5a: `About how long has it been since you last smoked cigarettes regularly? (continuous, in months)`
:smoke5: `About how long has it been since you last smoked cigarettes regularly? (categories)`
:sourcelastcig: `Was the last cigarette you smoked from a carton, a pack, a single or loosie, bummed, or did you roll your own?`
:cost20cigarettes: `Cost of 20 cigarettes (pack)`
:cigpurchase17: `Where did you buy the last cigarette you smoked? Was it in your neighborhood, in another part of New York City, or outside of New York City?`
:advisequitsmoke: `During the last 12 months has a doctor, nurse or other health professional advised you to quit smoking?`
:smokeecig12m: `In the past 12 months, have you tried an electronic cigarette, also known as an e-cigarette?`
:smokeecig30days: `In the past 30 days, did you smoke an e-cigarette every day, some days, or not at all?`
:ecighelpquit: `In the past 12 months, have you used an electronic cigarette to help you either cut back or quit smoking regular cigarettes?`
:smokehookah12m: `In the past 12 months, have you smoked a hookah, also called a water pipe?`
:smellcigsmoke: `How often do you smell cigarette smoke in your home that comes from another home or apartment or from outside?`

**Demographics**

:agegroup: `What is your age?`
:age18_64: `See above`
:age21up: `See above`
:age25up: `See above`
:age40new: `See above`	
:age45up: `See above`
:age50up: `See above`
:sex: `On your original birth certificate, was your sex assigned as male or female?`
:newgenderid: `How do you describe yourself? Combines sex at birth and gender identity questions`
:newrace: `Are you Hispanic or Latino? Some people, aside from being Hispanic, also consider themselves to be a member of a racial group. Which one or more of the following would you say is your race?`
:demog55: `Please tell me which group best represents your Hispanic or Latino origin or ancestry`
:demog135r: `Please tell me which group best represents your Asian heritage or ancestry`
:asianancestry: `Please tell me which group best represents your Asian heritage or ancestry`
:bthregion17: `Where were you born?`
:countrybirth17: `See bthregion17`
:bthregion2: `Where were you born?`
:usborn: `Where were you born? Please tell me the country`
:maritalstatus17: `Are you: Married, Divorced, Widowed, Separated, Never married, OR A member of an unmarried couple living together?`
:sexualid17: `Now I'll read a list of terms people sometimes use to describe themselves –– gay or lesbian; straight, that is not gay; bisexual; something else As I read the list again, please stop me when I get to the term that best describes how you think of yourself: Do you not understand the words, are you not sure yet, or do you mean something else? What do you mean by something else?`
:education: `What is the highest grade or year of school you completed?`
:child: `Presence of children in household`
:numadults2: `Total adults in household`
:hhsize: `Total household adults plus children(continuous)`
:employment17: `Are you currently: Employed for wages or salary, Self-employed, unemployed for 1 year or more, unemployed for less than 1 year, A Homemaker, A Student, Retired, Unable to work?`
:emp3: `Employment status-three categories`
:imputedpovertygroup: `Household annual income from all sources; imputed for those with missing data for povertygroup`
:imputedpov200: `Household annual income from all sources <200% FPL; imputed for those with missing data for pov200`
:imputedpovgroup3: `3-category household annual income from all sources`
:bmi: `About how tall are you without shoes? About how much do you weigh without shoes?`
:weight17in4: `See bmi`
:weight17in5: `See bmi`
:weightall: `See bmi`

**Neighborhoods**

:uhf34: `34 United Hospital Fund neighborhoods – few neighborhoods are combined due to the survey design categorized 1 to 34`
:borough: `Borough of residence based on uhf assignment`
:dphonew06: `District Public Health Offices in New York City`
:imputedneighpovgroup41216: `Neighborhood poverty; percent of zip code population living below 100% FPL per American Community Survey, 2012-2016`
:fluvaccineshot: `During the past 12 months, have you had a flu shot in your arm or a flu vaccine that was sprayed in your nose?`
:travelq1: `In the past 12 months, have you traveled to another country or a U.S. territory, such as Puerto Rico or U.S. Virgin Islands?`
:wheretravelq1: `To waht country or territory did you travel?`
:visittravelq1: `Was your MAIN reason for traveling to visit friends or relatives?`
:reasontravel3q1: `What was the main reason you traveled?`

**Cancer Screening**

:evercolon17: `Colonoscopy is an exam in which a tube is inserted in the rectum to view the bowel for signs of cancer or other health problems. Have you ever had a colonoscopy?`
:colonoscopy10yr17: `When was your most recent colonoscopy performed?`
:evercolon1745: `See evercolon16`
:colonoscopy10yr45: `See colonoscopy10yr16`
:imputedpaptestall 17: `A Pap smear is a test for cancer of the cervix. How long ago was your last pap smear?`
:imputedtimepaptest 17: `How long has it been since your last pap smear?`
:hiv12months17: `Have you had an HIV test in the last 12 months?`
:everhivtest17: `Have you ever had an HIV test?`

**Sexual Behavior**

:sexbehavactive17: `Sexual behavior, past 12 months`
:sexuallyactive17: `Sexually active in past 12 months`
:imputedsexpartner: `Number of male and female sex partners in the past 12 months`
:wsw: `Women who have sex with women, past 12 months`
:wswexclusive: `Women who have sex with women, exclusively in past 12 months`
:msm: `Men who have sex with men, past 12 months`
:msmexclusive: `Men who have sex with men, exclusively in past 12 months`
:condom17: `The last time you had sex, did you use a condom? Among all sexually active`
:condomusetrend: `The last time you had sex, did you use a condom? Among sexually active 18- 64 year olds who had sex with 1 or more partners of opposite sex in past 12 months`
:analsex: `In the past 12 months, have you had anal sex?`
:analsexcondomuse17: `In the past 12 months, when you have had anal sex have you or your partner used a condom?`
:otherbcnotcondom: `The last time you had vaginal sex, did you or your partner use any other method of birth control besides condoms to prevent a pregnancy?`
:bthcntrltype17: `Type of birth control used at last vaginal sex (EXCLUDES condoms)`
:bthcontrollastsex17: `Any birth control at last sex (includes condom use)`
:everheardofprep: `Have you heard of PrEP (Pre-Exposure Prophylaxis)?`
:everusedprep17: `Have you ever used PrEP to prevent yourself from becoming infected with HIV?`

**Alcohol**

:drinker: `Consumed at least one alcohol drink in past 30 days`
:daysalc30: `A drink of alcohol is 1 can or bottle of beer, 1 glass of wine, 1 can or bottle of wine cooler, 1 cocktail, or 1 shot of liquor. During the past 30 days, how many days per week or per month did you have at least 1 drink of any alcoholic beverage? STANDARDIZED TO PER MONTH`
:averagedrink17: `On the days when you drank, about how many drinks did you drink on average? Standardized to average number of drinks per day in last 30 days)`
:heavydrink17: `Heavy drinking defined as men having >2 drinks per day or women having >1 drink per day`
:bingenew: `During the past 30 days had [men: 5 or more drinks on one occasion ] [women: 4 or more drinks on one occasion]`

**Housing, Environment, and Noise**

:homeownership17: `Is this home or apartment owned or rented?`
:lowinchousing17: `Are you: a public housing resident, receive rental assistance such as Section 8, rent- controlled or rent- stabilized, or neither?`
:howlong17new: `How long have you lived in your home or apartment?`
:whereliving17: `Where were you living 2 years ago?`
:imputedhelpneighbors17cat: `People in your neighborhood are willing to help their neighbors.`
:imputedneighborg: `Suppose that because of budget cuts the fire station closest to your home was going to be closed down by the city. How likely is it that people in your neighborhood would organize to try and do something to keep the fire station open?`
:imputedadultslookup: `There are adults in your neighborhood that children can look up to`

**Justice Involvement**

:timeprison: `Have you ever in your life, spent any amount of time in a juvenile or adult correctional facility, jail, prison, or detention center OR have you ever been under probation or parole supervision?`
:familyprison: `Has an immediate family member such as a spouse or partner, child, sibling, or parent ever spent any amount of time in a juvenile or adult correctional facility, jail, prison, or detention center OR ever been under probation or parole supervision?`

**Administrative**

:qxvers: `identifies which VERSION of the questionnaire the respondent received`

