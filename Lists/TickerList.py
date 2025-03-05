TickerList = [
    # StockData
    "AU",       # Gold
    "AG",       # Silber
    "PT",       # Platin
    "PD",       # Palladium
    "NI",       # Nickel
    "CL",       # Rohöl (WTI)
    "NG",       # Erdgas
    "ZS",       # Sojabohnen
    "SB",       # Zucker
    "CC",       # Kakao
    "COAL",     # Kohle
    "PB",       # Blei
    "LC",       # Lebendrind
    "RH",       # Rhodium
    "IR",       # Eisen
    "LI",       # Lithium
    "BIT",      # Bitcoin
    "S",        # Weizen
    "MO",       # Molybdän
    "SN",       # Zinn
    "MG",       # Magnesium
    "V",        # Vanadium
    "CR",       # Chrom
    "BABA",     # Alibaba Group (China) - E-commerce/Technology, NYSE
    "TSM",      # Taiwan Semiconductor Manufacturing Company (TSMC) (Taiwan) - Semiconductors, NYSE
    "BIDU",     # Baidu (China) - Technology/Internet Services, NASDAQ
    "JD",       # JD.com (China) - E-commerce, NASDAQ
    "HDB",      # HDFC Bank (India) - Banking, NYSE
    "TM",       # Toyota Motor Corporation (Japan) - Automotive, NYSE
    "MUFG",     # Mitsubishi UFJ Financial Group (Japan) - Financial Services, NYSE
    "SONY",     # Sony Group Corporation (Japan) - Electronics/Entertainment, NYSE
    "INFY",     # Infosys (India) - IT Services, NYSE
    "SKM",      # SK Telecom (South Korea) - Telecommunications, NYSE
    "SHG",      # Shinhan Financial Group (South Korea) - Financial Services, NYSE
    "SNP",      # China Petroleum & Chemical Corporation (Sinopec) (China) - Oil & Gas, NYSE
    "SMFG",     # Sumitomo Mitsui Financial Group (Japan) - Banking, NYSE
    "PDD",      # Pinduoduo (China) - E-commerce, NASDAQ
    "KB",       # KB Financial Group (South Korea) - Banking, NYSE
    "PKX",      # POSCO Holdings (South Korea) - Steel Manufacturing, NYSE
    "BHP",      # BHP Group
    "RIO",      # Rio Tinto Group
    "CSL",      # CSL Limited
    "WES",      # Wesfarmers
    "WDS",      # Woodside Energy Group
    "TLS",      # Telstra Corporation
    "WOW",      # Woolworths Group
    "SUN",      # Suncorp Group
    "ALL",      # Aristocrat Leisure
    "AMP",      # AMP Limited
    "JHX",      # James Hardie Industries
    "APA",      # APA Group
    "BPT",      # Beach Energy
    "IAG",      # Insurance Australia Group
    "MGR",      # Mirvac Group
    "SMP",      # Smartgroup Corporation
    "EVN",       # Evolution Mining
    # AlphaVantage
    "ZN",       # Zink
    "KC",       # Kaffee
    "CO",       # Kobalt
    "GA",       # Gallium
    "TA",       # Tantal
    "SC",       # Scandium
    "TI",       # Titan
    "MN",       # Mangan
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
    "WBC",    # Westpac Banking Corporation
    "COL",    # Coles Group
    "SCG",    # Scentre Group
    "ORG",    # Origin Energy
    "ALD",    # Ampol Limited
    "BWP",    # BWP Trust
    "GPT",    # GPT Group
    "CHC",    # Charter Hall Group
    "STO",    # Santos Limited
    
    # Polygon IO
    
    # ~ 100 biggest fonds and ETFs
    "SPY",   # SPDR S&P 500 ETF Trust
    "IVV",   # iShares Core S&P 500 ETF
    "VOO",   # Vanguard S&P 500 ETF
    "QQQ",   # Invesco QQQ Trust
    "VTI",   # Vanguard Total Stock Market ETF
    "AGG",   # iShares Core U.S. Aggregate Bond ETF
    "EFA",   # iShares MSCI EAFE ETF
    "IWM",   # iShares Russell 2000 ETF
    "BND",   # Vanguard Total Bond Market ETF
    "GLD",   # SPDR Gold Trust
    "SLV",   # iShares Silver Trust
    "LQD",   # iShares iBoxx $ Investment Grade Corporate Bond ETF
    "HYG",   # iShares iBoxx $ High Yield Corporate Bond ETF
    "VEU",   # Vanguard FTSE All-World ex-US ETF
    "VWO",   # Vanguard FTSE Emerging Markets ETF
    "EEM",   # iShares MSCI Emerging Markets ETF
    "XLK",   # Technology Select Sector SPDR Fund
    "XLF",   # Financial Select Sector SPDR Fund
    "ARKK",  # ARK Innovation ETF
    "VNQ",   # Vanguard Real Estate ETF
    "XLE",   # Energy Select Sector SPDR Fund
    "XLV",   # Health Care Select Sector SPDR Fund
    "VTV",   # Vanguard Value ETF
    "VO",    # Vanguard Mid-Cap ETF
    "IJH",   # iShares Core S&P Mid-Cap ETF
    "VT",    # Vanguard Total World Stock ETF
    "DIA",   # SPDR Dow Jones Industrial Average ETF Trust
    "TLT",   # iShares 20+ Year Treasury Bond ETF
    "MCHI",  # iShares MSCI China ETF
    "IYR",   # iShares U.S. Real Estate ETF
    "VGT",   # Vanguard Information Technology ETF
    "GDX",   # VanEck Gold Miners ETF
    "XOP",   # SPDR S&P Oil & Gas Exploration & Production ETF
    "XBI",   # SPDR S&P Biotech ETF
    "ITOT",  # iShares Core S&P Total U.S. Stock Market ETF
    "VIG",   # Vanguard Dividend Appreciation ETF
    "SCHD",  # Schwab U.S. Dividend Equity ETF
    "FDN",   # First Trust Dow Jones Internet Index Fund
    "VYM",   # Vanguard High Dividend Yield ETF
    "XLU",   # Utilities Select Sector SPDR Fund
    "USMV",  # iShares MSCI USA Min Vol Factor ETF
    "MTUM",  # iShares MSCI USA Momentum Factor ETF
    "EWT",   # iShares MSCI Taiwan ETF
    "FXI",   # iShares China Large-Cap ETF
    "TIP",   # iShares TIPS Bond ETF
    "VCR",   # Vanguard Consumer Discretionary ETF
    "SPAB",  # SPDR Portfolio Aggregate Bond ETF
    "VDE",   # Vanguard Energy ETF
    "GDXJ",  # VanEck Junior Gold Miners ETF
    "SCHF",  # Schwab International Equity ETF
    "EMB",   # iShares J.P. Morgan USD Emerging Markets Bond ETF
    "MUB",   # iShares National Muni Bond ETF
    "BNDX",  # Vanguard Total International Bond ETF
    "JNK",   # SPDR Bloomberg High Yield Bond ETF
    "RSP",   # Invesco S&P 500 Equal Weight ETF
    "VTIP",  # Vanguard Short-Term Inflation-Protected Securities ETF
    "ACWI",  # iShares MSCI ACWI ETF
    "PFF",   # iShares Preferred and Income Securities ETF
    "XLRE",  # Real Estate Select Sector SPDR Fund
    "XLY",   # Consumer Discretionary Select Sector SPDR Fund
    "SPYG",  # SPDR Portfolio S&P 500 Growth ETF
    "VHT",   # Vanguard Health Care ETF
    "XLI",   # Industrial Select Sector SPDR Fund
    "IBB",   # iShares Biotechnology ETF
    "EWZ",   # iShares MSCI Brazil ETF
    "IJR",   # iShares Core S&P Small-Cap ETF
    "REM",   # iShares Mortgage Real Estate ETF
    "SCHX",  # Schwab U.S. Large-Cap ETF
    "VBK",   # Vanguard Small-Cap Growth ETF
    "XLC",   # Communication Services Select Sector SPDR Fund
    "NOBL",  # ProShares S&P 500 Dividend Aristocrats ETF
    "DGRO",  # iShares Core Dividend Growth ETF
    "SPHD",  # Invesco S&P 500 High Dividend Low Volatility ETF
    "QYLD",  # Global X NASDAQ 100 Covered Call ETF
    "VOE",   # Vanguard Mid-Cap Value ETF
    "CWB",   # SPDR Bloomberg Convertible Securities ETF
    "VBR",   # Vanguard Small-Cap Value ETF
    "BIV",   # Vanguard Intermediate-Term Bond ETF
    "VB",    # Vanguard Small-Cap ETF
    "SCHA",  # Schwab U.S. Small-Cap ETF
    "VFH",   # Vanguard Financials ETF
    "IXUS",  # iShares Core MSCI Total International Stock ETF
    "IGV",   # iShares Expanded Tech-Software Sector ETF
    "IUSV",  # iShares Core S&P U.S. Value ETF
    "MBB",   # iShares MBS ETF
    "PSQ",   # ProShares Short QQQ
    "TQQQ",  # ProShares UltraPro QQQ
    "AMLP",  # Alerian MLP ETF
    "ESGU",  # iShares ESG Aware MSCI USA ETF
    "SPTL",  # SPDR Portfolio Long Term Treasury ETF
    "FREL",  # Fidelity MSCI Real Estate Index ETF
    "BKLN",  # Invesco Senior Loan ETF
    "SPLG",  # SPDR Portfolio S&P 500 ETF
    "VLUE",  # iShares MSCI USA Value Factor ETF
    "IVW",   # iShares S&P 500 Growth ETF
    "VPU",   # Vanguard Utilities ETF
    "XLP",   # Consumer Staples Select Sector SPDR Fund
    "IDV",   # iShares International Select Dividend ETF
    "VXF",   # Vanguard Extended Market ETF
    "FTEC",  # Fidelity MSCI Information Technology Index ETF
    "USO",   # United States Oil Fund LP
    "PHYS",  # Sprott Physical Gold Trust
    
    # Shares
    "AAPL", # Apple Inc.
    "NVDA", # NVIDIA CORP
    "MSFT", # MICROSOFT CORP
    "GOOGL", # Alphabet Inc.
    "AMZN", # AMAZON COM INC
    "META", # Meta Platforms, Inc.
    "TSM", # TAIWAN SEMICONDUCTOR MANUFACTURING CO LTD
    "TSLA", # Tesla, Inc.
    "LLY", # ELI LILLY & Co
    "AVGO", # Broadcom Inc.
    "WMT", # Walmart Inc.
    "JPM", # JPMORGAN CHASE & CO
    "V", # VISA INC.
    "UNH", # UNITEDHEALTH GROUP INC
    "SPY", # SPDR S&P 500 ETF TRUST
    "XOM", # EXXON MOBIL CORP
    "NVO", # NOVO NORDISK A S
    "ORCL", # ORACLE CORP
    "MA", # Mastercard Inc
    "PG", # PROCTER & GAMBLE Co
    "HD", # HOME DEPOT, INC.
    "COST", # COSTCO WHOLESALE CORP /NEW
    "JNJ", # JOHNSON & JOHNSON
    "ABBV", # AbbVie Inc.
    "NFLX", # NETFLIX INC
    "BAC", # BANK OF AMERICA CORP /DE/
    "KO", # COCA COLA CO
    "CRM", # Salesforce, Inc.
    "SAP", # SAP SE
    "ASML", # ASML HOLDING NV
    "CVX", # CHEVRON CORP
    "MRK", # Merck & Co., Inc.
    "TMUS", # T-Mobile US, Inc.
    "BABA", # Alibaba Group Holding Ltd
    "AMD", # ADVANCED MICRO DEVICES INC
    "PEP", # PEPSICO INC
    "TM", # TOYOTA MOTOR CORP/
    "AZN", # ASTRAZENECA PLC
    "WFC", # WELLS FARGO & COMPANY/MN
    "CSCO", # CISCO SYSTEMS, INC.
    "LIN", # LINDE PLC
    "NVS", # NOVARTIS AG
    "ACN", # Accenture plc
    "MCD", # MCDONALDS CORP
    "ADBE", # ADOBE INC.
    "TMO", # THERMO FISHER SCIENTIFIC INC.
    "PM", # Philip Morris International Inc.
    "BX", # Blackstone Inc.
    "SHEL", # Shell plc
    "ABT", # ABBOTT LABORATORIES
    "NOW", # ServiceNow, Inc.
    "IBM", # INTERNATIONAL BUSINESS MACHINES CORP
    "AXP", # AMERICAN EXPRESS CO
    "QQQ", # INVESCO QQQ TRUST, SERIES 1
    "MS", # MORGAN STANLEY
    "GE", # GENERAL ELECTRIC CO
    "TXN", # TEXAS INSTRUMENTS INC
    "CAT", # CATERPILLAR INC
    "QCOM", # QUALCOMM INC/DE
    "ISRG", # INTUITIVE SURGICAL INC
    "DHR", # DANAHER CORP /DE/
    "VZ", # VERIZON COMMUNICATIONS INC
    "DIS", # Walt Disney Co
    "FMX", # MEXICAN ECONOMIC DEVELOPMENT INC
    "AMGN", # AMGEN INC
    "RY", # ROYAL BANK OF CANADA
    "INTU", # INTUIT INC.
    "CMCSA", # COMCAST CORP
    "HSBC", # HSBC HOLDINGS PLC
    "PDD", # PDD Holdings Inc.
    "GS", # GOLDMAN SACHS GROUP INC
    "NEE", # NEXTERA ENERGY INC
    "PFE", # PFIZER INC
    "T", # AT&T INC.
    "RTX", # RTX Corp
    "HDB", # HDFC BANK LTD
    "BKNG", # Booking Holdings Inc.
    "UL", # UNILEVER PLC
    "SPGI", # S&P Global Inc.
    "LOW", # LOWES COMPANIES INC
    "UBER", # Uber Technologies, Inc
    "AMAT", # APPLIED MATERIALS INC /DE
    "BLK", # BlackRock, Inc.
    "PGR", # PROGRESSIVE CORP/OH/
    "TTE", # TotalEnergies SE
    "UNP", # UNION PACIFIC CORP
    "BHP", # BHP Group Ltd
    "SYK", # STRYKER CORP
    "SNY", # Sanofi
    "HON", # HONEYWELL INTERNATIONAL INC
    "ETN", # Eaton Corp plc
    "SCHW", # SCHWAB CHARLES CORP
    "LMT", # LOCKHEED MARTIN CORP
    "TJX", # TJX COMPANIES INC /DE/
    "KKR", # KKR & Co. Inc.
    "COP", # CONOCOPHILLIPS
    "BSX", # BOSTON SCIENTIFIC CORP
    "MUFG", # MITSUBISHI UFJ FINANCIAL GROUP INC
    "VRTX", # VERTEX PHARMACEUTICALS INC / MA
    "C", # CITIGROUP INC
    "ANET", # Arista Networks, Inc.
    "BUD", # Anheuser-Busch InBev SA/NV
    "ADP", # AUTOMATIC DATA PROCESSING INC
    "PANW", # Palo Alto Networks Inc
    "UPS", # UNITED PARCEL SERVICE INC
    "MDT", # Medtronic plc
    "CB", # Chubb Ltd
    "NKE", # NIKE, Inc.
    "FI", # FISERV INC
    "BMY", # BRISTOL MYERS SQUIBB CO
    "DE", # DEERE & CO
    "GILD", # GILEAD SCIENCES, INC.
    "SBUX", # STARBUCKS CORP
    "ADI", # ANALOG DEVICES INC
    "MU", # MICRON TECHNOLOGY INC
    "BA", # BOEING CO
    "MMC", # MARSH & MCLENNAN COMPANIES, INC.
    "IBN", # ICICI BANK LTD
    "RIO", # RIO TINTO PLC
    "PLD", # Prologis, Inc.
    "SONY", # Sony Group Corp
    "MELI", # MERCADOLIBRE INC
    "SO", # SOUTHERN CO
    "AMT", # AMERICAN TOWER CORP /MA/
    "SHOP", # SHOPIFY INC.
    "UBS", # UBS Group AG
    "TD", # TORONTO DOMINION BANK
    "ELV", # Elevance Health, Inc.
    "LRCX", # LAM RESEARCH CORP
    "MO", # ALTRIA GROUP, INC.
    "HCA", # HCA Healthcare, Inc.
    "PLTR", # Palantir Technologies Inc.
    "INTC", # INTEL CORP
    "MDLZ", # Mondelez International, Inc.
    "REGN", # REGENERON PHARMACEUTICALS, INC.
    "SHW", # SHERWIN WILLIAMS CO
    "CI", # Cigna Group
    "ICE", # Intercontinental Exchange, Inc.
    "DUK", # Duke Energy CORP
    "KLAC", # KLA CORP
    "ENB", # ENBRIDGE INC
    "INFY", # Infosys Ltd
    "DELL", # Dell Technologies Inc.
    "RELX", # RELX PLC
    "RACE", # Ferrari N.V.
    "WM", # WASTE MANAGEMENT INC
    "EQIX", # EQUINIX INC
    "SCCO", # SOUTHERN COPPER CORP/
    "WELL", # WELLTOWER INC.
    "ABNB", # Airbnb, Inc.
    "PBR", # PETROBRAS - PETROLEO BRASILEIRO SA
    "CTAS", # CINTAS CORP
    "SMFG", # SUMITOMO MITSUI FINANCIAL GROUP, INC.
    "TT", # Trane Technologies plc
    "MCO", # MOODYS CORP /DE/
    "CEG", # Constellation Energy Corp
    "APO", # Apollo Global Management, Inc.
    "ZTS", # Zoetis Inc.
    "CME", # CME GROUP INC.
    "PH", # PARKER HANNIFIN CORP
    "GD", # GENERAL DYNAMICS CORP
    "APH", # AMPHENOL CORP /DE/
    "BN", # BROOKFIELD Corp /ON/
    "AON", # Aon plc
    "PYPL", # PayPal Holdings, Inc.
    "SNPS", # SYNOPSYS INC
    "ITW", # ILLINOIS TOOL WORKS INC
    "BP", # BP PLC
    "BTI", # British American Tobacco p.l.c.
    "CL", # COLGATE PALMOLIVE CO
    "SPOT", # Spotify Technology S.A.
    "CMG", # CHIPOTLE MEXICAN GRILL INC
    "GSK", # GSK plc
    "CDNS", # CADENCE DESIGN SYSTEMS INC
    "USB", # US BANCORP \DE\
    "MSI", # Motorola Solutions, Inc.
    "PNC", # PNC FINANCIAL SERVICES GROUP, INC.
    "SAN", # Banco Santander, S.A.
    "NOC", # NORTHROP GRUMMAN CORP /DE/
    "TRI", # THOMSON REUTERS CORP /CAN/
    "MAR", # MARRIOTT INTERNATIONAL INC /MD/
    "TDG", # TransDigm Group INC
    "NU", # Nu Holdings Ltd.
    "CRWD", # CrowdStrike Holdings, Inc.
    "CP", # CANADIAN PACIFIC KANSAS CITY LTD/CN
    "CNQ", # CANADIAN NATURAL RESOURCES LTD
    "CVS", # CVS HEALTH Corp
    "DEO", # DIAGEO PLC
    "ECL", # ECOLAB INC.
    "MMM", # 3M CO
    "APD", # Air Products & Chemicals, Inc.
    "TGT", # TARGET CORP
    "EOG", # EOG RESOURCES INC
    "MRVL", # Marvell Technology, Inc.
    "CNI", # CANADIAN NATIONAL RAILWAY CO
    "BDX", # BECTON DICKINSON & CO
    "FDX", # FEDEX CORP
    "ORLY", # O REILLY AUTOMOTIVE INC
    "BMO", # BANK OF MONTREAL /CAN/
    "GLD", # SPDR GOLD TRUST
    "CSX", # CSX CORP
    "MCK", # MCKESSON CORP
    "CARR", # CARRIER GLOBAL Corp
    "CRH", # CRH PUBLIC LTD CO
    "DASH", # DoorDash, Inc.
    "EQNR", # EQUINOR ASA
    "FCX", # FREEPORT-MCMORAN INC
    "IBKR", # Interactive Brokers Group, Inc.
    "WMB", # WILLIAMS COMPANIES, INC.
    "SPG", # SIMON PROPERTY GROUP INC /DE/
    "BNS", # BANK OF NOVA SCOTIA
    "WDAY", # Workday, Inc.
    "COF", # CAPITAL ONE FINANCIAL CORP
    "RSG", # REPUBLIC SERVICES, INC.
    "NGG", # NATIONAL GRID PLC
    "EPD", # ENTERPRISE PRODUCTS PARTNERS L.P.
    "AJG", # Arthur J. Gallagher & Co.
    "JD", # JD.com, Inc.
    "EMR", # EMERSON ELECTRIC CO
    "RDY", # DR REDDYS LABORATORIES LTD
    "ADSK", # Autodesk, Inc.
    "DLR", # DIGITAL REALTY TRUST, INC.
    "FTNT", # Fortinet, Inc.
    "CM", # CANADIAN IMPERIAL BANK OF COMMERCE /CAN/
    "NXPI", # NXP Semiconductors N.V.
    "TTD", # Trade Desk, Inc.
    "AFL", # AFLAC INC
    "PSA", # Public Storage
    "ROP", # ROPER TECHNOLOGIES INC
    "TFC", # TRUIST FINANCIAL CORP
    "HLT", # Hilton Worldwide Holdings Inc.
    "NSC", # NORFOLK SOUTHERN CORP
    "BBVA", # BANCO BILBAO VIZCAYA ARGENTARIA, S.A.
    "OKE", # ONEOK INC /NEW/
    "SLB", # SCHLUMBERGER LIMITED/NV
    "TRV", # TRAVELERS COMPANIES, INC.
    "APP", # AppLovin Corp
    "GM", # General Motors Co
    "ET", # Energy Transfer LP
    "RCL", # ROYAL CARIBBEAN CRUISES LTD
    "ITUB", # Itau Unibanco Holding S.A.
    "MET", # METLIFE INC
    "BK", # Bank of New York Mellon Corp
    "DHI", # HORTON D R INC /DE/
    "GWW", # W.W. GRAINGER, INC.
    "PCAR", # PACCAR INC
    "KMI", # KINDER MORGAN, INC.
    "ING", # ING GROEP NV
    "MFG", # MIZUHO FINANCIAL GROUP INC
    "SE", # Sea Ltd
    "SRE", # SEMPRA
    "PCG", # PG&E Corp
    "URI", # UNITED RENTALS, INC.
    "ARES", # Ares Management Corp
    "AEP", # AMERICAN ELECTRIC POWER CO INC
    "O", # REALTY INCOME CORP
    "MNST", # Monster Beverage Corp
    "NTES", # NetEase, Inc.
    "NEM", # NEWMONT Corp /DE/
    "FANG", # Diamondback Energy, Inc.
    "MFC", # MANULIFE FINANCIAL CORP
    "AZO", # AUTOZONE INC
    "JCI", # Johnson Controls International plc
    "PSX", # Phillips 66
    "PAYX", # PAYCHEX INC
    "D", # DOMINION ENERGY, INC
    "IAU", # ISHARES GOLD TRUST
    "AMP", # AMERIPRISE FINANCIAL INC
    "ALL", # ALLSTATE CORP
    "CPRT", # COPART INC
    "TEAM", # Atlassian Corp
    "MSTR", # MICROSTRATEGY Inc
    "FIS", # Fidelity National Information Services, Inc.
    "AIG", # AMERICAN INTERNATIONAL GROUP, INC.
    "FICO", # FAIR ISAAC CORP
    "MPC", # Marathon Petroleum Corp
    "AMX", # AMERICA MOVIL SAB DE CV/
    "TRP", # TC ENERGY CORP
    "E", # ENI SPA
    "SU", # SUNCOR ENERGY INC
    "HMC", # HONDA MOTOR CO LTD
    "CCI", # CROWN CASTLE INC.
    "CHTR", # CHARTER COMMUNICATIONS, INC. /MO/
    "LHX", # L3HARRIS TECHNOLOGIES, INC. /DE/
    "OXY", # OCCIDENTAL PETROLEUM CORP /DE/
    "ROST", # ROSS STORES, INC.
    "COIN", # Coinbase Global, Inc.
    "VALE", # Vale S.A.
    "WCN", # Waste Connections, Inc.
    "LEN", # LENNAR CORP /NEW/
    "CPNG", # Coupang, Inc.
    "ALC", # ALCON INC
    "MPLX", # MPLX LP
    "MSCI", # MSCI Inc.
    "FAST", # FASTENAL CO
    "CMI", # CUMMINS INC
    "BCS", # BARCLAYS PLC
    "KMB", # KIMBERLY CLARK CORP
    "KDP", # Keurig Dr Pepper Inc.
    "PEG", # PUBLIC SERVICE ENTERPRISE GROUP INC
    "PWR", # QUANTA SERVICES, INC.
    "SQ", # Block, Inc.
    "TAK", # TAKEDA PHARMACEUTICAL CO LTD
    "TEL", # TE Connectivity plc
    "PRU", # PRUDENTIAL FINANCIAL INC
    "KVUE", # Kenvue Inc.
    "HLN", # Haleon plc
    "ODFL", # OLD DOMINION FREIGHT LINE, INC.
    "AEM", # AGNICO EAGLE MINES LTD
    "LNG", # Cheniere Energy, Inc.
    "LYG", # Lloyds Banking Group plc
    "NDAQ", # NASDAQ, INC.
    "VST", # Vistra Corp.
    "STZ", # CONSTELLATION BRANDS, INC.
    "AME", # AMETEK INC/
    "CTVA", # Corteva, Inc.
    "DDOG", # Datadog, Inc.
    "TCOM", # Trip.com Group Ltd
    "HES", # HESS CORP
    "GLW", # CORNING INC /NY
    "VLO", # VALERO ENERGY CORP/TX
    "F", # FORD MOTOR CO
    "KHC", # Kraft Heinz Co
    "HWM", # Howmet Aerospace Inc.
    "VRT", # Vertiv Holdings Co
    "EW", # Edwards Lifesciences Corp
    "KR", # KROGER CO
    "CBRE", # CBRE GROUP, INC.
    "GEHC", # GE HealthCare Technologies Inc.
    "NWG", # NatWest Group plc
    "IMO", # IMPERIAL OIL LTD
    "EA", # ELECTRONIC ARTS INC.
    "EXC", # EXELON CORP
    "OTIS", # Otis Worldwide Corp
    "STLA", # Stellantis N.V.
    "FERG", # Ferguson Enterprises Inc. /DE/
    "VRSK", # Verisk Analytics, Inc.
    "IR", # Ingersoll Rand Inc.
    "MCHP", # MICROCHIP TECHNOLOGY INC
    "IT", # GARTNER INC
    "SNOW", # Snowflake Inc.
    "GRMN", # GARMIN LTD
    "GIS", # GENERAL MILLS INC
    "ACGL", # ARCH CAPITAL GROUP LTD.
    "IQV", # IQVIA HOLDINGS INC.
    "DFS", # Discover Financial Services
    "XEL", # XCEL ENERGY INC
    "LVS", # LAS VEGAS SANDS CORP
    "CTSH", # COGNIZANT TECHNOLOGY SOLUTIONS CORP
    "BKR", # Baker Hughes Co
    "A", # AGILENT TECHNOLOGIES, INC.
    "DAL", # DELTA AIR LINES, INC.
    "YUM", # YUM BRANDS INC
    "SYY", # SYSCO CORP
    "IRM", # IRON MOUNTAIN INC
    "EXR", # Extra Space Storage Inc.
    "LULU", # lululemon athletica inc.
    "TRGP", # Targa Resources Corp.
    "VMC", # Vulcan Materials CO
    "MLM", # MARTIN MARIETTA MATERIALS INC
    "MPWR", # MONOLITHIC POWER SYSTEMS INC
    "HSY", # HERSHEY CO
    "CCEP", # COCA-COLA EUROPACIFIC PARTNERS plc
    "ED", # CONSOLIDATED EDISON INC
    "BSBR", # Banco Santander (Brasil) S.A.
    "RMD", # RESMED INC
    "ARGX", # ARGENX SE
    "ABEV", # AMBEV S.A.
    "DD", # DuPont de Nemours, Inc.
    "ALNY", # ALNYLAM PHARMACEUTICALS, INC.
    "DOW", # DOW INC.
    "HPQ", # HP INC
    "WIT", # WIPRO LTD
    "DIA", # SPDR DOW JONES INDUSTRIAL AVERAGE ETF TRUST
    "GOLD", # BARRICK GOLD CORP
    "NUE", # NUCOR CORP
    "VEEV", # VEEVA SYSTEMS INC
    "IDXX", # IDEXX LABORATORIES INC /DE
    "VICI", # VICI PROPERTIES INC.
    "RBLX", # Roblox Corp
    "DB", # DEUTSCHE BANK AKTIENGESELLSCHAFT
    "ETR", # ENTERGY CORP /DE/
    "OWL", # BLUE OWL CAPITAL INC.
    "EFX", # EQUIFAX INC
    "MTB", # M&T BANK CORP
    "WAB", # WESTINGHOUSE AIR BRAKE TECHNOLOGIES CORP
    "HIG", # HARTFORD FINANCIAL SERVICES GROUP, INC.
    "EIX", # EDISON INTERNATIONAL
    "RKT", # Rocket Companies, Inc.
    "SLF", # SUN LIFE FINANCIAL INC
    "AXON", # AXON ENTERPRISE, INC.
    "BIDU", # Baidu, Inc.
    "QSR", # Restaurant Brands International Inc.
    "AVB", # AVALONBAY COMMUNITIES INC
    "CNC", # CENTENE CORP
    "MDY", # SPDR S&P MIDCAP 400 ETF TRUST
    "HUM", # HUMANA INC
    "WTW", # WILLIS TOWERS WATSON PLC
    "WEC", # WEC ENERGY GROUP, INC.
    "ROK", # ROCKWELL AUTOMATION, INC
    "RJF", # RAYMOND JAMES FINANCIAL INC
    "BRO", # BROWN & BROWN, INC.
    "CSGP", # COSTAR GROUP, INC.
    "NET", # Cloudflare, Inc.
    "XYL", # Xylem Inc.
    "WPM", # Wheaton Precious Metals Corp.
    "WDS", # WOODSIDE ENERGY GROUP LTD
    "FITB", # FIFTH THIRD BANCORP
    "CVNA", # CARVANA CO.
    "ON", # ON SEMICONDUCTOR CORP
    "CCL", # CARNIVAL CORP
    "HEI", # HEICO CORP
    "BCE", # BCE INC
    "CVE", # CENOVUS ENERGY INC.
    "CHT", # CHUNGHWA TELECOM CO LTD
    "PPG", # PPG INDUSTRIES INC
    "TSCO", # TRACTOR SUPPLY CO /DE/
    "HUBS", # HUBSPOT INC
    "TTWO", # TAKE TWO INTERACTIVE SOFTWARE INC
    "LYB", # LyondellBasell Industries N.V.
    "ANSS", # ANSYS INC
    "NVR", # NVR INC
    "EQR", # EQUITY RESIDENTIAL
    "ERIC", # ERICSSON LM TELEPHONE CO
    "EBAY", # EBAY INC
    "TW", # Tradeweb Markets Inc.
    "K", # KELLANOVA
    "VTR", # Ventas, Inc.
    "DXCM", # DEXCOM INC
    "ZS", # Zscaler, Inc.
    "MTD", # METTLER TOLEDO INTERNATIONAL INC/
    "STT", # STATE STREET CORP
    "FCNCA", # FIRST CITIZENS BANCSHARES INC /DE/
    "LYV", # Live Nation Entertainment, Inc.
    "AWK", # American Water Works Company, Inc.
    "BNTX", # BioNTech SE
    "BEKE", # KE Holdings Inc.
    "IOT", # Samsara Inc.
    "ADM", # Archer-Daniels-Midland Co
    "TPL", # Texas Pacific Land Corp
    "GPN", # GLOBAL PAYMENTS INC
    "PHM", # PULTEGROUP INC/MI/
    "CAH", # CARDINAL HEALTH INC
    "TEF", # TELEFONICA S A
    "DOV", # DOVER Corp
    "UAL", # United Airlines Holdings, Inc.
    "TYL", # TYLER TECHNOLOGIES INC
    "DTE", # DTE ENERGY CO
    "KEYS", # Keysight Technologies, Inc.
    "LI", # Li Auto Inc.
    "BIIB", # BIOGEN INC.
    "FNV", # FRANCO NEVADA Corp
    "IFF", # INTERNATIONAL FLAVORS & FRAGRANCES INC
    "STM", # STMicroelectronics N.V.
    "NOK", # NOKIA CORP
    "HPE", # Hewlett Packard Enterprise Co
    "DVN", # DEVON ENERGY CORP/DE
    "CDW", # CDW Corp
    "GIB", # CGI INC
    "CUK", # CARNIVAL PLC
    "PHG", # KONINKLIJKE PHILIPS NV
    "BBD", # BANK BRADESCO
    "SBAC", # SBA COMMUNICATIONS CORP
    "HST", # HOST HOTELS & RESORTS, INC.
    "KB", # KB Financial Group Inc.
    "EL", # ESTEE LAUDER COMPANIES INC
    "FTV", # Fortive Corp
    "CHD", # CHURCH & DWIGHT CO INC /DE/
    "TPG", # TPG Inc.
    "BR", # BROADRIDGE FINANCIAL SOLUTIONS, INC.
    "DECK", # DECKERS OUTDOOR CORP
    "HAL", # HALLIBURTON CO
    "LDOS", # Leidos Holdings, Inc.
    "CQP", # Cheniere Energy Partners, L.P.
    "TROW", # PRICE T ROWE GROUP INC
    "FE", # FIRSTENERGY CORP
    "PBA", # PEMBINA PIPELINE CORP
    "PPL", # PPL Corp
    "IX", # ORIX CORP
    "VOD", # VODAFONE GROUP PUBLIC LTD CO
    "RYAAY", # RYANAIR HOLDINGS PLC
    "TECK", # TECK RESOURCES LTD
    "ES", # EVERSOURCE ENERGY
    "NTAP", # NetApp, Inc.
    "TU", # TELUS CORP
    "NTR", # Nutrien Ltd.
    "GDDY", # GoDaddy Inc.
    "ERIE", # ERIE INDEMNITY CO
    "AEE", # AMEREN CORP
    "BGNE", # BeiGene, Ltd.
    "BAH", # Booz Allen Hamilton Holding Corp
    "ZM", # Zoom Video Communications, Inc.
    "ILMN", # ILLUMINA, INC.
    "HUBB", # HUBBELL INC
    "WY", # WEYERHAEUSER CO
    "WDC", # WESTERN DIGITAL CORP
    "HBAN", # HUNTINGTON BANCSHARES INC /MD/
    "ROL", # ROLLINS INC
    "CCJ", # CAMECO CORP
    "WST", # WEST PHARMACEUTICAL SERVICES INC
    "PUK", # PRUDENTIAL PLC
    "PTC", # PTC INC.
    "CINF", # CINCINNATI FINANCIAL CORP
    "CBOE", # Cboe Global Markets, Inc.
    "EQT", # EQT Corp
    "BAM", # Brookfield Asset Management Ltd.
    "WRB", # BERKLEY W R CORP
    "STE", # STERIS plc
    "ZBH", # ZIMMER BIOMET HOLDINGS, INC.
    "PINS", # PINTEREST, INC.
    "RF", # REGIONS FINANCIAL CORP
    "ATO", # ATMOS ENERGY CORP
    "FTS", # Fortis Inc.
    "SYF", # Synchrony Financial
    "LPLA", # LPL Financial Holdings Inc.
    "TDY", # TELEDYNE TECHNOLOGIES INC
    "LII", # LENNOX INTERNATIONAL INC
    "STX", # Seagate Technology Holdings plc
    "MKC", # MCCORMICK & CO INC
    "CMS", # CMS ENERGY CORP
    "TSN", # TYSON FOODS, INC.
    "FSLR", # FIRST SOLAR, INC.
    "HOOD", # Robinhood Markets, Inc.
    "COO", # COOPER COMPANIES, INC.
    "TEVA", # TEVA PHARMACEUTICAL INDUSTRIES LTD
    "EME", # EMCOR Group, Inc.
    "MRNA", # Moderna, Inc.
    "PKG", # PACKAGING CORP OF AMERICA
    "SNAP", # Snap Inc
    "ASX", # ASE Technology Holding Co., Ltd.
    "STLD", # STEEL DYNAMICS INC
    "WBD", # Warner Bros. Discovery, Inc.
    "EXPE", # Expedia Group, Inc.
    "MKL", # MARKEL GROUP INC.
    "BLDR", # Builders FirstSource, Inc.
    "NTRS", # NORTHERN TRUST CORP
    "MDB", # MongoDB, Inc.
    "GFS", # GLOBALFOUNDRIES Inc.
    "CLX", # CLOROX CO /DE/
    "RCI", # ROGERS COMMUNICATIONS INC
    "OMC", # OMNICOM GROUP INC.
    "TRU", # TransUnion
    "ARE", # ALEXANDRIA REAL ESTATE EQUITIES, INC.
    "ZBRA", # ZEBRA TECHNOLOGIES CORP
    "INVH", # Invitation Homes Inc.
    "CNP", # CENTERPOINT ENERGY INC
    "BBY", # BEST BUY CO INC
    "MT", # ArcelorMittal
    "IP", # INTERNATIONAL PAPER CO /NEW/
    "CSL", # CARLISLE COMPANIES INC
    "ESS", # ESSEX PROPERTY TRUST, INC.
    "WAT", # WATERS CORP /DE/
    "WSO", # WATSCO INC
    "CHKP", # CHECK POINT SOFTWARE TECHNOLOGIES LTD
    "LH", # LABCORP HOLDINGS INC.
    "SHG", # SHINHAN FINANCIAL GROUP CO LTD
    "PFG", # PRINCIPAL FINANCIAL GROUP INC
    "CRBG", # Corebridge Financial, Inc.
    "DRI", # DARDEN RESTAURANTS INC
    "MAA", # MID AMERICA APARTMENT COMMUNITIES INC.
    "HOLX", # HOLOGIC INC
    "CFG", # CITIZENS FINANCIAL GROUP INC/RI
    "TME", # Tencent Music Entertainment Group
    "FOXA", # Fox Corp
    "NRG", # NRG ENERGY, INC.
    "KOF", # COCA COLA FEMSA SAB DE CV
    "MOH", # MOLINA HEALTHCARE, INC.
    "LUV", # SOUTHWEST AIRLINES CO
    "ZTO", # ZTO Express (Cayman) Inc.
    "BAX", # BAXTER INTERNATIONAL INC
    "PKX", # POSCO HOLDINGS INC.
    "UMC", # UNITED MICROELECTRONICS CORP
    "JBHT", # HUNT J B TRANSPORT SERVICES INC
    "BALL", # BALL Corp
    "ICLR", # ICON PLC
    "GEN", # Gen Digital Inc.
    "TS", # TENARIS SA
    "AER", # AerCap Holdings N.V.
    "RYAN", # RYAN SPECIALTY HOLDINGS, INC.
    "CG", # Carlyle Group Inc.
    "TLK", # PERUSAHAAN PERSEROAN PERSERO PT TELEKOMUNIKASI INDONESIA TBK
    "DG", # DOLLAR GENERAL CORP
    "CTRA", # Coterra Energy Inc.
    "IHG", # INTERCONTINENTAL HOTELS GROUP PLC /NEW/
    "L", # LOEWS CORP
    "SUI", # SUN COMMUNITIES INC
    "J", # JACOBS SOLUTIONS INC.
    "SNA", # Snap-on Inc
    "SSNC", # SS&C Technologies Holdings Inc
    "ULTA", # Ulta Beauty, Inc.
    "FDS", # FACTSET RESEARCH SYSTEMS INC
    "DGX", # QUEST DIAGNOSTICS INC
    "MAS", # MASCO CORP /DE/
    "DKNG", # DraftKings Inc.
    "TER", # TERADYNE, INC
    "KEY", # KEYCORP /NEW/
    "VRSN", # VERISIGN INC/CA
    "WLK", # WESTLAKE CORP
    "BEP", # Brookfield Renewable Partners L.P.
    "SMCI", # Super Micro Computer, Inc.
    "WSM", # WILLIAMS SONOMA INC
    "TOST", # Toast, Inc.
    "EXPD", # EXPEDITORS INTERNATIONAL OF WASHINGTON INC
    "YUMC", # Yum China Holdings, Inc.
    "HRL", # HORMEL FOODS CORP /DE/
    "AVY", # Avery Dennison Corp
    "NTNX", # Nutanix, Inc.
    "UTHR", # UNITED THERAPEUTICS Corp
    "WMG", # Warner Music Group Corp.
    "FNF", # Fidelity National Financial, Inc.
    "PSTG", # Pure Storage, Inc.
    "GFL", # GFL Environmental Inc.
    "NI", # NISOURCE INC.
    "PNR", # PENTAIR plc
    "RPM", # RPM INTERNATIONAL INC/DE/
    "IEX", # IDEX CORP /DE/
    "AMCR", # Amcor plc
    "GRAB", # Grab Holdings Ltd
    "KIM", # KIMCO REALTY CORP
    "SYM", # Symbotic Inc.
    "RPRX", # Royalty Pharma plc
    "DT", # Dynatrace, Inc.
    "PODD", # INSULET CORP
    "MANH", # MANHATTAN ASSOCIATES INC
    "UDR", # UDR, Inc.
    "GPC", # GENUINE PARTS CO
    "DKS", # DICK'S SPORTING GOODS, INC.
    "UI", # Ubiquiti Inc.
    "EC", # ECOPETROL S.A.
    "DOC", # HEALTHPEAK PROPERTIES, INC.
    "BIP", # Brookfield Infrastructure Partners L.P.
    "NWSA", # NEWS CORP
    "BURL", # Burlington Stores, Inc.
    "EG", # EVEREST GROUP, LTD.
    "RBA", # RB GLOBAL INC.
    "ENTG", # ENTEGRIS INC
    "RS", # RELIANCE, INC.
    "MRO", # MARATHON OIL CORP
    "LNT", # ALLIANT ENERGY CORP
    "OC", # Owens Corning
    "GWRE", # Guidewire Software, Inc.
    "ALGN", # ALIGN TECHNOLOGY INC
    "NMR", # NOMURA HOLDINGS INC
    "AKAM", # AKAMAI TECHNOLOGIES INC
    "AVTR", # Avantor, Inc.
    "XPO", # XPO, Inc.
    "CAVA", # CAVA GROUP, INC.
    "AMH", # American Homes 4 Rent
    "USFD", # US Foods Holding Corp.
    "ONON", # On Holding AG
    "TXT", # TEXTRON INC
    "NTRA", # Natera, Inc.
    "EBR", # BRAZILIAN ELECTRIC POWER CO
    "GFI", # GOLD FIELDS LTD
    "VIV", # TELEFONICA BRASIL S.A.
    "AZPN", # Aspen Technology, Inc.
    "CF", # CF Industries Holdings, Inc.
    "TOL", # Toll Brothers, Inc.
    "TRMB", # TRIMBLE INC.
    "THC", # TENET HEALTHCARE CORP
    "RVTY", # REVVITY, INC.
    "BSY", # BENTLEY SYSTEMS INC
    "MNDY", # monday.com Ltd.
    "BAP", # CREDICORP LTD
    "EQH", # Equitable Holdings, Inc.
    "H", # Hyatt Hotels Corp
    "SWK", # STANLEY BLACK & DECKER, INC.
    "CASY", # CASEYS GENERAL STORES INC
    "WES", # Western Midstream Partners, LP
    "ACM", # AECOM
    "BXP", # BXP, Inc.
    "DPZ", # DOMINOS PIZZA INC
    "INCY", # INCYTE CORP
    "NDSN", # NORDSON CORP
    "ELS", # EQUITY LIFESTYLE PROPERTIES INC
    "GMAB", # GENMAB A/S
    "COHR", # COHERENT CORP.
    "DOCU", # DOCUSIGN, INC.
    "MORN", # Morningstar, Inc.
    "CPB", # CAMPBELL SOUP CO
    "RGA", # REINSURANCE GROUP OF AMERICA INC
    "CAG", # CONAGRA BRANDS INC.
    "EVRG", # Evergy, Inc.
    "VTRS", # Viatris Inc
    "POOL", # POOL CORP
    "SWKS", # SKYWORKS SOLUTIONS, INC.
    "ZG", # ZILLOW GROUP, INC.
    "GLPI", # Gaming & Leisure Properties, Inc.
    "JBL", # JABIL INC
    "FLEX", # FLEX LTD.
    "RNR", # RENAISSANCERE HOLDINGS LTD
    "FIX", # COMFORT SYSTEMS USA INC
    "AGR", # Avangrid, Inc.
    "DLTR", # DOLLAR TREE, INC.
    "GGG", # GRACO INC
    "CE", # Celanese Corp
    "ARCC", # ARES CAPITAL CORP
    "LAMR", # LAMAR ADVERTISING CO/NEW
    "JHX", # James Hardie Industries plc
    "AFRM", # Affirm Holdings, Inc.
    "UHS", # UNIVERSAL HEALTH SERVICES INC
    "FFIV", # F5, INC.
    "EWBC", # EAST WEST BANCORP INC
    "FTAI", # FTAI Aviation Ltd.
    "SMMT", # Summit Therapeutics Inc.
    "JKHY", # JACK HENRY & ASSOCIATES INC
    "PCVX", # Vaxcyte, Inc.
    "CW", # CURTISS WRIGHT CORP
    "REG", # REGENCY CENTERS CORP
    "UHAL", # U-Haul Holding Co /NV/
    "TTEK", # TETRA TECH INC
    "FUTU", # Futu Holdings Ltd
    "JEF", # Jefferies Financial Group Inc.
    "TWLO", # TWILIO INC
    "CNA", # CNA FINANCIAL CORP
    "SAIA", # SAIA INC
    "JLL", # JONES LANG LASALLE INC
    "APTV", # Aptiv PLC
    "SUZ", # Suzano S.A.
    "TXRH", # Texas Roadhouse, Inc.
    "SFM", # Sprouts Farmers Market, Inc.
    "JNPR", # JUNIPER NETWORKS INC
    "RTO", # RENTOKIL INITIAL PLC /FI
    "PFGC", # Performance Food Group Co
    "EXAS", # EXACT SCIENCES CORP
    "CLH", # CLEAN HARBORS INC
    "BMRN", # BIOMARIN PHARMACEUTICAL INC
    "DUOL", # Duolingo, Inc.
    "CACI", # CACI INTERNATIONAL INC /DE/
    "CPT", # CAMDEN PROPERTY TRUST
    "LOGI", # LOGITECH INTERNATIONAL S.A.
    "KGC", # KINROSS GOLD CORP
    "WPC", # W. P. Carey Inc.
    "PAYC", # Paycom Software, Inc.
    "RL", # RALPH LAUREN CORP
    "NVT", # nVent Electric plc
    "EMN", # EASTMAN CHEMICAL CO
    "CHRW", # C. H. ROBINSON WORLDWIDE, INC.
    "OKTA", # Okta, Inc.
    "NBIX", # NEUROCRINE BIOSCIENCES INC
    "SJM", # J M SMUCKER Co
    "FMS", # Fresenius Medical Care AG
    "SOFI", # SoFi Technologies, Inc.
    "ALLE", # Allegion plc
    "SRPT", # Sarepta Therapeutics, Inc.
    "CYBR", # CyberArk Software Ltd.
    "BG", # Bunge Global SA
    "HLI", # HOULIHAN LOKEY, INC.
    "UNM", # Unum Group
    "BCH", # BANK OF CHILE
    "TECH", # BIO-TECHNE Corp
    "AU", # AngloGold Ashanti PLC
    "WMS", # ADVANCED DRAINAGE SYSTEMS, INC.
    "SCI", # SERVICE CORP INTERNATIONAL
    "AES", # AES CORP
    "PPC", # PILGRIMS PRIDE CORP
    "INSM", # INSMED Inc
    "PSN", # PARSONS CORP
    "LBRDA", # Liberty Broadband Corp
    "ITT", # ITT INC.
    "WPP", # WPP plc
    "OHI", # OMEGA HEALTHCARE INVESTORS INC
    "DVA", # DAVITA INC.
    "HTHT", # H World Group Ltd
    "PAA", # PLAINS ALL AMERICAN PIPELINE LP
    "TAP", # MOLSON COORS BEVERAGE CO
    "FTI", # TechnipFMC plc
    "MGA", # MAGNA INTERNATIONAL INC
    "TFII", # TFI International Inc.
    "YPF", # YPF SOCIEDAD ANONIMA
    "KMX", # CARMAX INC
    "CCK", # CROWN HOLDINGS, INC.
    "BJ", # BJ's Wholesale Club Holdings, Inc.
    "NCLH", # Norwegian Cruise Line Holdings Ltd.
    "ATR", # APTARGROUP, INC.
    "NICE", # NICE Ltd.
    "ENPH", # Enphase Energy, Inc.
    "BWXT", # BWX Technologies, Inc.
    "RRX", # REGAL REXNORD CORP
    "ALB", # ALBEMARLE CORP
    "MGM", # MGM Resorts International
    "MMYT", # MakeMyTrip Ltd
    "TPR", # TAPESTRY, INC.
    "LW", # Lamb Weston Holdings, Inc.
    "SNN", # SMITH & NEPHEW PLC
    "LECO", # LINCOLN ELECTRIC HOLDINGS INC
    "CUBE", # CubeSmart
    "IPG", # INTERPUBLIC GROUP OF COMPANIES, INC.
    "FND", # Floor & Decor Holdings, Inc.
    "CHWY", # Chewy, Inc.
    "SBS", # COMPANHIA DE SANEAMENTO BASICO DO ESTADO DE SAO PAULO-SABESP
    "PR", # Permian Resources Corp
    "MBLY", # Mobileye Global Inc.
    "AOS", # SMITH A O CORP
    "BPYPP", # Brookfield Property Partners L.P.
    "NIO", # NIO Inc.
    "MKTX", # MARKETAXESS HOLDINGS INC
    "AFG", # AMERICAN FINANCIAL GROUP INC
    "EPAM", # EPAM Systems, Inc.
    "BEN", # FRANKLIN RESOURCES INC
    "ALLY", # Ally Financial Inc.
    "KEP", # KOREA ELECTRIC POWER CORP
    "SQM", # CHEMICAL & MINING CO OF CHILE INC
    "NLY", # ANNALY CAPITAL MANAGEMENT INC
    "BLD", # TopBuild Corp
    "CTLT", # Catalent, Inc.
    "WYNN", # WYNN RESORTS LTD
    "XPEV", # XPENG INC.
    "WTRG", # Essential Utilities, Inc.
    "SF", # STIFEL FINANCIAL CORP
    "ACI", # Albertsons Companies, Inc.
    "UWMC", # UWM Holdings Corp
    "PCTY", # Paylocity Holding Corp
    "FBIN", # Fortune Brands Innovations, Inc.
    "OVV", # Ovintiv Inc.
    "AA", # Alcoa Corp
    "AEG", # AEGON LTD.
    "CHDN", # Churchill Downs Inc
    "RIVN", # Rivian Automotive, Inc. / DE
    "EDU", # New Oriental Education & Technology Group Inc.
    "ESLT", # ELBIT SYSTEMS LTD
    "SLV", # iShares Silver Trust
    "DOX", # AMDOCS LTD
    "EHC", # Encompass Health Corp
    "EVR", # Evercore Inc.
    "PAG", # PENSKE AUTOMOTIVE GROUP, INC.
    "GNRC", # GENERAC HOLDINGS INC.
    "MUSA", # Murphy USA Inc.
    "AIZ", # ASSURANT, INC.
    "PNW", # PINNACLE WEST CAPITAL CORP
    "REXR", # Rexford Industrial Realty, Inc.
    "GME", # GameStop Corp.
    "KNSL", # Kinsale Capital Group, Inc.
    "GMED", # GLOBUS MEDICAL INC
    "ARMK", # Aramark
    "HLNE", # Hamilton Lane INC
    "BIO", # BIO-RAD LABORATORIES, INC.
    "COKE", # Coca-Cola Consolidated, Inc.
    "SNX", # TD SYNNEX CORP
    "MEDP", # Medpace Holdings, Inc.
    "VNOM", # Viper Energy, Inc.
    "WWD", # Woodward, Inc.
    "PSO", # PEARSON PLC
    "MTZ", # MASTEC INC
    "SEIC", # SEI INVESTMENTS CO
    "ONTO", # ONTO INNOVATION INC.
    "RGLD", # ROYAL GOLD INC
    "PCOR", # PROCORE TECHNOLOGIES, INC.
    "LKQ", # LKQ CORP
    "GL", # GLOBE LIFE INC.
    "EXP", # EAGLE MATERIALS INC
    "WCC", # WESCO INTERNATIONAL INC
    "EXEL", # EXELIXIS, INC.
    "TFX", # TELEFLEX INC
    "FRT", # FEDERAL REALTY INVESTMENT TRUST
    "QGEN", # QIAGEN N.V.
    "BSAC", # BANCO SANTANDER CHILE
    "MLI", # MUELLER INDUSTRIES INC
    "PRI", # Primerica, Inc.
    "YMM", # Full Truck Alliance Co. Ltd.
    "XP", # XP Inc.
    "MTCH", # Match Group, Inc.
    "SKX", # SKECHERS USA INC
    "ALSN", # Allison Transmission Holdings Inc
    "CRL", # CHARLES RIVER LABORATORIES INTERNATIONAL, INC.
    "FHN", # FIRST HORIZON CORP
    "STN", # STANTEC INC
    "APG", # APi Group Corp
    "AAON", # AAON, INC.
    "AYI", # ACUITY BRANDS INC
    "HAS", # HASBRO, INC.
    "WAL", # WESTERN ALLIANCE BANCORPORATION
    "CIEN", # CIENA CORP
    "NYT", # NEW YORK TIMES CO
    "ITCI", # Intra-Cellular Therapies, Inc.
    "SIRI", # SIRIUS XM HOLDINGS INC.
    "WIX", # Wix.com Ltd.
    "ORI", # OLD REPUBLIC INTERNATIONAL CORP
    "GLOB", # Globant S.A.
    "CR", # Crane Co
    "EDR", # Endeavor Group Holdings, Inc.
    "FLR", # FLUOR CORP
    "KBR", # KBR, INC.
    "AIT", # APPLIED INDUSTRIAL TECHNOLOGIES INC
    "HSIC", # HENRY SCHEIN INC
    "ENSG", # ENSIGN GROUP, INC
    "BILI", # Bilibili Inc.
    "CNM", # Core & Main, Inc.
    "FYBR", # Frontier Communications Parent, Inc.
    "PAC", # Pacific Airport Group
    "RVMD", # Revolution Medicines, Inc.
    "AAL", # American Airlines Group Inc.
    "WBS", # WEBSTER FINANCIAL CORP
    "LAD", # LITHIA MOTORS INC
    "DSGX", # DESCARTES SYSTEMS GROUP INC
    "ROKU", # ROKU, INC
    "DTM", # DT Midstream, Inc.
    "ALTR", # Altair Engineering Inc.
    "DCI", # DONALDSON Co INC
    "PEN", # Penumbra Inc
    "FN", # Fabrinet
    "SKM", # SK TELECOM CO LTD
    "X", # UNITED STATES STEEL CORP
    "APA", # APA Corp
    "INGR", # Ingredion Inc
    "VNO", # VORNADO REALTY TRUST
    "BRBR", # BELLRING BRANDS, INC.
    "EGP", # EASTGROUP PROPERTIES INC
    "BRKR", # BRUKER CORP
    "GTLB", # Gitlab Inc.
    "ROIV", # Roivant Sciences Ltd.
    "MOS", # MOSAIC CO
    "OLED", # UNIVERSAL DISPLAY CORP PA
    "USO", # United States Oil Fund, LP
    "AUR", # Aurora Innovation, Inc.
    "GPK", # GRAPHIC PACKAGING HOLDING CO
    "KNX", # Knight-Swift Transportation Holdings Inc.
    "WING", # Wingstop Inc.
    "CZR", # Caesars Entertainment, Inc.
    "AGI", # ALAMOS GOLD INC
    "MHK", # MOHAWK INDUSTRIES INC
    "PHYS", # Sprott Physical Gold Trust
    "CMA", # COMERICA INC /NEW/
    "PAAS", # PAN AMERICAN SILVER CORP
    "INFA", # Informatica Inc.
    "FSV", # FirstService Corp
    "SUM", # Summit Materials, Inc.
    "TPX", # TEMPUR SEALY INTERNATIONAL, INC.
    "CFLT", # Confluent, Inc.
    "WF", # WOORI FINANCIAL GROUP INC.
    "LEGN", # Legend Biotech Corp
    "HRB", # H&R BLOCK INC
    "TTC", # TORO CO
    "RBC", # RBC Bearings INC
    "LNW", # Light & Wonder, Inc.
    "BRX", # Brixmor Property Group Inc.
    "DBX", # DROPBOX, INC.
    "AXTA", # Axalta Coating Systems Ltd.
    "PNFP", # PINNACLE FINANCIAL PARTNERS INC
    "ESTC", # Elastic N.V.
    "CFR", # CULLEN/FROST BANKERS, INC.
    "S", # SentinelOne, Inc.
    "VFC", # V F CORP
    "ADC", # AGREE REALTY CORP
    "VKTX", # Viking Therapeutics, Inc.
    "CHE", # CHEMED CORP
    "WBA", # Walgreens Boots Alliance, Inc.
    "AR", # ANTERO RESOURCES Corp
    "CBSH", # COMMERCE BANCSHARES INC /MO/
    "FMC", # FMC CORP
    "OGE", # OGE ENERGY CORP.
    "BERY", # BERRY GLOBAL GROUP, INC.
    "OTEX", # OPEN TEXT CORP
    "NNN", # NNN REIT, INC.
    "MTSI", # MACOM Technology Solutions Holdings, Inc.
    "FOUR", # Shift4 Payments, Inc.
    "DRS", # Leonardo DRS, Inc.
    "U", # Unity Software Inc.
    "HESM", # Hess Midstream LP
    "ASR", # SOUTHEAST AIRPORT GROUP
    "CLS", # CELESTICA INC
    "VOYA", # Voya Financial, Inc.
    "AGNC", # AGNC Investment Corp.
    "GIL", # Gildan Activewear Inc.
    "CIGI", # Colliers International Group Inc.
    "KT", # KT CORP
    "SMAR", # SMARTSHEET INC
    "BFAM", # BRIGHT HORIZONS FAMILY SOLUTIONS INC.
    "IVZ", # Invesco Ltd.
    "CIB", # BANCOLOMBIA SA
    "WTFC", # WINTRUST FINANCIAL CORP
    "CHRD", # Chord Energy Corp
    "ZION", # ZIONS BANCORPORATION, NATIONAL ASSOCIATION /UT/
    "PARA", # Paramount Global
    "DOCS", # Doximity, Inc.
    "CX", # CEMEX SAB DE CV
    "APPF", # APPFOLIO INC
    "VIPS", # Vipshop Holdings Ltd
    "MASI", # MASIMO CORP
    "BWA", # BORGWARNER INC
    "SSD", # Simpson Manufacturing Co., Inc.
    "ASTS", # AST SpaceMobile, Inc.
    "TREX", # TREX CO INC
    "JXN", # Jackson Financial Inc.
    "RGEN", # REPLIGEN CORP
    "CRS", # CARPENTER TECHNOLOGY CORP
    "LNTH", # Lantheus Holdings, Inc.
    "BRFS", # BRF S.A.
    "ATI", # ATI INC
    "SSB", # SouthState Corp
    "UFPI", # UFP INDUSTRIES INC
    "AGCO", # AGCO CORP /DE
    "ESAB", # ESAB Corp
    "HQY", # HEALTHEQUITY, INC.
    "DINO", # HF Sinclair Corp
    "HII", # HUNTINGTON INGALLS INDUSTRIES, INC.
    "COLD", # AMERICOLD REALTY TRUST
    "GGAL", # GRUPO FINANCIERO GALICIA SA
    "ASND", # Ascendis Pharma A/S
    "RRC", # RANGE RESOURCES CORP
    "ALV", # AUTOLIV INC
    "WFG", # WEST FRASER TIMBER CO., LTD
    "FR", # FIRST INDUSTRIAL REALTY TRUST INC
    "SNV", # SYNOVUS FINANCIAL CORP
    "GKOS", # GLAUKOS Corp
    "LBTYA", # Liberty Global Ltd.
    "GXO", # GXO Logistics, Inc.
    "RLI", # RLI CORP
    "SAIC", # Science Applications International Corp
    "BLCO", # Bausch & Lomb Corp
    "RHI", # ROBERT HALF INC.
    "TMHC", # Taylor Morrison Home Corp
    "FCN", # FTI CONSULTING, INC
    "STAG", # STAG Industrial, Inc.
    "STEP", # StepStone Group Inc.
    "GNTX", # GENTEX CORP
    "PB", # PROSPERITY BANCSHARES INC
    "CGNX", # COGNEX CORP
    "DLB", # Dolby Laboratories, Inc.
    "MIDD", # MIDDLEBY Corp
    "FLS", # FLOWSERVE CORP
    "TIMB", # TIM S.A.
    "AM", # Antero Midstream Corp
    "CELH", # Celsius Holdings, Inc.
    "SUN", # Sunoco LP
    "LPX", # LOUISIANA-PACIFIC CORP
    "LSCC", # LATTICE SEMICONDUCTOR CORP
    "MAT", # MATTEL INC /DE/
    "PEGA", # PEGASYSTEMS INC
    "BOKF", # BOK FINANCIAL CORP
    "WEX", # WEX Inc.
    "STWD", # STARWOOD PROPERTY TRUST, INC.
    "GRFS", # Grifols SA
    "ENLC", # EnLink Midstream, LLC
    "HCP", # HashiCorp, Inc.
    "WH", # WYNDHAM HOTELS & RESORTS, INC.
    "LEVI", # LEVI STRAUSS & CO
    "G", # Genpact LTD
    "PATH", # UiPath, Inc.
    "JAZZ", # Jazz Pharmaceuticals plc
    "CVLT", # COMMVAULT SYSTEMS INC
    "SATS", # EchoStar CORP
    "EXLS", # ExlService Holdings, Inc.
    "SPXC", # SPX Technologies, Inc.
    "HMY", # HARMONY GOLD MINING CO LTD
    "PLNT", # Planet Fitness, Inc.
    "OSK", # OSHKOSH CORP
    "ANF", # ABERCROMBIE & FITCH CO /DE/
    "AXS", # AXIS CAPITAL HOLDINGS LTD
    "QRVO", # Qorvo, Inc.
    "TX", # Ternium S.A.
    "TAL", # TAL Education Group
    "KEX", # KIRBY CORP
    "FAF", # First American Financial Corp
    "MKSI", # MKS INSTRUMENTS INC
    "FRHC", # Freedom Holding Corp.
    "ZETA", # Zeta Global Holdings Corp.
    "CHH", # CHOICE HOTELS INTERNATIONAL INC /DE
    "ESI", # Element Solutions Inc
    "ADT", # ADT Inc.
    "JHG", # JANUS HENDERSON GROUP PLC
    "MTG", # MGIC INVESTMENT CORP
    "MTH", # Meritage Homes CORP
    "MSA", # MSA Safety Inc
    "LUMN", # Lumen Technologies, Inc.
    "CCCS", # CCC Intelligent Solutions Holdings Inc.
    "VERX", # Vertex, Inc.
    "COTY", # COTY INC.
    "GGB", # GERDAU S.A.
    "RHP", # Ryman Hospitality Properties, Inc.
    "CWAN", # Clearwater Analytics Holdings, Inc.
    "MTDR", # Matador Resources Co
    "BPOP", # POPULAR, INC.
    "WTS", # WATTS WATER TECHNOLOGIES INC
    "HALO", # HALOZYME THERAPEUTICS, INC.
    "SITE", # SiteOne Landscape Supply, Inc.
    "POST", # Post Holdings, Inc.
    "BZ", # Kanzhun Ltd
    "BXSL", # Blackstone Secured Lending Fund
    "ESNT", # Essent Group Ltd.
    "FRPT", # Freshpet, Inc.
    "AZEK", # AZEK Co Inc.
    "ARW", # ARROW ELECTRONICS, INC.
    "BYD", # BOYD GAMING CORP
    "GLBE", # Global-E Online Ltd.
    "VMI", # VALMONT INDUSTRIES INC
    "WSC", # WillScot Holdings Corp
    "AMKR", # AMKOR TECHNOLOGY, INC.
    "NUVL", # Nuvalent, Inc.
    "CWST", # CASELLA WASTE SYSTEMS INC
    "DAR", # DARLING INGREDIENTS INC.
    "CMC", # COMMERCIAL METALS Co
    "CROX", # Crocs, Inc.
    "BBWI", # Bath & Body Works, Inc.
    "LSTR", # LANDSTAR SYSTEM INC
    "SPSC", # SPS COMMERCE INC
    "ELAN", # Elanco Animal Health Inc
    "MTN", # VAIL RESORTS INC
    "R", # RYDER SYSTEM INC
    "CRDO", # Credo Technology Group Holding Ltd
    "HR", # Healthcare Realty Trust Inc
    "ERJ", # EMBRAER S.A.
    "AN", # AUTONATION, INC.
    "ONB", # OLD NATIONAL BANCORP /IN/
    "ALK", # ALASKA AIR GROUP, INC.
    "MNSO", # MINISO Group Holding Ltd
    "ZWS", # Zurn Elkay Water Solutions Corp
    "NOVT", # NOVANTA INC
    "CADE", # Cadence Bank
    "CIG", # ENERGY CO OF MINAS GERAIS
    "MOD", # MODINE MANUFACTURING CO
    "PDI", # PIMCO Dynamic Income Fund
    "IBP", # Installed Building Products, Inc.
    "LFUS", # LITTELFUSE INC /DE
    "AWI", # ARMSTRONG WORLD INDUSTRIES INC
    "IONS", # IONIS PHARMACEUTICALS INC
    "AVAV", # AeroVironment Inc
    "DDS", # DILLARD'S, INC.
    "CLF", # CLEVELAND-CLIFFS INC.
    "BILL", # BILL Holdings, Inc.
    "COLB", # COLUMBIA BANKING SYSTEM, INC.
    "NOV", # NOV Inc.
    "RCM", # R1 RCM Inc. /DE
    "LNC", # LINCOLN NATIONAL CORP
    "ETSY", # ETSY INC
    "CYTK", # CYTOKINETICS INC
    "OMF", # OneMain Holdings, Inc.
    "CBT", # CABOT CORP
    "HRI", # HERC HOLDINGS INC
    "ELF", # e.l.f. Beauty, Inc.
    "GBCI", # GLACIER BANCORP, INC.
    "TRNO", # Terreno Realty Corp
    "BMI", # BADGER METER INC
    "CSWI", # CSW INDUSTRIALS, INC.
    "RH", # RH
    "MDU", # MDU RESOURCES GROUP INC
    "IEP", # ICAHN ENTERPRISES L.P.
    "TKR", # TIMKEN CO
    "OBDC", # Blue Owl Capital Corp
    "CRUS", # CIRRUS LOGIC, INC.
    "INSP", # Inspire Medical Systems, Inc.
    "BMA", # Macro Bank Inc.
    "MMSI", # MERIT MEDICAL SYSTEMS INC
    "AMG", # AFFILIATED MANAGERS GROUP, INC.
    "LCID", # Lucid Group, Inc.
    "NXT", # Nextracker Inc.
    "KRG", # KITE REALTY GROUP TRUST
    "KBH", # KB HOME
    "NSIT", # INSIGHT ENTERPRISES INC
    "NXST", # NEXSTAR MEDIA GROUP, INC.
    "REYN", # Reynolds Consumer Products Inc.
    "COOP", # Mr. Cooper Group Inc.
    "VNT", # Vontier Corp
    "CAE", # CAE INC
    "SRCL", # STERICYCLE INC
    "WFRD", # Weatherford International plc
    "WHR", # WHIRLPOOL CORP /DE/
    "BECN", # BEACON ROOFING SUPPLY INC
    "FSK", # FS KKR Capital Corp
    "VRNS", # VARONIS SYSTEMS INC
    "CTRE", # CareTrust REIT, Inc.
    "OLLI", # Ollie's Bargain Outlet Holdings, Inc.
    "CWEN", # Clearway Energy, Inc.
    "EPRT", # ESSENTIAL PROPERTIES REALTY TRUST, INC.
    "SIGI", # SELECTIVE INSURANCE GROUP INC
    "MDGL", # MADRIGAL PHARMACEUTICALS, INC.
    "SLGN", # SILGAN HOLDINGS INC
    "BPMC", # Blueprint Medicines Corp
    "NFG", # NATIONAL FUEL GAS CO
    "IDA", # IDACORP INC
    "KNF", # Knife River Corp
    "BIPC", # Brookfield Infrastructure Corp
    "RITM", # Rithm Capital Corp.
    "BEPC", # Brookfield Renewable Corp
    "PSLV", # Sprott Physical Silver Trust
    "THO", # THOR INDUSTRIES INC
    "NSA", # National Storage Affiliates Trust
    "HOMB", # HOME BANCSHARES INC
    "BCPC", # BALCHEM CORP
    "PVH", # PVH CORP. /DE/
    "THG", # HANOVER INSURANCE GROUP, INC.
    "PJT", # PJT Partners Inc.
    "TKC", # TURKCELL ILETISIM HIZMETLERI A S
    "UMBF", # UMB FINANCIAL CORP
    "USM", # UNITED STATES CELLULAR CORP
    "CHX", # ChampionX Corp
    "ACT", # Enact Holdings, Inc.
    "ICL", # ICL Group Ltd.
    "KD", # Kyndryl Holdings, Inc.
    "MSGS", # Madison Square Garden Sports Corp.
    "NVMI", # NOVA LTD.
    "PI", # IMPINJ INC
    "RDN", # RADIAN GROUP INC
    "SEE", # SEALED AIR CORP/DE
    "LYFT", # Lyft, Inc.
    "SWX", # Southwest Gas Holdings, Inc.
    "DNB", # Dun & Bradstreet Holdings, Inc.
    "PHI", # PLDT Inc.
    "RRR", # Red Rock Resorts, Inc.
    "BC", # BRUNSWICK CORP
    "FNB", # FNB CORP/PA/
    "RKLB", # Rocket Lab USA, Inc.
    "ST", # Sensata Technologies Holding plc
    "W", # Wayfair Inc.
    "MMS", # MAXIMUS, INC.
    "FIVE", # FIVE BELOW, INC
    "CEF", # Sprott Physical Gold & Silver Trust
    "LEA", # LEAR CORP
    "STVN", # Stevanato Group S.p.A.
    "FFIN", # FIRST FINANCIAL BANKSHARES INC
    "VVV", # VALVOLINE INC
    "GTLS", # CHART INDUSTRIES INC
    "SON", # SONOCO PRODUCTS CO
    "BCC", # BOISE CASCADE Co
    "CRVL", # CORVEL CORP
    "SHAK", # Shake Shack Inc.
    "MATX", # Matson, Inc.
    "PECO", # Phillips Edison & Company, Inc.
    "UGI", # UGI CORP /PA/
    "ACIW", # ACI WORLDWIDE, INC.
    "RMBS", # RAMBUS INC
    "CACC", # CREDIT ACCEPTANCE CORP
    "NE", # Noble Corp plc
    "YOU", # Clear Secure, Inc.
    "UBSI", # UNITED BANKSHARES INC/WV
    "PFSI", # PennyMac Financial Services, Inc.
    "QFIN", # Qifu Technology, Inc.
    "CORT", # CORCEPT THERAPEUTICS INC
    "QTWO", # Q2 Holdings, Inc.
    "BROS", # Dutch Bros Inc.
    "FG", # F&G Annuities & Life, Inc.
    "CNX", # CNX Resources Corp
    "SKY", # Champion Homes, Inc.
    "BHVN", # Biohaven Ltd.
    "NEU", # NEWMARKET CORP
    "GTES", # Gates Industrial Corp plc
    "MGY", # Magnolia Oil & Gas Corp
    "DY", # DYCOM INDUSTRIES INC
    "CNS", # COHEN & STEERS, INC.
    "CRNX", # Crinetics Pharmaceuticals, Inc.
    "ITRI", # ITRON, INC.
    "SLG", # SL GREEN REALTY CORP
    "RNA", # Avidity Biosciences, Inc.
    "POR", # PORTLAND GENERAL ELECTRIC CO /OR/
    "OZK", # Bank OZK
    "AL", # AIR LEASE CORP
    "FSS", # FEDERAL SIGNAL CORP /DE/
    "SNDR", # Schneider National, Inc.
    "SMG", # SCOTTS MIRACLE-GRO CO
    "GATX", # GATX CORP
    "KRYS", # Krystal Biotech, Inc.
    "ESGR", # Enstar Group LTD
    "GPI", # GROUP 1 AUTOMOTIVE INC
    "MARA", # MARA Holdings, Inc.
    "VLY", # VALLEY NATIONAL BANCORP
    "KTB", # Kontoor Brands, Inc.
    "KRC", # KILROY REALTY CORP
    "RDNT", # RadNet, Inc.
    "EXPO", # EXPONENT INC
    "TENB", # Tenable Holdings, Inc.
    "SM", # SM Energy Co
    "ORA", # ORMAT TECHNOLOGIES, INC.
    "ELP", # ENERGY CO OF PARANA
    "OGN", # Organon & Co.
    "CLVT", # CLARIVATE PLC
    "OLN", # OLIN Corp
    "HXL", # HEXCEL CORP /DE/
    "CIVI", # CIVITAS RESOURCES, INC.
    "LANC", # LANCASTER COLONY CORP
    "LAZ", # Lazard, Inc.
    "AVT", # AVNET INC
    "VIRT", # Virtu Financial, Inc.
    "NVEI", # Nuvei Corp
    "RYN", # RAYONIER INC
    "MUR", # MURPHY OIL CORP
    "TIGO", # MILLICOM INTERNATIONAL CELLULAR SA
    "SLM", # SLM Corp
    "MC", # Moelis & Co
    "XRAY", # DENTSPLY SIRONA Inc.
    "BDC", # BELDEN INC.
    "COLM", # COLUMBIA SPORTSWEAR CO
    "CUZ", # COUSINS PROPERTIES INC
    "TSEM", # TOWER SEMICONDUCTOR LTD
    "STRL", # STERLING INFRASTRUCTURE, INC.
    "FLO", # FLOWERS FOODS INC
    "RARE", # Ultragenyx Pharmaceutical Inc.
    "LTH", # Life Time Group Holdings, Inc.
    "WTM", # WHITE MOUNTAINS INSURANCE GROUP LTD
    "IRT", # INDEPENDENCE REALTY TRUST, INC.
    "FCFS", # FirstCash Holdings, Inc.
    "CRC", # California Resources Corp
    "BGC", # BGC Group, Inc.
    "EAT", # BRINKER INTERNATIONAL, INC
    "ABG", # ASBURY AUTOMOTIVE GROUP INC
    "SFBS", # ServisFirst Bancshares, Inc.
    "SBRA", # Sabra Health Care REIT, Inc.
    "BOX", # BOX INC
    "ACA", # Arcosa, Inc.
    "RXO", # RXO, Inc.
    "NJR", # NEW JERSEY RESOURCES CORP
    "HWC", # HANCOCK WHITNEY CORP
    "BCO", # BRINKS CO
    "PRCT", # PROCEPT BioRobotics Corp
    "PIPR", # PIPER SANDLER COMPANIES
    "BBIO", # BridgeBio Pharma, Inc.
    "MAIN", # Main Street Capital CORP
    "ACLX", # Arcellx, Inc.
    "WK", # WORKIVA INC
    "MSM", # MSC INDUSTRIAL DIRECT CO INC
    "SHC", # Sotera Health Co
    "AGO", # ASSURED GUARANTY LTD
    "QLYS", # QUALYS, INC.
    "EEFT", # EURONET WORLDWIDE, INC.
    "FELE", # FRANKLIN ELECTRIC CO INC
    "RUSHA", # RUSH ENTERPRISES INC TX
    "UPST", # Upstart Holdings, Inc.
    "IMVT", # Immunovant, Inc.
    "CALM", # CAL-MAINE FOODS INC
    "NCNO", # nCino, Inc.
    "ABCB", # Ameris Bancorp
    "AVNT", # AVIENT CORP
    "BTG", # B2GOLD CORP
    "LITE", # Lumentum Holdings Inc.
    "IESC", # IES Holdings, Inc.
    "VRRM", # VERRA MOBILITY Corp
    "PAM", # Pampa Energy Inc.
    "FRO", # Frontline plc
    "AXSM", # Axsome Therapeutics, Inc.
    "M", # Macy's, Inc.
    "SIM", # GRUPO SIMEC, S.A.B. de C.V.
    "PRMW", # Primo Water Corp /CN/
    "FIZZ", # NATIONAL BEVERAGE CORP
    "HOG", # HARLEY-DAVIDSON, INC.
    "MAC", # MACERICH CO
    "SEM", # SELECT MEDICAL HOLDINGS CORP
    "TNET", # TRINET GROUP, INC.
    "ITGR", # Integer Holdings Corp
    "ICUI", # ICU MEDICAL INC/DE
    "AB", # ALLIANCEBERNSTEIN HOLDING L.P.
    "ALKS", # Alkermes plc.
    "ROAD", # Construction Partners, Inc.
    "HASI", # HA Sustainable Infrastructure Capital, Inc.
    "ASH", # ASHLAND INC.
    "BKH", # BLACK HILLS CORP /SD/
    "IAC", # IAC Inc.
    "NXE", # NexGen Energy Ltd.
    "GDS", # GDS Holdings Ltd
    "ASGN", # ASGN Inc
    "NNI", # NELNET INC
    "MHO", # M/I HOMES, INC.
    "IGT", # International Game Technology PLC
    "AEIS", # ADVANCED ENERGY INDUSTRIES INC
    "LRN", # Stride, Inc.
    "OSCR", # Oscar Health, Inc.
    "OGS", # ONE Gas, Inc.
    "CPA", # Copa Holdings, S.A.
    "SG", # Sweetgreen, Inc.
    "HIMS", # Hims & Hers Health, Inc.
    "LOPE", # Grand Canyon Education, Inc.
    "GSHD", # Goosehead Insurance, Inc.
    "SIG", # SIGNET JEWELERS LTD
    "KMPR", # KEMPER Corp
    "FUL", # FULLER H B CO
    "ZI", # ZoomInfo Technologies Inc.
    "GBDC", # GOLUB CAPITAL BDC, Inc.
    "TGS", # GAS TRANSPORTER OF THE SOUTH INC
    "PAGP", # PLAINS GP HOLDINGS LP
    "FUN", # Six Flags Entertainment Corporation/NEW
    "HL", # HECLA MINING CO/DE/
    "CRSP", # CRISPR Therapeutics AG
    "WHD", # Cactus, Inc.
    "ACHC", # Acadia Healthcare Company, Inc.
    "CCOI", # COGENT COMMUNICATIONS HOLDINGS, INC.
    "OPCH", # Option Care Health, Inc.
    "IPAR", # INTERPARFUMS INC
    "ALVO", # Alvotech
    "PLXS", # PLEXUS CORP
    "VCTR", # Victory Capital Holdings, Inc.
    "PII", # Polaris Inc.
    "ENS", # EnerSys
    "AX", # Axos Financial, Inc.
    "KAI", # KADANT INC
    "UGP", # ULTRAPAR HOLDINGS INC
    "ALIT", # Alight, Inc. / Delaware
    "FLNC", # Fluence Energy, Inc.
    "INTA", # Intapp, Inc.
    "SITM", # SITIME Corp
    "IBOC", # INTERNATIONAL BANCSHARES CORP
    "CLBT", # Cellebrite DI Ltd.
    "WEN", # Wendy's Co
    "BLKB", # BLACKBAUD INC
    "SANM", # SANMINA CORP
    "SKYW", # SKYWEST INC
    "HUN", # Huntsman CORP
    "TGTX", # TG THERAPEUTICS, INC.
    "MCY", # MERCURY GENERAL CORP
    "CSAN", # Cosan S.A.
    "ADMA", # ADMA BIOLOGICS, INC.
    "OR", # Osisko Gold Royalties LTD
    "RIG", # Transocean Ltd.
    "BOOT", # Boot Barn Holdings, Inc.
    "LPL", # LG Display Co., Ltd.
    "AEO", # AMERICAN EAGLE OUTFITTERS INC
    "TPH", # Tri Pointe Homes, Inc.
    "GOLF", # Acushnet Holdings Corp.
    "FTDR", # Frontdoor, Inc.
    "HGV", # Hilton Grand Vacations Inc.
    "GLNG", # GOLAR LNG LTD
    "ENIC", # Enel Chile S.A.
    "SPR", # Spirit AeroSystems Holdings, Inc.
    "JWN", # NORDSTROM INC
    "IDCC", # InterDigital, Inc.
    "WD", # Walker & Dunlop, Inc.
    "DNLI", # Denali Therapeutics Inc.
    "AQN", # ALGONQUIN POWER & UTILITIES CORP.
    "ALGM", # ALLEGRO MICROSYSTEMS, INC.
    "NMRK", # NEWMARK GROUP, INC.
    "SR", # SPIRE INC
    "IIPR", # INNOVATIVE INDUSTRIAL PROPERTIES INC
    "VAL", # Valaris Ltd
    "KFY", # KORN FERRY
    "ALE", # ALLETE INC
    "GVA", # GRANITE CONSTRUCTION INC
    "SRAD", # Sportradar Group AG
    "HGTY", # Hagerty, Inc.
    "HAE", # HAEMONETICS CORP
    "JOBY", # Joby Aviation, Inc.
    "SGRY", # Surgery Partners, Inc.
    "DXC", # DXC Technology Co
    "DOCN", # DigitalOcean Holdings, Inc.
    "SKT", # TANGER INC.
    "HIW", # HIGHWOODS PROPERTIES, INC.
    "CNO", # CNO Financial Group, Inc.
    "NWL", # NEWELL BRANDS INC.
    "PBH", # Prestige Consumer Healthcare Inc.
    "GHC", # Graham Holdings Co
    "BANF", # BANCFIRST CORP /OK/
    "NVST", # Envista Holdings Corp
    "WU", # Western Union CO
    "CNK", # Cinemark Holdings, Inc.
    "DOOO", # BRP Inc.
    "ALKT", # ALKAMI TECHNOLOGY, INC.
    "ATAT", # Atour Lifestyle Holdings Ltd
    "NOG", # NORTHERN OIL & GAS, INC.
    "TFSL", # TFS Financial CORP
    "GBTG", # Global Business Travel Group, Inc.
    "ASO", # Academy Sports & Outdoors, Inc.
    "ASB", # ASSOCIATED BANC-CORP
    "AXNX", # Axonics, Inc.
    "FRSH", # Freshworks Inc.
    "APLE", # Apple Hospitality REIT, Inc.
    "DEI", # Douglas Emmett Inc
    "JBT", # John Bean Technologies CORP
    "IBRX", # ImmunityBio, Inc.
    "EGO", # ELDORADO GOLD CORP /FI
    "CAMT", # CAMTEK LTD
    "SSL", # SASOL LTD
    "WDFC", # WD 40 CO
    "UAA", # Under Armour, Inc.
    "TCBI", # TEXAS CAPITAL BANCSHARES INC/TX
    "GMS", # GMS Inc.
    "DORM", # Dorman Products, Inc.
    "HAYW", # Hayward Holdings, Inc.
    "SLVM", # Sylvamo Corp
    "AROC", # Archrock, Inc.
    "HBM", # Hudbay Minerals Inc.
    "BNL", # Broadstone Net Lease, Inc.
    "DNP", # DNP SELECT INCOME FUND INC
    "PRGO", # PERRIGO Co plc
    "IPGP", # IPG PHOTONICS CORP
    "CBZ", # CBIZ, Inc.
    "IRDM", # Iridium Communications Inc.
    "EPR", # EPR PROPERTIES
    "BL", # BLACKLINE, INC.
    "ENV", # ENVESTNET, INC.
    "NEA", # Nuveen AMT-Free Quality Municipal Income Fund
    "MRUS", # Merus N.V.
    "INST", # INSTRUCTURE HOLDINGS, INC.
    "KTOS", # KRATOS DEFENSE & SECURITY SOLUTIONS, INC.
    "ATHM", # Autohome Inc.
    "CRK", # COMSTOCK RESOURCES INC
    "TEX", # TEREX CORP
    "STR", # Sitio Royalties Corp.
    "AUB", # Atlantic Union Bankshares Corp
    "POWI", # POWER INTEGRATIONS INC
    "TDS", # TELEPHONE & DATA SYSTEMS INC /DE/
    "CVCO", # CAVCO INDUSTRIES INC.
    "STNE", # StoneCo Ltd.
    "CORZ", # Core Scientific, Inc./tx
    "NHI", # NATIONAL HEALTH INVESTORS INC
    "MIR", # Mirion Technologies, Inc.
    "TFPM", # Triple Flag Precious Metals Corp.
    "FOLD", # AMICUS THERAPEUTICS, INC.
    "BTU", # PEABODY ENERGY CORP
    "SMPL", # Simply Good Foods Co
    "SMTC", # SEMTECH CORP
    "MWA", # Mueller Water Products, Inc.
    "UNF", # UNIFIRST CORP
    "BRC", # BRADY CORP
    "PRIM", # Primoris Services Corp
    "SAM", # BOSTON BEER CO INC
    "SLAB", # SILICON LABORATORIES INC.
    "APLS", # Apellis Pharmaceuticals, Inc.
    "ABM", # ABM INDUSTRIES INC /DE/
    "PBF", # PBF Energy Inc.
    "ARLP", # ALLIANCE RESOURCE PARTNERS LP
    "RELY", # Remitly Global, Inc.
    "SBSW", # Sibanye Stillwater Ltd
    "BHC", # Bausch Health Companies Inc.
    "HP", # Helmerich & Payne, Inc.
    "FULT", # FULTON FINANCIAL CORP
    "RNG", # RingCentral, Inc.
    "OTTR", # Otter Tail Corp
    "CATY", # CATHAY GENERAL BANCORP
    "URBN", # URBAN OUTFITTERS INC
    "MGEE", # MGE ENERGY INC
    "NWE", # NorthWestern Energy Group, Inc.
    "EBC", # Eastern Bankshares, Inc.
    "PCH", # POTLATCHDELTIC CORP
    "HCC", # WARRIOR MET COAL, INC.
    "FHI", # FEDERATED HERMES, INC.
    "TNL", # Travel & Leisure Co.
    "PAYO", # Payoneer Global Inc.
    "BBAR", # Banco BBVA Argentina S.A.
    "CEIX", # CONSOL Energy Inc.
    "ESE", # ESCO TECHNOLOGIES INC
    "FIBK", # FIRST INTERSTATE BANCSYSTEM INC
    "USLM", # UNITED STATES LIME & MINERALS INC
    "OMAB", # Central North Airport Group
    "BVN", # BUENAVENTURA MINING CO INC
    "SHOO", # STEVEN MADDEN, LTD.
    "IONQ", # IonQ, Inc.
    "FROG", # JFrog Ltd
    "ATMU", # Atmus Filtration Technologies Inc.
    "CBU", # COMMUNITY FINANCIAL SYSTEM, INC.
    "SXT", # SENSIENT TECHNOLOGIES CORP
    "BRZE", # Braze, Inc.
    "JJSF", # J&J SNACK FOODS CORP
    "TGLS", # Tecnoglass Inc.
    "RUN", # Sunrun Inc.
    "HCM", # HUTCHMED (China) Ltd
    "CARG", # CarGurus, Inc.
    "HTGC", # Hercules Capital, Inc.
    "ICFI", # ICF International, Inc.
    "FHB", # FIRST HAWAIIAN, INC.
    "PTON", # PELOTON INTERACTIVE, INC.
    "FBP", # FIRST BANCORP /PR/
    "BXMT", # BLACKSTONE MORTGAGE TRUST, INC.
    "AKR", # ACADIA REALTY TRUST
    "TEO", # TELECOM ARGENTINA SA
    "IOVA", # IOVANCE BIOTHERAPEUTICS, INC.
    "COMP", # Compass, Inc.
    "EWTX", # Edgewise Therapeutics, Inc.
    "IAG", # IAMGOLD CORP
    "TDW", # TIDEWATER INC
    "CWK", # Cushman & Wakefield plc
    "AMED", # AMEDISYS INC
    "XENE", # Xenon Pharmaceuticals Inc.
    "AWR", # AMERICAN STATES WATER CO
    "AI", # C3.ai, Inc.
    "NEOG", # NEOGEN CORP
    "TAC", # TRANSALTA CORP
    "CXT", # Crane NXT, Co.
    "PTCT", # PTC THERAPEUTICS, INC.
    "NMIH", # NMI Holdings, Inc.
    "IFS", # Intercorp Financial Services Inc.
    "GFF", # GRIFFON CORP
    "BSM", # Black Stone Minerals, L.P.
    "TDC", # TERADATA CORP /DE/
    "CWT", # CALIFORNIA WATER SERVICE GROUP
    "ESRT", # Empire State Realty Trust, Inc.
    "NPO", # Enpro Inc.
    "APAM", # Artisan Partners Asset Management Inc.
    "ZLAB", # Zai Lab Ltd
    "ATKR", # Atkore Inc.
    "PAY", # Paymentus Holdings, Inc.
    "UEC", # URANIUM ENERGY CORP
    "GEF", # GREIF, INC
    "POWL", # POWELL INDUSTRIES INC
    "JOE", # ST JOE Co
    "GRBK", # Green Brick Partners, Inc.
    "PENN", # PENN Entertainment, Inc.
    "CAAP", # CORPORACION AMERICA AIRPORTS S.A.
    "PTEN", # PATTERSON UTI ENERGY INC
    "MAN", # ManpowerGroup Inc.
    "RYTM", # RHYTHM PHARMACEUTICALS, INC.
    "ATGE", # Adtalem Global Education Inc.
    "BUR", # Burford Capital Ltd
    "KYMR", # Kymera Therapeutics, Inc.
    "YETI", # YETI Holdings, Inc.
    "UE", # Urban Edge Properties
    "NSP", # INSPERITY, INC.
    "FORM", # FORMFACTOR INC
    "OUT", # OUTFRONT Media Inc.
    "AESI", # Atlas Energy Solutions Inc.
    "AVA", # AVISTA CORP
    "MP", # MP Materials Corp. / DE
    "APGE", # Apogee Therapeutics, Inc.
    "CAR", # AVIS BUDGET GROUP, INC.
    "DBRG", # DigitalBridge Group, Inc.
    "PLTK", # Playtika Holding Corp.
    "WSFS", # WSFS FINANCIAL CORP
    "SFNC", # SIMMONS FIRST NATIONAL CORP
    "STNG", # Scorpio Tankers Inc.
    "GNW", # GENWORTH FINANCIAL INC
    "MLTX", # MoonLake Immunotherapeutics
    "PK", # Park Hotels & Resorts Inc.
    "ATS", # ATS Corp /ATS
    "KNTK", # Kinetik Holdings Inc.
    "NARI", # Inari Medical, Inc.
    "BHF", # Brighthouse Financial, Inc.
    "DV", # DoubleVerify Holdings, Inc.
    "ESBA", # Empire State Realty OP, L.P.
    "BOH", # BANK OF HAWAII CORP
    "TRN", # TRINITY INDUSTRIES INC
    "MLCO", # Melco Resorts & Entertainment LTD
    "SNEX", # StoneX Group Inc.
    "REZI", # RESIDEO TECHNOLOGIES, INC.
    "ACVA", # ACV Auctions Inc.
    "DYN", # Dyne Therapeutics, Inc.
    "PATK", # PATRICK INDUSTRIES INC
    "MQ", # Marqeta, Inc.
    "INTR", # Inter & Co, Inc.
    "LCII", # LCI INDUSTRIES
    "NOMD", # Nomad Foods Ltd
    "CRGY", # Crescent Energy Co
    "PRK", # PARK NATIONAL CORP /OH/
    "ZIM", # ZIM Integrated Shipping Services Ltd.
    "MPW", # MEDICAL PROPERTIES TRUST INC
    "LBRT", # Liberty Energy Inc.
    "LIVN", # LivaNova PLC
    "JANX", # Janux Therapeutics, Inc.
    "AGYS", # AGILYSYS INC
    "DFH", # Dream Finders Homes, Inc.
    "ACLS", # AXCELIS TECHNOLOGIES INC
    "LXP", # LXP Industrial Trust
    "WAFD", # WAFD INC
    "NAD", # Nuveen Quality Municipal Income Fund
    "MGRC", # MCGRATH RENTCORP
    "CCS", # Century Communities, Inc.
    "ABR", # ARBOR REALTY TRUST INC
    "PRGS", # PROGRESS SOFTWARE CORP /MA
    "RIOT", # Riot Platforms, Inc.
    "CSQ", # CALAMOS STRATEGIC TOTAL RETURN FUND
    "CNXC", # Concentrix Corp
    "VRNA", # Verona Pharma plc
    "CVBF", # CVB FINANCIAL CORP
    "ASAN", # Asana, Inc.
    "TGNA", # TEGNA INC
    "PYCR", # PAYCOR HCM, INC.
    "TMDX", # TransMedics Group, Inc.
    "KWR", # QUAKER CHEMICAL CORP
    "SYNA", # SYNAPTICS Inc
    "PTGX", # Protagonist Therapeutics, Inc
    "DIOD", # DIODES INC /DEL/
    "IOSP", # INNOSPEC INC.
    "NVG", # Nuveen AMT-Free Municipal Credit Income Fund
    "CPK", # CHESAPEAKE UTILITIES CORP
    "AMR", # Alpha Metallurgical Resources, Inc.
    "GH", # Guardant Health, Inc.
    "EVH", # Evolent Health, Inc.
    "INDB", # INDEPENDENT BANK CORP
    "MANU", # Manchester United plc
    "VAC", # MARRIOTT VACATIONS WORLDWIDE Corp
    "CC", # Chemours Co
    "SEB", # SEABOARD CORP /DE/
    "SID", # NATIONAL STEEL CO
    "CLSK", # CLEANSPARK, INC.
    "HUBG", # Hub Group, Inc.
    "FA", # FIRST ADVANTAGE CORP
    "ARCH", # ARCH RESOURCES, INC.
    "WLY", # JOHN WILEY & SONS, INC.
    "UTG", # REAVES UTILITY INCOME FUND
    "BKU", # BankUnited, Inc.
    "ALRM", # Alarm.com Holdings, Inc.
    "QS", # QuantumScape Corp
    "KGS", # Kodiak Gas Services, Inc.
    "AMRX", # Amneal Pharmaceuticals, Inc.
    "LAUR", # LAUREATE EDUCATION, INC.
    "MEOH", # METHANEX CORP
    "BANC", # BANC OF CALIFORNIA, INC.
    "FCPT", # Four Corners Property Trust, Inc.
    "QDEL", # QuidelOrtho Corp
    "VCYT", # VERACYTE, INC.
    "SDRL", # Seadrill Ltd
    "EE", # Excelerate Energy, Inc.
    "CPRX", # CATALYST PHARMACEUTICALS, INC.
    "PAGS", # PagSeguro Digital Ltd.
    "APPN", # APPIAN CORP
    "HTLF", # HEARTLAND FINANCIAL USA INC
    "LFST", # LifeStance Health Group, Inc.
    "VSTO", # Vista Outdoor Inc.
    "JPC", # Nuveen Preferred & Income Opportunities Fund
    "RPD", # Rapid7, Inc.
    "AY", # Atlantica Sustainable Infrastructure plc
    "PSMT", # PRICESMART INC
    "RLX", # RLX Technology Inc.
    "USAC", # USA Compression Partners, LP
    "CDE", # Coeur Mining, Inc.
    "SRRK", # Scholar Rock Holding Corp
    "GPOR", # GULFPORT ENERGY CORP
    "EXG", # Eaton Vance Tax-Managed Global Diversified Equity Income Fund
    "AGIO", # AGIOS PHARMACEUTICALS, INC.
    "EQX", # Equinox Gold Corp.
    "SPB", # Spectrum Brands Holdings, Inc.
    "IQ", # iQIYI, Inc.
    "AMPH", # Amphastar Pharmaceuticals, Inc.
    "BATRA", # Atlanta Braves Holdings, Inc.
    "VC", # VISTEON CORP
    "PPBI", # PACIFIC PREMIER BANCORP INC
    "DBC", # Invesco DB Commodity Index Tracking Fund
    "DLO", # dLocal Ltd
    "BFH", # BREAD FINANCIAL HOLDINGS, INC.
    "PFS", # PROVIDENT FINANCIAL SERVICES INC
    "TRMD", # TORM plc
    "FFBC", # FIRST FINANCIAL BANCORP /OH/
    "OII", # OCEANEERING INTERNATIONAL INC
    "GERN", # GERON CORP
    "WULF", # TERAWULF INC.
    "HBI", # Hanesbrands Inc.
    "KLIC", # KULICKE & SOFFA INDUSTRIES INC
    "ARCB", # ARCBEST CORP /DE/
    "NZF", # Nuveen Municipal Credit Income Fund
    "IBTX", # Independent Bank Group, Inc.
    "TBBK", # Bancorp, Inc.
    "DRVN", # Driven Brands Holdings Inc.
    "MCW", # Mister Car Wash, Inc.
    "UTF", # COHEN & STEERS INFRASTRUCTURE FUND INC
    "ACAD", # ACADIA PHARMACEUTICALS INC
    "PLUS", # EPLUS INC
    "ADX", # ADAMS DIVERSIFIED EQUITY FUND, INC.
    "RSI", # Rush Street Interactive, Inc.
    "ARWR", # ARROWHEAD PHARMACEUTICALS, INC.
    "PSNY", # Polestar Automotive Holding UK PLC
    "TWST", # Twist Bioscience Corp
    "VSCO", # Victoria's Secret & Co.
    "MTX", # MINERALS TECHNOLOGIES INC
    "PLMR", # Palomar Holdings, Inc.
    "GPCR", # Structure Therapeutics Inc.
    "IDYA", # IDEAYA Biosciences, Inc.
    "EPAC", # ENERPAC TOOL GROUP CORP
    "LGIH", # LGI Homes, Inc.
    "B", # BARNES GROUP INC
    "GDRX", # GoodRx Holdings, Inc.
    "HNI", # HNI CORP
    "BAK", # BRASKEM SA
    "CALX", # CALIX, INC
    "EVGO", # EVgo Inc.
    "GRND", # Grindr Inc.
    "CAKE", # CHEESECAKE FACTORY INC
    "PTY", # PIMCO CORPORATE & INCOME OPPORTUNITY FUND
    "LU", # Lufax Holding Ltd
    "ALHC", # Alignment Healthcare, Inc.
    "VSH", # VISHAY INTERTECHNOLOGY INC
    "TRUP", # TRUPANION, INC.
    "LBPH", # Longboard Pharmaceuticals, Inc.
    "FBK", # FB Financial Corp
    "AMBA", # AMBARELLA INC
    "ENOV", # Enovis CORP
    "LSPD", # Lightspeed Commerce Inc.
    "ENR", # ENERGIZER HOLDINGS, INC.
    "AZZ", # AZZ INC
    "SBCF", # SEACOAST BANKING CORP OF FLORIDA
    "AVAL", # Grupo Aval Acciones Y Valores S.A.
    "HWKN", # HAWKINS INC
    "TTMI", # TTM TECHNOLOGIES INC
    "IVT", # InvenTrust Properties Corp.
    "YELP", # YELP INC
    "MBC", # MasterBrand, Inc.
    "VEON", # VEON Ltd.
    "GT", # GOODYEAR TIRE & RUBBER CO /OH/
    "ENVA", # Enova International, Inc.
    "SPNT", # SiriusPoint Ltd
    "ETY", # Eaton Vance Tax-Managed Diversified Equity Income Fund
    "NABL", # N-able, Inc.
    "ADUS", # Addus HomeCare Corp
    "AVPT", # AvePoint, Inc.
    "CPRI", # Capri Holdings Ltd
    "WERN", # WERNER ENTERPRISES INC
    "IRTC", # iRhythm Technologies, Inc.
    "PSEC", # PROSPECT CAPITAL CORP
    "SWTX", # SpringWorks Therapeutics, Inc.
    "VTMX", # Vesta Real Estate Corporation, S.A.B. de C.V.
    "OMCL", # OMNICELL, INC.
    "GOF", # GUGGENHEIM STRATEGIC OPPORTUNITIES FUND
    "BTE", # BAYTEX ENERGY CORP.
    "VERA", # Vera Therapeutics, Inc.
    "PCT", # PureCycle Technologies, Inc.
    "OSIS", # OSI SYSTEMS INC
    "BANR", # BANNER CORP
    "VZIO", # Vizio Holding Corp.
    "FIVN", # Five9, Inc.
    "BE", # Bloom Energy Corp
    "WGS", # GeneDx Holdings Corp.
    "TRIP", # TripAdvisor, Inc.
    "FLYW", # Flywire Corp
    "WB", # WEIBO Corp
    "SXI", # STANDEX INTERNATIONAL CORP/DE/
    "AMBP", # Ardagh Metal Packaging S.A.
    "TR", # TOOTSIE ROLL INDUSTRIES INC
    "AG", # FIRST MAJESTIC SILVER CORP
    "NGD", # New Gold Inc. /FI
    "FL", # FOOT LOCKER, INC.
    "RNST", # RENASANT CORP
    "PRVA", # Privia Health Group, Inc.
    "KROS", # Keros Therapeutics, Inc.
    "FRME", # FIRST MERCHANTS CORP
    "BKE", # BUCKLE INC
    "SBLK", # Star Bulk Carriers Corp.
    "NXRT", # NexPoint Residential Trust, Inc.
    "VCEL", # Vericel Corp
    "SWI", # SolarWinds Corp
    "GCMG", # GCM Grosvenor Inc.
    "MYRG", # MYR GROUP INC.
    "ODD", # Oddity Tech Ltd
    "STRA", # Strategic Education, Inc.
    "TRMK", # TRUSTMARK CORP
    "WNS", # WNS (HOLDINGS) LTD
    "NFE", # New Fortress Energy Inc.
    "MTRN", # MATERION Corp
    "GDV", # GABELLI DIVIDEND & INCOME TRUST
    "AKRO", # Akero Therapeutics, Inc.
    "GEO", # GEO GROUP INC
    "JAMF", # Jamf Holding Corp.
    "AAP", # ADVANCE AUTO PARTS INC
    "SLNO", # SOLENO THERAPEUTICS INC
    "INSW", # International Seaways, Inc.
    "GOGL", # Golden Ocean Group Ltd
    "VSEC", # VSE CORP
    "AIR", # AAR CORP
    "EQC", # Equity Commonwealth
    "NBTB", # NBT BANCORP INC
    "PAR", # PAR TECHNOLOGY CORP
    "WSBC", # WESBANCO INC
    "AIN", # ALBANY INTERNATIONAL CORP /DE/
    "AAT", # American Assets Trust, Inc.
    "WVE", # Wave Life Sciences Ltd.
    "HLMN", # Hillman Solutions Corp.
    "EVTC", # EVERTEC, Inc.
    "CNMD", # CONMED Corp
    "ZD", # ZIFF DAVIS, INC.
    "TFIN", # Triumph Financial, Inc.
    "SPNS", # SAPIENS INTERNATIONAL CORP N V
    "UFPT", # UFP TECHNOLOGIES INC
    "VICR", # VICOR CORP
    "RNW", # ReNew Energy Global plc
    "SGHC", # Super Group (SGHC) Ltd
    "SHO", # Sunstone Hotel Investors, Inc.
    "PTVE", # Pactiv Evergreen Inc.
    "HURN", # Huron Consulting Group Inc.
    "ALG", # ALAMO GROUP INC
    "KSS", # KOHLS Corp
    "TNDM", # TANDEM DIABETES CARE INC
    "CCU", # UNITED BREWERIES CO INC
    "VIAV", # VIAVI SOLUTIONS INC.
    "CENT", # CENTRAL GARDEN & PET CO
    "ROCK", # GIBRALTAR INDUSTRIES, INC.
    "FIHL", # Fidelis Insurance Holdings Ltd
    "CLOV", # CLOVER HEALTH INVESTMENTS, CORP. /DE
    "EXPI", # EXP World Holdings, Inc.
    "GSAT", # Globalstar, Inc.
    "MSGE", # Madison Square Garden Entertainment Corp.
    "WRBY", # Warby Parker Inc.
    "PHIN", # PHINIA INC.
    "MYGN", # MYRIAD GENETICS INC
    "JBLU", # JETBLUE AIRWAYS CORP
    "AZTA", # Azenta, Inc.
    "ROIC", # RETAIL OPPORTUNITY INVESTMENTS CORP
    "LION", # Lionsgate Studios Corp.
    "EFSC", # ENTERPRISE FINANCIAL SERVICES CORP
    "HTH", # Hilltop Holdings Inc.
    "DKL", # Delek Logistics Partners, LP
    "USA", # LIBERTY ALL STAR EQUITY FUND
    "RXST", # RxSight, Inc.
    "PINC", # Premier, Inc.
    "CRI", # CARTERS INC
    "EXTR", # EXTREME NETWORKS INC
    "LMAT", # LEMAITRE VASCULAR INC
    "SAH", # SONIC AUTOMOTIVE INC
    "KMT", # KENNAMETAL INC
    "AGM", # FEDERAL AGRICULTURAL MORTGAGE CORP
    "EVCM", # EverCommerce Inc.
    "LGND", # LIGAND PHARMACEUTICALS INC
    "BLTE", # BELITE BIO, INC
    "YY", # JOYY Inc.
    "HI", # Hillenbrand, Inc.
    "MRCY", # MERCURY SYSTEMS INC
    "PRM", # Perimeter Solutions, SA
    "CNTA", # Centessa Pharmaceuticals plc
    "VVX", # V2X, Inc.
    "WOR", # WORTHINGTON ENTERPRISES, INC.
    "KYN", # Kayne Anderson Energy Infrastructure Fund, Inc.
    "TXG", # 10x Genomics, Inc.
    "CLM", # CORNERSTONE STRATEGIC VALUE FUND INC
    "SEMR", # SEMrush Holdings, Inc.
    "LILA", # Liberty Latin America Ltd.
    "MNKD", # MANNKIND CORP
    "TROX", # Tronox Holdings plc
    "SYBT", # Stock Yards Bancorp, Inc.
    "MRVI", # MARAVAI LIFESCIENCES HOLDINGS, INC.
    "STC", # STEWART INFORMATION SERVICES CORP
    "DNUT", # Krispy Kreme, Inc.
    "HEES", # H&E Equipment Services, Inc.
    "CABO", # Cable One, Inc.
    "ZGN", # Ermenegildo Zegna N.V.
    "THS", # TreeHouse Foods, Inc.
    "ENLT", # Enlight Renewable Energy Ltd.
    "OFG", # OFG BANCORP
    "TSLX", # Sixth Street Specialty Lending, Inc.
    "ROG", # ROGERS CORP
    "IAS", # INTEGRAL AD SCIENCE HOLDING CORP.
    "DNN", # DENISON MINES CORP.
    "CXM", # Sprinklr, Inc.
    "ERO", # Ero Copper Corp.
    "SUPN", # SUPERNUS PHARMACEUTICALS, INC.
    "HRMY", # Harmony Biosciences Holdings, Inc.
    "GBX", # GREENBRIER COMPANIES INC
    "PDCO", # PATTERSON COMPANIES, INC.
    "SJW", # SJW GROUP
    "OSW", # ONESPAWORLD HOLDINGS Ltd
    "ARCO", # Arcos Dorados Holdings Inc.
    "RXRX", # RECURSION PHARMACEUTICALS, INC.
    "TALO", # TALOS ENERGY INC.
    "NUV", # NUVEEN MUNICIPAL VALUE FUND INC
    "CRTO", # Criteo S.A.
    "MIRM", # Mirum Pharmaceuticals, Inc.
    "RQI", # COHEN & STEERS QUALITY INCOME REALTY FUND INC
    "FTF", # FRANKLIN LTD DURATION INCOME TRUST
    "GNL", # Global Net Lease, Inc.
    "PRG", # PROG Holdings, Inc.
    "SMR", # NUSCALE POWER Corp
    "CLMT", # Calumet, Inc. /DE
    "BEAM", # Beam Therapeutics Inc.
    "SOUN", # SOUNDHOUND AI, INC.
    "GLPG", # GALAPAGOS NV
    "CLBK", # Columbia Financial, Inc.
    "NHC", # NATIONAL HEALTHCARE CORP
    "DRH", # DiamondRock Hospitality Co
    "NEP", # NEXTERA ENERGY PARTNERS, LP
    "DSGR", # Distribution Solutions Group, Inc.
    "MODG", # Topgolf Callaway Brands Corp.
    "SKWD", # Skyward Specialty Insurance Group, Inc.
    "LOB", # Live Oak Bancshares, Inc.
    "SAND", # SANDSTORM GOLD LTD
    "AGX", # ARGAN INC
    "ARVN", # ARVINAS, INC.
    "EVT", # EATON VANCE TAX ADVANTAGED DIVIDEND INCOME FUND
    "PROK", # PROKIDNEY CORP.
    "UPWK", # UPWORK, INC
    "PAX", # Patria Investments Ltd
    "KOS", # Kosmos Energy Ltd.
    "CASH", # PATHWARD FINANCIAL, INC.
    "SIMO", # Silicon Motion Technology CORP
    "LTC", # LTC PROPERTIES INC
    "HE", # HAWAIIAN ELECTRIC INDUSTRIES INC
    "ASAI", # Sendas Distributor S.A.
    "RVLV", # Revolve Group, Inc.
    "RVT", # ROYCE SMALL-CAP TRUST, INC.
    "GTY", # GETTY REALTY CORP /MD/
    "DBD", # DIEBOLD NIXDORF, Inc
    "ECAT", # BlackRock ESG Capital Allocation Term Trust
    "FBNC", # FIRST BANCORP /NC/
    "IREN", # Iris Energy Ltd
    "MAG", # MAG SILVER CORP
    "CMPR", # CIMPRESS plc
    "LEU", # CENTRUS ENERGY CORP
    "KAR", # OPENLANE, Inc.
    "NRIX", # Nurix Therapeutics, Inc.
    "OI", # O-I Glass, Inc. /DE/
    "MGNI", # MAGNITE, INC.
    "CHCO", # CITY HOLDING CO
    "NBHC", # National Bank Holdings Corp
    "NEO", # NEOGENOMICS INC
    "AVDX", # AvidXchange Holdings, Inc.
    "PZZA", # PAPA JOHNS INTERNATIONAL INC
    "EPC", # EDGEWELL PERSONAL CARE Co
    "PWP", # Perella Weinberg Partners
    "PLUG", # PLUG POWER INC
    "CLDX", # Celldex Therapeutics, Inc.
    "BBUC", # Brookfield Business Corp
    "BCAT", # BlackRock Capital Allocation Term Trust
    "NWBI", # Northwest Bancshares, Inc.
    "ADNT", # Adient plc
    "VRE", # Veris Residential, Inc.
    "WMK", # WEIS MARKETS INC
    "CEPU", # CENTRAL PUERTO S.A.
    "PD", # PagerDuty, Inc.
    "LMND", # Lemonade, Inc.
    "DFIN", # Donnelley Financial Solutions, Inc.
    "GETY", # Getty Images Holdings, Inc.
    "MBIN", # Merchants Bancorp
    "FCF", # FIRST COMMONWEALTH FINANCIAL CORP /PA/
    "TY", # TRI-CONTINENTAL Corp
    "LKFN", # LAKELAND FINANCIAL CORP
    "OXLC", # Oxford Lane Capital Corp.
    "RAMP", # LiveRamp Holdings, Inc.
    "WOLF", # WOLFSPEED, INC.
    "NVCR", # NovoCure Ltd
    "VRDN", # Viridian Therapeutics, Inc.\DE
    "COCO", # Vita Coco Company, Inc.
    "TARS", # Tarsus Pharmaceuticals, Inc.
    "OCUL", # OCULAR THERAPEUTIX, INC
    "BCRX", # BIOCRYST PHARMACEUTICALS INC
    "CNXN", # PC CONNECTION INC
    "TNC", # TENNANT CO
    "NAC", # Nuveen California Quality Municipal Income Fund
    "MLNK", # MeridianLink, Inc.
    "CSTM", # CONSTELLIUM SE
    "APOG", # APOGEE ENTERPRISES, INC.
    "STGW", # Stagwell Inc
    "SCL", # STEPAN CO
    "CODI", # Compass Diversified Holdings
    "BIGZ", # BlackRock Innovation & Growth Term Trust
    "GAB", # GABELLI EQUITY TRUST INC
    "CENX", # CENTURY ALUMINUM CO
    "BCYC", # BICYCLE THERAPEUTICS PLC
    "DHT", # DHT Holdings, Inc.
    "SVV", # Savers Value Village, Inc.
    "NTB", # Bank of N.T. Butterfield & Son Ltd
    "HPK", # HighPeak Energy, Inc.
    "CERT", # Certara, Inc.
    "WGO", # WINNEBAGO INDUSTRIES INC
    "BBU", # Brookfield Business Partners L.P.
    "TNK", # TEEKAY TANKERS LTD.
    "LEG", # LEGGETT & PLATT INC
    "RUM", # Rumble Inc.
    "CIFR", # Cipher Mining Inc.
    "KNSA", # Kiniksa Pharmaceuticals International, plc
    "ATRC", # AtriCure, Inc.
    "AMRC", # Ameresco, Inc.
    "VECO", # VEECO INSTRUMENTS INC
    "SNDX", # Syndax Pharmaceuticals Inc
    "UPBD", # UPBOUND GROUP, INC.
    "CMRE", # Costamare Inc.
    "NAPA", # Duckhorn Portfolio, Inc.
    "CVI", # CVR ENERGY INC
    "LC", # LendingClub Corp
    "BMEZ", # BlackRock Health Sciences Term Trust
    "FOR", # Forestar Group Inc.
    "GTX", # Garrett Motion Inc.
    "ETV", # Eaton Vance Tax-Managed Buy-Write Opportunities Fund
    "LZB", # LA-Z-BOY INC
    "AMC", # AMC ENTERTAINMENT HOLDINGS, INC.
    "OPRA", # Opera Ltd
    "NMM", # Navios Maritime Partners L.P.
    "BDJ", # BlackRock Enhanced Equity Dividend Trust
    "INFN", # Infinera Corp
    "GLP", # GLOBAL PARTNERS LP
    "CHEF", # Chefs' Warehouse, Inc.
    "NAVI", # NAVIENT CORP
    "FINV", # FinVolution Group
    "BOWL", # Bowlero Corp.
    "BV", # BrightView Holdings, Inc.
    "HROW", # HARROW, INC.
    "DVAX", # DYNAVAX TECHNOLOGIES CORP
    "DAC", # Danaos Corp
    "PDO", # PIMCO Dynamic Income Opportunities Fund
    "MLKN", # MILLERKNOLL, INC.
    "ANDE", # Andersons, Inc.
    "FDP", # FRESH DEL MONTE PRODUCE INC
    "TDOC", # Teladoc Health, Inc.
    "HLIO", # HELIOS TECHNOLOGIES, INC.
    "BHE", # BENCHMARK ELECTRONICS INC
    "GSBD", # Goldman Sachs BDC, Inc.
    "SA", # SEABRIDGE GOLD INC
    "NIC", # NICOLET BANKSHARES INC
    "ENVX", # Enovix Corp
    "XHR", # Xenia Hotels & Resorts, Inc.
    "VRTS", # VIRTUS INVESTMENT PARTNERS, INC.
    "NVAX", # NOVAVAX INC
    "SAFE", # Safehold Inc.
    "IMCR", # Immunocore Holdings plc
    "NAMS", # NewAmsterdam Pharma Co N.V.
    "FSM", # FORTUNA MINING CORP.
    "SFL", # SFL Corp Ltd.
    "CXW", # CoreCivic, Inc.
    "SASR", # SANDY SPRING BANCORP INC
    "RCKT", # ROCKET PHARMACEUTICALS, INC.
    "DOLE", # Dole plc
    "ORLA", # Orla Mining Ltd.
    "HMN", # HORACE MANN EDUCATORS CORP /DE/
    "WKC", # WORLD KINECT CORP
    "KRP", # Kimbell Royalty Partners, LP
    "SPHR", # Sphere Entertainment Co.
    "KN", # Knowles Corp
    "FOXF", # FOX FACTORY HOLDING CORP
    "SPT", # Sprout Social, Inc.
    "NWN", # Northwest Natural Holding Co
    "ZUO", # ZUORA INC
    "NGVT", # Ingevity Corp
    "NTCT", # NETSCOUT SYSTEMS INC
    "SONO", # Sonos Inc
    "AVDL", # AVADEL PHARMACEUTICALS PLC
    "FTRE", # Fortrea Holdings Inc.
    "HOPE", # HOPE BANCORP INC
    "ELME", # Elme Communities
    "SGML", # Sigma Lithium Corp
    "AFYA", # Afya Ltd
    "VITL", # Vital Farms, Inc.
    "XPRO", # EXPRO GROUP HOLDINGS N.V.
    "CTS", # CTS CORP
    "STEW", # SRH Total Return Fund, Inc.
    "WT", # WisdomTree, Inc.
    "CGAU", # Centerra Gold Inc.
    "KW", # Kennedy-Wilson Holdings, Inc.
    "NVEE", # NV5 Global, Inc.
    "NEXT", # NextDecade Corp.
    "HUT", # Hut 8 Corp.
    "SILV", # SilverCrest Metals Inc.
    "UMH", # UMH PROPERTIES, INC.
    "UCTT", # Ultra Clean Holdings, Inc.
    "DQ", # DAQO NEW ENERGY CORP.
    "KEN", # Kenon Holdings Ltd.
    "MMI", # Marcus & Millichap, Inc.
    "VBTX", # Veritex Holdings, Inc.
    "TLRY", # Tilray Brands, Inc.
    "BSTZ", # BlackRock Science & Technology Term Trust
    "PLAY", # Dave & Buster's Entertainment, Inc.
    "CUBI", # Customers Bancorp, Inc.
    "PRDO", # PERDOCEO EDUCATION Corp
    "PEB", # Pebblebrook Hotel Trust
    "SRCE", # 1ST SOURCE CORP
    "STBA", # S&T BANCORP INC
    "XNCR", # Xencor Inc
    "STEL", # Stellar Bancorp, Inc.
    "APLD", # Applied Digital Corp.
    "NN", # NEXTNAV INC.
    "COMM", # CommScope Holding Company, Inc.
    "AMN", # AMN HEALTHCARE SERVICES INC
    "JBGS", # JBG SMITH Properties
    "HELE", # HELEN OF TROY LTD
    "LADR", # Ladder Capital Corp
    "EDN", # EDENOR
    "DAWN", # Day One Biopharmaceuticals, Inc.
    "UTZ", # Utz Brands, Inc.
    "IART", # INTEGRA LIFESCIENCES HOLDINGS CORP
    "MTTR", # Matterport, Inc./DE
    "TWKS", # Thoughtworks Holding, Inc.
    "PLAB", # PHOTRONICS INC
    "GENI", # Genius Sports Ltd
    "MCRI", # MONARCH CASINO & RESORT INC
    "VET", # VERMILION ENERGY INC.
    "NTLA", # Intellia Therapeutics, Inc.
    "CRCT", # Cricut, Inc.
    "ASPN", # ASPEN AEROGELS INC
    "TCBK", # TRICO BANCSHARES /
    "HYT", # BLACKROCK CORPORATE HIGH YIELD FUND, INC.
    "CDRE", # Cadre Holdings, Inc.
    "DEA", # Easterly Government Properties, Inc.
    "AMWD", # AMERICAN WOODMARK CORP
    "ETG", # EATON VANCE TAX ADVANTAGED GLOBAL DIVIDEND INCOME FUND
    "UP", # Wheels Up Experience Inc.
    "BXMX", # Nuveen S&P 500 BuyWrite Income Fund
    "BLMN", # Bloomin' Brands, Inc.
    "GO", # Grocery Outlet Holding Corp.
    "RCUS", # Arcus Biosciences, Inc.
    "NSSC", # NAPCO SECURITY TECHNOLOGIES, INC
    "BUSE", # FIRST BUSEY CORP /NV/
    "HLX", # HELIX ENERGY SOLUTIONS GROUP INC
    "AHCO", # AdaptHealth Corp.
    "STAA", # STAAR SURGICAL CO
    "DAVA", # Endava plc
    "SPRY", # ARS Pharmaceuticals, Inc.
    "BTT", # BlackRock Municipal 2030 Target Term Trust
    "RLJ", # RLJ Lodging Trust
    "CSGS", # CSG SYSTEMS INTERNATIONAL INC
    "WABC", # WESTAMERICA BANCORPORATION
    "NX", # Quanex Building Products CORP
    "SCS", # STEELCASE INC
    "ARDX", # ARDELYX, INC.
    "ULCC", # Frontier Group Holdings, Inc.
    "ALEX", # Alexander & Baldwin, Inc.
    "EVO", # Evotec SE
    "DCBO", # Docebo Inc.
    "REVG", # REV Group, Inc.
    "BFS", # SAUL CENTERS, INC.
    "GEL", # GENESIS ENERGY LP
    "TPC", # TUTOR PERINI CORP
    "ELVN", # Enliven Therapeutics, Inc.
    "PGNY", # Progyny, Inc.
    "QCRH", # QCR HOLDINGS INC
    "BLBD", # Blue Bird Corp
    "ADEA", # Adeia Inc.
    "SBH", # Sally Beauty Holdings, Inc.
    "IRON", # Disc Medicine, Inc.
    "TV", # GRUPO TELEVISA, S.A.B.
    "TVTX", # Travere Therapeutics, Inc.
    "KRO", # KRONOS WORLDWIDE INC
    "OCSL", # Oaktree Specialty Lending Corp
    "BB", # BLACKBERRY Ltd
    "VRNT", # VERINT SYSTEMS INC
    "RBCAA", # REPUBLIC BANCORP INC /KY/
    "GIII", # G III APPAREL GROUP LTD /DE/
    "WINA", # WINMARK CORP
    "INMD", # InMode Ltd.
    "DSL", # DoubleLine Income Solutions Fund
    "CET", # CENTRAL SECURITIES CORP
    "BRDG", # Bridge Investment Group Holdings Inc.
    "FSCO", # FS Credit Opportunities Corp.
    "FLNG", # Flex LNG Ltd.
    "PHVS", # Pharvaris N.V.
    "GSG", # iShares S&P GSCI Commodity-Indexed Trust
    "FORTY", # FORMULA SYSTEMS (1985) LTD
    "BTDR", # Bitdeer Technologies Group
    "JKS", # JinkoSolar Holding Co., Ltd.
    "PSFE", # Paysafe Ltd
    "WLFC", # WILLIS LEASE FINANCE CORP
    "LNN", # LINDSAY CORP
    "PBI", # PITNEY BOWES INC /DE/
    "HLIT", # HARMONIC INC
    "THRM", # GENTHERM Inc
    "UVV", # UNIVERSAL CORP /VA/
    "SDGR", # Schrodinger, Inc.
    "COGT", # Cogent Biosciences, Inc.
    "RDFN", # Redfin Corp
    "WTTR", # Select Water Solutions, Inc.
    "MRTN", # MARTEN TRANSPORT LTD
    "IMAX", # IMAX CORP
    "GATO", # Gatos Silver, Inc.
    "KURA", # Kura Oncology, Inc.
    "MFA", # MFA FINANCIAL, INC.
    "LZ", # LEGALZOOM.COM, INC.
    "DMLP", # DORCHESTER MINERALS, L.P.
    "MFIC", # MidCap Financial Investment Corp
    "LOMA", # Loma Negra Compania Industrial Argentina Sociedad Anonima
    "NRP", # NATURAL RESOURCE PARTNERS LP
    "UNIT", # Uniti Group Inc.
    "DNOW", # DNOW Inc.
    "MOMO", # Hello Group Inc.
    "ACHR", # Archer Aviation Inc.
    "CNNE", # Cannae Holdings, Inc.
    "PRAX", # Praxis Precision Medicines, Inc.
    "PDM", # Piedmont Office Realty Trust, Inc.
    "BKD", # Brookdale Senior Living Inc.
    "VTEX", # VTEX
    "NMFC", # New Mountain Finance Corp
    "PX", # P10, Inc.
    "BMBL", # Bumble Inc.
    "CMPO", # CompoSecure, Inc.
    "WWW", # WOLVERINE WORLD WIDE INC /DE/
    "IE", # Ivanhoe Electric Inc.
    "OPEN", # Opendoor Technologies Inc.
    "SSRM", # SSR MINING INC.
    "BST", # BlackRock Science & Technology Trust
    "CSR", # CENTERSPACE
    "GAM", # GENERAL AMERICAN INVESTORS CO INC
    "ARI", # Apollo Commercial Real Estate Finance, Inc.
    "UNFI", # UNITED NATURAL FOODS INC
    "SABR", # Sabre Corp
    "CIM", # CHIMERA INVESTMENT CORP
    "INVA", # Innoviva, Inc.
    "ESTA", # ESTABLISHMENT LABS HOLDINGS INC.
    "USPH", # U S PHYSICAL THERAPY INC /NV
    "VSAT", # VIASAT INC
    "EIG", # Employers Holdings, Inc.
    "QQQX", # Nuveen NASDAQ 100 Dynamic Overwrite Fund
    "SAVA", # CASSAVA SCIENCES INC
    "RES", # RPC INC
    "NMZ", # NUVEEN MUNICIPAL HIGH INCOME OPPORTUNITY FUND
    "EXK", # ENDEAVOUR SILVER CORP
    "KARO", # Karooooo Ltd.
    "NTST", # NETSTREIT Corp.
    "GABC", # GERMAN AMERICAN BANCORP, INC.
    "LPG", # DORIAN LPG LTD.
    "LVWR", # LiveWire Group, Inc.
    "ANIP", # ANI PHARMACEUTICALS INC
    "SPH", # SUBURBAN PROPANE PARTNERS LP
    "BY", # BYLINE BANCORP, INC.
    "JELD", # JELD-WEN Holding, Inc.
    "IMKTA", # INGLES MARKETS INC
    "AIV", # APARTMENT INVESTMENT & MANAGEMENT CO
    "KALU", # KAISER ALUMINUM CORP
    "MSC", # STUDIO CITY INTERNATIONAL HOLDINGS Ltd
    "GDYN", # GRID DYNAMICS HOLDINGS, INC.
    "HCI", # HCI Group, Inc.
    "OLPX", # OLAPLEX HOLDINGS, INC.
    "TWO", # TWO HARBORS INVESTMENT CORP.
    "NFJ", # Virtus Dividend, Interest & Premium Strategy Fund
    "CRAI", # CRA INTERNATIONAL, INC.
    "UDMY", # Udemy, Inc.
    "DCOM", # Dime Community Bancshares, Inc. /NY/
    "ANGI", # Angi Inc.
    "BHLB", # BERKSHIRE HILLS BANCORP INC
    "EVV", # EATON VANCE LTD DURATION INCOME FUND
    "CDNA", # CareDx, Inc.
    "ARHS", # Arhaus, Inc.
    "AGRO", # Adecoagro S.A.
    "BLX", # FOREIGN TRADE BANK OF LATIN AMERICA, INC.
    "WOOF", # Petco Health & Wellness Company, Inc.
    "QNST", # QUINSTREET, INC
    "IDT", # IDT CORP
    "JFR", # NUVEEN FLOATING RATE INCOME FUND
    "PMT", # PennyMac Mortgage Investment Trust
    "ALX", # ALEXANDERS INC
    "SAFT", # SAFETY INSURANCE GROUP INC
    "TIGR", # UP Fintech Holding Ltd
    "UUUU", # ENERGY FUELS INC
    "NG", # NOVAGOLD RESOURCES INC
    "COHU", # COHU INC
    "ACMR", # ACM Research, Inc.
    "RC", # Ready Capital Corp
    "PGRE", # Paramount Group, Inc.
    "PHAT", # Phathom Pharmaceuticals, Inc.
    "SBGI", # Sinclair, Inc.
    "EOS", # Eaton Vance Enhanced Equity Income Fund II
    "ALGT", # Allegiant Travel CO
    "CSWC", # CAPITAL SOUTHWEST CORP
    "OXM", # OXFORD INDUSTRIES INC
    "MAX", # MediaAlpha, Inc.
    "INDV", # INDIVIOR PLC
    "EVRI", # Everi Holdings Inc.
    "FPF", # First Trust Intermediate Duration Preferred & Income Fund
    "ATSG", # Air Transport Services Group, Inc.
    "SII", # SPROTT INC.
    "GB", # Global Blue Group Holding AG
    "PFBC", # Preferred Bank
    "HY", # HYSTER-YALE, INC.
    "KRUS", # KURA SUSHI USA, INC.
    "AMPL", # Amplitude, Inc.
    "KFRC", # KFORCE INC
    "ATUS", # Altice USA, Inc.
    "PTA", # Cohen & Steers Tax-Advantaged Preferred Securities & Income Fund
    "TBLA", # Taboola.com Ltd.
    "TASK", # TaskUs, Inc.
    "PEBO", # PEOPLES BANCORP INC
    "AHH", # Armada Hoffler Properties, Inc.
    "ULH", # UNIVERSAL LOGISTICS HOLDINGS, INC.
    "DAN", # DANA INC
    "ATEC", # Alphatec Holdings, Inc.
    "SSTK", # Shutterstock, Inc.
    "COLL", # COLLEGIUM PHARMACEUTICAL, INC
    "PLYA", # Playa Hotels & Resorts N.V.
    "RNP", # COHEN & STEERS REIT & PREFERRED & INCOME FUND INC
    "PNTG", # Pennant Group, Inc.
    "COUR", # Coursera, Inc.
    "MXL", # MAXLINEAR, INC
    "TRS", # TRIMAS CORP
    "IRS", # IRSA INVESTMENTS & REPRESENTATIONS INC
    "PDFS", # PDF SOLUTIONS INC
    "MSEX", # MIDDLESEX WATER CO
    "ECPG", # ENCORE CAPITAL GROUP INC
    "REAX", # Real Brokerage Inc
    "AORT", # ARTIVION, INC.
    "PGRU", # PROPERTYGURU GROUP LTD
    "KRNT", # Kornit Digital Ltd.
    "TGI", # TRIUMPH GROUP INC
    "ATEN", # A10 Networks, Inc.
    "OCFC", # OCEANFIRST FINANCIAL CORP
    "MGPI", # MGP INGREDIENTS INC
    "BLFS", # BIOLIFE SOLUTIONS INC
    "IMTX", # Immatics N.V.
    "EH", # EHang Holdings Ltd
    "FBRT", # Franklin BSP Realty Trust, Inc.
    "XPEL", # XPEL, Inc.
    "ROOT", # Root, Inc.
    "NRDS", # NERDWALLET, INC.
    "BCSF", # Bain Capital Specialty Finance, Inc.
    "BORR", # Borr Drilling Ltd
    "MD", # Pediatrix Medical Group, Inc.
    "FIGS", # FIGS, Inc.
    "AGL", # agilon health, inc.
    "ASTL", # Algoma Steel Group Inc.
    "NVGS", # Navigator Holdings Ltd.
    "CBRL", # CRACKER BARREL OLD COUNTRY STORE, INC
    "EAI", # ENTERGY ARKANSAS, LLC
    "CARS", # Cars.com Inc.
    "NEXA", # Nexa Resources S.A.
    "HOV", # HOVNANIAN ENTERPRISES INC
    "FBMS", # FIRST BANCSHARES INC /MS/
    "EFC", # Ellington Financial Inc.
    "DGII", # DIGI INTERNATIONAL INC
    "PHR", # Phreesia, Inc.
    "OPK", # OPKO HEALTH, INC.
    "NYAX", # Nayax Ltd.
    "MRC", # MRC GLOBAL INC.
    "TIXT", # TELUS International (Cda) Inc.
    "ODP", # ODP Corp
    "ARR", # Armour Residential REIT, Inc.
    "AUPH", # Aurinia Pharmaceuticals Inc.
    "MUC", # BLACKROCK MUNIHOLDINGS CALIFORNIA QUALITY FUND, INC.
    "AMTD", # AMTD IDEA GROUP
    "CAL", # CALERES INC
    "DRD", # DRDGOLD LTD
    "AMSF", # AMERISAFE INC
    "FVRR", # Fiverr International Ltd.
    "ERII", # Energy Recovery, Inc.
    "FWRG", # First Watch Restaurant Group, Inc.
    "DESP", # Despegar.com, Corp.
    "VIR", # Vir Biotechnology, Inc.
    "IGIC", # International General Insurance Holdings Ltd.
    "VTLE", # Vital Energy, Inc.
    "JBI", # Janus International Group, Inc.
    "SDA", # SunCar Technology Group Inc.
    "AMAL", # Amalgamated Financial Corp.
    "SCSC", # SCANSOURCE, INC.
    "SHCO", # Soho House & Co Inc.
    "BBN", # BlackRock Taxable Municipal Bond Trust
    "TILE", # INTERFACE INC
    "GIC", # GLOBAL INDUSTRIAL Co
    "EOLS", # Evolus, Inc.
    "SKE", # Skeena Resources Ltd
    "BBDC", # Barings BDC, Inc.
    "IGMS", # IGM Biosciences, Inc.
    "WEAV", # Weave Communications, Inc.
    "DK", # Delek US Holdings, Inc.
    "XRX", # Xerox Holdings Corp
    "APLT", # Applied Therapeutics, Inc.
    "FWRD", # FORWARD AIR CORP
    "HEPS", # D-MARKET Electronic Services & Trading
    "BELFA", # BEL FUSE INC /NJ
    "ARRY", # Array Technologies, Inc.
    "BRKL", # BROOKLINE BANCORP INC
    "MDRX", # Veradigm Inc.
    "MDXG", # MIMEDX GROUP, INC.
    "FSLY", # Fastly, Inc.
    "SVM", # SILVERCORP METALS INC
    "BTZ", # BLACKROCK CREDIT ALLOCATION INCOME TRUST
    "IHS", # IHS Holding Ltd
    "HIMX", # Himax Technologies, Inc.
    "ADV", # Advantage Solutions Inc.
    "ARLO", # Arlo Technologies, Inc.
    "OBK", # Origin Bancorp, Inc.
    "OMI", # OWENS & MINOR INC/VA/
    "MTAL", # Metals Acquisition Ltd
    "PLSE", # PULSE BIOSCIENCES, INC.
    "SBSI", # SOUTHSIDE BANCSHARES INC
    "GRC", # GORMAN RUPP CO
    "NBXG", # Neuberger Berman Next Generation Connectivity Fund Inc.
    "BSIG", # BrightSphere Investment Group Inc.
    "VHI", # VALHI INC /DE/
    "MESO", # MESOBLAST LTD
    "CTOS", # Custom Truck One Source, Inc.
    "DX", # DYNEX CAPITAL INC
    "SEDG", # SOLAREDGE TECHNOLOGIES, INC.
    "RWT", # REDWOOD TRUST INC
    "BHRB", # Burke & Herbert Financial Services Corp.
    "ARQT", # Arcutis Biotherapeutics, Inc.
    "ARIS", # Aris Water Solutions, Inc.
    "BZH", # BEAZER HOMES USA INC
    "BBSI", # BARRETT BUSINESS SERVICES INC
    "XMTR", # Xometry, Inc.
    "VTOL", # Bristow Group Inc.
    "CSTL", # CASTLE BIOSCIENCES INC
    "AOSL", # ALPHA & OMEGA SEMICONDUCTOR Ltd
    "PRTA", # PROTHENA CORP PUBLIC LTD CO
    "ACDC", # ProFrac Holding Corp.
    "JACK", # JACK IN THE BOX INC
    "GOOS", # Canada Goose Holdings Inc.
    "CRF", # CORNERSTONE TOTAL RETURN FUND INC
    "GCT", # GigaCloud Technology Inc
    "PLYM", # Plymouth Industrial REIT, Inc.
    "NRK", # NUVEEN NEW YORK AMT-FREE QUALITY MUNICIPAL INCOME FUND
    "CTBI", # COMMUNITY TRUST BANCORP INC /KY/
    "PAHC", # PHIBRO ANIMAL HEALTH CORP
    "TMP", # TOMPKINS FINANCIAL CORP
    "UTL", # UNITIL CORP
    "CNOB", # ConnectOne Bancorp, Inc.
    "ZYME", # Zymeworks Inc.
    "AWF", # ALLIANCEBERNSTEIN GLOBAL HIGH INCOME FUND INC
    "ZIP", # ZIPRECRUITER, INC.
    "PRO", # PROS Holdings, Inc.
    "BFC", # Bank First Corp
    "CMCO", # COLUMBUS MCKINNON CORP
    "CAPR", # CAPRICOR THERAPEUTICS, INC.
    "ECC", # Eagle Point Credit Co Inc.
    "SCVL", # SHOE CARNIVAL INC
    "KIND", # Nextdoor Holdings, Inc.
    "FMBH", # FIRST MID BANCSHARES, INC.
    "JBSS", # SANFILIPPO JOHN B & SON INC
    "EVEX", # Eve Holding, Inc.
    "BXC", # BlueLinx Holdings Inc.
    "CSIQ", # Canadian Solar Inc.
    "SUPV", # Grupo Supervielle S.A.
    "ACEL", # Accel Entertainment, Inc.
    "YEXT", # Yext, Inc.
    "AOD", # abrdn Total Dynamic Dividend Fund
    "MEG", # Montrose Environmental Group, Inc.
    "CWH", # Camping World Holdings, Inc.
    "AMSC", # AMERICAN SUPERCONDUCTOR CORP /DE/
    "ETW", # Eaton Vance Tax-Managed Global Buy-Write Opportunities Fund
    "SHLS", # Shoals Technologies Group, Inc.
    "RLAY", # Relay Therapeutics, Inc.
    "AUTL", # Autolus Therapeutics plc
    "LQDA", # Liquidia Corp
    "HQH", # abrdn Healthcare Investors
    "TUYA", # Tuya Inc.
    "ICHR", # ICHOR HOLDINGS, LTD.
    "ETWO", # E2open Parent Holdings, Inc.
    "CHY", # CALAMOS CONVERTIBLE & HIGH INCOME FUND
    "AVAH", # Aveanna Healthcare Holdings, Inc.
    "RDWR", # RADWARE LTD
    "BLND", # Blend Labs, Inc.
    "CGEM", # Cullinan Therapeutics, Inc.
    "CINT", # CI&T Inc
    "UTI", # UNIVERSAL TECHNICAL INSTITUTE INC
    "TRNS", # TRANSCAT INC
    "AMTB", # Amerant Bancorp Inc.
    "CLB", # Core Laboratories Inc. /DE/
    "MQY", # BLACKROCK MUNIYIELD QUALITY FUND, INC.
    "MUI", # BLACKROCK MUNICIPAL INCOME FUND, INC.
    "BDN", # BRANDYWINE REALTY TRUST
    "PFC", # PREMIER FINANCIAL CORP
    "AMRK", # A-Mark Precious Metals, Inc.
    "SBR", # SABINE ROYALTY TRUST
    "THR", # Thermon Group Holdings, Inc.
    "MBUU", # MALIBU BOATS, INC.
    "CMTG", # Claros Mortgage Trust, Inc.
    "OEC", # Orion S.A.
    "HSTM", # HEALTHSTREAM INC
    "BITF", # Bitfarms Ltd
    "BVS", # Bioventus Inc.
    "VNET", # VNET Group, Inc.
    "NESR", # National Energy Services Reunited Corp.
    "DCO", # DUCOMMUN INC /DE/
    "PLRX", # PLIANT THERAPEUTICS, INC.
    "DDL", # Dingdong (Cayman) Ltd
    "PARR", # PAR PACIFIC HOLDINGS, INC.
    "CCB", # COASTAL FINANCIAL CORP
    "SXC", # SunCoke Energy, Inc.
    "DHC", # DIVERSIFIED HEALTHCARE TRUST
    "GES", # GUESS INC
    "LAC", # LITHIUM AMERICAS CORP.
    "CHI", # CALAMOS CONVERTIBLE OPPORTUNITIES & INCOME FUND
    "THQ", # abrdn Healthcare Opportunities Fund
    "GHLD", # Guild Holdings Co
    "CGBD", # Carlyle Secured Lending, Inc.
    "TYRA", # Tyra Biosciences, Inc.
    "SEAT", # Vivid Seats Inc.
    "BJRI", # BJs RESTAURANTS INC
    "FIP", # FTAI Infrastructure Inc.
    "VLRS", # Controladora Vuela Compania de Aviacion, S.A.B. de C.V.
    "HTZ", # HERTZ GLOBAL HOLDINGS, INC
    "LMB", # Limbach Holdings, Inc.
    "PGY", # Pagaya Technologies Ltd.
    "HTLD", # HEARTLAND EXPRESS INC
    "MATV", # Mativ Holdings, Inc.
    "AVNS", # AVANOS MEDICAL, INC.
    "CFFN", # Capitol Federal Financial, Inc.
    "SITC", # SITE Centers Corp.
    "AVO", # Mission Produce, Inc.
    "PDS", # PRECISION DRILLING Corp
    "TPB", # Turning Point Brands, Inc.
    "ETNB", # 89bio, Inc.
    "SLRC", # SLR Investment Corp.
    "DLX", # DELUXE CORP
    "CECO", # CECO ENVIRONMENTAL CORP
    "GOGO", # Gogo Inc.
    "GDEN", # GOLDEN ENTERTAINMENT, INC.
    "ENFN", # Enfusion, Inc.
    "GSL", # Global Ship Lease, Inc.
    "TTGT", # TechTarget Inc
    "MNRO", # MONRO, INC.
    "BASE", # Couchbase, Inc.
    "EEX", # Emerald Holding, Inc.
    "REPL", # Replimune Group, Inc.
    "CII", # BLACKROCK ENHANCED CAPITAL & INCOME FUND, INC.
    "PFLT", # PennantPark Floating Rate Capital Ltd.
    "EFXT", # Enerflex Ltd.
    "EYE", # National Vision Holdings, Inc.
    "EMBC", # Embecta Corp.
    "CAPL", # CrossAmerica Partners LP
    "CBL", # CBL & ASSOCIATES PROPERTIES INC
    "HTD", # JOHN HANCOCK TAX-ADVANTAGED DIVIDEND INCOME FUND
    "UVSP", # UNIVEST FINANCIAL Corp
    "SLN", # Silence Therapeutics plc
    "EOI", # Eaton Vance Enhanced Equity Income Fund
    "NOAH", # Noah Holdings Ltd
    "OLO", # Olo Inc.
    "IGR", # CBRE GLOBAL REAL ESTATE INCOME FUND
    "KREF", # KKR Real Estate Finance Trust Inc.
    "GPRE", # Green Plains Inc.
    "VVI", # VIAD CORP
    "PRAA", # PRA GROUP INC
    "CRON", # Cronos Group Inc.
    "HCSG", # HEALTHCARE SERVICES GROUP INC
    "PTLO", # Portillo's Inc.
    "MNTK", # Montauk Renewables, Inc.
    "EGBN", # EAGLE BANCORP INC
    "IMOS", # CHIPMOS TECHNOLOGIES INC
    "ABCL", # AbCellera Biologics Inc.
    "BRSP", # BrightSpire Capital, Inc.
    "GOTU", # Gaotu Techedu Inc.
    "HSII", # HEIDRICK & STRUGGLES INTERNATIONAL INC
    "PHK", # PIMCO HIGH INCOME FUND
    "PCN", # PIMCO CORPORATE & INCOME STRATEGY FUND
    "WLKP", # Westlake Chemical Partners LP
    "CATX", # Perspective Therapeutics, Inc.
    "SANA", # Sana Biotechnology, Inc.
    "HAIN", # HAIN CELESTIAL GROUP INC
    "INNV", # InnovAge Holding Corp.
    "VMEO", # Vimeo, Inc.
    "HFWA", # HERITAGE FINANCIAL CORP /WA/
    "REX", # REX AMERICAN RESOURCES Corp
    "CFB", # CROSSFIRST BANKSHARES, INC.
    "SKYH", # Sky Harbour Group Corp
    "IIIV", # i3 Verticals, Inc.
    "GSM", # Ferroglobe PLC
    "HUYA", # HUYA Inc.
    "DXPE", # DXP ENTERPRISES INC
    "ANNX", # Annexon, Inc.
    "WDI", # Western Asset Diversified Income Fund (WDI)
    "ECVT", # Ecovyst Inc.
    "ARKO", # ARKO Corp.
    "BFST", # Business First Bancshares, Inc.
    "GRNT", # Granite Ridge Resources, Inc.
    "FCBC", # FIRST COMMUNITY BANKSHARES INC /VA/
    "PRA", # PROASSURANCE CORP
    "GLDD", # Great Lakes Dredge & Dock CORP
    "TIPT", # TIPTREE INC.
    "HAYN", # HAYNES INTERNATIONAL INC
    "JQC", # Nuveen Credit Strategies Income Fund
    "AIO", # Virtus Artificial Intelligence & Technology Opportunities Fund
    "FFC", # Flaherty & Crumrine PREFERRED & INCOME SECURITIES FUND INC
    "SPLP", # STEEL PARTNERS HOLDINGS L.P.
    "SHEN", # SHENANDOAH TELECOMMUNICATIONS CO/VA/
    "HLF", # HERBALIFE LTD.
    "BCX", # BlackRock Resources & Commodities Strategy Trust
    "TREE", # LendingTree, Inc.
    "ASIX", # AdvanSix Inc.
    "TK", # TEEKAY CORP LTD
    "PCRX", # Pacira BioSciences, Inc.
    "MCBS", # MetroCity Bankshares, Inc.
    "MLR", # MILLER INDUSTRIES INC /TN/
    "UXIN", # Uxin Ltd
    "RSKD", # RISKIFIED LTD.
    "DLY", # DoubleLine Yield Opportunities Fund
    "STKL", # SunOpta Inc.
    "TH", # Target Hospitality Corp.
    "AC", # Associated Capital Group, Inc.
    "RPAY", # Repay Holdings Corp
    "WNC", # WABASH NATIONAL Corp
    "OSBC", # OLD SECOND BANCORP INC
    "MYI", # BLACKROCK MUNIYIELD QUALITY FUND III, INC.
    "SCWX", # SecureWorks Corp
    "ERAS", # Erasca, Inc.
    "EIM", # EATON VANCE MUNICIPAL BOND FUND
    "SNCY", # Sun Country Airlines Holdings, Inc.
    "DSP", # Viant Technology Inc.
    "CPF", # CENTRAL PACIFIC FINANCIAL CORP
    "SWIM", # Latham Group, Inc.
    "TRIN", # Trinity Capital Inc.
    "VTS", # Vitesse Energy, Inc.
    "RA", # Brookfield Real Assets Income Fund Inc.
    "NUVB", # Nuvation Bio Inc.
    "ORRF", # ORRSTOWN FINANCIAL SERVICES INC
    "PUMP", # ProPetro Holding Corp.
    "ADPT", # Adaptive Biotechnologies Corp
    "ASTE", # ASTEC INDUSTRIES INC
    "ABUS", # Arbutus Biopharma Corp
    "ADSE", # Ads-Tec Energy Public Ltd Co
    "PUBM", # PubMatic, Inc.
    "LAB", # STANDARD BIOTOOLS INC.
    "MEGI", # NYLI CBRE Global Infrastructure Megatrends Term Fund
    "EU", # enCore Energy Corp.
    "TXO", # TXO Partners, L.P.
    "CCO", # Clear Channel Outdoor Holdings, Inc.
    "IMNM", # Immunome Inc.
    "KELYA", # KELLY SERVICES INC
    "SPTN", # SpartanNash Co
    "MATW", # MATTHEWS INTERNATIONAL CORP
    "OCS", # Oculis Holding AG
    "TRTX", # TPG RE Finance Trust, Inc.
    "HBNC", # HORIZON BANCORP INC /IN/
    "BALY", # Bally's Corp
    "KOP", # Koppers Holdings Inc.
    "USNA", # USANA HEALTH SCIENCES INC
    "LXRX", # LEXICON PHARMACEUTICALS, INC.
    "NBR", # NABORS INDUSTRIES LTD
    "NXP", # NUVEEN SELECT TAX FREE INCOME PORTFOLIO
    "MBWM", # MERCANTILE BANK CORP
    "SMWB", # SIMILARWEB LTD.
    "DBA", # INVESCO DB AGRICULTURE FUND
    "ETD", # ETHAN ALLEN INTERIORS INC
    "SCHL", # SCHOLASTIC CORP
    "HAFC", # HANMI FINANCIAL CORP
    "RYI", # Ryerson Holding Corp
    "IBCP", # INDEPENDENT BANK CORP /MI/
    "WSR", # Whitestone REIT
    "NOVA", # Sunnova Energy International Inc.
    "PAXS", # PIMCO Access Income Fund
    "SMP", # STANDARD MOTOR PRODUCTS, INC.
    "GCI", # Gannett Co., Inc.
    "KC", # Kingsoft Cloud Holdings Ltd
    "TCPC", # BlackRock TCP Capital Corp.
    "NCMI", # National CineMedia, Inc.
    "PRLB", # Proto Labs Inc
    "HBT", # HBT Financial, Inc.
    "GOOD", # GLADSTONE COMMERCIAL CORP
    "BGS", # B&G Foods, Inc.
    "DDI", # DoubleDown Interactive Co., Ltd.
    "NAT", # NORDIC AMERICAN TANKERS Ltd
    "AACT", # Ares Acquisition Corp II
    "UAN", # CVR PARTNERS, LP
    "FAX", # ABRDN ASIA-PACIFIC INCOME FUND, INC.
    "LDI", # loanDepot, Inc.
    "OPT", # Opthea Ltd
    "HCKT", # HACKETT GROUP, INC.
    "GSBC", # GREAT SOUTHERN BANCORP, INC.
    "BOE", # BlackRock Enhanced Global Dividend Trust
    "SMBC", # SOUTHERN MISSOURI BANCORP, INC.
    "CCAP", # Crescent Capital BDC, Inc.
    "INN", # Summit Hotel Properties, Inc.
    "GGN", # GAMCO Global Gold, Natural Resources & Income Trust
    "WRLD", # WORLD ACCEPTANCE CORP
    "DJCO", # DAILY JOURNAL CORP
    "VMO", # Invesco Municipal Opportunity Trust
    "CVLG", # COVENANT LOGISTICS GROUP, INC.
    "GNK", # GENCO SHIPPING & TRADING LTD
    "ANAB", # ANAPTYSBIO, INC
    "AXL", # AMERICAN AXLE & MANUFACTURING HOLDINGS INC
    "LPRO", # Open Lending Corp
    "BTO", # JOHN HANCOCK FINANCIAL OPPORTUNITIES FUND
    "IFN", # INDIA FUND, INC.
    "EOSE", # Eos Energy Enterprises, Inc.
    "CRSR", # Corsair Gaming, Inc.
    "DOGZ", # Dogness (International) Corp
    "CRESY", # CRESUD INC
    "HZO", # MARINEMAX INC
    "ORIC", # Oric Pharmaceuticals, Inc.
    "EQBK", # EQUITY BANCSHARES INC
    "NVRI", # ENVIRI Corp
    "WLDN", # Willdan Group, Inc.
    "PFN", # PIMCO Income Strategy Fund II
    "LQDT", # LIQUIDITY SERVICES INC
    "YALA", # Yalla Group Ltd
    "NPWR", # NET Power Inc.
    "DMRC", # Digimarc CORP
    "STRW", # Strawberry Fields REIT, Inc.
    "FSBC", # FIVE STAR BANCORP
    "ATXS", # Astria Therapeutics, Inc.
    "OLMA", # Olema Pharmaceuticals, Inc.
    "MLYS", # Mineralys Therapeutics, Inc.
    "CTLP", # CANTALOUPE, INC.
    "GDEV", # GDEV Inc.
    "STOK", # Stoke Therapeutics, Inc.
    "TGB", # TASEKO MINES LTD
    "RGR", # STURM RUGER & CO INC
    "FLGT", # Fulgent Genetics, Inc.
    "PL", # Planet Labs PBC
    "PPTA", # PERPETUA RESOURCES CORP.
    "CTKB", # Cytek Biosciences, Inc.
    "YMAB", # Y-mAbs Therapeutics, Inc.
    "IRWD", # IRONWOOD PHARMACEUTICALS INC
    "EVER", # EverQuote, Inc.
    "FDUS", # FIDUS INVESTMENT Corp
    "KIDS", # ORTHOPEDIATRICS CORP
    "MREO", # Mereo BioPharma Group plc
    "CDMO", # Avid Bioservices, Inc.
    "CCD", # Calamos Dynamic Convertible & Income Fund
    "TRDA", # Entrada Therapeutics, Inc.
    "AAOI", # APPLIED OPTOELECTRONICS, INC.
    "ABL", # Abacus Life, Inc.
    "FNKO", # Funko, Inc.
    "EXAI", # Exscientia plc
    "IPX", # IPERIONX Ltd
    "TEN", # TSAKOS ENERGY NAVIGATION LTD
    "NDMO", # Nuveen Dynamic Municipal Opportunities Fund
    "NIE", # Virtus Equity & Convertible Income Fund
    "MHD", # BLACKROCK MUNIHOLDINGS FUND, INC.
    "OSPN", # OneSpan Inc.
    "TRST", # TRUSTCO BANK CORP N Y
    "CLNE", # Clean Energy Fuels Corp.
    "OPAL", # OPAL Fuels Inc.
    "VEL", # Velocity Financial, Inc.
    "IRMD", # IRADIMED CORP
    "BHK", # BLACKROCK CORE BOND TRUST
    "PDT", # JOHN HANCOCK PREMIUM DIVIDEND FUND
    "HPP", # Hudson Pacific Properties, Inc.
    "EZPW", # EZCORP INC
    "TSAT", # Telesat Corp
    "NGVC", # Natural Grocers by Vitamin Cottage, Inc.
    "RBBN", # Ribbon Communications Inc.
    "CVAC", # CureVac N.V.
    "HUMA", # Humacyte, Inc.
    "EYPT", # EyePoint Pharmaceuticals, Inc.
    "NKX", # NUVEEN CALIFORNIA AMT-FREE QUALITY MUNICIPAL INCOME FUND
    "CION", # CION Investment Corp
    "AXGN", # Axogen, Inc.
    "CAC", # CAMDEN NATIONAL CORP
    "MUJ", # BLACKROCK MUNIHOLDINGS NEW JERSEY QUALITY FUND, INC.
    "MLAB", # MESA LABORATORIES INC /CO/
    "ETJ", # Eaton Vance Risk-Managed Diversified Equity Income Fund
    "ECX", # ECARX Holdings Inc.
    "NTGR", # NETGEAR, INC.
    "OFIX", # Orthofix Medical Inc.
    "MOFG", # MidWestOne Financial Group, Inc.
    "HKD", # AMTD Digital Inc.
    "GDOT", # GREEN DOT CORP
    "LASR", # NLIGHT, INC.
    "RVNC", # Revance Therapeutics, Inc.
    "DAKT", # DAKTRONICS INC /SD/
    "ATRO", # ASTRONICS CORP
    "MCB", # Metropolitan Bank Holding Corp.
    "LEGH", # Legacy Housing Corp
    "MCS", # MARCUS CORP
    "FPH", # Five Point Holdings, LLC
    "XPOF", # Xponential Fitness, Inc.
    "NMCO", # Nuveen Municipal Credit Opportunities Fund
    "ATEX", # Anterix Inc.
    "LDP", # Cohen & Steers Ltd Duration Preferred & Income Fund, Inc.
    "DAO", # Youdao, Inc.
    "HTBK", # HERITAGE COMMERCE CORP
    "GMRE", # Global Medical REIT Inc.
    "PLPC", # PREFORMED LINE PRODUCTS CO
    "PEO", # ADAMS NATURAL RESOURCES FUND, INC.
    "CCBG", # CAPITAL CITY BANK GROUP INC
    "ORC", # Orchid Island Capital, Inc.
    "VVR", # Invesco Senior Income Trust
    "WASH", # WASHINGTON TRUST BANCORP INC
    "SVRA", # Savara Inc
    "TNGX", # Tango Therapeutics, Inc.
    "INDI", # indie Semiconductor, Inc.
    "OPY", # OPPENHEIMER HOLDINGS INC
    "WEST", # Westrock Coffee Co
    "GTN", # GRAY TELEVISION INC
    "CNDT", # CONDUENT Inc
    "CTO", # CTO Realty Growth, Inc.
    "LXU", # LSB INDUSTRIES, INC.
    "HTBI", # HomeTrust Bancshares, Inc.
    "ALTI", # AlTi Global, Inc.
    "PML", # PIMCO MUNICIPAL INCOME FUND II
    "ASC", # Ardmore Shipping Corp
    "IIM", # Invesco Value Municipal Income Trust
    "FPI", # Farmland Partners Inc.
    "SIBN", # SI-BONE, Inc.
    "SWBI", # SMITH & WESSON BRANDS, INC.
    "PGC", # PEAPACK GLADSTONE FINANCIAL CORP
    "AVXL", # ANAVEX LIFE SCIENCES CORP.
    "TERN", # Terns Pharmaceuticals, Inc.
    "NR", # NEWPARK RESOURCES INC
    "PACB", # PACIFIC BIOSCIENCES OF CALIFORNIA, INC.
    "HIPO", # Hippo Holdings Inc.
    "OLP", # ONE LIBERTY PROPERTIES INC
    "CRMD", # CorMedix Inc.
    "UVE", # UNIVERSAL INSURANCE HOLDINGS, INC.
    "FUBO", # fuboTV Inc. /FL
    "INOD", # INNODATA INC
    "THRD", # Third Harmonic Bio, Inc.
    "CASS", # CASS INFORMATION SYSTEMS INC
    "IMXI", # International Money Express, Inc.
    "PHAR", # Pharming Group N.V.
    "REPX", # Riley Exploration Permian, Inc.
    "CELC", # Celcuity Inc.
    "BIT", # BlackRock Multi-Sector Income Trust
    "HSAI", # Hesai Group
    "EMD", # WESTERN ASSET EMERGING MARKETS DEBT FUND INC.
    "CSV", # CARRIAGE SERVICES INC
    "CYH", # COMMUNITY HEALTH SYSTEMS INC
    "MMU", # WESTERN ASSET MANAGED MUNICIPALS FUND INC.
    "BTBT", # Bit Digital, Inc
    "FFWM", # First Foundation Inc.
    "OPFI", # OppFi Inc.
    "ESQ", # Esquire Financial Holdings, Inc.
    "SMBK", # SMARTFINANCIAL INC.
    "MGIC", # MAGIC SOFTWARE ENTERPRISES LTD
    "VKQ", # Invesco Municipal Trust
    "SPFI", # SOUTH PLAINS FINANCIAL, INC.
    "VGM", # Invesco Trust for Investment Grade Municipals
    "SNDL", # SNDL Inc.
    "VZLA", # Vizsla Silver Corp.
    "UHT", # UNIVERSAL HEALTH REALTY INCOME TRUST
    "JMIA", # Jumia Technologies AG
    "AMPS", # Altus Power, Inc.
    "FRPH", # FRP HOLDINGS, INC.
    "SLP", # Simulations Plus, Inc.
    "CEVA", # CEVA INC
    "RSVR", # Reservoir Media, Inc.
    "TBLD", # Thornburg Income Builder Opportunities Trust
    "GEVO", # Gevo, Inc.
    "EGY", # VAALCO ENERGY INC /DE/
    "CRVS", # Corvus Pharmaceuticals, Inc.
    "CPAC", # CEMENTOS PACASMAYO SAA
    "BGY", # BlackRock Enhanced International Dividend Trust
    "SLRN", # ACELYRIN, Inc.
    "CNSL", # Consolidated Communications Holdings, Inc.
    "ATLC", # Atlanticus Holdings Corp
    "BGB", # Blackstone Strategic Credit 2027 Term Fund
    "ALLO", # Allogene Therapeutics, Inc.
    "BME", # BlackRock Health Sciences Trust
    "EMO", # ClearBridge Energy Midstream Opportunity Fund Inc.
    "GLUE", # Monte Rosa Therapeutics, Inc.
    "VREX", # Varex Imaging Corp
    "VINP", # Vinci Partners Investments Ltd.
    "STK", # Columbia Seligman Premium Technology Growth Fund, Inc.
    "BAND", # Bandwidth Inc.
    "KRT", # Karat Packaging Inc.
    "RXT", # Rackspace Technology, Inc.
    "FTHY", # FIRST TRUST HIGH YIELD OPPORTUNITIES 2027 TERM FUND
    "AMBC", # AMBAC FINANCIAL GROUP INC
    "CCNE", # CNB FINANCIAL CORP/PA
    "CLCO", # Cool Co Ltd.
    "METC", # Ramaco Resources, Inc.
    "SVC", # Service Properties Trust
    "WIW", # WESTERN ASSET INFLATION-LINKED OPPORTUNITIES & INCOME FUND
    "SRDX", # SURMODICS INC
    "OFLX", # Omega Flex, Inc.
    "MYTE", # MYT Netherlands Parent B.V.
    "MSBI", # Midland States Bancorp, Inc.
    "CHCT", # Community Healthcare Trust Inc
    "HONE", # HarborOne Bancorp, Inc.
    "IQI", # Invesco Quality Municipal Income Trust
    "EBF", # ENNIS, INC.
    "LRMR", # Larimar Therapeutics, Inc.
    "DIAX", # Nuveen Dow 30sm Dynamic Overwrite Fund
    "MPB", # MID PENN BANCORP INC
    "ITRN", # Ituran Location & Control Ltd.
    "RYAM", # RAYONIER ADVANCED MATERIALS INC.
    "IIIN", # INSTEEL INDUSTRIES INC
    "CHPT", # ChargePoint Holdings, Inc.
    "NGL", # NGL Energy Partners LP
    "TALK", # Talkspace, Inc.
    "FLWS", # 1 800 FLOWERS COM INC
    "GLAD", # GLADSTONE CAPITAL CORP
    "URGN", # UroGen Pharma Ltd.
    "RERE", # ATRenew Inc.
    "BUI", # BlackRock Utilities, Infrastructure & Power Opportunities Trust
    "NYMT", # NEW YORK MORTGAGE TRUST INC
    "NOA", # North American Construction Group Ltd.
    "PLOW", # DOUGLAS DYNAMICS, INC
    "FMNB", # FARMERS NATIONAL BANC CORP /OH/
    "FC", # FRANKLIN COVEY CO
    "BBW", # BUILD-A-BEAR WORKSHOP INC
    "SIGA", # SIGA TECHNOLOGIES INC
    "LZM", # Lifezone Metals Ltd
    "CMP", # COMPASS MINERALS INTERNATIONAL INC
    "GUG", # Guggenheim Active Allocation Fund
    "ALRS", # ALERUS FINANCIAL CORP
    "CLFD", # Clearfield, Inc.
    "HPS", # JOHN HANCOCK PREFERRED INCOME FUND III
    "LX", # LexinFintech Holdings Ltd.
    "GHY", # PGIM Global High Yield Fund, Inc.
    "BLE", # BLACKROCK MUNICIPAL INCOME TRUST II
    "CGC", # Canopy Growth Corp
    "THFF", # FIRST FINANCIAL CORP /IN/
    "SSYS", # STRATASYS LTD.
    "LIND", # LINDBLAD EXPEDITIONS HOLDINGS, INC.
    "NPK", # NATIONAL PRESTO INDUSTRIES INC
    "PACK", # Ranpak Holdings Corp.
    "THRY", # Thryv Holdings, Inc.
    "NXJ", # NUVEEN NEW JERSEY QUALITY MUNICIPAL INCOME FUND
    "DSU", # BLACKROCK DEBT STRATEGIES FUND, INC.
    "NFBK", # Northfield Bancorp, Inc.
    "PBT", # PERMIAN BASIN ROYALTY TRUST
    "YORW", # YORK WATER CO
    "DGICA", # DONEGAL GROUP INC
    "BLW", # BLACKROCK Ltd DURATION INCOME TRUST
    "RDW", # Redwire Corp
    "SNDA", # SONIDA SENIOR LIVING, INC.
    "UFCS", # UNITED FIRE GROUP INC
    "LESL", # Leslie's, Inc.
    "YRD", # Yiren Digital Ltd.
    "AQST", # Aquestive Therapeutics, Inc.
    "QTRX", # Quanterix Corp
    "BHB", # BAR HARBOR BANKSHARES
    "MYD", # BLACKROCK MUNIYIELD FUND, INC.
    "GAIN", # GLADSTONE INVESTMENT CORPORATIONDE
    "AURA", # Aura Biosciences, Inc.
    "ODC", # Oil-Dri Corp of America
    "MUX", # McEwen Mining Inc.
    "ASGI", # abrdn Global Infrastructure Income Fund
    "LE", # LANDS' END, INC.
    "VCV", # Invesco California Value Municipal Income Trust
    "PRTC", # PureTech Health plc
    "ASPI", # ASP Isotopes Inc.
    "GCBC", # GREENE COUNTY BANCORP INC
    "LVRO", # Lavoro Ltd
    "SHBI", # SHORE BANCSHARES INC
    "DH", # Definitive Healthcare Corp.
    "DAVE", # Dave Inc./DE
    "LYTS", # LSI INDUSTRIES INC
    "OTLY", # Oatly Group AB
    "ADTN", # ADTRAN Holdings, Inc.
    "FRA", # BLACKROCK FLOATING RATE INCOME STRATEGIES FUND, INC.
    "AROW", # ARROW FINANCIAL CORP
    "ARCT", # Arcturus Therapeutics Holdings Inc.
    "GLRE", # GREENLIGHT CAPITAL RE, LTD.
    "VERV", # Verve Therapeutics, Inc.
    "LUNR", # Intuitive Machines, Inc.
    "NNDM", # Nano Dimension Ltd.
    "PKST", # Peakstone Realty Trust
    "HPI", # JOHN HANCOCK PREFERRED INCOME FUND
    "VALN", # Valneva SE
    "OABI", # OmniAb, Inc.
    "UIS", # UNISYS CORP
    "PFIS", # PEOPLES FINANCIAL SERVICES CORP.
    "ALEC", # Alector, Inc.
    "NBB", # Nuveen Taxable Municipal Income Fund
    "XERS", # Xeris Biopharma Holdings, Inc.
    "CVGW", # CALAVO GROWERS INC
    "EBS", # Emergent BioSolutions Inc.
    "ACCO", # ACCO BRANDS Corp
    "HCAT", # Health Catalyst, Inc.
    "RMT", # ROYCE MICRO-CAP TRUST, INC.
    "BWMX", # BETTERWARE DE MEXICO, S.A.P.I. DE C.V
    "LAND", # GLADSTONE LAND Corp
    "CYD", # CHINA YUCHAI INTERNATIONAL LTD
    "BLDP", # Ballard Power Systems Inc.
    "THW", # abrdn World Healthcare Fund
    "DIN", # Dine Brands Global, Inc.
    "ALT", # Altimmune, Inc.
    "NML", # Neuberger Berman Energy Infrastructure & Income Fund Inc.
    "LMNR", # Limoneira CO
    "CLMB", # Climb Global Solutions, Inc.
    "SOHU", # Sohu.com Ltd
    "ML", # MONEYLION INC.
    "AGS", # PlayAGS, Inc.
    "PRME", # Prime Medicine, Inc.
    "BOC", # BOSTON OMAHA Corp
    "ISD", # PGIM High Yield Bond Fund, Inc.
    "SKYT", # SkyWater Technology, Inc
    "MMD", # NYLI MacKay DefinedTerm Muni Opportunities Fund
    "MNMD", # Mind Medicine (MindMed) Inc.
    "CGNT", # Cognyte Software Ltd.
    "BCAL", # California BanCorp CA
    "GBLI", # Global Indemnity Group, LLC
    "FFIC", # FLUSHING FINANCIAL CORP
    "KRNY", # Kearny Financial Corp.
    "VALU", # VALUE LINE INC
    "ACTG", # ACACIA RESEARCH CORP
    "URG", # UR-ENERGY INC
    "IONR", # ioneer Ltd
    "LOVE", # Lovesac Co
    "ABSI", # Absci Corp
    "QD", # Qudian Inc.
    "NPFD", # Nuveen Variable Rate Preferred & Income Fund
    "PNNT", # PENNANTPARK INVESTMENT CORP
    "MVF", # BLACKROCK MUNIVEST FUND, INC.
    "TCBX", # Third Coast Bancshares, Inc.
    "WALD", # Waldencast plc
    "ITIC", # INVESTORS TITLE CO
    "LSAK", # LESAKA TECHNOLOGIES INC
    "NVTS", # Navitas Semiconductor Corp
    "IVR", # Invesco Mortgage Capital Inc.
    "MUA", # BLACKROCK MUNIASSETS FUND, INC.
    "BFK", # BLACKROCK MUNICIPAL INCOME TRUST
    "MYE", # MYERS INDUSTRIES INC
    "SB", # SAFE BULKERS, INC.
    "NQP", # NUVEEN PENNSYLVANIA QUALITY MUNICIPAL INCOME FUND
    "KE", # Kimball Electronics, Inc.
    "KALV", # KalVista Pharmaceuticals, Inc.
    "NWPX", # NORTHWEST PIPE CO
    "SHYF", # SHYFT GROUP, INC.
    "GRVY", # GRAVITY Co., Ltd.
    "EAF", # GRAFTECH INTERNATIONAL LTD
    "CHW", # Calamos Global Dynamic Income Fund
    "HIVE", # HIVE Digital Technologies Ltd.
    "TTI", # TETRA TECHNOLOGIES INC
    "DPG", # Duff & Phelps Utility & Infrastructure Fund Inc.
    "DADA", # Dada Nexus Ltd
    "ZVRA", # ZEVRA THERAPEUTICS, INC.
    "FNA", # Paragon 28, Inc.
    "NFGC", # New Found Gold Corp.
    "HNRG", # HALLADOR ENERGY CO
    "HOUS", # Anywhere Real Estate Inc.
    "MGTX", # MeiraGTx Holdings plc
    "SLI", # STANDARD LITHIUM LTD.
    "MLP", # MAUI LAND & PINEAPPLE CO INC
    "MERC", # MERCER INTERNATIONAL INC.
    "TYG", # TORTOISE ENERGY INFRASTRUCTURE CORP
    "GPRK", # GeoPark Ltd
    "GAU", # Galiano Gold Inc.
    "NRC", # NATIONAL RESEARCH CORP
    "SENEA", # Seneca Foods Corp
    "OBE", # OBSIDIAN ENERGY LTD.
    "CARE", # Carter Bankshares, Inc.
    "EWCZ", # European Wax Center, Inc.
    "TRC", # TEJON RANCH CO
    "CCSI", # Consensus Cloud Solutions, Inc.
    "VLGEA", # VILLAGE SUPER MARKET INC
    "IGD", # Voya GLOBAL EQUITY DIVIDEND & PREMIUM OPPORTUNITY FUND
    "GNE", # Genie Energy Ltd.
    "PSTL", # Postal Realty Trust, Inc.
    "GHRS", # GH Research PLC
    "MEC", # Mayville Engineering Company, Inc.
    "RGNX", # REGENXBIO Inc.
    "WOW", # WideOpenWest, Inc.
    "CBNK", # Capital Bancorp Inc
    "DHIL", # DIAMOND HILL INVESTMENT GROUP INC
    "DNA", # Ginkgo Bioworks Holdings, Inc.
    "ETB", # Eaton Vance Tax-Managed Buy-Write Income Fund
    "NMAI", # Nuveen Multi-Asset Income Fund
    "XPER", # Xperi Inc.
    "TWI", # TITAN INTERNATIONAL INC
    "FDMT", # 4D Molecular Therapeutics, Inc.
    "FHTX", # Foghorn Therapeutics Inc.
    "RDVT", # Red Violet, Inc.
    "ASA", # ASA Gold & Precious Metals Ltd
    "DFP", # Flaherty & Crumrine Dynamic Preferred & Income Fund Inc
    "PRTH", # Priority Technology Holdings, Inc.
    "WDH", # Waterdrop Inc.
    "ETO", # Eaton Vance Tax-Advantaged Global Dividend Opportunities Fund
    "LINC", # LINCOLN EDUCATIONAL SERVICES CORP
    "EVN", # EATON VANCE MUNICIPAL INCOME TRUST
    "HYLN", # Hyliion Holdings Corp.
    "BSRR", # SIERRA BANCORP
    "AEHR", # AEHR TEST SYSTEMS
    "BIGC", # BigCommerce Holdings, Inc.
    "SD", # SANDRIDGE ENERGY INC
    "GBAB", # Guggenheim Taxable Municipal Bond & Investment Grade Debt Trust
    "GRPN", # Groupon, Inc.
    "SDHY", # PGIM Short Duration High Yield Opportunities Fund
    "CLW", # Clearwater Paper Corp
    "MOV", # MOVADO GROUP INC
    "LND", # BrasilAgro - Brazilian Agricultural Real Estate Co
    "TBPH", # Theravance Biopharma, Inc.
    "USAP", # UNIVERSAL STAINLESS & ALLOY PRODUCTS INC
    "BIOX", # Bioceres Crop Solutions Corp.
    "DBO", # Invesco DB Oil Fund
    "COOK", # Traeger, Inc.
    "RMR", # RMR GROUP INC.
    "IAUX", # i-80 Gold Corp.
    "ESPR", # Esperion Therapeutics, Inc.
    "MCI", # BARINGS CORPORATE INVESTORS
    "BWB", # Bridgewater Bancshares Inc
    "EBTC", # ENTERPRISE BANCORP INC /MA/
    "HQL", # abrdn Life Sciences Investors
    "CLDT", # Chatham Lodging Trust
    "EAD", # ALLSPRING INCOME OPPORTUNITIES FUND
    "RBB", # RBB Bancorp
    "HBB", # Hamilton Beach Brands Holding Co
    "ZEUS", # OLYMPIC STEEL INC
    "VKI", # Invesco Advantage Municipal Income Trust II
    "MITK", # MITEK SYSTEMS INC
    "FFA", # FIRST TRUST ENHANCED EQUITY INCOME FUND
    "BYND", # BEYOND MEAT, INC.
    "DDD", # 3D SYSTEMS CORP
    "BSVN", # Bank7 Corp.
    "SFIX", # Stitch Fix, Inc.
    "HIX", # WESTERN ASSET HIGH INCOME FUND II INC.
    "LAZR", # Luminar Technologies, Inc./DE
    "ZUMZ", # Zumiez Inc
    "PKOH", # PARK OHIO HOLDINGS CORP
    "RMAX", # RE/MAX Holdings, Inc.
    "LEO", # BNY MELLON STRATEGIC MUNICIPALS, INC.
    "MYN", # BLACKROCK MUNIYIELD NEW YORK QUALITY FUND, INC.
    "SGU", # STAR GROUP, L.P.
    "AVK", # ADVENT CONVERTIBLE & INCOME FUND
    "UNTY", # UNITY BANCORP INC /NJ/
    "LWAY", # Lifeway Foods, Inc.
    "BBAI", # BigBear.ai Holdings, Inc.
    "RICK", # RCI HOSPITALITY HOLDINGS, INC.
    "RWAY", # Runway Growth Finance Corp.
    "CCRN", # CROSS COUNTRY HEALTHCARE INC
    "LWLG", # Lightwave Logic, Inc.
    "PERI", # Perion Network Ltd.
    "VBNK", # VersaBank
    "LXFR", # LUXFER HOLDINGS PLC
    "HBCP", # HOME BANCORP, INC.
    "MXCT", # MAXCYTE, INC.
    "GUT", # GABELLI UTILITY TRUST
    "HPF", # JOHN HANCOCK PREFERRED INCOME FUND II
    "YSG", # Yatsen Holding Ltd
    "BRY", # Berry Corp (bry)
    "CWCO", # Consolidated Water Co. Ltd.
    "KTF", # DWS MUNICIPAL INCOME TRUST
    "XFLT", # XAI Octagon Floating Rate & Alternative Income Trust
    "KODK", # EASTMAN KODAK CO
    "BFLY", # Butterfly Network, Inc.
    "KIO", # KKR Income Opportunities Fund
    "FMAO", # FARMERS & MERCHANTS BANCORP INC
    "NL", # NL INDUSTRIES INC
    "LSEA", # Landsea Homes Corp
    "CURV", # Torrid Holdings Inc.
    "FISI", # FINANCIAL INSTITUTIONS INC
    "ZIMV", # ZimVie Inc.
    "HIO", # WESTERN ASSET HIGH INCOME OPPORTUNITY FUND INC.
    "SAGE", # Sage Therapeutics, Inc.
    "CVEO", # Civeo Corp
    "GNTY", # GUARANTY BANCSHARES INC /TX/
    "ZH", # Zhihu Inc.
    "HFRO", # HIGHLAND OPPORTUNITIES & INCOME FUND
    "CCCC", # C4 Therapeutics, Inc.
    "HNST", # Honest Company, Inc.
    "ORGO", # Organogenesis Holdings Inc.
    "SGMO", # SANGAMO THERAPEUTICS, INC
    "EFR", # EATON VANCE SENIOR FLOATING RATE TRUST
    "TKNO", # Alpha Teknova, Inc.
    "AMLX", # Amylyx Pharmaceuticals, Inc.
    "HRZN", # Horizon Technology Finance Corp
    "AWP", # abrdn Global Premier Properties Fund
    "BWMN", # Bowman Consulting Group Ltd.
    "LOCO", # El Pollo Loco Holdings, Inc.
    "WTBA", # WEST BANCORPORATION INC
    "VYGR", # Voyager Therapeutics, Inc.
    "NRIM", # NORTHRIM BANCORP INC
    "JILL", # J.Jill, Inc.
    "SCM", # Stellus Capital Investment Corp
    "HVT", # HAVERTY FURNITURE COMPANIES INC
    "NVEC", # NVE CORP /NEW/
    "ALF", # Centurion Acquisition Corp.
    "RRBI", # RED RIVER BANCSHARES INC
    "TSHA", # Taysha Gene Therapies, Inc.
    "SOR", # SOURCE CAPITAL INC /DE/
    "TRUE", # TrueCar, Inc.
    "PRQR", # ProQR Therapeutics N.V.
    "BMRC", # Bank of Marin Bancorp
    "JRI", # Nuveen Real Asset Income & Growth Fund
    "AMCX", # AMC Networks Inc.
    "FBIZ", # FIRST BUSINESS FINANCIAL SERVICES, INC.
    "ACNB", # ACNB CORP
    "AMBI", # Ambipar Emergency Response
    "DCGO", # DocGo Inc.
    "CWBC", # Community West Bancshares
    "AKBA", # Akebia Therapeutics, Inc.
    "CIX", # COMPX INTERNATIONAL INC
    "CDRO", # Codere Online Luxembourg, S.A.
    "RCS", # PIMCO STRATEGIC INCOME FUND, INC.
    "NYXH", # Nyxoah SA
    "LAW", # CS Disco, Inc.
    "GAMB", # Gambling.com Group Ltd
    "BFZ", # BLACKROCK CALIFORNIA MUNICIPAL INCOME TRUST
    "FOF", # Cohen & Steers Closed-End Opportunity Fund, Inc.
    "NATH", # NATHANS FAMOUS, INC.
    "NAN", # NUVEEN NEW YORK QUALITY MUNICIPAL INCOME FUND
    "ONEW", # OneWater Marine Inc.
    "MTLS", # MATERIALISE NV
    "BMEA", # Biomea Fusion, Inc.
    "ACRE", # Ares Commercial Real Estate Corp
    "TCMD", # TACTILE SYSTEMS TECHNOLOGY INC
    "ARTNA", # ARTESIAN RESOURCES CORP
    "FSBW", # FS Bancorp, Inc.
    "XOMA", # XOMA Royalty Corp
    "EHAB", # Enhabit, Inc.
    "PFL", # PIMCO INCOME STRATEGY FUND
    "CAN", # Canaan Inc.
    "HDSN", # HUDSON TECHNOLOGIES INC /NY
    "FARO", # FARO TECHNOLOGIES INC
    "JAKK", # JAKKS PACIFIC INC
    "ARDC", # Ares Dynamic Credit Allocation Fund, Inc.
    "BGR", # BlackRock Energy & Resources Trust
    "SLQT", # SelectQuote, Inc.
    "PPT", # PUTNAM PREMIER INCOME TRUST
    "RFI", # COHEN & STEERS TOTAL RETURN REALTY FUND INC
    "NREF", # NexPoint Real Estate Finance, Inc.
    "LNZA", # LanzaTech Global, Inc.
    "CLPT", # ClearPoint Neuro, Inc.
    "EFT", # Eaton Vance Floating-Rate Income Trust
    "DOYU", # DouYu International Holdings Ltd
    "AZUL", # AZUL SA
    "JFIN", # Jiayin Group Inc.
    "QUAD", # Quad/Graphics, Inc.
    "NEWT", # NewtekOne, Inc.
    "SMRT", # SmartRent, Inc.
    "RFMZ", # RiverNorth Flexible Municipal Income Fund II, Inc.
    "PSNL", # Personalis, Inc.
    "NAUT", # Nautilus Biotechnology, Inc.
    "UROY", # Uranium Royalty Corp.
    "ACP", # abrdn Income Credit Strategies Fund
    "IPXX", # Inflection Point Acquisition Corp. II
    "MIY", # BLACKROCK MUNIYIELD MICHIGAN QUALITY FUND, INC.
    "ASG", # LIBERTY ALL STAR GROWTH FUND INC.
    "VMD", # VIEMED HEALTHCARE, INC.
    "NECB", # NorthEast Community Bancorp, Inc./MD/
    "EVLV", # Evolv Technologies Holdings, Inc.
    "IPI", # Intrepid Potash, Inc.
    "AIRS", # Airsculpt Technologies, Inc.
    "DENN", # DENNY'S Corp
    "KMDA", # KAMADA LTD
    "PTSI", # PAM TRANSPORTATION SERVICES INC
    "HEAR", # Turtle Beach Corp
    "CYRX", # Cryoport, Inc.
    "APPS", # Digital Turbine, Inc.
    "MTW", # MANITOWOC CO INC
    "JOUT", # JOHNSON OUTDOORS INC
    "NNOX", # Nano-X Imaging Ltd.
    "MSB", # MESABI TRUST
    "MPX", # MARINE PRODUCTS CORP
    "FINS", # Angel Oak Financial Strategies Income Term Trust
    "CIVB", # CIVISTA BANCSHARES, INC.
    "PMO", # PUTNAM MUNICIPAL OPPORTUNITIES TRUST
    "ATNI", # ATN International, Inc.
    "MTA", # Metalla Royalty & Streaming Ltd.
    "NPCT", # Nuveen Core Plus Impact Fund
    "NODK", # NI Holdings, Inc.
    "AFB", # ALLIANCEBERNSTEIN NATIONAL MUNICIPAL INCOME FUND
    "OOMA", # OOMA INC
    "CMPS", # COMPASS Pathways plc
    "GMGI", # Golden Matrix Group, Inc.
    "SAR", # SARATOGA INVESTMENT CORP.
    "HRTG", # Heritage Insurance Holdings, Inc.
    "MHN", # BLACKROCK MUNIHOLDINGS NEW YORK QUALITY FUND, INC.
    "CRMT", # AMERICAS CARMART INC
    "ISPR", # Ispire Technology Inc.
    "NBH", # NEUBERGER BERMAN MUNICIPAL FUND INC.
    "TITN", # Titan Machinery Inc.
    "WEYS", # WEYCO GROUP INC
    "BRW", # Saba Capital Income & Opportunities Fund
    "OUST", # Ouster, Inc.
    "JSPR", # Jasper Therapeutics, Inc.
    "CVRX", # CVRx, Inc.
    "SPOK", # Spok Holdings, Inc
    "TMC", # TMC the metals Co Inc.
    "RLGT", # RADIANT LOGISTICS, INC
    "BYRN", # Byrna Technologies Inc.
    "SFST", # SOUTHERN FIRST BANCSHARES INC
    "NUS", # NU SKIN ENTERPRISES, INC.
    "ALDX", # Aldeyra Therapeutics, Inc.
    "WTI", # W&T OFFSHORE INC
    "ZJYL", # Jin Medical International Ltd.
    "BLZE", # Backblaze, Inc.
    "TWN", # TAIWAN FUND INC
    "HLLY", # Holley Inc.
    "GHM", # GRAHAM CORP
    "MTRX", # MATRIX SERVICE CO
    "DOMO", # DOMO, INC.
    "OIA", # Invesco Municipal Income Opportunities Trust
    "REAL", # TheRealReal, Inc.
    "SNBR", # Sleep Number Corp
    "JWSM", # Jaws Mustang Acquisition Corp
    "VPG", # Vishay Precision Group, Inc.
    "ITOS", # iTeos Therapeutics, Inc.
    "MEI", # METHODE ELECTRONICS INC
    "MIN", # MFS INTERMEDIATE INCOME TRUST
    "ITI", # ITERIS, INC.
    "SSBK", # Southern States Bancshares, Inc.
    "OBT", # Orange County Bancorp, Inc. /DE/
    "RZLT", # Rezolute, Inc.
    "IBEX", # IBEX Ltd
    "XYF", # X Financial
    "BGH", # BARINGS GLOBAL SHORT DURATION HIGH YIELD FUND
    "GWRS", # Global Water Resources, Inc.
    "FLXS", # FLEXSTEEL INDUSTRIES INC
    "DSGN", # Design Therapeutics, Inc.
    "CERS", # CERUS CORP
    "OSUR", # ORASURE TECHNOLOGIES INC
    "NCV", # Virtus Convertible & Income Fund
    "INBK", # First Internet Bancorp
    "CPZ", # Calamos Long/Short Equity & Dynamic Income Trust
    "JMSB", # John Marshall Bancorp, Inc.
    "EB", # Eventbrite, Inc.
    "EDD", # Morgan Stanley Emerging Markets Domestic Debt Fund, Inc.
    "NEWP", # NEW PACIFIC METALS CORP
    "RMM", # RiverNorth Managed Duration Municipal Income Fund, Inc.
    "FDBC", # FIDELITY D & D BANCORP INC
    "PFMT", # Performant Financial Corp
    "PANL", # Pangaea Logistics Solutions Ltd.
    "DSM", # BNY MELLON STRATEGIC MUNICIPAL BOND FUND, INC.
    "OIS", # OIL STATES INTERNATIONAL, INC
    "SPXX", # Nuveen S&P 500 Dynamic Overwrite Fund
    "GHG", # GreenTree Hospitality Group Ltd.
    "BBCP", # Concrete Pumping Holdings, Inc.
    "ACB", # AURORA CANNABIS INC
    "COFS", # CHOICEONE FINANCIAL SERVICES INC
    "JGH", # Nuveen Global High Income Fund
    "BRT", # BRT Apartments Corp.
    "BYM", # BLACKROCK MUNICIPAL INCOME QUALITY TRUST
    "TTSH", # TILE SHOP HOLDINGS, INC.
    "DCTH", # DELCATH SYSTEMS, INC.
    "GILT", # GILAT SATELLITE NETWORKS LTD
    "IHRT", # iHeartMedia, Inc.
    "NCA", # NUVEEN CALIFORNIA MUNICIPAL VALUE FUND
    "RM", # Regional Management Corp.
    "REFI", # Chicago Atlantic Real Estate Finance, Inc.
    "INZY", # Inozyme Pharma, Inc.
    "WSBF", # Waterstone Financial, Inc.
    "JPI", # Nuveen Preferred Securities & Income Opportunities Fund
    "BGT", # BLACKROCK FLOATING RATE INCOME TRUST
    "GENC", # GENCOR INDUSTRIES INC
    "FNLC", # First Bancorp, Inc /ME/
    "REI", # RING ENERGY, INC.
    "PBFS", # Pioneer Bancorp, Inc./MD
    "CZNC", # CITIZENS & NORTHERN CORP
    "CMCL", # Caledonia Mining Corp Plc
    "GNFT", # Genfit S.A.
    "GHI", # Greystone Housing Impact Investors LP
    "HSHP", # Himalaya Shipping Ltd.
    "NEN", # NEW ENGLAND REALTY ASSOCIATES LIMITED PARTNERSHIP
    "PMM", # PUTNAM MANAGED MUNICIPAL INCOME TRUST
    "MCFT", # MasterCraft Boat Holdings, Inc.
    "SSP", # E.W. SCRIPPS Co
    "DBI", # Designer Brands Inc.
    "GENK", # GEN Restaurant Group, Inc.
    "ESEA", # EUROSEAS LTD.
    "SCD", # LMP CAPITAL & INCOME FUND INC.
    "FLIC", # FIRST OF LONG ISLAND CORP
    "SMTI", # Sanara MedTech Inc.
    "GCO", # GENESCO INC
    "TMCI", # TREACE MEDICAL CONCEPTS, INC.
    "FORR", # FORRESTER RESEARCH, INC.
    "EGHT", # 8X8 INC /DE/
    "DSX", # DIANA SHIPPING INC.
    "RNGR", # Ranger Energy Services, Inc.
    "ACIU", # AC Immune SA
    "USCB", # USCB FINANCIAL HOLDINGS, INC.
    "CZFS", # CITIZENS FINANCIAL SERVICES INC
    "ZURA", # Zura Bio Ltd
    "FRST", # Primis Financial Corp.
    "QURE", # uniQure N.V.
    "BLDE", # Blade Air Mobility, Inc.
    "PNRG", # PRIMEENERGY RESOURCES CORP
    "ASLE", # AerSale Corp
    "ZTR", # Virtus Total Return Fund Inc.
    "AFRI", # Forafric Global PLC
    "CLPR", # Clipper Realty Inc.
    "CTV", # Innovid Corp.
    "STRO", # SUTRO BIOPHARMA, INC.
    "PKE", # PARK AEROSPACE CORP
    "VNDA", # Vanda Pharmaceuticals Inc.
    "CANG", # Cango Inc.
    "ZYXI", # ZYNEX INC
    "PINE", # Alpine Income Property Trust, Inc.
    "BCML", # BayCom Corp
    "ADCT", # ADC Therapeutics SA
    "AVIR", # Atea Pharmaceuticals, Inc.
    "WHF", # WhiteHorse Finance, Inc.
    "HYI", # Western Asset High Yield Defined Opportunity Fund Inc.
    "EOT", # Eaton Vance National Municipal Opportunities Trust
    "ABEO", # ABEONA THERAPEUTICS INC.
    "RLTY", # Cohen & Steers Real Estate Opportunities & Income Fund
    "RAIL", # FreightCar America, Inc.
    "CDXC", # ChromaDex Corp.
    "RGP", # RESOURCES CONNECTION, INC.
    "ANGO", # ANGIODYNAMICS INC
    "NRGV", # Energy Vault Holdings, Inc.
    "AEF", # ABRDN EMERGING MARKETS EQUITY INCOME FUND, INC.
    "IIF", # MORGAN STANLEY INDIA INVESTMENT FUND, INC.
    "CBAN", # COLONY BANKCORP INC
    "IMMR", # IMMERSION CORP
    "PCB", # PCB BANCORP
    "APEI", # AMERICAN PUBLIC EDUCATION INC
    "SERA", # SERA PROGNOSTICS, INC.
    "FCT", # FIRST TRUST SENIOR FLOATING RATE INCOME FUND II
    "AUDC", # AUDIOCODES LTD
    "TG", # TREDEGAR CORP
    "FF", # FutureFuel Corp.
    "IMMP", # IMMUTEP Ltd
    "EIC", # Eagle Point Income Co Inc.
    "MCR", # MFS CHARTER INCOME TRUST
    "BTMD", # biote Corp.
    "ASUR", # ASURE SOFTWARE INC
    "SAVE", # Spirit Airlines, Inc.
    "AIP", # Arteris, Inc.
    "UHG", # United Homes Group, Inc.
    "OCGN", # Ocugen, Inc.
    "TPVG", # TriplePoint Venture Growth BDC Corp.
    "MMT", # MFS MULTIMARKET INCOME TRUST
    "LNKB", # LINKBANCORP, Inc.
    "CTGO", # Contango ORE, Inc.
    "MG", # Mistras Group, Inc.
    "AMPY", # Amplify Energy Corp.
    "RIV", # RIVERNORTH OPPORTUNITIES FUND, INC.
    "GOCO", # GoHealth, Inc.
    "PMX", # PIMCO MUNICIPAL INCOME FUND III
    "VPV", # Invesco Pennsylvania Value Municipal Income Trust
    "IRBT", # IROBOT CORP
    "ACCD", # Accolade, Inc.
    "RCEL", # AVITA Medical, Inc.
    "FATE", # FATE THERAPEUTICS INC
    "DBL", # DoubleLine Opportunistic Credit Fund
    "HRTX", # HERON THERAPEUTICS, INC. /DE/
    "AVNW", # AVIAT NETWORKS, INC.
    "POET", # POET TECHNOLOGIES INC.
    "TEI", # TEMPLETON EMERGING MARKETS INCOME FUND
    "JRS", # NUVEEN REAL ESTATE INCOME FUND
    "BNED", # Barnes & Noble Education, Inc.
    "BARK", # Bark, Inc.
    "NTG", # Tortoise Midstream Energy Fund, Inc.
    "API", # Agora, Inc.
    "ONTF", # ON24 INC.
    "BNY", # BLACKROCK NEW YORK MUNICIPAL INCOME TRUST
    "ERC", # ALLSPRING MULTI-SECTOR INCOME FUND
    "PDLB", # Ponce Financial Group, Inc.
    "RGTI", # Rigetti Computing, Inc.
    "SVII", # Spring Valley Acquisition Corp. II
    "PKBK", # PARKE BANCORP, INC.
    "AEYE", # AUDIOEYE INC
    "PCYO", # PURE CYCLE CORP
    "AGD", # abrdn Global Dynamic Dividend Fund
    "INSE", # Inspired Entertainment, Inc.
    "PMF", # PIMCO MUNICIPAL INCOME FUND
    "PLL", # Piedmont Lithium Inc.
    "TLS", # TELOS CORP
    "KFS", # KINGSWAY FINANCIAL SERVICES INC
    "BKT", # BLACKROCK INCOME TRUST, INC.
    "PLBC", # PLUMAS BANCORP
    "SGC", # SUPERIOR GROUP OF COMPANIES, INC.
    "TTEC", # TTEC Holdings, Inc.
    "SGHT", # Sight Sciences, Inc.
    "EVI", # EVI INDUSTRIES, INC.
    "RENE", # Cartesian Growth Corp II
    "NUW", # Nuveen AMT-Free Municipal Value Fund
    "ANIK", # Anika Therapeutics, Inc.
    "ACRV", # Acrivon Therapeutics, Inc.
    "MVBF", # MVB FINANCIAL CORP
    "AENT", # ALLIANCE ENTERTAINMENT HOLDING CORP
    "PSF", # Cohen & Steers Select Preferred & Income Fund, Inc.
    "ICG", # Intchains Group Ltd
    "NGS", # NATURAL GAS SERVICES GROUP INC
    "BPRN", # Princeton Bancorp, Inc.
    "PMTS", # CPI Card Group Inc.
    "CHSN", # Chanson International Holding
    "AKA", # A.K.A. BRANDS HOLDING CORP.
    "ENTA", # ENANTA PHARMACEUTICALS INC
    "SBT", # Sterling Bancorp, Inc.
    "GROY", # Gold Royalty Corp.
    "TCRX", # TScan Therapeutics, Inc.
    "LUNG", # Pulmonx Corp
    "AMRN", # AMARIN CORP PLC\UK
    "ORN", # Orion Group Holdings Inc
    "RIGL", # RIGEL PHARMACEUTICALS INC
    "JCE", # Nuveen Core Equity Alpha Fund
    "SOPH", # SOPHiA GENETICS SA
    "BDSX", # BIODESIX INC
    "TSBK", # TIMBERLAND BANCORP INC
    "OZ", # Belpointe PREP, LLC
    "TCI", # TRANSCONTINENTAL REALTY INVESTORS INC
    "NATR", # NATURES SUNSHINE PRODUCTS INC
    "EDIT", # Editas Medicine, Inc.
    "ILPT", # Industrial Logistics Properties Trust
    "TSI", # TCW STRATEGIC INCOME FUND INC
    "SIFY", # SIFY TECHNOLOGIES LTD
    "SPIR", # Spire Global, Inc.
    "QRTEA", # Qurate Retail, Inc.
    "IVA", # Inventiva S.A.
    "SNFCA", # SECURITY NATIONAL FINANCIAL CORP
    "FVCB", # FVCBankcorp, Inc.
    "NEGG", # Newegg Commerce, Inc.
    "PGEN", # PRECIGEN, INC.
    "JRVR", # James River Group Holdings, Ltd.
    "SRG", # Seritage Growth Properties
    "OMER", # OMEROS CORP
    "NWTN", # NWTN, Inc.
    "NWFL", # NORWOOD FINANCIAL CORP
    "CIA", # CITIZENS, INC.
    "INBX", # Inhibrx Biosciences, Inc.
    "NPV", # NUVEEN VIRGINIA QUALITY MUNICIPAL INCOME FUND
    "LYEL", # Lyell Immunopharma, Inc.
    "BLFY", # Blue Foundry Bancorp
    "CHMG", # CHEMUNG FINANCIAL CORP
    "ARL", # AMERICAN REALTY INVESTORS INC
    "FUND", # SPROTT FOCUS TRUST INC.
    "HITI", # High Tide Inc.
    "MFM", # MFS MUNICIPAL INCOME TRUST
    "MQT", # BLACKROCK MUNIYIELD QUALITY FUND II, INC.
    "HIE", # Miller/Howard High Income Equity Fund
    "EVM", # EATON VANCE CALIFORNIA MUNICIPAL BOND FUND
    "NC", # NACCO INDUSTRIES INC
    "VIRC", # VIRCO MFG CORPORATION
    "TROO", # Troops, Inc. /Cayman Islands/
    "MVT", # BLACKROCK MUNIVEST FUND II, INC.
    "PSTX", # Poseida Therapeutics, Inc.
    "RCAT", # Red Cat Holdings, Inc.
    "NCZ", # Virtus Convertible & Income Fund II
    "BWFG", # Bankwell Financial Group, Inc.
    "NHS", # Neuberger Berman High Yield Strategies Fund Inc.
    "MGNX", # MACROGENICS INC
    "PHT", # PIONEER HIGH INCOME FUND, INC.
    "MRSN", # Mersana Therapeutics, Inc.
    "TSVT", # 2seventy bio, Inc.
    "MODV", # ModivCare Inc
    "MUE", # BLACKROCK MUNIHOLDINGS QUALITY FUND II, INC.
    "MBCN", # MIDDLEFIELD BANC CORP
    "LCNB", # LCNB CORP
    "BHR", # Braemar Hotels & Resorts Inc.
    "TBI", # TrueBlue, Inc.
    "XBIT", # XBiotech Inc.
    "CMPX", # Compass Therapeutics, Inc.
    "TDF", # TEMPLETON DRAGON FUND INC
    "OVLY", # Oak Valley Bancorp
    "EPIX", # ESSA Pharma Inc.
    "GLO", # Clough Global Opportunities Fund
    "PEPG", # PepGen Inc.
    "MFIN", # MEDALLION FINANCIAL CORP
    "NVX", # NOVONIX Ltd
    "FINW", # Finwise Bancorp
    "PBPB", # POTBELLY CORP
    "NKTR", # NEKTAR THERAPEUTICS
    "CAF", # Morgan Stanley China A Share Fund, Inc.
    "EVBN", # EVANS BANCORP INC
    "NXDT", # NEXPOINT DIVERSIFIED REAL ESTATE TRUST
    "DHY", # CREDIT SUISSE HIGH YIELD BOND FUND
    "PRCH", # Porch Group, Inc.
    "CPS", # Cooper-Standard Holdings Inc.
    "IDR", # Idaho Strategic Resources, Inc.
    "BRCC", # BRC Inc.
    "UTMD", # UTAH MEDICAL PRODUCTS INC
    "OPBK", # OP Bancorp
    "MVIS", # MICROVISION, INC.
    "ETON", # Eton Pharmaceuticals, Inc.
    "DRUG", # BRIGHT MINDS BIOSCIENCES INC.
    "TRVI", # Trevi Therapeutics, Inc.
    "NAK", # NORTHERN DYNASTY MINERALS LTD
    "WBX", # Wallbox N.V.
    "CDXS", # CODEXIS, INC.
    "NKTX", # Nkarta, Inc.
    "CLBR", # COLOMBIER ACQUISITION CORP. II
    "VTN", # Invesco Trust for Investment Grade New York Municipals
    "IVCB", # Investcorp Europe Acquisition Corp I
    "LGI", # LAZARD GLOBAL TOTAL RETURN & INCOME FUND INC
    "PESI", # PERMA FIX ENVIRONMENTAL SERVICES INC
    "ALTG", # ALTA EQUIPMENT GROUP INC.
    "MITT", # AG Mortgage Investment Trust, Inc.
    "JOF", # JAPAN SMALLER CAPITALIZATION FUND INC
    "DBB", # INVESCO DB BASE METALS FUND
    "GPJA", # GEORGIA POWER CO
    "TIL", # Instil Bio, Inc.
    "AHG", # Akso Health Group
    "FRGE", # Forge Global Holdings, Inc.
    "SCWO", # 374Water Inc.
    "SLDP", # Solid Power, Inc.
    "EVC", # ENTRAVISION COMMUNICATIONS CORP
    "PYXS", # Pyxis Oncology, Inc.
    "ACV", # Virtus Diversified Income & Convertible Fund
    "VSTA", # Vasta Platform Ltd
    "MHI", # PIONEER MUNICIPAL HIGH INCOME FUND, INC.
    "PROC", # Procaps Group, S.A.
    "WRN", # Western Copper & Gold Corp
    "CDLX", # Cardlytics, Inc.
    "ONL", # Orion Office REIT Inc.
    "TUSK", # MAMMOTH ENERGY SERVICES, INC.
    "DBP", # Invesco DB Precious Metals Fund
    "QBTS", # D-Wave Quantum Inc.
    "BRBS", # BLUE RIDGE BANKSHARES, INC.
    "VABK", # Virginia National Bankshares Corp
    "SLDB", # Solid Biosciences Inc.
    "AOMR", # Angel Oak Mortgage REIT, Inc.
    "OB", # Outbrain Inc.
    "BKN", # BLACKROCK INVESTMENT QUALITY MUNICIPAL TRUST, INC.
    "KNOP", # KNOT Offshore Partners LP
    "CYBN", # CYBIN INC.
    "GASS", # StealthGas Inc.
    "CIO", # City Office REIT, Inc.
    "NBTX", # Nanobiotix S.A.
    "LFCR", # LIFECORE BIOMEDICAL, INC. \DE\
    "BW", # Babcock & Wilcox Enterprises, Inc.
    "TZOO", # TRAVELZOO
    "CRNT", # CERAGON NETWORKS LTD
    "RGCO", # RGC RESOURCES INC
    "TCX", # TUCOWS INC /PA/
    "BCBP", # BCB BANCORP INC
    "FSTR", # FOSTER L B CO
    "SMLR", # Semler Scientific, Inc.
    "CAMP", # Camp4 Therapeutics Corp
    "INGN", # Inogen Inc
    "SCPH", # scPharmaceuticals Inc.
    "EOD", # ALLSPRING GLOBAL DIVIDEND OPPORTUNITY FUND
    "MXF", # MEXICO FUND INC
    "EMX", # EMX Royalty Corp
    "ISTR", # Investar Holding Corp
    "BNTC", # Benitec Biopharma Inc.
    "FFNW", # First Financial Northwest, Inc.
    "PWOD", # PENNS WOODS BANCORP INC
    "FUNC", # FIRST UNITED CORP/MD/
    "FXE", # Invesco CurrencyShares Euro Trust
    "SWKH", # SWK Holdings Corp
    "CDZI", # CADIZ INC
    "ZNTL", # Zentalis Pharmaceuticals, Inc.
    "MAV", # PIONEER MUNICIPAL HIGH INCOME ADVANTAGE FUND, INC.
    "BOOM", # DMC Global Inc.
    "NVRO", # NEVRO CORP
    "GPRO", # GoPro, Inc.
    "MIO", # Pioneer Municipal High Income Opportunities Fund, Inc.
    "ETX", # Eaton Vance Municipal Income 2028 Term Trust
    "ORGN", # Origin Materials, Inc.
    "AFCG", # Advanced Flower Capital Inc.
    "CFFI", # C & F FINANCIAL CORP
    "GHIX", # Gores Holdings IX, Inc.
    "MBI", # MBIA INC
    "OBIO", # Orchestra BioMed Holdings, Inc.
    "CPSS", # CONSUMER PORTFOLIO SERVICES, INC.
    "SKIN", # Beauty Health Co
    "SANG", # Sangoma Technologies Corp
    "MED", # MEDIFAST INC
    "BLNK", # Blink Charging Co.
    "INSG", # INSEEGO CORP.
    "EMF", # TEMPLETON EMERGING MARKETS FUND
    "KOD", # Kodiak Sciences Inc.
    "DC", # Dakota Gold Corp.
    "OPP", # RiverNorth/DoubleLine Strategic Opportunity Fund, Inc.
    "GOSS", # Gossamer Bio, Inc.
    "EML", # EASTERN CO
    "HWBK", # HAWTHORN BANCSHARES, INC.
    "PCF", # HIGH INCOME SECURITIES FUND
    "DMB", # BNY Mellon Municipal Bond Infrastructure Fund, Inc.
    "FULC", # Fulcrum Therapeutics, Inc.
    "RELL", # RICHARDSON ELECTRONICS, LTD.
    "PIII", # P3 Health Partners Inc.
    "TATT", # TAT TECHNOLOGIES LTD
    "NKLA", # Nikola Corp
    "EMP", # ENTERGY MISSISSIPPI, LLC
    "KLTR", # KALTURA INC
    "ENJ", # ENTERGY NEW ORLEANS, LLC
    "MDWD", # MediWound Ltd.
    "SENS", # Senseonics Holdings, Inc.
    "SHIP", # Seanergy Maritime Holdings Corp.
    "FCEL", # FUELCELL ENERGY INC
    "VLN", # Valens Semiconductor Ltd.
    "ESSA", # ESSA Bancorp, Inc.
    "BROG", # Brooge Energy Ltd
    "PAYS", # Paysign, Inc.
    "AEVA", # Aeva Technologies, Inc.
    "GTE", # GRAN TIERRA ENERGY INC.
    "WIA", # WESTERN ASSET INFLATION-LINKED INCOME FUND
    "ELMD", # Electromed, Inc.
    "SMHI", # SEACOR Marine Holdings Inc.
    "PCK", # PIMCO CALIFORNIA MUNICIPAL INCOME FUND II
    "CRBP", # Corbus Pharmaceuticals Holdings, Inc.
    "HYB", # NEW AMERICA HIGH INCOME FUND INC
    "ESOA", # Energy Services of America CORP
    "HQI", # HireQuest, Inc.
    "NPCE", # NeuroPace Inc
    "BKSY", # BlackSky Technology Inc.
    "ELDN", # Eledon Pharmaceuticals, Inc.
    "FXNC", # FIRST NATIONAL CORP /VA/
    "SRI", # STONERIDGE INC
    "ALCO", # ALICO, INC.
    "CLLS", # Cellectis S.A.
    "SEVN", # Seven Hills Realty Trust
    "ADAP", # Adaptimmune Therapeutics PLC
    "ODV", # Osisko Development Corp.
    "PCQ", # PIMCO CALIFORNIA MUNICIPAL INCOME FUND
    "DMAC", # DiaMedica Therapeutics Inc.
    "OGI", # ORGANIGRAM HOLDINGS INC.
    "PERF", # Perfect Corp.
    "FT", # FRANKLIN UNIVERSAL TRUST
    "DHF", # BNY MELLON HIGH YIELD STRATEGIES FUND
    "FSP", # FRANKLIN STREET PROPERTIES CORP /MA/
    "STRS", # STRATUS PROPERTIES INC
    "SJT", # SAN JUAN BASIN ROYALTY TRUST
    "EM", # Smart Share Global Ltd
    "NKSH", # NATIONAL BANKSHARES INC
    "NRO", # NEUBERGER BERMAN REAL ESTATE SECURITIES INCOME FUND INC
    "PVBC", # Provident Bancorp, Inc. /MD/
    "OXSQ", # Oxford Square Capital Corp.
    "FSFG", # First Savings Financial Group, Inc.
    "VBF", # Invesco Bond Fund
    "BSL", # Blackstone Senior Floating Rate 2027 Term Fund
    "INSI", # Insight Select Income Fund
    "PLG", # PLATINUM GROUP METALS LTD
    "WNEB", # Western New England Bancorp, Inc.
    "MYFW", # First Western Financial Inc
    "ESCA", # ESCALADE INC
    "MPV", # BARINGS PARTICIPATION INVESTORS
    "SMID", # SMITH MIDLAND CORP
    "DOUG", # Douglas Elliman Inc.
    "IGI", # Western Asset Investment Grade Defined Opportunity Trust Inc.
    "RMBL", # RumbleOn, Inc.
    "LANV", # Lanvin Group Holdings Ltd
    "BZUN", # Baozun Inc.
    "SPCE", # Virgin Galactic Holdings, Inc
    "FCCO", # FIRST COMMUNITY CORP /SC/
    "PROF", # Profound Medical Corp.
    "MOLN", # MOLECULAR PARTNERS AG
    "GLSI", # Greenwich LifeSciences, Inc.
    "HFFG", # HF Foods Group Inc.
    "ELLO", # Ellomay Capital Ltd.
    "ABOS", # Acumen Pharmaceuticals, Inc.
    "FLL", # FULL HOUSE RESORTS INC
    "ARAY", # ACCURAY INC
    "ATAI", # ATAI Life Sciences N.V.
    "RILY", # B. Riley Financial, Inc.
    "GDO", # WESTERN ASSET GLOBAL CORPORATE DEFINED OPPORTUNITY FUND INC.
    "ASM", # AVINO SILVER & GOLD MINES LTD
    "CRBU", # Caribou Biosciences, Inc.
    "BAER", # Bridger Aerospace Group Holdings, Inc.
    "CABA", # Cabaletta Bio, Inc.
    "PLCE", # Childrens Place, Inc.
    "FLC", # FLAHERTY & CRUMRINE TOTAL RETURN FUND INC
    "IDE", # Voya Infrastructure, Industrials & Materials Fund
    "ATOS", # ATOSSA THERAPEUTICS, INC.
    "SKGR", # SK Growth Opportunities Corp
    "HCVI", # Hennessy Capital Investment Corp. VI
    "GLDG", # GoldMining Inc.
    "HGLB", # HIGHLAND GLOBAL ALLOCATION FUND
    "HOFT", # HOOKER FURNISHINGS Corp
    "VOXX", # VOXX International Corp
    "LFMD", # LifeMD, Inc.
    "SES", # SES AI Corp
    "MYPS", # PLAYSTUDIOS, Inc.
    "NIU", # Niu Technologies
    "EPM", # EVOLUTION PETROLEUM CORP
    "TEAF", # TORTOISE SUSTAINABLE & SOCIAL IMPACT TERM FUND
    "FET", # FORUM ENERGY TECHNOLOGIES, INC.
    "BRKH", # BurTech Acquisition Corp.
    "CADL", # Candel Therapeutics, Inc.
    "VXRT", # Vaxart, Inc.
    "HMST", # HomeStreet, Inc.
    "LOGC", # ContextLogic Inc.
    "ENX", # EATON VANCE NEW YORK MUNICIPAL BOND FUND
    "STHO", # Star Holdings
    "PTMN", # Portman Ridge Finance Corp
    "MRCC", # MONROE CAPITAL Corp
    "MX", # MAGNACHIP SEMICONDUCTOR Corp
    "SAMG", # Silvercrest Asset Management Group Inc.
    "RCMT", # RCM TECHNOLOGIES, INC.
    "RRAC", # Rigel Resource Acquisition Corp.
    "BWAY", # Brainsway Ltd.
    "RTC", # Baijiayun Group Ltd
    "TSE", # Trinseo PLC
    "DIBS", # 1stdibs.com, Inc.
    "CHGG", # CHEGG, INC
    "SGMT", # Sagimet Biosciences Inc.
    "EP", # EMPIRE PETROLEUM CORP
    "JYNT", # JOINT Corp
    "STXS", # Stereotaxis, Inc.
    "MCAA", # Mountain & Co. I Acquisition Corp.
    "RDCM", # RADCOM LTD
    "WILC", # G WILLI FOOD INTERNATIONAL LTD
    "GNSS", # Genasys Inc.
    "EARN", # Ellington Credit Co
    "TWIN", # TWIN DISC INC
    "EXFY", # Expensify, Inc.
    "PZC", # PIMCO CALIFORNIA MUNICIPAL INCOME FUND III
    "ALCY", # Alchemy Investments Acquisition Corp 1
    "DM", # Desktop Metal, Inc.
    "CLAR", # Clarus Corp
    "CTRN", # Citi Trends Inc
    "EVE", # EVe Mobility Acquisition Corp
    "AMLI", # American Lithium Corp.
    "ACHV", # ACHIEVE LIFE SCIENCES, INC.
    "BGX", # Blackstone Long-Short Credit Income Fund
    "NRDY", # Nerdy Inc.
    "GRX", # Gabelli Healthcare & WellnessRx Trust
    "CNTX", # Context Therapeutics Inc.
    "TPIC", # TPI COMPOSITES, INC
    "QSG", # QuantaSing Group Ltd
    "EUDA", # EUDA Health Holdings Ltd
    "NMG", # Nouveau Monde Graphite Inc.
    "DRTS", # Alpha Tau Medical Ltd.
    "MDV", # MODIV INDUSTRIAL, INC.
    "IKT", # Inhibikase Therapeutics, Inc.
    "QRHC", # Quest Resource Holding Corp
    "SPE", # SPECIAL OPPORTUNITIES FUND, INC.
    "NNY", # NUVEEN NEW YORK MUNICIPAL VALUE FUND
    "MHLD", # Maiden Holdings, Ltd.
    "AXR", # AMREP CORP.
    "DXLG", # DESTINATION XL GROUP, INC.
    "PIM", # PUTNAM MASTER INTERMEDIATE INCOME TRUST
    "NNBR", # NN INC
    "SPPP", # SPROTT PHYSICAL PLATINUM & PALLADIUM TRUST
    "MRBK", # Meridian Corp
    "FACT", # FACT II Acquisition Corp.
    "CIK", # CREDIT SUISSE ASSET MANAGEMENT INCOME FUND, INC.
    "LCTX", # Lineage Cell Therapeutics, Inc.
    "STRT", # STRATTEC SECURITY CORP
    "GALT", # GALECTIN THERAPEUTICS INC
    "RCKY", # ROCKY BRANDS, INC.
    "MPA", # BLACKROCK MUNIYIELD PENNSYLVANIA QUALITY FUND
    "EHI", # WESTERN ASSET GLOBAL HIGH INCOME FUND INC.
    "BDTX", # Black Diamond Therapeutics, Inc.
    "MMLP", # MARTIN MIDSTREAM PARTNERS L.P.
    "LFVN", # Lifevantage Corp
    "CKPT", # Checkpoint Therapeutics, Inc.
    "BRLT", # Brilliant Earth Group, Inc.
    "MSD", # MORGAN STANLEY EMERGING MARKETS DEBT FUND INC
    "CFBK", # CF BANKSHARES INC.
    "LGO", # Largo Inc.
    "BFAC", # Battery Future Acquisition Corp.
    "ADVM", # Adverum Biotechnologies, Inc.
    "UBFO", # UNITED SECURITY BANCSHARES
    "UNG", # United States Natural Gas Fund, LP
    "VTYX", # Ventyx Biosciences, Inc.
    "BMN", # BlackRock 2037 Municipal Target Term Trust
    "ATLO", # AMES NATIONAL CORP
    "RMNI", # Rimini Street, Inc.
    "GBIO", # Generation Bio Co.
    "LTRX", # LANTRONIX INC
    "III", # Information Services Group Inc.
    "TNYA", # Tenaya Therapeutics, Inc.
    "AVD", # AMERICAN VANGUARD CORP
    "GPMT", # Granite Point Mortgage Trust Inc.
    "TSQ", # Townsquare Media, Inc.
    "VSTM", # Verastem, Inc.
    "DMF", # BNY MELLON MUNICIPAL INCOME, INC.
    "MHF", # WESTERN ASSET MUNICIPAL HIGH INCOME FUND INC.
    "EVG", # Eaton Vance Short Duration Diversified Income Fund
    "ATLX", # Atlas Lithium Corp
    "BCSA", # Blockchain Coinvestors Acquisition Corp. I
    "ARBE", # Arbe Robotics Ltd.
    "EDF", # Virtus Stone Harbor Emerging Markets Income Fund
    "CXDO", # Crexendo, Inc.
    "BFIN", # BankFinancial CORP
    "VOXR", # VOX ROYALTY CORP.
    "VIGL", # Vigil Neuroscience, Inc.
    "TAYD", # TAYLOR DEVICES, INC.
    "EHTH", # eHealth, Inc.
    "PFD", # FLAHERTY & CRUMRINE PREFERRED & INCOME FUND INC
    "BANX", # ArrowMark Financial Corp.
    "FTK", # FLOTEK INDUSTRIES INC/CN/
    "EGAN", # EGAIN Corp
    "AMPX", # Amprius Technologies, Inc.
    "IPHA", # Innate Pharma SA
    "ACU", # ACME UNITED CORP
    "MPLN", # MultiPlan Corp
    "GEOS", # GEOSPACE TECHNOLOGIES CORP
    "WHG", # WESTWOOD HOLDINGS GROUP INC
    "ARC", # ARC DOCUMENT SOLUTIONS, INC.
    "MCN", # Madison Covered Call & Equity Strategy Fund
    "FRAF", # FRANKLIN FINANCIAL SERVICES CORP /PA/
    "ISRL", # Israel Acquisitions Corp
    "CGEN", # COMPUGEN LTD
    "CRDL", # Cardiol Therapeutics Inc.
    "CRDF", # Cardiff Oncology, Inc.
    "IGA", # Voya Global Advantage & Premium Opportunity Fund
    "LPTX", # LEAP THERAPEUTICS, INC.
    "MPTI", # M-tron Industries, Inc.
    "RPTX", # Repare Therapeutics Inc.
    "ULBI", # ULTRALIFE CORP
    "VRA", # Vera Bradley, Inc.
    "AKYA", # Akoya Biosciences, Inc.
    "CZWI", # Citizens Community Bancorp Inc.
    "HNVR", # Hanover Bancorp, Inc. /NY
    "AJX", # Great Ajax Corp.
    "BWG", # BrandywineGLOBAL-Global Income Opportunities Fund Inc
    "PBYI", # PUMA BIOTECHNOLOGY, INC.
    "CSTE", # Caesarstone Ltd.
    "CBFV", # CB Financial Services, Inc.
    "SLND", # Southland Holdings, Inc.
    "SSTI", # SOUNDTHINKING, INC.
    "HURC", # HURCO COMPANIES INC
    "LAKE", # LAKELAND INDUSTRIES INC
    "PEBK", # PEOPLES BANCORP OF NORTH CAROLINA INC
    "GGR", # Gogoro Inc.
    "ALTO", # Alto Ingredients, Inc.
    "DCF", # BNY Mellon Alcentra Global Credit Income 2024 Target Term Fund, Inc.
    "INO", # INOVIO PHARMACEUTICALS, INC.
    "DLNG", # Dynagas LNG Partners LP
    "GF", # NEW GERMANY FUND INC
    "ELA", # Envela Corp
    "TOUR", # Tuniu Corp
    "BTA", # BlackRock Long-Term Municipal Advantage Trust
    "AFBI", # Affinity Bancshares, Inc.
    "AMWL", # American Well Corp
    "NVCT", # Nuvectis Pharma, Inc.
    "GATE", # Marblegate Acquisition Corp.
    "DMO", # Western Asset Mortgage Opportunity Fund Inc.
    "FREY", # FREYR Battery, Inc. /DE/
    "MRAM", # EVERSPIN TECHNOLOGIES INC
    "LEV", # Lion Electric Co
    "CAAS", # CHINA AUTOMOTIVE SYSTEMS INC
    "ECBK", # ECB Bancorp, Inc. /MD/
    "OTLK", # Outlook Therapeutics, Inc.
    "FNWD", # Finward Bancorp
    "CMT", # CORE MOLDING TECHNOLOGIES INC
    "EBMT", # Eagle Bancorp Montana, Inc.
    "PHX", # PHX MINERALS INC.
    "NAZ", # NUVEEN ARIZONA QUALITY MUNICIPAL INCOME FUND
    "RMMZ", # RiverNorth Managed Duration Municipal Income Fund II, Inc.
    "LTBR", # LIGHTBRIDGE Corp
    "CURI", # CuriosityStream Inc.
    "ALLT", # Allot Ltd.
    "INFU", # InfuSystem Holdings, Inc
    "ACRS", # Aclaris Therapeutics, Inc.
    "MNTN", # Everest Consolidator Acquisition Corp
    "CSLR", # Complete Solaria, Inc.
    "RANI", # Rani Therapeutics Holdings, Inc.
    "SUAC", # ShoulderUP Technology Acquisition Corp.
    "JHS", # JOHN HANCOCK INCOME SECURITIES TRUST
    "QH", # QUHUO Ltd
    "MCRB", # Seres Therapeutics, Inc.
    "CATO", # CATO CORP
    "MAXN", # Maxeon Solar Technologies, Ltd.
    "MAPS", # WM TECHNOLOGY, INC.
    "ATEK", # Athena Technology Acquisition Corp. II
    "FGBI", # First Guaranty Bancshares, Inc.
    "UNB", # UNION BANKSHARES INC
    "MNSB", # MainStreet Bancshares, Inc.
    "VFL", # abrdn National Municipal Income Fund
    "WEA", # WESTERN ASSET PREMIER BOND FUND
    "FMN", # Federated Hermes Premier Municipal Income Fund
    "DLTH", # DULUTH HOLDINGS INC.
    "SKYX", # SKYX Platforms Corp.
    "REE", # REE Automotive Ltd.
    "XNET", # Xunlei Ltd
    "HEQ", # John Hancock Hedged Equity & Income Fund
    "GGT", # GABELLI MULTIMEDIA TRUST INC.
    "POWW", # AMMO, INC.
    "VGAS", # Verde Clean Fuels, Inc.
    "RMBI", # Richmond Mutual Bancorporation, Inc.
    "KPTI", # Karyopharm Therapeutics Inc.
    "AZ", # A2Z CUST2MATE SOLUTIONS CORP.
    "AVTX", # Avalo Therapeutics, Inc.
    "BSET", # BASSETT FURNITURE INDUSTRIES INC
    "GLQ", # Clough Global Equity Fund
    "EPSN", # Epsilon Energy Ltd.
    "SFBC", # Sound Financial Bancorp, Inc.
    "LFT", # Lument Finance Trust, Inc.
    "ISSC", # INNOVATIVE SOLUTIONS & SUPPORT INC
    "ECF", # ELLSWORTH GROWTH & INCOME FUND LTD
    "USAS", # Americas Gold & Silver Corp
    "GAIA", # GAIA, INC
    "AMTX", # AEMETIS, INC
    "LCUT", # LIFETIME BRANDS, INC
    "CRNC", # Cerence Inc.
    "CMCM", # Cheetah Mobile Inc.
    "NOTE", # FiscalNote Holdings, Inc.
    "SOL", # Emeren Group Ltd
    "SKIL", # Skillsoft Corp.
    "FXY", # Invesco CurrencyShares Japanese Yen Trust
    "DBE", # Invesco DB Energy Fund
    "THM", # INTERNATIONAL TOWER HILL MINES LTD
    "SBFG", # SB FINANCIAL GROUP, INC.
    "JHI", # JOHN HANCOCK INVESTORS TRUST
    "SCLX", # Scilex Holding Co
    "CHN", # China Fund, Inc.
    "VERI", # Veritone, Inc.
    "GRWG", # GrowGeneration Corp.
    "ADAG", # Adagene Inc.
    "IMPP", # Imperial Petroleum Inc./Marshall Islands
    "NTIC", # NORTHERN TECHNOLOGIES INTERNATIONAL CORP
    "FCAP", # FIRST CAPITAL INC
    "CSPI", # CSP INC /MA/
    "ACR", # ACRES Commercial Realty Corp.
    "ANVS", # Annovis Bio, Inc.
    "PHD", # Pioneer Floating Rate Fund, Inc.
    "RCFA", # Perception Capital Corp. IV
    "CCRD", # CoreCard Corp
    "KINS", # KINGSTONE COMPANIES, INC.
    "TLYS", # TILLY'S, INC.
    "FEIM", # FREQUENCY ELECTRONICS INC
    "PAI", # Western Asset Investment Grade Income Fund Inc.
    "ME", # 23andMe Holding Co.
    "PDSB", # PDS Biotechnology Corp
    "FENC", # FENNEC PHARMACEUTICALS INC.
    "CXE", # MFS HIGH INCOME MUNICIPAL TRUST
    "FOA", # Finance of America Companies Inc.
    "ZOM", # Zomedica Corp.
    "SRV", # NXG Cushing Midstream Energy Fund
    "PFO", # Flaherty & Crumrine PREFERRED & INCOME OPPORTUNITY FUND INC
    "PLAO", # Patria Latin American Opportunity Acquisition Corp.
    "COYA", # Coya Therapeutics, Inc.
    "ATOM", # Atomera Inc
    "KRMD", # KORU Medical Systems, Inc.
    "SRL", # Scully Royalty Ltd.
    "OCCI", # OFS Credit Company, Inc.
    "PFIE", # PROFIRE ENERGY INC
    "DERM", # Journey Medical Corp
    "KOPN", # KOPIN CORP
    "BYNO", # byNordic Acquisition Corp
    "APXI", # APx Acquisition Corp. I
    "CBUS", # Cibus, Inc.
    "CGO", # CALAMOS GLOBAL TOTAL RETURN FUND
    "IAF", # ABRDN AUSTRALIA EQUITY FUND, INC.
    "SEER", # Seer, Inc.
    "DTI", # Drilling Tools International Corp
    "MNTX", # Manitex International, Inc.
    "MHH", # Mastech Digital, Inc.
    "TRVG", # trivago N.V.
    "LARK", # LANDMARK BANCORP INC
    "WMPN", # William Penn Bancorporation
    "DLHC", # DLH Holdings Corp.
    "NXG", # NXG NextGen Infrastructure Income Fund
    "SEDA", # SDCL EDGE Acquisition Corp
    "INMB", # Inmune Bio, Inc.
    "MRT", # Marti Technologies, Inc.
    "SNCR", # SYNCHRONOSS TECHNOLOGIES INC
    "BRAG", # Bragg Gaming Group Inc.
    "CFFS", # CF Acquisition Corp. VII
    "VBFC", # Village Bank & Trust Financial Corp.
    "QIPT", # Quipt Home Medical Corp.
    "RMTI", # ROCKWELL MEDICAL, INC.
    "KNDI", # Kandi Technologies Group, Inc.
    "NEON", # Neonode Inc.
    "HOWL", # Werewolf Therapeutics, Inc.
    "OVBC", # OHIO VALLEY BANC CORP
    "SBI", # WESTERN ASSET INTERMEDIATE MUNI FUND INC.
    "ANIX", # Anixa Biosciences Inc
    "NIM", # NUVEEN SELECT MATURITIES MUNICIPAL FUND
    "UEIC", # UNIVERSAL ELECTRONICS INC
    "NUTX", # Nutex Health, Inc.
    "CHCI", # Comstock Holding Companies, Inc.
    "AXTI", # AXT INC
    "MOND", # Mondee Holdings, Inc.
    "VERU", # VERU INC.
    "ALLK", # Allakos Inc.
    "IMUX", # IMMUNIC, INC.
    "KSM", # DWS STRATEGIC MUNICIPAL INCOME TRUST
    "SACH", # Sachem Capital Corp.
    "EVF", # EATON VANCE SENIOR INCOME TRUST
    "LEE", # LEE ENTERPRISES, Inc
    "TRX", # TRX GOLD Corp
    "MASS", # 908 Devices Inc.
    "UFI", # UNIFI INC
    "TPZ", # TORTOISE POWER & ENERGY INFRASTRUCTURE FUND INC
    "BATL", # BATTALION OIL CORP
    "TELA", # TELA Bio, Inc.
    "TLGY", # TLGY ACQUISITION CORP
    "MYO", # MYOMO, INC.
    "NMT", # NUVEEN MASSACHUSETTS QUALITY MUNICIPAL INCOME FUND
    "OFS", # OFS Capital Corp
    "CMTL", # COMTECH TELECOMMUNICATIONS CORP /DE/
    "AOUT", # American Outdoor Brands, Inc.
    "ACET", # Adicet Bio, Inc.
    "OCFT", # ONECONNECT FINANCIAL TECHNOLOGY CO., LTD.
    "QUBT", # Quantum Computing Inc.
    "IVVD", # Invivyd, Inc.
    "SSSS", # SURO CAPITAL CORP.
    "ASMB", # ASSEMBLY BIOSCIENCES, INC.
    "EDAP", # EDAP TMS SA
    "CSLM", # CSLM ACQUISITION CORP.
    "SFWL", # SHENGFENG DEVELOPMENT Ltd
    "STKS", # ONE Group Hospitality, Inc.
    "CNTY", # CENTURY CASINOS INC /CO/
    "THCH", # TH International Ltd
    "QUIK", # QUICKLOGIC Corp
    "PBHC", # Pathfinder Bancorp, Inc.
    "SRTS", # Sensus Healthcare, Inc.
    "LPSN", # LIVEPERSON INC
    "PROV", # PROVIDENT FINANCIAL HOLDINGS INC
    "PPYA", # Papaya Growth Opportunity Corp. I
    "GNLX", # GENELUX Corp
    "PDEX", # PRO DEX INC
    "SWZ", # SWISS HELVETIA FUND, INC.
    "ALVR", # Allovir, Inc.
    "RLMD", # RELMADA THERAPEUTICS, INC.
    "GECC", # Great Elm Capital Corp.
    "PPIH", # Perma-Pipe International Holdings, Inc.
    "MGF", # MFS GOVERNMENT MARKETS INCOME TRUST
    "OPTN", # OptiNose, Inc.
    "NEOV", # NeoVolta Inc.
    "QSI", # Quantum-Si Inc
    "CHMI", # Cherry Hill Mortgage Investment Corp
    "HBIO", # HARVARD BIOSCIENCE INC
    "AIRG", # AIRGAIN INC
    "KF", # KOREA FUND INC
    "HNW", # Pioneer Diversified High Income Fund, Inc.
    "MPAA", # MOTORCAR PARTS OF AMERICA INC
    "USGO", # U.S. GoldMining Inc.
    "INVZ", # Innoviz Technologies Ltd.
    "SKLZ", # Skillz Inc.
    "MVO", # MV Oil Trust
    "ITRG", # Integra Resources Corp.
    "BSBK", # Bogota Financial Corp.
    "ERH", # ALLSPRING UTILITIES & HIGH INCOME FUND
    "RMI", # RiverNorth Opportunistic Municipal Income Fund, Inc.
    "RBKB", # Rhinebeck Bancorp, Inc.
    "OPOF", # OLD POINT FINANCIAL CORP
    "CVGI", # Commercial Vehicle Group, Inc.
    "FNGR", # FingerMotion, Inc.
    "TMQ", # Trilogy Metals Inc.
    "GGZ", # Gabelli Global Small & Mid Cap Value Trust
    "THCP", # Thunder Bridge Capital Partners IV, Inc.
    "IPSC", # Century Therapeutics, Inc.
    "RVSB", # RIVERVIEW BANCORP INC
    "ALOT", # AstroNova, Inc.
    "JLS", # Nuveen Mortgage & Income Fund/MA/
    "TBMC", # Trailblazer Merger Corp I
    "FRD", # FRIEDMAN INDUSTRIES INC
    "SIEB", # SIEBERT FINANCIAL CORP
    "TLSA", # Tiziana Life Sciences Ltd
    "SPWH", # SPORTSMAN'S WAREHOUSE HOLDINGS, INC.
    "OPRT", # Oportun Financial Corp
    "FONR", # FONAR CORP
    "BCV", # BANCROFT FUND LTD
    "IHD", # Voya Emerging Markets High Dividend Equity Fund
    "ASRT", # Assertio Holdings, Inc.
    "VFF", # Village Farms International, Inc.
    "RGLS", # Regulus Therapeutics Inc.
    "GLU", # GABELLI GLOBAL UTILITY & INCOME TRUST
    "MDXH", # MDxHealth SA
    "PRPL", # Purple Innovation, Inc.
    "NMI", # NUVEEN MUNICIPAL INCOME FUND INC
    "PCM", # PCM FUND, INC.
    "CODA", # Coda Octopus Group, Inc.
    "PFX", # PhenixFIN Corp
    "RFM", # RiverNorth Flexible Municipal Income Fund, Inc.
    "BCOV", # BRIGHTCOVE INC
    "ORMP", # ORAMED PHARMACEUTICALS INC.
    "OPRX", # OptimizeRx Corp
    "CNDA", # Concord Acquisition Corp II
    "EVTL", # Vertical Aerospace Ltd.
    "GDL", # GDL FUND
    "FNWB", # First Northwest Bancorp
    "CBAT", # CBAK Energy Technology, Inc.
    "BKTI", # BK Technologies Corp
    "ACNT", # ASCENT INDUSTRIES CO.
    "EVGR", # Evergreen Corp
    "DSAQ", # Direct Selling Acquisition Corp.
    "GNT", # GAMCO Natural Resources, Gold & Income Trust
    "BCAB", # BioAtla, Inc.
    "RGC", # Regencell Bioscience Holdings Ltd
    "CPHC", # Canterbury Park Holding Corp
    "PWUP", # PowerUp Acquisition Corp.
    "REKR", # Rekor Systems, Inc.
    "ACAB", # Atlantic Coastal Acquisition Corp. II
    "ALAR", # Alarum Technologies Ltd.
    "GNTA", # Genenta Science S.p.A.
    "BLUE", # bluebird bio, Inc.
    "AGEN", # AGENUS INC
    "CASI", # CASI Pharmaceuticals, Inc.
    "IH", # iHuman Inc.
    "BZFD", # BuzzFeed, Inc.
    "KEQU", # KEWAUNEE SCIENTIFIC CORP /DE/
    "CITE", # Cartica Acquisition Corp
    "CNGL", # Canna-Global Acquisition Corp
    "IVCA", # Investcorp AI Acquisition Corp.
    "KVHI", # KVH INDUSTRIES INC \DE\
    "SST", # System1, Inc.
    "PGP", # PIMCO Global StocksPLUS & Income Fund
    "HLVX", # HilleVax, Inc.
    "STG", # Sunlands Technology Group
    "GIFI", # GULF ISLAND FABRICATION INC
    "SY", # So-Young International Inc.
    "ONYX", # Onyx Acquisition Co. I
    "CDTX", # Cidara Therapeutics, Inc.
    "CMU", # MFS HIGH YIELD MUNICIPAL TRUST
    "MAYS", # MAYS J W INC
    "FAT", # Fat Brands, Inc
    "VGI", # Virtus Global Multi-Sector Income Fund
    "RRGB", # RED ROBIN GOURMET BURGERS INC
    "COE", # 51Talk Online Education Group
    "IVAC", # INTEVAC INC
    "MKFG", # Markforged Holding Corp
    "TTP", # TORTOISE PIPELINE & ENERGY FUND, INC.
    "INTT", # INTEST CORP
    "GAQ", # Generation Asia I Acquisition Ltd
    "SATL", # Satellogic Inc.
    "CUE", # Cue Biopharma, Inc.
    "BYSI", # BeyondSpring Inc.
    "OPI", # OFFICE PROPERTIES INCOME TRUST
    "PFTA", # Perception Capital Corp. III
    "ONCY", # ONCOLYTICS BIOTECH INC
    "VIOT", # Viomi Technology Co., Ltd
    "HSPO", # Horizon Space Acquisition I Corp.
    "SGA", # SAGA COMMUNICATIONS INC
    "SND", # Smart Sand, Inc.
    "IFRX", # InflaRx N.V.
    "XFOR", # X4 Pharmaceuticals, Inc
    "VOC", # VOC Energy Trust
    "CMRX", # CHIMERIX INC
    "GWH", # ESS Tech, Inc.
    "ARBK", # Argo Blockchain Plc
    "BIRD", # Allbirds, Inc.
    "NXC", # NUVEEN CALIFORNIA SELECT TAX FREE INCOME PORTFOLIO
    "TISI", # TEAM INC
    "ARMP", # Armata Pharmaceuticals, Inc.
    "PLBY", # PLBY Group, Inc.
    "ALRN", # Aileron Therapeutics, Inc.
    "CHRS", # Coherus BioSciences, Inc.
    "PLX", # Protalix BioTherapeutics, Inc.
    "ATMC", # ALPHATIME ACQUISITION CORP
    "VUZI", # Vuzix Corp
    "RSSS", # Research Solutions, Inc.
    "ESP", # ESPEY MFG & ELECTRONICS CORP
    "VMCA", # Valuence Merger Corp. I
    "VTGN", # Vistagen Therapeutics, Inc.
    "WEL", # Integrated Wellness Acquisition Corp
    "IRRX", # INTEGRATED RAIL & RESOURCES ACQUISITION CORP
    "INAQ", # Insight Acquisition Corp. /DE
    "OAKU", # Oak Woods Acquisition Corp
    "BLEU", # bleuacacia ltd
    "PETS", # PETMED EXPRESS INC
    "GLT", # Glatfelter Corp
    "LATG", # Chenghe Acquisition I Co.
    "PMVP", # PMV Pharmaceuticals, Inc.
    "LODE", # Comstock Inc.
    "SILC", # SILICOM LTD.
    "PNI", # PIMCO NEW YORK MUNICIPAL INCOME FUND II
    "DPCS", # DP Cap Acquisition Corp I
    "INVE", # Identiv, Inc.
    "LASE", # Laser Photonics Corp
    "WIMI", # WiMi Hologram Cloud Inc.
    "IMAB", # I-Mab
    "IKNA", # Ikena Oncology, Inc.
    "TBNK", # Territorial Bancorp Inc.
    "IMAQ", # International Media Acquisition Corp.
    "PUCK", # Goal Acquisitions Corp.
    "WW", # WW INTERNATIONAL, INC.
    "NPAB", # New Providence Acquisition Corp. II
    "MNOV", # MEDICINOVA INC
    "YTRA", # Yatra Online, Inc.
    "GAN", # GAN Ltd
    "IOBT", # IO Biotech, Inc.
    "OPAD", # Offerpad Solutions Inc.
    "BGSF", # BGSF, INC.
    "DBVT", # DBV Technologies S.A.
    "SLNG", # Stabilis Solutions, Inc.
    "OVID", # Ovid Therapeutics Inc.
    "GSIT", # GSI TECHNOLOGY INC
    "BRID", # BRIDGFORD FOODS CORP
    "TGAA", # Target Global Acquisition I Corp.
    "PED", # PEDEVCO CORP
    "JEQ", # ABRDN JAPAN EQUITY FUND, INC.
    "IRAA", # Iris Acquisition Corp
    "DHX", # DHI GROUP, INC.
    "WRAP", # WRAP TECHNOLOGIES, INC.
    "PRLH", # Pearl Holdings Acquisition Corp
    "NMS", # Nuveen Minnesota Quality Municipal Income Fund
    "MGYR", # Magyar Bancorp, Inc.
    "TCOA", # Zalatoris Acquisition Corp.
    "INCR", # Intercure Ltd.
    "PHUN", # Phunware, Inc.
    "VATE", # INNOVATE Corp.
    "VGZ", # VISTA GOLD CORP
    "DTF", # DTF TAX-FREE INCOME 2028 TERM FUND INC
    "ATMV", # AlphaVest Acquisition Corp.
    "FCO", # ABRDN GLOBAL INCOME FUND, INC.
    "HNNA", # HENNESSY ADVISORS INC
    "SBXC", # SilverBox Corp III
    "DMA", # Destra Multi-Alternative Fund
    "FNVT", # Finnovate Acquisition Corp.
    "SUP", # SUPERIOR INDUSTRIES INTERNATIONAL INC
    "CTMX", # CytomX Therapeutics, Inc.
    "MTC", # MMTec, Inc.
    "MCHX", # MARCHEX INC
    "AREC", # American Resources Corp
    "CBRG", # Chain Bridge I
    "LICN", # Lichen China Ltd
    "MIST", # Milestone Pharmaceuticals Inc.
    "PORT", # Southport Acquisition Corp
    "LSBK", # LAKE SHORE BANCORP, INC.
    "ALXO", # ALX ONCOLOGY HOLDINGS INC
    "AUID", # authID Inc.
    "OWLT", # Owlet, Inc.
    "OCAX", # OCA Acquisition Corp.
    "UBCP", # UNITED BANCORP INC /OH/
    "ZVIA", # Zevia PBC
    "IVCP", # Swiftmerge Acquisition Corp.
    "BOCN", # Blue Ocean Acquisition Corp
    "ASYS", # AMTECH SYSTEMS INC
    "NCTY", # The9 LTD
    "CLSD", # Clearside Biomedical, Inc.
    "AUBN", # AUBURN NATIONAL BANCORPORATION, INC
    "MSSA", # Metal Sky Star Acquisition Corp
    "SLS", # SELLAS Life Sciences Group, Inc.
    "DIT", # AMCON DISTRIBUTING CO
    "RAPT", # RAPT Therapeutics, Inc.
    "KLXE", # KLX Energy Services Holdings, Inc.
    "XTNT", # Xtant Medical Holdings, Inc.
    "BEEM", # Beam Global
    "LSF", # Laird Superfood, Inc.
    "CNF", # CNFinance Holdings Ltd.
    "CEV", # EATON VANCE CALIFORNIA MUNICIPAL INCOME TRUST
    "ECOR", # electroCore, Inc.
    "AVTE", # Aerovate Therapeutics, Inc.
    "MITA", # Coliseum Acquisition Corp.
    "REFR", # RESEARCH FRONTIERS INC
    "ZTEK", # Zentek Ltd.
    "DTC", # Solo Brands, Inc.
    "VLT", # Invesco High Income Trust II
    "NOVV", # Nova Vision Acquisition Corp
    "RGT", # ROYCE GLOBAL TRUST, INC.
    "AEAE", # AltEnergy Acquisition Corp
    "MGRM", # Monogram Technologies Inc.
    "BHAC", # Focus Impact BH3 Acquisition Co
    "FIAC", # Focus Impact Acquisition Corp.
    "GLV", # Clough Global Dividend & Income Fund
    "ELTK", # ELTEK LTD
    "ICCH", # ICC Holdings, Inc.
    "CLRB", # Cellectar Biosciences, Inc.
    "GCV", # GABELLI CONVERTIBLE & INCOME SECURITIES FUND INC
    "TYGO", # TIGO ENERGY, INC.
    "PGZ", # Principal Real Estate Income Fund
    "MODD", # Modular Medical, Inc.
    "ELVA", # Electrovaya Inc.
    "VANI", # Vivani Medical, Inc.
    "FRLA", # Fortune Rise Acquisition Corp
    "WPRT", # WESTPORT FUEL SYSTEMS INC.
    "HYPR", # Hyperfine, Inc.
    "IAE", # Voya Asia Pacific High Dividend Equity Income Fund
    "NB", # NIOCORP DEVELOPMENTS LTD
    "DIST", # Distoken Acquisition Corp
    "LILM", # Lilium N.V.
    "AE", # ADAMS RESOURCES & ENERGY, INC.
    "CTXR", # Citius Pharmaceuticals, Inc.
    "LTCH", # Latch, Inc.
    "NVAC", # NorthView Acquisition Corp
    "CLEU", # China Liberal Education Holdings Ltd
    "GLLI", # GLOBALINK INVESTMENT INC.
    "VTSI", # VirTra, Inc
    "TDUP", # ThredUp Inc.
    "PRLD", # Prelude Therapeutics Inc
    "HAIA", # Healthcare AI Acquisition Corp.
    "ZENV", # Zenvia Inc.
    "CEE", # CENTRAL & EASTERN EUROPE FUND, INC.
    "NHTC", # NATURAL HEALTH TRENDS CORP
    "MFH", # Mercurity Fintech Holding Inc.
    "SOTK", # SONO TEK CORP
    "FTCI", # FTC Solar, Inc.
    "FURY", # FURY GOLD MINES LTD
    "IROQ", # IF Bancorp, Inc.
    "STCN", # Steel Connect, Inc.
    "LVO", # LiveOne, Inc.
    "PPSI", # PIONEER POWER SOLUTIONS, INC.
    "IHTA", # Invesco High Income 2024 Target Term Fund
    "SYRS", # Syros Pharmaceuticals, Inc.
    "IOR", # INCOME OPPORTUNITY REALTY INVESTORS INC /TX/
    "FUSB", # FIRST US BANCSHARES, INC.
    "NTRB", # NutriBand Inc.
    "ENTX", # Entera Bio Ltd.
    "CULP", # CULP INC
    "LRFC", # Logan Ridge Finance Corp.
    "STEM", # STEM, INC.
    "SPRO", # Spero Therapeutics, Inc.
    "SDIG", # Stronghold Digital Mining, Inc.
    "OMGA", # Omega Therapeutics, Inc.
    "CXH", # MFS INVESTMENT GRADE MUNICIPAL TRUST
    "FOSL", # Fossil Group, Inc.
    "UAMY", # UNITED STATES ANTIMONY CORP
    "USAU", # U.S. GOLD CORP.
    "NDP", # TORTOISE ENERGY INDEPENDENCE FUND, INC.
    "KOSS", # KOSS CORP
    "FTII", # FutureTech II Acquisition Corp.
    "GOEV", # Canoo Inc.
    "MAIA", # MAIA Biotechnology, Inc.
    "QNCX", # Quince Therapeutics, Inc.
    "LOOP", # Loop Industries, Inc.
    "BEAT", # HeartBeam, Inc.
    "CNTB", # Connect Biopharma Holdings Ltd
    "CRGO", # Freightos Ltd
    "KTCC", # KEY TRONIC CORP
    "BYFC", # BROADWAY FINANCIAL CORP DE
    "NSPR", # InspireMD, Inc.
    "SATX", # SatixFy Communications Ltd.
    "FORA", # Forian Inc.
    "PNF", # PIMCO NEW YORK MUNICIPAL INCOME FUND
    "APT", # ALPHA PRO TECH LTD
    "MPU", # Mega Matrix Inc
    "LNSR", # LENSAR, Inc.
    "BKKT", # Bakkt Holdings, Inc.
    "HGBL", # Heritage Global Inc.
    "GANX", # Gain Therapeutics, Inc.
    "LPTH", # LIGHTPATH TECHNOLOGIES INC
    "YI", # 111, Inc.
    "LOAN", # MANHATTAN BRIDGE CAPITAL, INC
    "CLOE", # Clover Leaf Capital Corp.
    "PAVS", # Paranovus Entertainment Technology Ltd.
    "TOP", # TOP Financial Group Ltd
    "CRT", # CROSS TIMBERS ROYALTY TRUST
    "NA", # Nano Labs Ltd
    "MVST", # Microvast Holdings, Inc.
    "VRCA", # Verrica Pharmaceuticals Inc.
    "INLX", # INTELLINETICS, INC.
    "TORO", # TORO CORP.
    "RCON", # Recon Technology, Ltd
    "GBBK", # Global Blockchain Acquisition Corp.
    "LVLU", # Lulu's Fashion Lounge Holdings, Inc.
    "UG", # UNITED GUARDIAN INC
    "UPLD", # Upland Software, Inc.
    "MLSS", # MILESTONE SCIENTIFIC INC.
    "DTIL", # PRECISION BIOSCIENCES INC
    "STTK", # Shattuck Labs, Inc.
    "BOTJ", # BANK OF THE JAMES FINANCIAL GROUP INC
    "BEDU", # Bright Scholar Education Holdings Ltd
    "NVNO", # enVVeno Medical Corp
    "CCTS", # Cactus Acquisition Corp. 1 Ltd
    "RSF", # RiverNorth Capital & Income Fund, Inc.
    "FGB", # FIRST TRUST SPECIALTY FINANCE & FINANCIAL OPPORTUNITIES FUND
    "WFCF", # Where Food Comes From, Inc.
    "SQNS", # SEQUANS COMMUNICATIONS
    "EEA", # EUROPEAN EQUITY FUND, INC / MD
    "NSTS", # NSTS Bancorp, Inc.
    "ENZ", # ENZO BIOCHEM INC
    "CCEL", # CRYO CELL INTERNATIONAL INC
    "KRON", # Kronos Bio, Inc.
    "MDIA", # Mediaco Holding Inc.
    "HYMC", # HYCROFT MINING HOLDING CORP
    "ONDS", # Ondas Holdings Inc.
    "BMTX", # BM Technologies, Inc.
    "VCSA", # Vacasa, Inc.
    "JMM", # Nuveen Multi-Market Income Fund
    "SELF", # Global Self Storage, Inc.
    "BHM", # Bluerock Homes Trust, Inc.
    "PRE", # Prenetics Global Ltd
    "THTX", # Theratechnologies Inc.
    "SGRP", # SPAR Group, Inc.
    "KSCP", # Knightscope, Inc.
    "CVM", # CEL SCI CORP
    "TMTC", # TMT Acquisition Corp.
    "BAFN", # BayFirst Financial Corp.
    "BCOW", # 1895 Bancorp of Wisconsin, Inc. /MD/
    "ROCL", # Roth CH Acquisition V Co.
    "IMRX", # Immuneering Corp
    "CTSO", # Cytosorbents Corp
    "VNRX", # VOLITIONRX LTD
    "IPWR", # Ideal Power Inc.
    "MAQC", # Maquia Capital Acquisition Corp
    "UONE", # URBAN ONE, INC.
    "FTHM", # Fathom Holdings Inc.
    "ATNM", # Actinium Pharmaceuticals, Inc.
    "VOR", # Vor Biopharma Inc.
    "KULR", # KULR Technology Group, Inc.
    "KZR", # Kezar Life Sciences, Inc.
    "BEST", # BEST Inc.
    "BRAC", # Broad Capital Acquisition Corp
    "OPXS", # Optex Systems Holdings Inc
    "XLO", # Xilio Therapeutics, Inc.
    "NBST", # Newbury Street Acquisition Corp
    "CSBR", # CHAMPIONS ONCOLOGY, INC.
    "NDLS", # NOODLES & Co
    "SNAL", # Snail, Inc.
    "GEG", # Great Elm Group, Inc.
    "AHT", # ASHFORD HOSPITALITY TRUST INC
    "XPL", # SOLITARIO RESOURCES CORP.
    "LICY", # Li-Cycle Holdings Corp.
    "MGLD", # Marygold Companies, Inc.
    "CLRC", # ClimateRock
    "SCYX", # SCYNEXIS INC
    "EMCG", # Embrace Change Acquisition Corp.
    "RGS", # REGIS CORP
    "RFAC", # RF Acquisition Corp.
    "FBIO", # Fortress Biotech, Inc.
    "GROV", # Grove Collaborative Holdings, Inc.
    "ATRA", # Atara Biotherapeutics, Inc.
    "HHS", # HARTE HANKS INC
    "EDRY", # EuroDry Ltd.
    "LINK", # INTERLINK ELECTRONICS INC
    "PVL", # Permianville Royalty Trust
    "OCX", # Oncocyte Corp
    "FMY", # FIRST TRUST MORTGAGE INCOME FUND
    "AFMD", # Affimed N.V.
    "ANGH", # Anghami Inc
    "GRRR", # Gorilla Technology Group Inc.
    "HOUR", # Hour Loop, Inc
    "CLST", # Catalyst Bancorp, Inc.
    "AQU", # Aquaron Acquisition Corp.
    "WLGS", # WANG & LEE GROUP, Inc.
    "LUNA", # LUNA INNOVATIONS INC
    "DWSN", # DAWSON GEOPHYSICAL CO
    "CPTN", # Cepton, Inc.
    "GODN", # Golden Star Acquisition Corp
    "HOLO", # MicroCloud Hologram Inc.
    "LTRPA", # Liberty TripAdvisor Holdings, Inc.
    "FLNT", # Fluent, Inc.
    "UNCY", # Unicycive Therapeutics, Inc.
    "WAVE", # Eco Wave Power Global AB (publ)
    "CLNN", # Clene Inc.
    "FSI", # FLEXIBLE SOLUTIONS INTERNATIONAL INC
    "SHLT", # SHL TELEMEDICINE LTD
    "MARX", # Mars Acquisition Corp.
    "TARA", # Protara Therapeutics, Inc.
    "ICAD", # ICAD INC
    "ANEB", # Anebulo Pharmaceuticals, Inc.
    "DGHI", # Digihost Technology Inc.
    "IDN", # Intellicheck, Inc.
    "ZEPP", # Zepp Health Corp
    "ELTX", # Elicio Therapeutics, Inc.
    "MNPR", # Monopar Therapeutics
    "AADI", # Aadi Bioscience, Inc.
    "SOHO", # Sotherly Hotels Inc.
    "OSS", # ONE STOP SYSTEMS, INC.
    "LUCD", # Lucid Diagnostics Inc.
    "ALSA", # Alpha Star Acquisition Corp
    "FLUX", # Flux Power Holdings, Inc.
    "FKWL", # FRANKLIN WIRELESS CORP
    "AOGO", # Arogo Capital Acquisition Corp.
    "BMR", # Beamr Imaging Ltd.
    "BDL", # FLANIGANS ENTERPRISES INC
    "LVTX", # LAVA Therapeutics NV
    "PXS", # Pyxis Tankers Inc.
    "TCBS", # Texas Community Bancshares, Inc.
    "SPRU", # SPRUCE POWER HOLDING CORP
    "PRT", # PermRock Royalty Trust
    "STBX", # Starbox Group Holdings Ltd.
    "MATH", # Metalpha Technology Holding Ltd
    "IZEA", # IZEA Worldwide, Inc.
    "NXN", # NUVEEN NEW YORK SELECT TAX -FREE INCOME PORTFOLIO
    "NRT", # NORTH EUROPEAN OIL ROYALTY TRUST
    "CRWS", # CROWN CRAFTS INC
    "RPID", # RAPID MICRO BIOSYSTEMS, INC.
    "INTE", # Integral Acquisition Corp 1
    "OPHC", # OptimumBank Holdings, Inc.
    "NCSM", # NCS Multistage Holdings, Inc.
    "GLST", # Global Star Acquisition Inc.
    "NOTV", # Inotiv, Inc.
    "CFSB", # CFSB Bancorp, Inc. /MA/
    "BIVI", # BIOVIE INC.
    "RBOT", # Vicarious Surgical Inc.
    "VIVK", # Vivakor, Inc.
    "ASRV", # AMERISERV FINANCIAL INC /PA/
    "PRTS", # CarParts.com, Inc.
    "BNIX", # Bannix Acquisition Corp.
    "NTZ", # NATUZZI S P A
    "RFL", # Rafael Holdings, Inc.
    "FORL", # Four Leaf Acquisition Corp
    "BLAC", # Bellevue Life Sciences Acquisition Corp.
    "AXDX", # Accelerate Diagnostics, Inc
    "KACL", # Kairous Acquisition Corp. Ltd
    "AIRT", # AIR T INC
    "AGAE", # Allied Gaming & Entertainment Inc.
    "INTS", # INTENSITY THERAPEUTICS, INC.
    "MOBQ", # Mobiquity Technologies, Inc.
    "IPW", # iPower Inc.
    "YOTA", # Yotta Acquisition Corp
    "CREX", # CREATIVE REALITIES, INC.
    "DUET", # DUET Acquisition Corp.
    "FSEA", # First Seacoast Bancorp, Inc.
    "IMMX", # Immix Biopharma, Inc.
    "ICCM", # IceCure Medical Ltd.
    "ZDGE", # Zedge, Inc.
    "MLAC", # Mountain Lake Acquisition Corp.
    "RFIL", # R F INDUSTRIES LTD
    "DXR", # DAXOR CORP
    "ICMB", # Investcorp Credit Management BDC, Inc.
    "CLGN", # CollPlant Biotechnologies Ltd
    "PRPH", # ProPhase Labs, Inc.
    "BGI", # BIRKS GROUP INC.
    "ACHL", # Achilles Therapeutics plc
    "CVU", # CPI AEROSTRUCTURES INC
    "TECTP", # Tectonic Financial, Inc.
    "EYEN", # EYENOVIA, INC.
    "RLYB", # Rallybio Corp
    "XGN", # EXAGEN INC.
    "RAVE", # RAVE RESTAURANT GROUP, INC.
    "TACT", # TRANSACT TECHNOLOGIES INC
    "UCL", # uCloudlink Group Inc.
    "AGMH", # AGM GROUP HOLDINGS, INC.
    "RDI", # READING INTERNATIONAL INC
    "HSON", # Hudson Global, Inc.
    "JG", # Aurora Mobile Ltd
    "CLIR", # ClearSign Technologies Corp
    "DMYY", # dMY Squared Technology Group, Inc.
    "DSWL", # DESWELL INDUSTRIES INC
    "RAND", # RAND CAPITAL CORP
    "BWEN", # BROADWIND, INC.
    "APYX", # Apyx Medical Corp
    "NAAS", # NaaS Technology Inc.
    "SYT", # SYLA Technologies Co., Ltd.
    "WAVS", # Western Acquisition Ventures Corp.
    "CARM", # Carisma Therapeutics Inc.
    "DRRX", # DURECT CORP
    "XAIR", # Beyond Air, Inc.
    "EBON", # Ebang International Holdings Inc.
    "VYNE", # VYNE Therapeutics Inc.
    "MLGO", # MicroAlgo Inc.
    "FARM", # FARMER BROTHERS CO
    "SRZN", # Surrozen, Inc./DE
    "PXLW", # PIXELWORKS, INC
    "CALC", # CalciMedica, Inc.
    "DNMR", # Danimer Scientific, Inc.
    "DRCT", # Direct Digital Holdings, Inc.
    "LITB", # LightInTheBox Holding Co., Ltd.
    "CUBA", # HERZFELD CARIBBEAN BASIN FUND INC
    "MNDO", # MIND CTI LTD
    "INDO", # Indonesia Energy Corp Ltd
    "OKYO", # OKYO Pharma Ltd
    "HKIT", # HiTek Global Inc.
    "CENN", # Cenntro Inc.
    "HFBL", # Home Federal Bancorp, Inc. of Louisiana
    "IXHL", # Incannex Healthcare Inc.
    "WINV", # WinVest Acquisition Corp.
    "HUIZ", # Huize Holding Ltd
    "CNVS", # Cineverse Corp.
    "GRF", # EAGLE CAPITAL GROWTH FUND, INC.
    "PASG", # Passage BIO, Inc.
    "ARKR", # ARK RESTAURANTS CORP
    "GDST", # Goldenstone Acquisition Ltd.
    "USEG", # US ENERGY CORP
    "BHIL", # Benson Hill, Inc.
    "CLPS", # CLPS Inc
    "LEXX", # Lexaria Bioscience Corp.
    "MXE", # MEXICO EQUITY & INCOME FUND INC
    "RAYA", # Erayak Power Solution Group Inc.
    "NINE", # Nine Energy Service, Inc.
    "LUMO", # LUMOS PHARMA, INC.
    "USIO", # Usio, Inc.
    "CODX", # Co-Diagnostics, Inc.
    "BGFV", # BIG 5 SPORTING GOODS Corp
    "RVPH", # REVIVA PHARMACEUTICALS HOLDINGS, INC.
    "MCAG", # Mountain Crest Acquisition Corp. V
    "KALA", # KALA BIO, Inc.
    "CTRM", # Castor Maritime Inc.
    "MESA", # MESA AIR GROUP INC
    "HOOK", # HOOKIPA Pharma Inc.
    "JRSH", # Jerash Holdings (US), Inc.
    "AIXI", # Xiao-I Corp
    "ISDR", # ISSUER DIRECT CORP
    "KORE", # KORE Group Holdings, Inc.
    "DUOT", # DUOS TECHNOLOGIES GROUP, INC.
    "NXTC", # NextCure, Inc.
    "WTMA", # Welsbach Technology Metals Acquisition Corp.
    "CCLD", # CareCloud, Inc.
    "TOPS", # TOP SHIPS INC.
    "ARQQ", # Arqit Quantum Inc.
    "BRFH", # BARFRESH FOOD GROUP INC.
    "BLRX", # BioLineRx Ltd.
    "CMCT", # Creative Media & Community Trust Corp
    "WWR", # WESTWATER RESOURCES, INC.
    "ISPO", # Inspirato Inc
    "AUST", # Austin Gold Corp.
    "TLF", # TANDY LEATHER FACTORY INC
    "MRKR", # Marker Therapeutics, Inc.
    "MYNA", # Mynaric AG
    "EGF", # BlackRock Enhanced Government Fund, Inc.
    "DARE", # Dare Bioscience, Inc.
    "SJ", # Scienjoy Holding Corp
    "PET", # Wag! Group Co.
    "KPLT", # Katapult Holdings, Inc.
    "XOS", # Xos, Inc.
    "RENT", # Rent the Runway, Inc.
    "CMBM", # Cambium Networks Corp
    "GLBS", # GLOBUS MARITIME LTD
    "APWC", # ASIA PACIFIC WIRE & CABLE CORP LTD
    "PBBK", # PB Bankshares, Inc.
    "GTEC", # Greenland Technologies Holding Corp.
    "WYY", # WIDEPOINT CORP
    "PYN", # PIMCO NEW YORK MUNICIPAL INCOME FUND III
    "TPCS", # TECHPRECISION CORP
    "AP", # AMPCO PITTSBURGH CORP
    "CETY", # Clean Energy Technologies, Inc.
    "SNT", # Senstar Technologies Corp
    "AWRE", # AWARE INC /MA/
    "ELEV", # Elevation Oncology, Inc.
    "CCM", # Concord Medical Services Holdings Ltd
    "AAME", # ATLANTIC AMERICAN CORP
    "INUV", # Inuvo, Inc.
    "LIVE", # LIVE VENTURES Inc
    "OMIC", # Singular Genomics Systems, Inc.
    "GROW", # U S GLOBAL INVESTORS INC
    "SOND", # Sonder Holdings Inc.
    "NISN", # Nisun International Enterprise Development Group Co., Ltd
    "ASPS", # ALTISOURCE PORTFOLIO SOLUTIONS S.A.
    "NTWK", # NETSOL TECHNOLOGIES INC
    "VTVT", # vTv Therapeutics Inc.
    "FGF", # Fundamental Global Inc.
    "LTRN", # Lantern Pharma Inc.
    "FENG", # Phoenix New Media Ltd
    "ANTX", # AN2 Therapeutics, Inc.
    "ICLK", # iClick Interactive Asia Group Ltd
    "FEAM", # 5E Advanced Materials, Inc.
    "DECA", # Denali Capital Acquisition Corp.
    "DFLI", # Dragonfly Energy Holdings Corp.
    "NSYS", # NORTECH SYSTEMS INC
    "TURN", # 180 DEGREE CAPITAL CORP. /NY/
    "PMN", # ProMIS Neurosciences Inc.
    "SVT", # SERVOTRONICS INC /DE/
    "NXPL", # NextPlat Corp
    "CIF", # MFS INTERMEDIATE HIGH INCOME FUND
    "LGL", # LGL GROUP INC
    "FGEN", # FIBROGEN INC
    "OESX", # ORION ENERGY SYSTEMS, INC.
    "FTEK", # FUEL TECH, INC.
    "DYAI", # DYADIC INTERNATIONAL INC
    "MLEC", # Moolec Science SA
    "STIM", # Neuronetics, Inc.
    "EQ", # Equillium, Inc.
    "HYFM", # HYDROFARM HOLDINGS GROUP, INC.
    "INTG", # INTERGROUP CORP
    "DRIO", # DarioHealth Corp.
    "AKTX", # Akari Therapeutics Plc
    "CELU", # Celularity Inc
    "AACG", # ATA Creativity Global
    "SURG", # SurgePays, Inc.
    "SABS", # SAB Biotherapeutics, Inc.
    "OCEA", # Ocean Biomedical, Inc.
    "SYPR", # SYPRIS SOLUTIONS INC
    "ACXP", # Acurx Pharmaceuticals, Inc.
    "LGVN", # Longeveron Inc.
    "MIGI", # Mawson Infrastructure Group Inc.
    "IGTA", # Inception Growth Acquisition Ltd
    "ALGS", # Aligos Therapeutics, Inc.
    "IGC", # IGC Pharma, Inc.
    "BTCM", # BIT Mining Ltd
    "NTIP", # NETWORK-1 TECHNOLOGIES, INC.
    "LPCN", # Lipocine Inc.
    "GTIM", # Good Times Restaurants Inc.
    "FEMY", # FEMASYS INC
    "ITRM", # Iterum Therapeutics plc
    "NMTC", # NEUROONE MEDICAL TECHNOLOGIES Corp
    "OM", # Outset Medical, Inc.
    "ELBM", # Electra Battery Materials Corp
    "TOON", # Kartoon Studios, Inc.
    "HUDI", # Huadi International Group Co., Ltd.
    "ENLV", # Enlivex Therapeutics Ltd.
    "QOMO", # Qomolangma Acquisition Corp.
    "MIND", # MIND TECHNOLOGY, INC
    "KUKE", # Kuke Music Holding Ltd
    "BNR", # Burning Rock Biotech Ltd
    "DALN", # DallasNews Corp
    "ICCC", # IMMUCELL CORP /DE/
    "BANL", # CBL International Ltd
    "EVTV", # Envirotech Vehicles, Inc.
    "NAII", # NATURAL ALTERNATIVES INTERNATIONAL INC
    "BCTX", # BriaCell Therapeutics Corp.
    "SWVL", # Swvl Holdings Corp
    "SLNH", # Soluna Holdings, Inc
    "BTAI", # BioXcel Therapeutics, Inc.
    "HUDA", # Hudson Acquisition I Corp.
    "SCOR", # COMSCORE, INC.
    "INKT", # MiNK Therapeutics, Inc.
    "CGA", # China Green Agriculture, Inc.
    "UTSI", # UTSTARCOM HOLDINGS CORP.
    "JOB", # GEE Group Inc.
    "NXL", # Nexalin Technology, Inc.
    "GDTC", # CytoMed Therapeutics Ltd
    "FPAY", # FlexShopper, Inc.
    "CMMB", # Chemomab Therapeutics Ltd.
    "BTM", # Bitcoin Depot Inc.
    "BGXX", # Bright Green Corp
    "CKX", # CKX LANDS, INC.
    "GP", # GREENPOWER MOTOR Co INC.
    "GLYC", # GLYCOMIMETICS INC
    "PLUR", # Pluri Inc.
    "CRIS", # CURIS INC
    "UCAR", # U Power Ltd
    "PZG", # Paramount Gold Nevada Corp.
    "IRIX", # IRIDEX CORP
    "EPOW", # Sunrise New Energy Co., Ltd.
    "TRT", # TRIO-TECH INTERNATIONAL
    "GREE", # Greenidge Generation Holdings Inc.
    "FFIE", # FARADAY FUTURE INTELLIGENT ELECTRIC INC.
    "KNW", # KNOW LABS, INC.
    "DZSI", # DZS INC.
    "IZM", # ICZOOM Group Inc.
    "PSHG", # Performance Shipping Inc.
    "CVKD", # Cadrenal Therapeutics, Inc.
    "NOM", # NUVEEN MISSOURI QUALITY MUNICIPAL INCOME FUND
    "PTN", # PALATIN TECHNOLOGIES INC
    "CPSH", # CPS TECHNOLOGIES CORP/DE/
    "DAIO", # DATA I/O CORP
    "BNGO", # Bionano Genomics, Inc.
    "BOLT", # Bolt Biotherapeutics, Inc.
    "FEDU", # Four Seasons Education (Cayman) Inc.
    "DTST", # Data Storage Corp
    "IBIO", # iBio, Inc.
    "MXC", # MEXCO ENERGY CORP
    "GAME", # GameSquare Holdings, Inc.
    "MOGO", # Mogo Inc.
    "VHC", # VirnetX Holding Corp
    "TOI", # Oncology Institute, Inc.
    "POCI", # PRECISION OPTICS CORPORATION, INC.
    "LSTA", # LISATA THERAPEUTICS, INC.
    "ATER", # Aterian, Inc.
    "IINN", # Inspira Technologies OXY B.H.N. Ltd
    "NYC", # American Strategic Investment Co.
    "PYPD", # PolyPid Ltd.
    "TPST", # Tempest Therapeutics, Inc.
    "NRSN", # NeuroSense Therapeutics Ltd.
    "RETO", # ReTo Eco-Solutions, Inc.
    "ATIP", # ATI Physical Therapy, Inc.
    "RNXT", # RenovoRx, Inc.
    "KFFB", # Kentucky First Federal Bancorp
    "CXAI", # CXApp Inc.
    "VNCE", # VINCE HOLDING CORP.
    "MKTW", # MARKETWISE, INC.
    "GYRO", # Gyrodyne, LLC
    "WKSP", # Worksport Ltd
    "PIRS", # PIERIS PHARMACEUTICALS, INC.
    "UBX", # Unity Biotechnology, Inc.
    "SIF", # SIFCO INDUSTRIES INC
    "BPT", # BP PRUDHOE BAY ROYALTY TRUST
    "SHFS", # SHF Holdings, Inc.
    "JYD", # Jayud Global Logistics Ltd
    "XIN", # Xinyuan Real Estate Co., Ltd.
    "NRBO", # NeuroBo Pharmaceuticals, Inc.
    "RVP", # RETRACTABLE TECHNOLOGIES INC
    "SPRB", # SPRUCE BIOSCIENCES, INC.
    "APRE", # Aprea Therapeutics, Inc.
    "MOVE", # Movano Inc.
    "ANY", # Sphere 3D Corp.
    "UGRO", # urban-gro, Inc.
    "BIAF", # bioAffinity Technologies, Inc.
    "KIRK", # KIRKLAND'S, INC
    "CYTH", # Cyclo Therapeutics, Inc.
    "LOCL", # Local Bounti Corporation/DE
    "HTCR", # HeartCore Enterprises, Inc.
    "QMCO", # QUANTUM CORP /DE/
    "USEA", # United Maritime Corp
    "JZ", # Jianzhi Education Technology Group Co Ltd
    "MEIP", # MEI Pharma, Inc.
    "CMLS", # CUMULUS MEDIA INC
    "SWAG", # Stran & Company, Inc.
    "AQMS", # Aqua Metals, Inc.
    "NNVC", # NANOVIRICIDES, INC.
    "WKEY", # Wisekey International Holding S.A.
    "INAB", # IN8BIO, INC.
    "BTCS", # BTCS Inc.
    "ZKIN", # ZK International Group Co., Ltd.
    "BFRG", # BullFrog AI Holdings, Inc.
    "CVV", # CVD EQUIPMENT CORP
    "OCC", # OPTICAL CABLE CORP
    "RMCF", # Rocky Mountain Chocolate Factory, Inc.
    "AMS", # AMERICAN SHARED HOSPITAL SERVICES
    "TNXP", # Tonix Pharmaceuticals Holding Corp.
    "CGTX", # COGNITION THERAPEUTICS INC
    "JFU", # 9F Inc.
    "LUCY", # Innovative Eyewear Inc
    "FNCH", # Finch Therapeutics Group, Inc.
    "AREN", # Arena Group Holdings, Inc.
    "FLGC", # Flora Growth Corp.
    "BBGI", # BEASLEY BROADCAST GROUP INC
    "TKLF", # Yoshitsu Co., Ltd
    "ILAG", # Intelligent Living Application Group Inc.
    "AIRI", # AIR INDUSTRIES GROUP
    "EKSO", # EKSO BIONICS HOLDINGS, INC.
    "XELB", # XCel Brands, Inc.
    "EQS", # EQUUS TOTAL RETURN, INC.
    "BRN", # BARNWELL INDUSTRIES INC
    "COCP", # Cocrystal Pharma, Inc.
    "WKHS", # Workhorse Group Inc.
    "PLAG", # Planet Green Holdings Corp.
    "MHUA", # Meihua International Medical Technologies Co., Ltd.
    "CPOP", # Pop Culture Group Co., Ltd
    "NXGL", # NEXGEL, INC.
    "TXMD", # TherapeuticsMD, Inc.
    "LYRA", # Lyra Therapeutics, Inc.
    "KZIA", # KAZIA THERAPEUTICS LTD
    "CVR", # CHICAGO RIVET & MACHINE CO
    "FCUV", # FOCUS UNIVERSAL INC.
    "TOMZ", # TOMI Environmental Solutions, Inc.
    "APCX", # AppTech Payments Corp.
    "BSGM", # BioSig Technologies, Inc.
    "BHV", # BLACKROCK VIRGINIA MUNICIPAL BOND TRUST
    "EMKR", # EMCORE CORP
    "PEV", # PHOENIX MOTOR INC.
    "EDUC", # EDUCATIONAL DEVELOPMENT CORP
    "JVA", # COFFEE HOLDING CO INC
    "DTSS", # DATASEA INC.
    "WVVI", # WILLAMETTE VALLEY VINEYARDS INC
    "TAIT", # TAITRON COMPONENTS INC
    "SYBX", # SYNLOGIC, INC.
    "BOSC", # BOS BETTER ONLINE SOLUTIONS LTD
    "CARA", # Cara Therapeutics, Inc.
    "GOVX", # GeoVax Labs, Inc.
    "OXBR", # OXBRIDGE RE HOLDINGS Ltd
    "LIFW", # MSP Recovery, Inc.
    "WHLM", # Wilhelmina International, Inc.
    "MRNS", # MARINUS PHARMACEUTICALS, INC.
    "HLP", # Hongli Group Inc.
    "IHT", # INNSUITES HOSPITALITY TRUST
    "NERV", # Minerva Neurosciences, Inc.
    "SGMA", # SIGMATRON INTERNATIONAL INC
    "EZFL", # EzFill Holdings Inc
    "ATHA", # Athira Pharma, Inc.
    "CPIX", # CUMBERLAND PHARMACEUTICALS INC
    "PALT", # PALTALK, INC.
    "EDTK", # Skillful Craftsman Education Technology Ltd
    "COHN", # Cohen & Co Inc.
    "MGIH", # Millennium Group International Holdings Ltd
    "VRM", # Vroom, Inc.
    "TCS", # Container Store Group, Inc.
    "SEED", # Origin Agritech LTD
    "PWM", # Prestige Wealth Inc.
    "TRIB", # TRINITY BIOTECH PLC
    "HCWB", # HCW Biologics Inc.
    "CJJD", # China Jo-Jo Drugstores, Inc.
    "BHAT", # Blue Hat Interactive Entertainment Technology
    "NCRA", # NOCERA, INC.
    "GLBZ", # GLEN BURNIE BANCORP
    "AIM", # AIM ImmunoTech Inc.
    "COSM", # Cosmos Health Inc.
    "GVP", # GSE SYSTEMS INC
    "MOGU", # MOGU Inc.
    "SONM", # SONIM TECHNOLOGIES INC
    "MBOT", # Microbot Medical Inc.
    "SOS", # SOS Ltd
    "PT", # Pintec Technology Holdings Ltd
    "NEPH", # NEPHROS INC
    "GIGM", # GIGAMEDIA Ltd
    "TTOO", # T2 Biosystems, Inc.
    "RCG", # RENN Fund, Inc.
    "MRM", # Medirom Healthcare Technologies Inc.
    "YQ", # 17 Education & Technology Group Inc.
    "OPGN", # OPGEN INC
    "TENX", # TENAX THERAPEUTICS, INC.
    "VISL", # Vislink Technologies, Inc.
    "SLGL", # Sol-Gel Technologies Ltd.
    "BTOG", # BIT ORIGIN Ltd
    "GDC", # GD Culture Group Ltd
    "EVAX", # Evaxion Biotech A/S
    "CNFR", # Conifer Holdings, Inc.
    "OPTT", # Ocean Power Technologies, Inc.
    "MTEX", # MANNATECH INC
    "MTEK", # Maris Tech Ltd.
    "DUO", # Fangdd Network Group Ltd.
    "AWH", # Aspira Women's Health Inc.
    "NLSP", # NLS Pharmaceutics Ltd.
    "HUSA", # HOUSTON AMERICAN ENERGY CORP
    "CLRO", # CLEARONE INC
    "CWD", # CaliberCos Inc.
    "PMCB", # PharmaCyte Biotech, Inc.
    "NRXP", # NRX Pharmaceuticals, Inc.
    "VINE", # Fresh Vine Wine, Inc.
    "PMD", # PSYCHEMEDICS CORP
    "GNS", # Genius Group Ltd
    "MMV", # MultiMetaVerse Holdings Ltd
    "JZXN", # Jiuzi Holdings, Inc.
    "CANF", # Can-Fite BioPharma Ltd.
    "SOBR", # SOBR Safe, Inc.
    "ELSE", # ELECTRO SENSORS INC
    "ATHE", # ALTERITY THERAPEUTICS LTD
    "HUBC", # Hub Cyber Security Ltd.
    "MDRR", # Medalist Diversified REIT, Inc.
    "IMNN", # Imunon, Inc.
    "AEI", # Alset Inc.
    "IPA", # ImmunoPrecise Antibodies Ltd.
    "PHGE", # BiomX Inc.
    "ARBB", # ARB IOT Group Ltd
    "PETZ", # TDH Holdings, Inc.
    "MNTS", # Momentus Inc.
    "APLM", # Apollomics Inc.
    "MCVT", # Mill City Ventures III, Ltd
    "ICU", # SeaStar Medical Holding Corp
    "SSKN", # STRATA Skin Sciences, Inc.
    "MRAI", # Marpai, Inc.
    "GORO", # GOLD RESOURCE CORP
    "VRME", # VerifyMe, Inc.
    "DLPN", # Dolphin Entertainment, Inc.
    "GFAI", # Guardforce AI Co., Ltd.
    "VCIG", # VCI Global Ltd
    "VVOS", # Vivos Therapeutics, Inc.
    "VRAR", # Glimpse Group, Inc.
    "SPI", # SPI Energy Co., Ltd.
    "CUTR", # CUTERA INC
    "BIOR", # BIORA THERAPEUTICS, INC.
    "ASTC", # ASTROTECH Corp
    "XELA", # Exela Technologies, Inc.
    "SNSE", # Sensei Biotherapeutics, Inc.
    "OP", # OceanPal Inc.
    "CING", # Cingulate Inc.
    "CISS", # C3is Inc.
    "EVGN", # Evogene Ltd.
    "HTOO", # Fusion Fuel Green PLC
    "INDP", # Indaptus Therapeutics, Inc.
    "CLWT", # EURO TECH HOLDINGS CO LTD
    "CJET", # Chijet Motor Company, Inc.
    "SMSI", # SMITH MICRO SOFTWARE, INC.
    "AYTU", # AYTU BIOPHARMA, INC
    "STRR", # STAR EQUITY HOLDINGS, INC.
    "MULN", # MULLEN AUTOMOTIVE INC.
    "IMRN", # Immuron Ltd
    "BREA", # Brera Holdings PLC
    "BLIN", # Bridgeline Digital, Inc.
    "MTR", # MESA ROYALTY TRUST/TX
    "DXYN", # DIXIE GROUP INC
    "GRFX", # Graphex Group Ltd
    "XTLB", # XTL BIOPHARMACEUTICALS LTD
    "BOF", # BranchOut Food Inc.
    "RGF", # Real Good Food Company, Inc.
    "MBIO", # MUSTANG BIO, INC.
    "PETV", # PetVivo Holdings, Inc.
    "LAES", # SEALSQ Corp
    "ADXN", # Addex Therapeutics Ltd.
    "HOFV", # Hall of Fame Resort & Entertainment Co
    "KPRX", # KIORA PHARMACEUTICALS INC
    "EDSA", # Edesa Biotech, Inc.
    "IPDN", # Professional Diversity Network, Inc.
    "MSN", # EMERSON RADIO CORP
    "LITM", # Snow Lake Resources Ltd.
    "DOMH", # Dominari Holdings Inc.
    "VINC", # Vincerx Pharma, Inc.
    "RDHL", # RedHill Biopharma Ltd.
    "OMEX", # ODYSSEY MARINE EXPLORATION INC
    "AMPG", # AmpliTech Group, Inc.
    "BRTX", # BioRestorative Therapies, Inc.
    "WISA", # WISA TECHNOLOGIES, INC.
    "SBEV", # SPLASH BEVERAGE GROUP, INC.
    "GIPR", # GENERATION INCOME PROPERTIES, INC.
    "PAVM", # PAVmed Inc.
    "MEGL", # Magic Empire Global Ltd
    "ATIF", # ATIF Holdings Ltd
    "AWX", # AVALON HOLDINGS CORP
    "BTBD", # BT Brands, Inc.
    "GCTK", # Glucotrack, Inc.
    "FRSX", # Foresight Autonomous Holdings Ltd.
    "BCLI", # BRAINSTORM CELL THERAPEUTICS INC.
    "SIDU", # Sidus Space Inc.
    "SNTI", # Senti Biosciences, Inc.
    "SQFT", # Presidio Property Trust, Inc.
    "LIQT", # LIQTECH INTERNATIONAL INC
    "EEIQ", # EpicQuest Education Group International Ltd
    "ZAPP", # Zapp Electric Vehicles Group Ltd
    "BTCY", # BIOTRICITY INC.
    "JAGX", # Jaguar Health, Inc.
    "REED", # REED'S, INC.
    "HYZN", # Hyzon Motors Inc.
    "RVSN", # Rail Vision Ltd.
    "YJ", # Yunji Inc.
    "BLBX", # BLACKBOXSTOCKS INC.
    "LIDR", # AEye, Inc.
    "PRPO", # Precipio, Inc.
    "STRM", # STREAMLINE HEALTH SOLUTIONS INC.
    "ADD", # Color Star Technology Co., Ltd.
    "XWEL", # XWELL, Inc.
    "RVYL", # RYVYL Inc.
    "AIHS", # Senmiao Technology Ltd
    "GLTO", # Galecto, Inc.
    "DSS", # DSS, INC.
    "VRAX", # Virax Biolabs Group Ltd
    "FGI", # FGI Industries Ltd.
    "CISO", # CISO Global, Inc.
    "CARV", # CARVER BANCORP INC
    "TFFP", # TFF Pharmaceuticals, Inc.
    "HLGN", # Heliogen, Inc.
    "GDHG", # GOLDEN HEAVEN GROUP HOLDINGS LTD.
    "VCNX", # VACCINEX, INC.
    "AKTS", # Akoustis Technologies, Inc.
    "MOB", # Mobilicom Ltd
    "YGMZ", # MingZhu Logistics Holdings Ltd
    "UPXI", # UPEXI, INC.
    "CDIO", # Cardio Diagnostics Holdings, Inc.
    "ABVC", # ABVC BIOPHARMA, INC.
    "MWG", # Multi Ways Holdings Ltd
    "DPRO", # Draganfly Inc.
    "ENSC", # Ensysce Biosciences, Inc.
    "HIHO", # HIGHWAY HOLDINGS LTD
    "SNGX", # SOLIGENIX, INC.
    "STKH", # Steakholder Foods Ltd.
    "CTM", # Castellum, Inc.
    "LEDS", # SemiLEDs Corp
    "BCDA", # BioCardia, Inc.
    "SCKT", # SOCKET MOBILE, INC.
    "ARTW", # ARTS WAY MANUFACTURING CO INC
    "KRKR", # 36Kr Holdings Inc.
    "VERB", # Verb Technology Company, Inc.
    "WHLR", # Wheeler Real Estate Investment Trust, Inc.
    "GWAV", # Greenwave Technology Solutions, Inc.
    "OMH", # Ohmyhome Ltd
    "JXJT", # JX Luxventure Ltd
    "NURO", # NeuroMetrix, Inc.
    "PULM", # Pulmatrix, Inc.
    "CMAX", # CareMax, Inc.
    "RNAZ", # Transcode Therapeutics, Inc.
    "VIRX", # Viracta Therapeutics, Inc.
    "MARPS", # MARINE PETROLEUM TRUST
    "LMFA", # LM FUNDING AMERICA, INC.
    "HCTI", # Healthcare Triangle, Inc.
    "BFRI", # Biofrontera Inc.
    "COEP", # Coeptis Therapeutics Holdings, Inc.
    "OTRK", # Ontrak, Inc.
    "EGRX", # EAGLE PHARMACEUTICALS, INC.
    "ASNS", # ACTELIS NETWORKS INC
    "AMST", # Amesite Inc.
    "PSTV", # PLUS THERAPEUTICS, INC.
    "EJH", # E-Home Household Service Holdings Ltd
    "APM", # Aptorum Group Ltd
    "CYCN", # Cyclerion Therapeutics, Inc.
    "POLA", # Polar Power, Inc.
    "WAFU", # Wah Fu Education Group Ltd
    "MBRX", # Moleculin Biotech, Inc.
    "ZCMD", # Zhongchao Inc.
    "ANTE", # AIRNET TECHNOLOGY INC.
    "CYN", # Cyngn Inc.
    "CTCX", # Carmell Corp
    "EFOI", # ENERGY FOCUS, INC/DE
    "MGOL", # MGO Global Inc.
    "CELZ", # CREATIVE MEDICAL TECHNOLOGY HOLDINGS, INC.
    "CRKN", # Crown Electrokinetics Corp.
    "ALZN", # Alzamend Neuro, Inc.
    "ONVO", # ORGANOVO HOLDINGS, INC.
    "APTO", # Aptose Biosciences Inc.
    "GURE", # GULF RESOURCES, INC.
    "KAVL", # Kaival Brands Innovations Group, Inc.
    "ENG", # ENGLOBAL CORP
    "GSUN", # Golden Sun Health Technology Group Ltd
    "GRNQ", # Greenpro Capital Corp.
    "MRIN", # MARIN SOFTWARE INC
    "ENSV", # Enservco Corp
    "SRAX", # SRAX, Inc.
    "FBRX", # Forte Biosciences, Inc.
    "CHEK", # Check-Cap Ltd
    "GTBP", # GT Biopharma, Inc.
    "CREG", # Smart Powerr Corp.
    "CHNR", # CHINA NATURAL RESOURCES INC
    "LCFY", # Locafy Ltd
    "BENF", # Beneficient
    "FTFT", # Future FinTech Group Inc.
    "NXU", # Nxu, Inc.
    "SPCB", # SuperCom Ltd
    "KITT", # Nauticus Robotics, Inc.
    "REBN", # Reborn Coffee, Inc.
    "BMRA", # BIOMERICA INC
    "TPET", # Trio Petroleum Corp.
    "CNEY", # CN ENERGY GROUP. INC.
    "ADIL", # ADIAL PHARMACEUTICALS, INC.
    "VVPR", # VivoPower International PLC
    "XBIO", # Xenetic Biosciences, Inc.
    "UPC", # Universe Pharmaceuticals INC
    "MYNZ", # MAINZ BIOMED N.V.
    "MITQ", # MOVING iMAGE TECHNOLOGIES INC.
    "SNTG", # Sentage Holdings Inc.
    "XCUR", # EXICURE, INC.
    "GBR", # New Concept Energy, Inc.
    "MARK", # REMARK HOLDINGS, INC.
    "BNRG", # Brenmiller Energy Ltd.
    "GNPX", # Genprex, Inc.
    "ORGS", # Orgenesis Inc.
    "OCG", # Oriental Culture Holding LTD
    "PNBK", # PATRIOT NATIONAL BANCORP INC
    "AGRI", # AGRIFORCE GROWING SYSTEMS LTD.
    "ONFO", # Onfolio Holdings, Inc
    "GETR", # Getaround, Inc
    "INBS", # INTELLIGENT BIO SOLUTIONS INC.
    "HOTH", # Hoth Therapeutics, Inc.
    "YOSH", # Yoshiharu Global Co.
    "SSY", # SUNLINK HEALTH SYSTEMS INC
    "PRTG", # PORTAGE BIOTECH INC.
    "SGLY", # Singularity Future Technology Ltd.
    "BON", # Bon Natural Life Ltd
    "JEWL", # Adamas One Corp.
    "JCSE", # JE Cleantech Holdings Ltd
    "MGRX", # MANGOCEUTICALS, INC.
    "OST", # Ostin Technology Group Co., Ltd.
    "RKDA", # Arcadia Biosciences, Inc.
    "CMND", # Clearmind Medicine Inc.
    "SBFM", # Sunshine Biopharma Inc.
    "ERNA", # Eterna Therapeutics Inc.
    "LUXH", # LUXURBAN HOTELS INC.
    "CEAD", # CEA Industries Inc.
    "PRSO", # Peraso Inc.
    "SHPH", # Shuttle Pharmaceuticals Holdings, Inc.
    "AEMD", # AETHLON MEDICAL INC
    "IMTE", # Integrated Media Technology Ltd
    "AUMN", # Golden Minerals Co
    "PPBT", # PURPLE BIOTECH LTD.
    "AYRO", # AYRO, Inc.
    "BCAN", # Femto Technologies Inc.
    "SANW", # S&W Seed Co
    "STSS", # Sharps Technology Inc.
    "SILO", # Silo Pharma, Inc.
    "VS", # Versus Systems Inc.
    "INTZ", # INTRUSION INC
    "ADN", # ADVENT TECHNOLOGIES HOLDINGS, INC.
    "TGL", # TREASURE GLOBAL INC
    "UUU", # UNIVERSAL SECURITY INSTRUMENTS INC
    "NDRA", # ENDRA Life Sciences Inc.
    "CNSP", # CNS Pharmaceuticals, Inc.
    "EVOK", # Evoke Pharma Inc
    "LIXT", # LIXTE BIOTECHNOLOGY HOLDINGS, INC.
    "MSGM", # Motorsport Games Inc.
    "VEEE", # Twin Vee PowerCats, Co.
    "IMCC", # IM Cannabis Corp.
    "GLMD", # Galmed Pharmaceuticals Ltd.
    "POAI", # Predictive Oncology Inc.
    "DATS", # DatChat, Inc.
    "PIK", # KIDPIK CORP.
    "AEHL", # Antelope Enterprise Holdings Ltd
    "SISI", # SHINECO, INC.
    "AQB", # AQUABOUNTY TECHNOLOGIES INC
    "XRTX", # XORTX Therapeutics Inc.
    "XXII", # 22nd Century Group, Inc.
    "LKCO", # Luokung Technology Corp.
    "CYAN", # CYANOTECH CORP
    "LFLY", # Leafly Holdings, Inc. /DE
    "TIRX", # TIAN RUIXIANG HOLDINGS LTD
    "ENVB", # Enveric Biosciences, Inc.
    "AMBO", # Ambow Education Holding Ltd.
    "CPHI", # CHINA PHARMA HOLDINGS, INC.
    "BOXL", # Boxlight Corp
    "LTRY", # Lottery.com Inc.
    "ONCT", # Oncternal Therapeutics, Inc.
    "AFIB", # Acutus Medical, Inc.
    "LPTV", # Loop Media, Inc.
    "VINO", # Gaucho Group Holdings, Inc.
    "PCSA", # Processa Pharmaceuticals, Inc.
    "IDAI", # T Stamp Inc
    "SNPX", # Synaptogenix, Inc.
    "FRES", # Fresh2 Group Ltd
    "MDJH", # MDJM LTD
    "KTTA", # Pasithea Therapeutics Corp.
    "JWEL", # Jowell Global Ltd.
    "CNET", # ZW Data Action Technologies Inc.
    "AGFY", # Agrify Corp
    "ATXG", # ADDENTAX GROUP CORP.
    "ATNF", # 180 Life Sciences Corp.
    "FORD", # Forward Industries, Inc.
    "FRZA", # Forza X1, Inc.
    "KXIN", # Kaixin Holdings
    "QNRX", # Quoin Pharmaceuticals, Ltd.
    "SNAX", # STRYVE FOODS, INC.
    "WATT", # Energous Corp
    "PW", # Power REIT
    "CTHR", # CHARLES & COLVARD LTD
    "SYTA", # Siyata Mobile Inc.
    "SBIG", # SpringBig Holdings, Inc.
    "AZTR", # Azitra, Inc.
    "IFBD", # Infobird Co., Ltd
    "PALI", # PALISADE BIO, INC.
    "BKYI", # BIO KEY INTERNATIONAL INC
    "OBLG", # Oblong, Inc.
    "LXEH", # Lixiang Education Holding Co. Ltd.
    "GENE", # GENETIC TECHNOLOGIES LTD
    "SNOA", # Sonoma Pharmaceuticals, Inc.
    "ARTL", # ARTELO BIOSCIENCES, INC.
    "HEPA", # Hepion Pharmaceuticals, Inc.
    "PTPI", # Petros Pharmaceuticals, Inc.
    "AIMD", # Ainos, Inc.
    "NCNA", # NuCana plc
    "LIPO", # LIPELLA PHARMACEUTICALS INC.
    "OLB", # OLB GROUP, INC.
    "IVDA", # Iveda Solutions, Inc.
    "BDRX", # Biodexa Pharmaceuticals Plc
    "INM", # InMed Pharmaceuticals Inc.
    "NBY", # NovaBay Pharmaceuticals, Inc.
    "VLCN", # Volcon, Inc.
    "VRPX", # Virpax Pharmaceuticals, Inc.
    "DGLY", # DIGITAL ALLY, INC.
    "APVO", # Aptevo Therapeutics Inc.
    "OCTO", # Eightco Holdings Inc.
    "ISPC", # iSpecimen Inc.
    "NVOS", # Novo Integrated Sciences, Inc.
    "ATXI", # AVENUE THERAPEUTICS, INC.
    "WLDS", # Wearable Devices Ltd.
    "TTNP", # TITAN PHARMACEUTICALS INC
    "BPTH", # BIO-PATH HOLDINGS, INC.
    "NVFY", # Nova Lifestyle, Inc.
    "OGEN", # ORAGENICS INC
    "RHE", # REGIONAL HEALTH PROPERTIES, INC
    "ALBT", # Avalon GloboCare Corp.
    "AUUD", # AUDDIA INC.
    "ASTI", # Ascent Solar Technologies, Inc.
    "BNOX", # BIONOMICS LIMITED/FI
    "TCRT", # Alaunos Therapeutics, Inc.
    "NUWE", # Nuwellis, Inc.
    "BTTR", # Better Choice Co Inc.
    "REVB", # REVELATION BIOSCIENCES, INC.
    "LYT", # Lytus Technologies Holdings PTV. Ltd.
    "TOVX", # Theriva Biologics, Inc.
    "GRI", # GRI BIO, Inc.
    "FAMI", # Farmmi, Inc.
    "ASST", # Asset Entities Inc.
    "SONX", # Sonendo, Inc.
    "MTNB", # Matinas BioPharma Holdings, Inc.
    "SOPA", # SOCIETY PASS INCORPORATED.
    "BAOS", # Baosheng Media Group Holdings Ltd
    "MTEM", # Molecular Templates, Inc.
    "RELI", # Reliance Global Group, Inc.
    "JFBR", # Jeffs' Brands Ltd
    "SONN", # Sonnet BioTherapeutics Holdings, Inc.
    "TAOP", # Taoping Inc.
    "VERO", # Venus Concept Inc.
    "SNES", # SenesTech, Inc.
    "AREB", # AMERICAN REBEL HOLDINGS INC
    "GRTX", # Galera Therapeutics, Inc.
    "RSLS", # ReShape Lifesciences Inc.
    "EZGO", # EZGO Technologies Ltd.
    "HSCS", # HeartSciences Inc.
    "BBLG", # Bone Biologics Corp
    "VMAR", # Vision Marine Technologies Inc.
    "PTIX", # Protagenic Therapeutics, Inc.new
    "PHIO", # Phio Pharmaceuticals Corp.
    "EDBL", # Edible Garden AG Inc
    "QLGN", # Qualigen Therapeutics, Inc.
    "WNW", # Meiwu Technology Co Ltd
    "SBET", # SharpLink Gaming, Inc.
    "ADTX", # Aditxt, Inc.
    "SPRC", # SciSparc Ltd.
    "WINT", # WINDTREE THERAPEUTICS INC /DE/
    "TBIO", # Telesis Bio Inc.
    "ITP", # IT TECH PACKAGING, INC.
    "NVVE", # Nuvve Holding Corp.
    "SINT", # Sintx Technologies, Inc.
    "SLRX", # Salarius Pharmaceuticals, Inc.
    "FRGT", # Freight Technologies, Inc.
    "UAVS", # AgEagle Aerial Systems Inc.
    "XPON", # Expion360 Inc.
    "SXTC", # China SXT Pharmaceuticals, Inc.
    "ZVSA", # ZyVersa Therapeutics, Inc.
    "TNON", # Tenon Medical, Inc.
    "TBLT", # Toughbuilt Industries, Inc
    "AKAN", # AKANDA CORP.
    "YCBD", # cbdMD, Inc.
    "SGBX", # SAFE & GREEN HOLDINGS CORP.
    "ALLR", # Allarity Therapeutics, Inc.
    "DRMA", # Dermata Therapeutics, Inc.
    "EAST", # Eastside Distilling, Inc.
    "BURU", # Nuburu, Inc.
    "BACK", # IMAC Holdings, Inc.
    "CYTO", # Altamira Therapeutics Ltd.
    "BQ", # Boqii Holding Ltd
    "TPHS", # Trinity Place Holdings Inc.
    "ACON", # Aclarion, Inc.
    "PBLA", # Panbela Therapeutics, Inc.
    "APDN", # APPLIED DNA SCIENCES INC
    "OMQS", # OMNIQ Corp.
    "WORX", # SCWorx Corp.
    "HSDT", # HELIUS MEDICAL TECHNOLOGIES, INC.
    "FOXO", # FOXO TECHNOLOGIES INC.
    "TIVC", # Tivic Health Systems, Inc.
    "KRBP", # Kiromic Biopharma, Inc.
    "UK", # Ucommune International Ltd
    "AVGR", # Avinger Inc
    "NCPL", # Netcapital Inc.
    "GNLN", # Greenlane Holdings, Inc.
    "SVRE", # SaverOne 2014 Ltd.
    "MYSZ", # My Size, Inc.
    "TRVN", # TREVENA INC
    "PKBO", # Peak Bio, Inc.
    "STAF", # Staffing 360 Solutions, Inc.
    "TRNR", # Interactive Strength, Inc.
    "TC", # TuanChe Ltd
    "PMVC", # PMV Consumer Acquisition Corp.
    "KWE", # KWESST Micro Systems Inc.
    "SXTP", # 60 DEGREES PHARMACEUTICALS, INC.
    "NAOV", # NanoVibronix, Inc.
    "CWBR", # CohBar, Inc.
    "BJDX", # Bluejay Diagnostics, Inc.
    "CYCC", # Cyclacel Pharmaceuticals, Inc.
    "LGMK", # LogicMark, Inc.
    "LGHL", # Lion Group Holding Ltd
    "PEGY", # Pineapple Energy Inc.
    "TANH", # TANTECH HOLDINGS LTD
    "PRFX", # PAINREFORM LTD.
    "SMX", # SMX (Security Matters) Public Ltd Co
    "MINM", # MINIM, INC.
    "PXMD", # PaxMedica, Inc.
    "MCOM", # micromobility.com Inc.
    "DBGI", # Digital Brands Group, Inc.
    "DYNT", # DYNATRONICS CORP
    "MVLA", # Movella Holdings Inc.
    "TCBP", # TC BioPharm (Holdings) plc
    "BSFC", # Blue Star Foods Corp.
    "SEEL", # SEELOS THERAPEUTICS, INC.
    "YTEN", # YIELD10 BIOSCIENCE, INC.
    "EFSH", # 1847 Holdings LLC
    "CUEN", # Cuentas Inc.
    "NEXI", # NexImmune, Inc.
    "IONM", # Assure Holdings Corp.
    "MGAM", # Mobile Global Esports, Inc.
    "BIMI", # BIMI Holdings Inc.
    "HPCO", # Hempacco Co., Inc.
    "CETX", # CEMTREX INC
    "RIBT", # RiceBran Technologies
    "EBET", # EBET, Inc.
    "ELYS", # Elys BMG Group, Inc.
    "STAB", # Statera Biopharma, Inc.
    "AWIN", # AERWINS Technologies Inc.
    "THMO", # ThermoGenesis Holdings, Inc.
    "NMRD", # Nemaura Medical Inc.
    "BBIG", # Vinco Ventures, Inc.
    "GROM", # Grom Social Enterprises, Inc.
    "SMFL", # SMART FOR LIFE, INC.
    "ELOX", # Eloxx Pharmaceuticals, Inc.
    "NRUC", # NATIONAL RURAL UTILITIES COOPERATIVE FINANCE CORP /DC/
    "HTIA", # National Healthcare Properties, Inc.
    "IBIT", # iShares Bitcoin Trust ETF
    "FXC", # Invesco CurrencyShares Canadian Dollar Trust
    "GLDM", # World Gold Trust
    "AAAU", # Goldman Sachs Physical Gold ETF
    "GLTR", # abrdn Precious Metals Basket ETF Trust
    "TFSA", # Terra Income Fund 6, LLC
    "PLTM", # GraniteShares Platinum Trust
    "PPLT", # abrdn Platinum ETF Trust
    "DEFI", # Tidal Commodities Trust I
    "TETEU", # Technology & Telecommunication Acquisition Corp
    "UNL", # United States 12 Month Natural Gas Fund, LP
    "QVCD", # QVC INC
    "BNO", # United States Brent Oil Fund, LP
    "UUP", # Invesco DB US Dollar Index Bullish Fund
    "FXF", # Invesco CurrencyShares Swiss Franc Trust
    "IAUM", # iShares Gold Trust Micro
    "IPB", # MERRILL LYNCH DEPOSITOR INC INDEXPLUS TRUST SERIES 2003-1
    "GJS", # STRATS(SM) Trust for Goldman Sachs Group Securities, Series 2006-2
    "GJO", # STRATS SM TRUST FOR WAL-MART STORES, INC. SECURITIES, SERIES 2005-4
    "PYT", # PPLUS Trust Series GSC-2
    "GJR", # STRATS(SM) Trust for Procter & Gamble Securities, Series 2006-1
    "FXB", # Invesco CurrencyShares British Pound Sterling Trust
    "FXA", # Invesco CurrencyShares Australian Dollar Trust
    "ELC", # ENTERGY LOUISIANA, LLC
    "CHSCP", # CHS INC
    "OUNZ", # VanEck Merk Gold ETF
    "FGDL", # Franklin Templeton Holdings Trust
    "PALL", # abrdn Palladium ETF Trust
    "KTH", # STRUCTURED PRODUCTS CORP CORTS TR FOR PECO ENERGY CAP TR III
    "TPTA", # Terra Property Trust, Inc.
    "UGA", # United States Gasoline Fund, LP
    "USL", # United States 12 Month Oil Fund, LP
    "SIVR", # abrdn Silver ETF Trust
    "SGOL", # abrdn Gold ETF Trust
    "UDN", # INVESCO DB US DOLLAR INDEX BEARISH FUND
    "WEIX", # Dynamic Shares Trust
    "KTN", # STRUCTURED PRODUCTS CORP CRED ENHANCE CORTS TR FOR AON CAP A
    "GJT", # STRATS(SM) Trust for Allstate Corp Securities, Series 2006-3
    "GJP", # STRATS(SM) TRUST FOR DOMINION RESOURCES, INC. SECURITIES, SERIES 2005-6
    "BAR", # GraniteShares Gold Trust
    "CTBB", # QWEST CORP
    "JBK", # LEHMAN ABS CORP GOLDMAN SACHS CAP 1 SEC BACKED SER 2004-6
    "GJH", # STRATS SM TRUST FOR U S CELL CORP SEC SERIES 2004 6
    "GOOG", # Alphabet Inc.
    "TBB", # AT&T INC.
    "CCZ", # COMCAST CORP
    "BBDO", # BANK BRADESCO
    "SOJC", # SOUTHERN CO
    "FWONK", # Liberty Media Corp
    "FWONA", # Liberty Media Corp
    "FOX", # Fox Corp
    "FITBI", # FIFTH THIRD BANCORP
    "NWS", # NEWS CORP
    "Z", # ZILLOW GROUP, INC.
    "ACGLO", # ARCH CAPITAL GROUP LTD.
    "FNGD", # BANK OF MONTREAL /CAN/
    "LBRDK", # Liberty Broadband Corp
    "LBTYB", # Liberty Global Ltd.
    "AGNCN", # AGNC Investment Corp.
    "AGNCM", # AGNC Investment Corp.
    "RZB", # REINSURANCE GROUP OF AMERICA INC
    "PSNYW", # Polestar Automotive Holding UK PLC
    "PARAA", # Paramount Global
    "LBTYK", # Liberty Global Ltd.
    "CMSA", # CMS ENERGY CORP
    "UNMA", # Unum Group
    "JSM", # NAVIENT CORP
    "VIST", # Vista Energy, S.A.B. de C.V.
    "BHFAL", # Brighthouse Financial, Inc.
    "NYCB", # NEW YORK COMMUNITY BANCORP, INC.
    "RUSHB", # RUSH ENTERPRISES INC TX
    "DTW", # DTE ENERGY CO
    "BHFAP", # Brighthouse Financial, Inc.
    "SLMBP", # SLM Corp
    "WTFCM", # WINTRUST FINANCIAL CORP
    "UA", # Under Armour, Inc.
    "ESGRP", # Enstar Group LTD
    "VLYPP", # VALLEY NATIONAL BANCORP
    "ESGRO", # Enstar Group LTD
    "VLYPO", # VALLEY NATIONAL BANCORP
    "HOVNP", # HOVNANIAN ENTERPRISES INC
    "BATRK", # Atlanta Braves Holdings, Inc.
    "CENTA", # CENTRAL GARDEN & PET CO
    "LILAK", # Liberty Latin America Ltd.
    "WLYB", # JOHN WILEY & SONS, INC.
    "FISK", # Empire State Realty OP, L.P.
    "STER", # Sterling Check Corp.
    "OGCP", # Empire State Realty OP, L.P.
    "MHLA", # Maiden Holdings, Ltd.
    "HCXY", # Hercules Capital, Inc.
    "NYMTN", # NEW YORK MORTGAGE TRUST INC
    "BELFB", # BEL FUSE INC /NJ
    "PETQ", # PetIQ, Inc.
    "KELYB", # KELLY SERVICES INC
    "SHCR", # Sharecare, Inc.
    "BH", # Biglari Holdings Inc.
    "DGICB", # DONEGAL GROUP INC
    "ECCX", # Eagle Point Credit Co Inc.
    "OXLCO", # Oxford Lane Capital Corp.
    "AIRTP", # AIR T INC
    "LANDM", # GLADSTONE LAND Corp
    "SENEB", # Seneca Foods Corp
    "GAINL", # GLADSTONE INVESTMENT CORPORATIONDE
    "APLMW", # Apollomics Inc.
    "LANDP", # GLADSTONE LAND Corp
    "QRTEB", # Qurate Retail, Inc.
    "ENO", # ENTERGY NEW ORLEANS, LLC
    "SRNE", # Sorrento Therapeutics, Inc.
    "LTRPB", # Liberty TripAdvisor Holdings, Inc.
    "PHYT", # Pyrophyte Acquisition Corp.
    "RDIB", # READING INTERNATIONAL INC
    "FATBB", # Fat Brands, Inc
    "SOHOO", # Sotherly Hotels Inc.
    "FANH", # FANHUA INC.
    "CDAQ", # Compass Digital Acquisition Corp.
    "SOHOB", # Sotherly Hotels Inc.
    "SOHON", # Sotherly Hotels Inc.
    "BKSC", # BANK OF SOUTH CAROLINA CORP
    "TCBC", # TC Bancshares, Inc.
    "TETE", # Technology & Telecommunication Acquisition Corp
    "ZIVO", # Zivo Bioscience, Inc.
    "CULL", # Cullman Bancorp, Inc. /MD/
    "OFED", # Oconee Federal Financial Corp.
    "FFBW", # FFBW, Inc. /MD/
    "UONEK", # URBAN ONE, INC.
    "LLAP", # Terran Orbital Corp
    "CIZN", # CITIZENS HOLDING CO /MS/
    "VSAC", # VISION SENSING ACQUISITION CORP.
    "MSVB", # Mid-Southern Bancorp, Inc.
    "AATC", # AUTOSCOPE TECHNOLOGIES CORP
    "ACST", # Grace Therapeutics, Inc.
    "GBNY", # Generations Bancorp NY, Inc.
    "OCUP", # Opus Genetics, Inc.
    "AVHI", # Achari Ventures Holdings Corp. I
    "FBIOP", # Fortress Biotech, Inc.
    "WVVIP", # WILLAMETTE VALLEY VINEYARDS INC
    "AFGC", # AMERICAN FINANCIAL GROUP INC
    "CYCCP", # Cyclacel Pharmaceuticals, Inc.
    "WHLRD", # Wheeler Real Estate Investment Trust, Inc.
    "SEAC", # SEACHANGE INTERNATIONAL INC
    "TVE", # Tennessee Valley Authority
    "TVC", # Tennessee Valley Authority
    "VAXX", # Vaxxinity, Inc.
    "SALM", # SALEM MEDIA GROUP, INC. /DE/
    "NUZE", # NuZee, Inc.
    "FXLV", # F45 Training Holdings Inc.
    "FRTX", # Fresh Tracks Therapeutics, Inc.
    "GHSI", # Guardion Health Sciences, Inc.
    "GRTS", # Gritstone bio, Inc.
    "RBCN", # Rubicon Technology, Inc.
    "PIXY", # ShiftPixy, Inc.
    "INVO", # NAYA Biosciences, Inc.
    "TLIS", # Talis Biomedical Corp
    "VEV", # VICINITY MOTOR CORP
    "CETXP", # CEMTREX INC
    "IDEX", # IDEANOMICS, INC.
    "SVVC", # Firsthand Technology Value Fund, Inc.
    "WHLRP", # Wheeler Real Estate Investment Trust, Inc.
    "PRST", # Presto Automation Inc.
    "MOBBW", # Mobilicom Ltd
    "USDP", # USD Partners LP
    "BLPH", # Bellerophon Therapeutics, Inc.
    "VIVE", # VIVEVE MEDICAL, INC.
    "GMBL", # ESPORTS ENTERTAINMENT GROUP, INC.
    "SCPS", # Scopus BioPharma Inc.
    "ALPP", # ALPINE 4 HOLDINGS, INC.
    "CALA", # Calithera Biosciences, Inc.
    "OXBRW", # OXBRIDGE RE HOLDINGS Ltd
    "EFTR", # eFFECTOR Therapeutics, Inc.
    "TCON", # Tracon Pharmaceuticals, Inc.
    "AMPE", # Ampio Pharmaceuticals, Inc.
    "COMS", # COMSovereign Holding Corp.
    "HALL", # HALLMARK FINANCIAL SERVICES INC
    "EVLO", # Evelo Biosciences, Inc.
    "ASPU", # ASPEN GROUP, INC.
    "MOTS", # Motus GI Holdings, Inc.
    "ARDS", # Aridis Pharmaceuticals, Inc.
    "CMRA", # Comera Life Sciences Holdings, Inc.
    "WTER", # ALKALINE WATER Co INC
    "NAVB", # NAVIDEA BIOPHARMACEUTICALS, INC.
    "AIMDW", # Ainos, Inc.
    "LILMW", # Lilium N.V.
    "NXPLW", # NextPlat Corp
    "PRLHU", # Pearl Holdings Acquisition Corp
    "PRLHW", # Pearl Holdings Acquisition Corp
    "GECCO", # Great Elm Capital Corp.
    "CLRCR", # ClimateRock
    "CLRCU", # ClimateRock
    "CLRCW", # ClimateRock
    "QSIAW", # Quantum-Si Inc
    "TBLAW", # Taboola.com Ltd.
    "BLACR", # Bellevue Life Sciences Acquisition Corp.
    "BLACU", # Bellevue Life Sciences Acquisition Corp.
    "BLACW", # Bellevue Life Sciences Acquisition Corp.
    "CLNNW", # Clene Inc.
    "GFAIW", # Guardforce AI Co., Ltd.
    "ARBEW", # Arbe Robotics Ltd.
    "CSWCZ", # CAPITAL SOUTHWEST CORP
    "PNFPP", # PINNACLE FINANCIAL PARTNERS INC
    "KITTW", # Nauticus Robotics, Inc.
    "AIMAU", # Aimfinity Investment Corp. I
    "AIMAW", # Aimfinity Investment Corp. I
    "AIMBU", # Aimfinity Investment Corp. I
    "MTEKW", # Maris Tech Ltd.
    "LGHLW", # Lion Group Holding Ltd
    "CTDD", # QWEST CORP
    "HSPOR", # Horizon Space Acquisition I Corp.
    "HSPOU", # Horizon Space Acquisition I Corp.
    "HSPOW", # Horizon Space Acquisition I Corp.
    "ALCYU", # Alchemy Investments Acquisition Corp 1
    "ALCYW", # Alchemy Investments Acquisition Corp 1
    "BNH", # BROOKFIELD Corp /ON/
    "BNJ", # BROOKFIELD Corp /ON/
    "AMPGW", # AmpliTech Group, Inc.
    "RNWWW", # ReNew Energy Global plc
    "KWESW", # KWESST Micro Systems Inc.
    "BLEUR", # bleuacacia ltd
    "BLEUU", # bleuacacia ltd
    "BLEUW", # bleuacacia ltd
    "GMBLP", # ESPORTS ENTERTAINMENT GROUP, INC.
    "GMBLW", # ESPORTS ENTERTAINMENT GROUP, INC.
    "GMBLZ", # ESPORTS ENTERTAINMENT GROUP, INC.
    "SBBA", # Scorpio Tankers Inc.
    "LATGU", # Chenghe Acquisition I Co.
    "BYNOU", # byNordic Acquisition Corp
    "BYNOW", # byNordic Acquisition Corp
    "AVPTW", # AvePoint, Inc.
    "GLDI", # CREDIT SUISSE AG
    "SLVO", # CREDIT SUISSE AG
    "USOI", # CREDIT SUISSE AG
    "RFACR", # RF Acquisition Corp.
    "RFACU", # RF Acquisition Corp.
    "RFACW", # RF Acquisition Corp.
    "WAFDP", # WAFD INC
    "RSVRW", # Reservoir Media, Inc.
    "CRGOW", # Freightos Ltd
    "GRABW", # Grab Holdings Ltd
    "MSSAR", # Metal Sky Star Acquisition Corp
    "MSSAU", # Metal Sky Star Acquisition Corp
    "MSSAW", # Metal Sky Star Acquisition Corp
    "METCB", # Ramaco Resources, Inc.
    "METCL", # Ramaco Resources, Inc.
    "ISPOW", # Inspirato Inc
    "DTSTW", # Data Storage Corp
    "VIASP", # Via Renewables, Inc.
    "BROGW", # Brooge Energy Ltd
    "DUETU", # DUET Acquisition Corp.
    "DUETW", # DUET Acquisition Corp.
    "SCLXW", # Scilex Holding Co
    "DDT", # DILLARD'S, INC.
    "MCAAU", # Mountain & Co. I Acquisition Corp.
    "MCAAW", # Mountain & Co. I Acquisition Corp.
    "CITEU", # Cartica Acquisition Corp
    "CITEW", # Cartica Acquisition Corp
    "ATMCR", # ALPHATIME ACQUISITION CORP
    "ATMCU", # ALPHATIME ACQUISITION CORP
    "ATMCW", # ALPHATIME ACQUISITION CORP
    "BWNB", # Babcock & Wilcox Enterprises, Inc.
    "BWSN", # Babcock & Wilcox Enterprises, Inc.
    "GDSTR", # Goldenstone Acquisition Ltd.
    "GDSTU", # Goldenstone Acquisition Ltd.
    "GDSTW", # Goldenstone Acquisition Ltd.
    "LFLYW", # Leafly Holdings, Inc. /DE
    "TRINL", # Trinity Capital Inc.
    "SCCC", # Sachem Capital Corp.
    "SCCD", # Sachem Capital Corp.
    "SCCE", # Sachem Capital Corp.
    "SCCF", # Sachem Capital Corp.
    "SCCG", # Sachem Capital Corp.
    "SACC", # Sachem Capital Corp.
    "AEFC", # AEGON LTD.
    "OXLCL", # Oxford Lane Capital Corp.
    "OXLCN", # Oxford Lane Capital Corp.
    "INVZW", # Innoviz Technologies Ltd.
    "OXLCP", # Oxford Lane Capital Corp.
    "OXLCZ", # Oxford Lane Capital Corp.
    "PIIIW", # P3 Health Partners Inc.
    "HTIBP", # National Healthcare Properties, Inc.
    "MBINM", # Merchants Bancorp
    "MBINN", # Merchants Bancorp
    "MBINO", # Merchants Bancorp
    "SVIIR", # Spring Valley Acquisition Corp. II
    "SVIIU", # Spring Valley Acquisition Corp. II
    "SVIIW", # Spring Valley Acquisition Corp. II
    "PFXNZ", # PhenixFIN Corp
    "IPXXW", # Inflection Point Acquisition Corp. II
    "IPXXU", # Inflection Point Acquisition Corp. II
    "OCSAW", # Oculis Holding AG
    "KPLTW", # Katapult Holdings, Inc.
    "FATBP", # Fat Brands, Inc
    "FATBW", # Fat Brands, Inc
    "ORGNW", # Origin Materials, Inc.
    "SBFMW", # Sunshine Biopharma Inc.
    "BRACR", # Broad Capital Acquisition Corp
    "BRACU", # Broad Capital Acquisition Corp
    "PFH", # PRUDENTIAL FINANCIAL INC
    "PRH", # PRUDENTIAL FINANCIAL INC
    "PRS", # PRUDENTIAL FINANCIAL INC
    "BENFW", # Beneficient
    "NAMSW", # NewAmsterdam Pharma Co N.V.
    "BEPH", # Brookfield Renewable Partners L.P.
    "BEPI", # Brookfield Renewable Partners L.P.
    "KMPB", # KEMPER Corp
    "MCOMW", # micromobility.com Inc.
    "BPOPM", # POPULAR, INC.
    "SABSW", # SAB Biotherapeutics, Inc.
    "THCPU", # Thunder Bridge Capital Partners IV, Inc.
    "THCPW", # Thunder Bridge Capital Partners IV, Inc.
    "COEPW", # Coeptis Therapeutics Holdings, Inc.
    "DPCSU", # DP Cap Acquisition Corp I
    "DPCSW", # DP Cap Acquisition Corp I
    "PETVW", # PetVivo Holdings, Inc.
    "SKGRW", # SK Growth Opportunities Corp
    "SKGRU", # SK Growth Opportunities Corp
    "CRESW", # CRESUD INC
    "PTIXW", # Protagenic Therapeutics, Inc.new
    "UKOMW", # Ucommune International Ltd
    "INAQU", # Insight Acquisition Corp. /DE
    "INAQW", # Insight Acquisition Corp. /DE
    "BZFDW", # BuzzFeed, Inc.
    "FTIIU", # FutureTech II Acquisition Corp.
    "FTIIW", # FutureTech II Acquisition Corp.
    "NVVEW", # Nuvve Holding Corp.
    "FGFPP", # Fundamental Global Inc.
    "HBANM", # HUNTINGTON BANCSHARES INC /MD/
    "HBANP", # HUNTINGTON BANCSHARES INC /MD/
    "HBANL", # HUNTINGTON BANCSHARES INC /MD/
    "CCLDO", # CareCloud, Inc.
    "CCLDP", # CareCloud, Inc.
    "PROCW", # Procaps Group, S.A.
    "BWBBP", # Bridgewater Bancshares Inc
    "ADVWW", # Advantage Solutions Inc.
    "NRSNW", # NeuroSense Therapeutics Ltd.
    "INBKZ", # First Internet Bancorp
    "IGTAR", # Inception Growth Acquisition Ltd
    "IGTAU", # Inception Growth Acquisition Ltd
    "IGTAW", # Inception Growth Acquisition Ltd
    "PRSTW", # Presto Automation Inc.
    "KACLR", # Kairous Acquisition Corp. Ltd
    "KACLU", # Kairous Acquisition Corp. Ltd
    "KACLW", # Kairous Acquisition Corp. Ltd
    "GGROW", # Gogoro Inc.
    "BTBDW", # BT Brands, Inc.
    "OCCIN", # OFS Credit Company, Inc.
    "OCCIO", # OFS Credit Company, Inc.
    "OTRKP", # Ontrak, Inc.
    "IVCBU", # Investcorp Europe Acquisition Corp I
    "IVCBW", # Investcorp Europe Acquisition Corp I
    "BKDT", # Brookdale Senior Living Inc.
    "SATLW", # Satellogic Inc.
    "BDRY", # Amplify Commodity Trust
    "BWET", # Amplify Commodity Trust
    "SXTPW", # 60 DEGREES PHARMACEUTICALS, INC.
    "ATMP", # BARCLAYS BANK PLC
    "DJP", # BARCLAYS BANK PLC
    "VXZ", # BARCLAYS BANK PLC
    "VXX", # BARCLAYS BANK PLC
    "GRN", # BARCLAYS BANK PLC
    "ARBKL", # Argo Blockchain Plc
    "SBIGW", # SpringBig Holdings, Inc.
    "GIPRW", # GENERATION INCOME PROPERTIES, INC.
    "SWVLW", # Swvl Holdings Corp
    "OFSSH", # OFS Capital Corp
    "NXLIW", # Nexalin Technology, Inc.
    "ECXWW", # ECARX Holdings Inc.
    "PAVMZ", # PAVmed Inc.
    "EFSCP", # ENTERPRISE FINANCIAL SERVICES CORP
    "SOJD", # SOUTHERN CO
    "SOJE", # SOUTHERN CO
    "PFTAU", # Perception Capital Corp. III
    "PFTAW", # Perception Capital Corp. III
    "RCB", # Ready Capital Corp
    "RCC", # Ready Capital Corp
    "YOTAR", # Yotta Acquisition Corp
    "YOTAU", # Yotta Acquisition Corp
    "YOTAW", # Yotta Acquisition Corp
    "TNONW", # Tenon Medical, Inc.
    "BCSAU", # Blockchain Coinvestors Acquisition Corp. I
    "BCSAW", # Blockchain Coinvestors Acquisition Corp. I
    "FFIEW", # FARADAY FUTURE INTELLIGENT ELECTRIC INC.
    "STSSW", # Sharps Technology Inc.
    "AGQ", # ProShares Trust II
    "BOIL", # ProShares Trust II
    "EUO", # ProShares Trust II
    "GLL", # ProShares Trust II
    "VIXM", # ProShares Trust II
    "VIXY", # ProShares Trust II
    "YCL", # ProShares Trust II
    "YCS", # ProShares Trust II
    "ZSL", # ProShares Trust II
    "SVXY", # ProShares Trust II
    "UCO", # ProShares Trust II
    "UGL", # ProShares Trust II
    "ULE", # ProShares Trust II
    "UVXY", # ProShares Trust II
    "KOLD", # ProShares Trust II
    "SCO", # ProShares Trust II
    "CLOER", # Clover Leaf Capital Corp.
    "CLOEU", # Clover Leaf Capital Corp.
    "RCKTW", # ROCKET PHARMACEUTICALS, INC.
    "SNCRL", # SYNCHRONOSS TECHNOLOGIES INC
    "AQNB", # ALGONQUIN POWER & UTILITIES CORP.
    "GEGGL", # Great Elm Group, Inc.
    "MSBIP", # Midland States Bancorp, Inc.
    "PLAOU", # Patria Latin American Opportunity Acquisition Corp.
    "PLAOW", # Patria Latin American Opportunity Acquisition Corp.
    "ARKOW", # ARKO Corp.
    "VGASW", # Verde Clean Fuels, Inc.
    "ZIONL", # ZIONS BANCORPORATION, NATIONAL ASSOCIATION /UT/
    "ZIONO", # ZIONS BANCORPORATION, NATIONAL ASSOCIATION /UT/
    "ZIONP", # ZIONS BANCORPORATION, NATIONAL ASSOCIATION /UT/
    "FCNCO", # FIRST CITIZENS BANCSHARES INC /DE/
    "FCNCP", # FIRST CITIZENS BANCSHARES INC /DE/
    "LIFWW", # MSP Recovery, Inc.
    "LIFWZ", # MSP Recovery, Inc.
    "CDZIP", # CADIZ INC
    "FRLAU", # Fortune Rise Acquisition Corp
    "FRLAW", # Fortune Rise Acquisition Corp
    "AGNCL", # AGNC Investment Corp.
    "AGNCO", # AGNC Investment Corp.
    "AGNCP", # AGNC Investment Corp.
    "RZC", # REINSURANCE GROUP OF AMERICA INC
    "GOVXW", # GeoVax Labs, Inc.
    "MBNKP", # MEDALLION FINANCIAL CORP
    "QRTEP", # Qurate Retail, Inc.
    "ANGHW", # Anghami Inc
    "MLECW", # Moolec Science SA
    "JSPRW", # Jasper Therapeutics, Inc.
    "HUBCW", # Hub Cyber Security Ltd.
    "HUBCZ", # Hub Cyber Security Ltd.
    "HTOOW", # Fusion Fuel Green PLC
    "OXSQG", # Oxford Square Capital Corp.
    "OXSQZ", # Oxford Square Capital Corp.
    "XELAP", # Exela Technologies, Inc.
    "MGR", # AFFILIATED MANAGERS GROUP, INC.
    "MGRB", # AFFILIATED MANAGERS GROUP, INC.
    "MGRD", # AFFILIATED MANAGERS GROUP, INC.
    "BPYPM", # Brookfield Property Partners L.P.
    "BPYPN", # Brookfield Property Partners L.P.
    "BPYPO", # Brookfield Property Partners L.P.
    "IINNW", # Inspira Technologies OXY B.H.N. Ltd
    "TETEW", # Technology & Telecommunication Acquisition Corp
    "IRAAU", # Iris Acquisition Corp
    "IRAAW", # Iris Acquisition Corp
    "FOSLL", # Fossil Group, Inc.
    "DFLIW", # Dragonfly Energy Holdings Corp.
    "ACONW", # Aclarion, Inc.
    "NXGLW", # NEXGEL, INC.
    "CPTNW", # Cepton, Inc.
    "ACABU", # Atlantic Coastal Acquisition Corp. II
    "ACABW", # Atlantic Coastal Acquisition Corp. II
    "ONYXU", # Onyx Acquisition Co. I
    "ONYXW", # Onyx Acquisition Co. I
    "ALVOW", # Alvotech
    "AUROW", # Aurora Innovation, Inc.
    "MOBQW", # Mobiquity Technologies, Inc.
    "AVHIU", # Achari Ventures Holdings Corp. I
    "AVHIW", # Achari Ventures Holdings Corp. I
    "LIXTW", # LIXTE BIOTECHNOLOGY HOLDINGS, INC.
    "RELIW", # Reliance Global Group, Inc.
    "BANFP", # BANCFIRST CORP /OK/
    "RENEU", # Cartesian Growth Corp II
    "RENEW", # Cartesian Growth Corp II
    "SHCRW", # Sharecare, Inc.
    "PWUPU", # PowerUp Acquisition Corp.
    "PWUPW", # PowerUp Acquisition Corp.
    "IVCPU", # Swiftmerge Acquisition Corp.
    "IVCPW", # Swiftmerge Acquisition Corp.
    "ADNWW", # ADVENT TECHNOLOGIES HOLDINGS, INC.
    "NCPLW", # Netcapital Inc.
    "CCNEP", # CNB FINANCIAL CORP/PA
    "CMSC", # CMS ENERGY CORP
    "CMSD", # CMS ENERGY CORP
    "BEATW", # HeartBeam, Inc.
    "SEATW", # Vivid Seats Inc.
    "RVPHW", # REVIVA PHARMACEUTICALS HOLDINGS, INC.
    "DHCNI", # DIVERSIFIED HEALTHCARE TRUST
    "DHCNL", # DIVERSIFIED HEALTHCARE TRUST
    "EMCGW", # Embrace Change Acquisition Corp.
    "EMCGR", # Embrace Change Acquisition Corp.
    "EMCGU", # Embrace Change Acquisition Corp.
    "LFMDP", # LifeMD, Inc.
    "SVIX", # VS Trust
    "UVIX", # VS Trust
    "EVGRU", # Evergreen Corp
    "EVGRW", # Evergreen Corp
    "BTMWW", # Bitcoin Depot Inc.
    "SQLLW", # ATLANTIC INTERNATIONAL CORP.
    "BIAFW", # bioAffinity Technologies, Inc.
    "FITBO", # FIFTH THIRD BANCORP
    "FITBP", # FIFTH THIRD BANCORP
    "GDEVW", # GDEV Inc.
    "DTB", # DTE ENERGY CO
    "DTG", # DTE ENERGY CO
    "SSSSL", # SURO CAPITAL CORP.
    "SLNHP", # Soluna Holdings, Inc
    "QVCC", # QVC INC
    "MNTSW", # Momentus Inc.
    "GLLIR", # GLOBALINK INVESTMENT INC.
    "GLLIU", # GLOBALINK INVESTMENT INC.
    "GLLIW", # GLOBALINK INVESTMENT INC.
    "SREA", # SEMPRA
    "CXAIW", # CXApp Inc.
    "BAERW", # Bridger Aerospace Group Holdings, Inc.
    "LVROW", # Lavoro Ltd
    "TELZ", # TELLURIAN INC. /DE/
    "CDROW", # Codere Online Luxembourg, S.A.
    "JFBRW", # Jeffs' Brands Ltd
    "KKRS", # KKR & Co. Inc.
    "ONBPP", # OLD NATIONAL BANCORP /IN/
    "ONBPO", # OLD NATIONAL BANCORP /IN/
    "IMPPP", # Imperial Petroleum Inc./Marshall Islands
    "ZIVOW", # Zivo Bioscience, Inc.
    "WLDSW", # Wearable Devices Ltd.
    "NIOBW", # NIOCORP DEVELOPMENTS LTD
    "SHFSW", # SHF Holdings, Inc.
    "BLDEW", # Blade Air Mobility, Inc.
    "WSBCP", # WESBANCO INC
    "BFRGW", # BullFrog AI Holdings, Inc.
    "CSLMR", # CSLM ACQUISITION CORP.
    "CSLMU", # CSLM ACQUISITION CORP.
    "CSLMW", # CSLM ACQUISITION CORP.
    "LBRDP", # Liberty Broadband Corp
    "LTRYW", # Lottery.com Inc.
    "SLDPW", # Solid Power, Inc.
    "PPYAU", # Papaya Growth Opportunity Corp. I
    "PPYAW", # Papaya Growth Opportunity Corp. I
    "RUMBW", # Rumble Inc.
    "VRMEW", # VerifyMe, Inc.
    "GODNU", # Golden Star Acquisition Corp
    "GODNR", # Golden Star Acquisition Corp
    "LCFYW", # Locafy Ltd
    "ATCOL", # Atlas Corp.
    "WTMAR", # Welsbach Technology Metals Acquisition Corp.
    "WTMAU", # Welsbach Technology Metals Acquisition Corp.
    "OAKUU", # Oak Woods Acquisition Corp
    "OAKUW", # Oak Woods Acquisition Corp
    "OAKUR", # Oak Woods Acquisition Corp
    "AOGOU", # Arogo Capital Acquisition Corp.
    "AOGOW", # Arogo Capital Acquisition Corp.
    "DCOMP", # Dime Community Bancshares, Inc. /NY/
    "CINGW", # Cingulate Inc.
    "HROWL", # HARROW, INC.
    "HROWM", # HARROW, INC.
    "HWCPZ", # HANCOCK WHITNEY CORP
    "KTTAW", # Pasithea Therapeutics Corp.
    "HPKEW", # HighPeak Energy, Inc.
    "DGP", # DEUTSCHE BANK AKTIENGESELLSCHAFT
    "DGZ", # DEUTSCHE BANK AKTIENGESELLSCHAFT
    "DZZ", # DEUTSCHE BANK AKTIENGESELLSCHAFT
    "MVSTW", # Microvast Holdings, Inc.
    "SRZNW", # Surrozen, Inc./DE
    "DATSW", # DatChat, Inc.
    "SNAXW", # STRYVE FOODS, INC.
    "LUCYW", # Innovative Eyewear Inc
    "PUCKU", # Goal Acquisitions Corp.
    "PUCKW", # Goal Acquisitions Corp.
    "GHIXU", # Gores Holdings IX, Inc.
    "GHIXW", # Gores Holdings IX, Inc.
    "GREEL", # Greenidge Generation Holdings Inc.
    "SYTAW", # Siyata Mobile Inc.
    "WTFCP", # WINTRUST FINANCIAL CORP
    "EVLVW", # Evolv Technologies Holdings, Inc.
    "RVSNW", # Rail Vision Ltd.
    "TGAAU", # Target Global Acquisition I Corp.
    "TGAAW", # Target Global Acquisition I Corp.
    "GATEU", # Marblegate Acquisition Corp.
    "GATEW", # Marblegate Acquisition Corp.
    "CDIOW", # Cardio Diagnostics Holdings, Inc.
    "FGIWW", # FGI Industries Ltd.
    "FIACU", # Focus Impact Acquisition Corp.
    "FIACW", # Focus Impact Acquisition Corp.
    "AUUDW", # AUDDIA INC.
    "LSEAW", # Landsea Homes Corp
    "BIPH", # Brookfield Infrastructure Partners L.P.
    "BIPI", # Brookfield Infrastructure Partners L.P.
    "AEAEU", # AltEnergy Acquisition Corp
    "AEAEW", # AltEnergy Acquisition Corp
    "TFINP", # Triumph Financial, Inc.
    "ATMVR", # AlphaVest Acquisition Corp.
    "ATMVU", # AlphaVest Acquisition Corp.
    "APCXW", # AppTech Payments Corp.
    "GRRRW", # Gorilla Technology Group Inc.
    "FRMEP", # FIRST MERCHANTS CORP
    "SURGW", # SurgePays, Inc.
    "POWWP", # AMMO, INC.
    "INTEU", # Integral Acquisition Corp 1
    "INTEW", # Integral Acquisition Corp 1
    "UHGWW", # United Homes Group, Inc.
    "CURIW", # CuriosityStream Inc.
    "CUBB", # Customers Bancorp, Inc.
    "RWAYL", # Runway Growth Finance Corp.
    "RWAYZ", # Runway Growth Finance Corp.
    "NEOVW", # NeoVolta Inc.
    "DECAU", # Denali Capital Acquisition Corp.
    "DECAW", # Denali Capital Acquisition Corp.
    "NESRW", # National Energy Services Reunited Corp.
    "SONDW", # Sonder Holdings Inc.
    "ADSEW", # Ads-Tec Energy Public Ltd Co
    "AREBW", # AMERICAN REBEL HOLDINGS INC
    "SAT", # SARATOGA INVESTMENT CORP.
    "SAY", # SARATOGA INVESTMENT CORP.
    "SAZ", # SARATOGA INVESTMENT CORP.
    "SAJ", # SARATOGA INVESTMENT CORP.
    "TCBPW", # TC BioPharm (Holdings) plc
    "ASTLW", # Algoma Steel Group Inc.
    "CIFRW", # Cipher Mining Inc.
    "XOSWW", # Xos, Inc.
    "OCFCP", # OCEANFIRST FINANCIAL CORP
    "REVBW", # REVELATION BIOSCIENCES, INC.
    "BHACU", # Focus Impact BH3 Acquisition Co
    "BHACW", # Focus Impact BH3 Acquisition Co
    "LANDO", # GLADSTONE LAND Corp
    "AIZN", # ASSURANT, INC.
    "CANE", # Teucrium Commodity Trust
    "SOYB", # Teucrium Commodity Trust
    "TAGS", # Teucrium Commodity Trust
    "WEAT", # Teucrium Commodity Trust
    "CORN", # Teucrium Commodity Trust
    "CTCXW", # Carmell Corp
    "ASBA", # ASSOCIATED BANC-CORP
    "SDAWW", # SunCar Technology Group Inc.
    "TBC", # AT&T INC.
    "ARGD", # Argo Group International Holdings, Inc.
    "GLSTR", # Global Star Acquisition Inc.
    "GLSTU", # Global Star Acquisition Inc.
    "GLSTW", # Global Star Acquisition Inc.
    "FORLW", # Four Leaf Acquisition Corp
    "FORLU", # Four Leaf Acquisition Corp
    "HNNAZ", # HENNESSY ADVISORS INC
    "HCVIU", # Hennessy Capital Investment Corp. VI
    "HCVIW", # Hennessy Capital Investment Corp. VI
    "BBLGW", # Bone Biologics Corp
    "ATLCL", # Atlanticus Holdings Corp
    "ATLCP", # Atlanticus Holdings Corp
    "MAQCU", # Maquia Capital Acquisition Corp
    "MAQCW", # Maquia Capital Acquisition Corp
    "DISTR", # Distoken Acquisition Corp
    "DISTW", # Distoken Acquisition Corp
    "NRXPW", # NRX Pharmaceuticals, Inc.
    "UZD", # UNITED STATES CELLULAR CORP
    "UZE", # UNITED STATES CELLULAR CORP
    "UZF", # UNITED STATES CELLULAR CORP
    "GBBKR", # Global Blockchain Acquisition Corp.
    "GBBKW", # Global Blockchain Acquisition Corp.
    "ONFOW", # Onfolio Holdings, Inc
    "CMAXW", # CareMax, Inc.
    "TALKW", # Talkspace, Inc.
    "OPINL", # OFFICE PROPERTIES INCOME TRUST
    "LUNRW", # Intuitive Machines, Inc.
    "GSMGW", # Cheer Holding, Inc.
    "IMTXW", # Immatics N.V.
    "FGBIP", # First Guaranty Bancshares, Inc.
    "CPER", # United States Commodity Index Funds Trust
    "USCI", # United States Commodity Index Funds Trust
    "HTLFP", # HEARTLAND FINANCIAL USA INC
    "NWTNW", # NWTN, Inc.
    "SMXWW", # SMX (Security Matters) Public Ltd Co
    "CEADW", # CEA Industries Inc.
    "NETDU", # Nabors Energy Transition Corp. II
    "CHSCL", # CHS INC
    "CHSCM", # CHS INC
    "CHSCN", # CHS INC
    "CHSCO", # CHS INC
    "GOODN", # GLADSTONE COMMERCIAL CORP
    "GOODO", # GLADSTONE COMMERCIAL CORP
    "EUDAW", # EUDA Health Holdings Ltd
    "WHLRL", # Wheeler Real Estate Investment Trust, Inc.
    "SWAGW", # Stran & Company, Inc.
    "TMCWW", # TMC the metals Co Inc.
    "HOFVW", # Hall of Fame Resort & Entertainment Co
    "CGABL", # Carlyle Group Inc.
    "SFB", # STIFEL FINANCIAL CORP
    "DUKB", # Duke Energy CORP
    "HYZNW", # Hyzon Motors Inc.
    "TCBIO", # TEXAS CAPITAL BANCSHARES INC/TX
    "RGTIW", # Rigetti Computing, Inc.
    "LEXXW", # Lexaria Bioscience Corp.
    "OCAXU", # OCA Acquisition Corp.
    "OCAXW", # OCA Acquisition Corp.
    "AFGD", # AMERICAN FINANCIAL GROUP INC
    "AFGE", # AMERICAN FINANCIAL GROUP INC
    "AFGB", # AMERICAN FINANCIAL GROUP INC
    "WALDW", # Waldencast plc
    "DRMAW", # Dermata Therapeutics, Inc.
    "EDBLW", # Edible Garden AG Inc
    "STRRP", # STAR EQUITY HOLDINGS, INC.
    "ALSAR", # Alpha Star Acquisition Corp
    "ALSAU", # Alpha Star Acquisition Corp
    "ALSAW", # Alpha Star Acquisition Corp
    "ATNFW", # 180 Life Sciences Corp.
    "CMPOW", # CompoSecure, Inc.
    "CORZW", # Core Scientific, Inc./tx
    "AQUNR", # Aquaron Acquisition Corp.
    "AQUNU", # Aquaron Acquisition Corp.
    "WGSWW", # GeneDx Holdings Corp.
    "DRTSW", # Alpha Tau Medical Ltd.
    "NOVVR", # Nova Vision Acquisition Corp
    "NOVVU", # Nova Vision Acquisition Corp
    "NOVVW", # Nova Vision Acquisition Corp
    "GAINN", # GLADSTONE INVESTMENT CORPORATIONDE
    "GAINZ", # GLADSTONE INVESTMENT CORPORATIONDE
    "UNOV", # Earth Science Tech, Inc.
    "MCAGR", # Mountain Crest Acquisition Corp. V
    "MCAGU", # Mountain Crest Acquisition Corp. V
    "AFRIW", # Forafric Global PLC
    "BCTXW", # BriaCell Therapeutics Corp.
    "CELUW", # Celularity Inc
    "PCTTU", # PureCycle Technologies, Inc.
    "PCTTW", # PureCycle Technologies, Inc.
    "EVGOW", # EVgo Inc.
    "IVDAW", # Iveda Solutions, Inc.
    "PGYWW", # Pagaya Technologies Ltd.
    "CNOBP", # ConnectOne Bancorp, Inc.
    "HTZWW", # HERTZ GLOBAL HOLDINGS, INC
    "CYTHW", # Cyclo Therapeutics, Inc.
    "BHFAM", # Brighthouse Financial, Inc.
    "BHFAN", # Brighthouse Financial, Inc.
    "BHFAO", # Brighthouse Financial, Inc.
    "HAIAU", # Healthcare AI Acquisition Corp.
    "HAIAW", # Healthcare AI Acquisition Corp.
    "USGOW", # U.S. GoldMining Inc.
    "PRENW", # Prenetics Global Ltd
    "MMVWW", # MultiMetaVerse Holdings Ltd
    "OCEAW", # Ocean Biomedical, Inc.
    "HTFB", # Horizon Technology Finance Corp
    "HTFC", # Horizon Technology Finance Corp
    "IMAQR", # International Media Acquisition Corp.
    "IMAQU", # International Media Acquisition Corp.
    "IMAQW", # International Media Acquisition Corp.
    "MYPSW", # PLAYSTUDIOS, Inc.
    "XOMAO", # XOMA Royalty Corp
    "XOMAP", # XOMA Royalty Corp
    "ZAPPW", # Zapp Electric Vehicles Group Ltd
    "EICA", # Eagle Point Income Co Inc.
    "HSCSW", # HeartSciences Inc.
    "TLGYU", # TLGY ACQUISITION CORP
    "TLGYW", # TLGY ACQUISITION CORP
    "FCRX", # Crescent Capital BDC, Inc.
    "BOWNU", # Bowen Acquisition Corp
    "HUDAR", # Hudson Acquisition I Corp.
    "HUDAU", # Hudson Acquisition I Corp.
    "HOLOW", # MicroCloud Hologram Inc.
    "BNIXR", # Bannix Acquisition Corp.
    "BNIXW", # Bannix Acquisition Corp.
    "LIDRW", # AEye, Inc.
    "GOEVW", # Canoo Inc.
    "LNZAW", # LanzaTech Global, Inc.
    "TOIIW", # Oncology Institute, Inc.
    "CSLRW", # Complete Solaria, Inc.
    "BOCNU", # Blue Ocean Acquisition Corp
    "BOCNW", # Blue Ocean Acquisition Corp
    "OZKAP", # Bank OZK
    "PKBOW", # Peak Bio, Inc.
    "VMCAU", # Valuence Merger Corp. I
    "VMCAW", # Valuence Merger Corp. I
    "NTRBW", # NutriBand Inc.
    "WAVSU", # Western Acquisition Ventures Corp.
    "WAVSW", # Western Acquisition Ventures Corp.
    "AMNA", # UBS AG
    "AMND", # UBS AG
    "AMTR", # UBS AG
    "AMUB", # UBS AG
    "UCIB", # UBS AG
    "USML", # UBS AG
    "WUCT", # UBS AG
    "SCDL", # UBS AG
    "SMHB", # UBS AG
    "MVRL", # UBS AG
    "PFFL", # UBS AG
    "QULL", # UBS AG
    "MLPB", # UBS AG
    "MLPR", # UBS AG
    "MTUL", # UBS AG
    "IWDL", # UBS AG
    "IWFL", # UBS AG
    "IWML", # UBS AG
    "HDLB", # UBS AG
    "IFED", # UBS AG
    "BDCX", # UBS AG
    "BDCZ", # UBS AG
    "CEFD", # UBS AG
    "DJCB", # UBS AG
    "ESUS", # UBS AG
    "FEDL", # UBS AG
    "MITAU", # Coliseum Acquisition Corp.
    "MITAW", # Coliseum Acquisition Corp.
    "SVREW", # SaverOne 2014 Ltd.
    "SQFTP", # Presidio Property Trust, Inc.
    "SQFTW", # Presidio Property Trust, Inc.
    "BFRIW", # Biofrontera Inc.
    "EOSEW", # Eos Energy Enterprises, Inc.
    "FNVTU", # Finnovate Acquisition Corp.
    "FNVTW", # Finnovate Acquisition Corp.
    "CCTSU", # Cactus Acquisition Corp. 1 Ltd
    "CCTSW", # Cactus Acquisition Corp. 1 Ltd
    "SOUNW", # SOUNDHOUND AI, INC.
    "MNSBP", # MainStreet Bancshares, Inc.
    "MAPSW", # WM TECHNOLOGY, INC.
    "MARXU", # Mars Acquisition Corp.
    "MARXR", # Mars Acquisition Corp.
    "NYMTL", # NEW YORK MORTGAGE TRUST INC
    "NYMTM", # NEW YORK MORTGAGE TRUST INC
    "NYMTZ", # NEW YORK MORTGAGE TRUST INC
    "RILYP", # B. Riley Financial, Inc.
    "RILYT", # B. Riley Financial, Inc.
    "RILYZ", # B. Riley Financial, Inc.
    "RILYG", # B. Riley Financial, Inc.
    "RILYK", # B. Riley Financial, Inc.
    "RILYL", # B. Riley Financial, Inc.
    "RILYM", # B. Riley Financial, Inc.
    "RILYN", # B. Riley Financial, Inc.
    "SIGIP", # SELECTIVE INSURANCE GROUP INC
    "NNAVW", # NEXTNAV INC.
    "NLSPW", # NLS Pharmaceutics Ltd.
    "NPABU", # New Providence Acquisition Corp. II
    "NPABW", # New Providence Acquisition Corp. II
    "CFFSU", # CF Acquisition Corp. VII
    "CFFSW", # CF Acquisition Corp. VII
    "ABLLW", # Abacus Life, Inc.
    "VSSYW", # Versus Systems Inc.
    "APXIU", # APx Acquisition Corp. I
    "APXIW", # APx Acquisition Corp. I
    "ISRLU", # Israel Acquisitions Corp
    "ISRLW", # Israel Acquisitions Corp
    "MDRRP", # Medalist Diversified REIT, Inc.
    "CBRGU", # Chain Bridge I
    "OABIW", # OmniAb, Inc.
    "ARQQW", # Arqit Quantum Inc.
    "AENTW", # ALLIANCE ENTERTAINMENT HOLDING CORP
    "TBMCR", # Trailblazer Merger Corp I
    "ROCLU", # Roth CH Acquisition V Co.
    "ROCLW", # Roth CH Acquisition V Co.
    "MHNC", # Maiden Holdings, Ltd.
    "TMTCU", # TMT Acquisition Corp.
    "TMTCR", # TMT Acquisition Corp.
    "ECCC", # Eagle Point Credit Co Inc.
    "ECCV", # Eagle Point Credit Co Inc.
    "ECCW", # Eagle Point Credit Co Inc.
    "ACGLN", # ARCH CAPITAL GROUP LTD.
    "QOMOR", # Qomolangma Acquisition Corp.
    "QOMOU", # Qomolangma Acquisition Corp.
    "QOMOW", # Qomolangma Acquisition Corp.
    "BUJAU", # Bukit Jalil Global Acquisition 1 Ltd.
    "BRKHU", # BurTech Acquisition Corp.
    "BRKHW", # BurTech Acquisition Corp.
    "WINVR", # WinVest Acquisition Corp.
    "WINVU", # WinVest Acquisition Corp.
    "WINVW", # WinVest Acquisition Corp.
    "FTAIM", # FTAI Aviation Ltd.
    "FTAIN", # FTAI Aviation Ltd.
    "FTAIO", # FTAI Aviation Ltd.
    "FTAIP", # FTAI Aviation Ltd.
    "DAVEW", # Dave Inc./DE
    "BULZ", # BANK OF MONTREAL /CAN/
    "JETU", # BANK OF MONTREAL /CAN/
    "JETD", # BANK OF MONTREAL /CAN/
    "CARD", # BANK OF MONTREAL /CAN/
    "CARU", # BANK OF MONTREAL /CAN/
    "WTID", # BANK OF MONTREAL /CAN/
    "WTIU", # BANK OF MONTREAL /CAN/
    "OILD", # BANK OF MONTREAL /CAN/
    "OILU", # BANK OF MONTREAL /CAN/
    "SHNY", # BANK OF MONTREAL /CAN/
    "FNGS", # BANK OF MONTREAL /CAN/
    "FNGU", # BANK OF MONTREAL /CAN/
    "GDXD", # BANK OF MONTREAL /CAN/
    "GDXU", # BANK OF MONTREAL /CAN/
    "DULL", # BANK OF MONTREAL /CAN/
    "FLYD", # BANK OF MONTREAL /CAN/
    "FLYU", # BANK OF MONTREAL /CAN/
    "HYMCL", # HYCROFT MINING HOLDING CORP
    "HYMCW", # HYCROFT MINING HOLDING CORP
    "FNGO", # BANK OF MONTREAL /CAN/
    "ICUCW", # SeaStar Medical Holding Corp
    "PETWW", # Wag! Group Co.
    "BERZ", # BANK OF MONTREAL /CAN/
    "PXSAW", # Pyxis Tankers Inc.
    "NVACR", # NorthView Acquisition Corp
    "NVACW", # NorthView Acquisition Corp
    "VSACU", # VISION SENSING ACQUISITION CORP.
    "VSACW", # VISION SENSING ACQUISITION CORP.
    "HUMAW", # Humacyte, Inc.
    "NTRSO", # NORTHERN TRUST CORP
    "IVCAU", # Investcorp AI Acquisition Corp.
    "IVCAW", # Investcorp AI Acquisition Corp.
    "GCMGW", # GCM Grosvenor Inc.
    "FULTP", # FULTON FINANCIAL CORP
    "NEWTZ", # NewtekOne, Inc.
    "DBGIW", # Digital Brands Group, Inc.

    ]