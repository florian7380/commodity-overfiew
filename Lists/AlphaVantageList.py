# DAX 40, Euro Stoxx 50, FTSE 100, CAC 40, IBEX 35 und OMX Stockholm 30

AlphaVantageList = [
    "COAL",      # Kohle
    "ZN",       # Zink
    "KC",       # Kaffee
    "CO",       # Kobalt
    "GA",       # Gallium
    "TA",       # Tantal
    "SC",       # Scandium
    "TI",       # Titan
    "MN",       # Mangan
    "LI",       # Lithium
    "S",        # Weizen
    "SN",       # Zinn
    "ADS.DE",   # Adidas
    "AIR.DE",   # Airbus
    "ALV.DE",   # Allianz
    "BAS.DE",   # BASF
    "BAYN.DE",  # Bayer
    "BMW.DE",   # BMW
    "CBK.DE",   # Commerzbank
    "CON.DE",   # Continental
    "1COV.DE",  # Covestro
    "DHER.DE",  # Delivery Hero
    "DTE.DE",   # Deutsche Telekom
    "DBK.DE",   # Deutsche Bank
    "ENR.DE",   # E.ON
    "FME.DE",   # Fresenius Medical Care
    "FRE.DE",   # Fresenius
    "HEN3.DE",  # Henkel
    "IFX.DE",   # Infineon Technologies
    "LIN.DE",   # Linde
    "MRK.DE",   # Merck
    "MUV2.DE",  # Munich RE
    "RWE.DE",   # RWE
    "SAP.DE",   # SAP
    "SIE.DE",   # Siemens
    "VNA.DE",   # Vonovia
    "VOW3.DE",  # Volkswagen (Vorzugsaktien)
    "MTX.DE",   # MTU Aero Engines
    "SY1.DE",   # Symrise
    "ZAL.DE",   # Zalando
    "PUM.DE",   # Puma
    "HFG.DE",   # HelloFresh
    "BNR.DE",   # Brenntag
    "BOSS.DE",  # Hugo Boss
    "EVT.DE",   # Evotec
    "SRT3.DE",  # Sartorius
    "PAH3.DE",  # Porsche Automobil Holding
    "SHL.DE",   # Siemens Healthineers
    "HEI.DE",   # Heidelberg Materials
    "MBG.DE",    # Mercedes-Benz Group
    "SONY",     # Sony Group Corporation (Japan) - Electronics/Entertainment, NYSE
    "SKM",      # SK Telecom (South Korea) - Telecommunications, NYSE
    "SSNLF", # Samsung Electronics (South Korea) - Electronics/Semiconductors, Korea Exchange
    "RLNIY",  # Reliance Industries (India) - Energy/Retail/Telecom, National Stock Exchange of India
    "CHL",  # China Mobile (China) - Telecommunications, Hong Kong Stock Exchange
    "PNGAY",  # Ping An Insurance (China) - Financial Services, Hong Kong Stock Exchange
    "IDCBY",  # ICBC (Industrial and Commercial Bank of China) (China) - Banking, Hong Kong Stock Exchange
    "CICHY",  # China Construction Bank (China) - Banking, Hong Kong Stock Exchange
    "AAGIY",  # AIA Group (Hong Kong) - Insurance, Hong Kong Stock Exchange
    "SFTBY",    # SoftBank Group (Japan) - Investment/Telecom, OTC Markets
    "MSBHF",   # Mitsubishi Corporation (Japan) - Trading/Investment, Tokyo Stock Exchange
    "CIHKY",  # China Merchants Bank (China) - Banking, Hong Kong Stock Exchange
    "600519.SS", # Kweichow Moutai (China) - Alcoholic Beverages, Shanghai Stock Exchange
    "NTTYY",    # Nippon Telegraph and Telephone Corporation (NTT) (Japan) - Telecommunications, OTC Markets
    "LGCLF", # LG Chem (South Korea) - Chemicals/Batteries, Korea Exchange
    "CHPXF",  # China Pacific Insurance (Group) Co. (China) - Insurance, Hong Kong Stock Exchange
    "BYDDF",    # BYD Company (China) - Electric Vehicles/Batteries, OTC Markets
    "HTHIY",    # Hitachi Ltd. (Japan) - Electronics/Engineering, OTC Markets
    "600000.SS", # Shanghai Pudong Development Bank (China) - Banking, Shanghai Stock Exchange
    "HYMTF",    # Hyundai Motor Company (South Korea) - Automotive, OTC Markets
    "SIUIF",  # SMIC (Semiconductor Manufacturing International Corporation) (China) - Semiconductors, Hong Kong Stock Exchange
    "ABI.BR",   # Anheuser-Busch InBev
    "AD.AS",    # Ahold Delhaize
    "AI.PA",    # Air Liquide
    "ASML.AS",  # ASML Holding
    "BN.PA",    # Danone
    "BNP.PA",   # BNP Paribas
    "CS.PA",    # AXA
    "DAI.DE",   # Mercedes-Benz Group (Daimler)
    "DB1.DE",   # Deutsche Börse
    "DG.PA",    # Vinci
    "ENGI.PA",  # Engie
    "INGA.AS",  # ING Groep
    "KER.PA",   # Kering
    "MC.PA",    # LVMH Moet Hennessy Louis Vuitton
    "NG.L",     # National Grid
    "OR.PA",    # L'Oreal
    "PHIA.AS",  # Philips
    "RMS.PA",   # Hermes International
    "SAF.PA",   # Safran
    "SAN.PA",   # Sanofi
    "SU.PA",    # Schneider Electric
    "UNA.AS",   # Unilever
    "VIV.PA",   # Vivendi
    "III.L",    # 3i Group
    "ADM.L",    # Admiral Group
    "AAL.L",    # Anglo American
    "ANTO.L",   # Antofagasta
    "ABF.L",    # Associated British Foods
    "AHT.L",    # Ashtead Group
    "AZN.L",    # AstraZeneca
    "AUTO.L",   # Auto Trader Group
    "AV.L",     # Aviva
    "BA.L",     # BAE Systems
    "BARC.L",   # Barclays
    "BATS.L",   # British American Tobacco
    "BP.L",     # BP
    "BT-A.L",   # BT Group
    "CCH.L",    # Coca-Cola HBC
    "CCL.L",    # Carnival
    "CRH.L",    # CRH
    "CNA.L",    # Centrica
    "CPG.L",    # Compass Group
    "DCC.L",    # DCC
    "DGE.L",    # Diageo
    "EXPN.L",   # Experian
    "FERG.L",   # Ferguson
    "FLTR.L",   # Flutter Entertainment
    "FRES.L",   # Fresnillo
    "GLEN.L",   # Glencore
    "GSK.L",    # GSK (GlaxoSmithKline)
    "HLMA.L",   # Halma
    "HSBA.L",   # HSBC Holdings
    "IMB.L",    # Imperial Brands
    "INF.L",    # Informa
    "IHG.L",    # InterContinental Hotels Group
    "ITRK.L",   # Intertek Group
    "JD.L",     # JD Sports Fashion
    "JMAT.L",   # Johnson Matthey
    "KGF.L",    # Kingfisher
    "LAND.L",   # Land Securities Group
    "LGEN.L",   # Legal & General Group
    "LLOY.L",   # Lloyds Banking Group
    "LSEG.L",   # London Stock Exchange Group
    "MNG.L",    # M&G
    "MRO.L",    # Melrose Industries
    "MNDI.L",   # Mondi
    "NG.L",     # National Grid
    "NXT.L",    # Next
    "PHNX.L",   # Phoenix Group
    "PSON.L",   # Pearson
    "PSN.L",    # Persimmon
    "PRU.L",    # Prudential
    "RKT.L",    # Reckitt Benckiser
    "REL.L",    # Relx
    "RMV.L",    # Rightmove
    "RR.L",     # Rolls-Royce Holdings
    "SGE.L",    # Sage Group
    "SBRY.L",   # Sainsbury (J)
    "SDR.L",    # Schroders
    "SGRO.L",   # Segro
    "SVT.L",    # Severn Trent
    "SHEL.L",   # Shell
    "SMT.L",    # Scottish Mortgage Investment Trust
    "SSE.L",    # SSE
    "STAN.L",   # Standard Chartered
    "STJ.L",    # St. James's Place
    "TSCO.L",   # Tesco
    "ULVR.L",   # Unilever
    "UU.L",     # United Utilities Group
    "VOD.L",    # Vodafone
    "WTB.L",    # Whitbread
    "WPP.L",     # WPP
    "AC.PA",    # Accor
    "ALO.PA",   # Alstom
    "MT.PA",    # ArcelorMittal
    "ATO.PA",   # Atos
    "CAP.PA",   # Capgemini
    "CA.PA",    # Carrefour
    "DSY.PA",   # Dassault Systèmes
    "EDF.PA",   # EDF
    "EN.PA",    # Bouygues
    "EL.PA",    # EssilorLuxottica
    "ML.PA",    # Michelin
    "ORA.PA",   # Orange
    "PUB.PA",   # Publicis Groupe
    "RI.PA",    # Pernod Ricard
    "SGO.PA",   # Saint-Gobain
    "SW.PA",    # Sodexo
    "STM.PA",   # STMicroelectronics
    "UG.PA",    # Peugeot (Stellantis)
    "WLN.PA",   # Worldline
    "VIE.PA",   # Veolia Environnement
    "RNO.PA",   # Renault
    "HO.PA",    # Thales
    "FP.PA",     # TotalEnergies
    "SMP",      # Smartgroup Corporation
    "WBC",    # Westpac Banking Corporation
    "COL",    # Coles Group
    "SCG",    # Scentre Group
    "ORG",    # Origin Energy
    "ALD",    # Ampol Limited
    "BWP",    # BWP Trust
    "GPT",    # GPT Group
    "CHC",    # Charter Hall Group
    "STO",    # Santos Limited
    ]