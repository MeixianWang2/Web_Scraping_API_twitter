# get timeline tweet (including statue and reply)
from TwitterAPI import TwitterAPI, TwitterPager
import pandas as pd
from datetime import datetime
screen_name = 'amazon'
api = TwitterAPI("NZdbhxBnNsRT3Hr95NiKnvopu",
                 "vRtA7GbyemzeVJIYLTaMTtp4bqZzUMKzTRgGefZlaDDcpmzdVL",
                 "1133765235636989962-UCNSXfoqZt5w2vUu4i6QWMNcLV1E7R",
                 "mjiCNOaww4BPYwiFCn4PycSgtiAPnuAFnO452eZa8Oki3")

def get_all_tweets(screen_name):
    pager = TwitterPager(api,'statuses/user_timeline',{'screen_name': screen_name, 'count': 200})
# count = 0
# for item in pager.get_iterator(wait=3.5):
# 	if 'text' in item:
# # delete retweet and reply
#           if item['text'][0:2] == 'RT':
#                 continue
#           elif item['text'][0] == '@':
#                 continue
#           elif item['text'][0:2] != 'RT':
#                 count = count + 1
#                 print(count, item['text'])
#
# 	elif 'message' in item:
# 		print(item['message'])
# 		break
    alltweets = pager.get_iterator(wait=3.5)
    print(alltweets)
    for tweet in alltweets:
        print(tweet)
    # outtweets = [[screen_name, tweet['id_str'], pd.to_datetime(tweet['created_at']), tweet['text'], tweet['retweet_count'],
    #              tweet['user']['location'], tweet['favorite_count'], tweet['truncated'], tweet['is_quote_status'],
    #              tweet['lang'], tweet['place']]for tweet in alltweets]
    #
    # df = pd.DataFrame(outtweets, columns=['user_name', 'id', 'time', 'text', 'retweets', 'geo', 'favorite_count',
    #                                   'truncated', 'quoted', 'language', 'test'])
    #
    # df.to_csv(str(screen_name) + '.csv', index=False)
    # print('finish')

if __name__ == '__main__':
    get_all_tweets('amazon')
    # list = ['Microsoft', 'Apple', 'Amazon', 'facebook', 'jpmorgan', 'Google', 'JNJCares', 'Visa', 'ProcterGamble', 'exxonmobil', 'ATT', 'BankofAmerica', 'WaltDisneyCo', 'UnitedHealthGrp', 'intel', 'Mastercard', 'verizon', 'HomeDepot', 'Chevron', 'Merck', 'WellsFargo', 'pfizer', 'CocaCola', 'comcast', 'Boeing', 'Cisco', 'pepsi', 'Walmart', 'Citi', 'Medtronic', 'AbbottGlobal', 'McDonalds', 'Adobe', 'salesforce', 'Amgen', 'netflix', 'bmsnews', 'Costco', 'InsidePMI', 'nvidia', 'Accenture', 'thermofisher', 'honeywell', 'PayPal', 'Broadcom', 'UnionPacific', 'Oracle', 'Nike', 'IBM', 'nexteraenergy', 'TXInstruments', 'Lindeplc', 'LillyPad', 'Starbucks', 'CVSHealth', 'LockheedMartin', '3M', 'Qualcomm', 'DanaherCareers', 'generalelectric', 'AltriaNews', 'Lowes', 'usbank', 'FISGlobal', 'GileadSciences', 'BookingHoldings', 'AmericanExpress', 'UPS', 'CaterpillarInc', 'MDLZ', 'GetSpectrum', 'Cigna', 'ADP', 'CMEGroup', 'BBT', 'TJXCareers', 'AnthemInc', 'GoldmanSachs', 'Chubb', 'BDandCo', 'conocophillips', 'PNCBank', 'SPGlobal', 'Intuit', 'IntuitiveSurg', 'DominionEnergy', 'DukeEnergy', 'Fiserv', 'Target', 'Stryker_Jobs', 'SouthernCompany', 'MorganStanley', 'bostonsci', 'Allergan', 'Raytheon', 'Zoetis', 'CP_News', 'blackrock', 'Prologis', 'CharlesSchwab', 'CSX', 'VertexPharma', 'MicronTech', 'MMC_Global', 'Applied4Tech', 'JohnDeere', 'CrownCastle', 'northropgrumman', 'biogen', 'GlobalPayInc', 'Phillips66Co', 'airproducts', 'ICE_Markets', 'biogen', 'nscorp', 'Equinix', 'Aon_plc', 'Humana', 'EdwardsLifesci', 'CapitalOne', 'illumina', 'Ecolab', 'L3HarrisTech', 'Emerson_News', 'KCCorp', 'AEPnews', 'SherwinWilliams', 'EsteeLauder', 'DuPont_News', 'ATVI_AB', 'WasteManagement', 'GM', 'SimonPropertyGp', 'Walgreens', 'AIGinsurance', 'Progressive', 'Exelon', 'baxter_intl', 'Sysco', 'Ross_Stores', 'BNYMellon', 'LamResearch', 'generaldynamics', 'SempraEnergy', 'Kinder_Morgan', 'autodesk', 'WeAreOxy', 'MetLife', 'MarriottIntl', 'HCAhealthcare', 'eatoncorp', 'MoodysInvSvc', 'DollarGeneral', 'DowNewsroom', 'aflac', 'ValeroEnergy', 'MarathonPetroCo', 'Prudential', 'FedEx', 'Allstate', 'Ford', 'Travelers', 'Delta', 'Cognizant', 'oreillyauto', 'TEConnectivity', 'xcelenergy', 'cbrands', 'AmphenolPCD', 'EA', 'PublicStorage', 'johnsoncontrols', 'GeneralMills', 'HP', 'IngersollRand', 'VFCorp', 'IHSMarkit', 'yumbrands', 'ONEOK', 'HiltonHotels', 'Regeneron', 'zimmerbiomet', 'PPG', 'StateStreet', 'TRowePrice', 'PSEGNews', 'ConEdison', 'AvalonBay', 'IQVIA_global', 'MotoSolutions', 'EquityRes', 'WilliamsUpdates', 'KLAcorp', 'Paychex', 'Agilent', 'TysonFoods', 'EversourceCorp', 'autozone', 'paccar', 'MicrochipTech', 'eBay', 'Cummins', 'Discover', 'WTWcorporate', 'Centene', 'McKesson', 'firstenergycorp', 'SouthwestAir', 'PPLCorp', 'Verisk', 'Twitter', 'MonsterEnergy', 'XilinxInc', 'AlexionPharma', 'StanleyBlkDeckr', 'TMobile', 'DTE_Energy', 'digitalrealty', 'RealtyIncome', 'ADMupdates', 'IDEXX', 'LasVegasSands', 'Entergy', 'PXDtweets', 'Cerner', 'ROKAutomation', 'CintasCorp', 'LyondellBasell', 'Corning', 'FortiveCorp', 'NorthernTrust', 'Aptiv', 'MSCI_Inc', 'Weyerhaeuser', 'amwater', 'BallCorpHQ', 'ResMed', 'RoyalCaribbean', 'ANSYS', 'AMETEKInc', 'kroger', 'VERISIGN', 'synopsys', 'HersheyCompany', 'ChipotleTweets', 'TheHartford', 'ameriprise', 'MandT_Bank', 'DollarTree', 'synchrony', 'ViacomCBS', 'corteva', 'Halliburton', 'FastenalCompany', 'BestBuy', 'McCormickCorp', 'FifthThird', 'CBRE', 'mettlertoledo', 'EssexProperties', 'Copart', 'bxpboston', 'westerndigital', 'CarnivalPLC', 'CloroxCo', 'CDWCorp', 'firstrepublic', 'Keysight', 'keybank', 'HP', 'AmerenCorp', 'DRHorton', 'KraftHeinzCo', 'ConsumersEnergy', 'Lennar', 'Equifax', 'united', 'GallagherGlobal', 'KelloggCompany', 'IntlPaperCo', 'CitizensBank', 'maximintegrated', 'amcorpackaging', 'DoverCorp', 'Omnicom', 'Fortinet', 'HessCorporation', 'MGMResortsIntl', 'CarMax', 'ConagraBrands', 'cardinalhealth', 'symantec', 'Paycom', 'ultabeauty', 'Akamai', 'citrix', 'WatersCorp', 'ExpediaGroup', 'askRegions', 'Broadridge', 'QuestDX', 'Garmin', 'Hologic', 'XylemInc', 'IFF', 'TiffanyAndCo', 'Gartner_inc', 'Seagate', 'darden', 'grainger', 'bakerhughesco', 'genuinepartsco', 'WabtecCorp', 'principal', 'UDRMarketing', 'Huntington_Bank', 'atmosenergy', 'alliantenergy', 'extraspace', 'MASCOLMA', 'Loews_Hotels', 'Healthcare_ABC', 'CenturyLink', 'CBOE', 'TheAESCorp', 'SVB_Financial', 'FOXTV', 'DukeRealty', 'Nasdaq', 'Incyte', 'Hasbro', 'ZebraTechnology', 'RyanHomes1948, NVHomes1979', 'energyinsights', 'NetApp', 'celanese', 'STERIS', 'MarketAxess', 'JacobsConnects', 'VarianMedSys', 'DentsplySirona', 'QorvoInc', 'HormelFoods', 'JackHenryAssoc', 'AllegionPlc', 'Seagate', 'AristaNetworks', 'brownforman', 'EXPD_Official', 'smuckers', 'arconic', 'WesternUnion', 'PulteHomes', 'lincolnfingroup', 'AmericanAir', 'EverestIns', 'TractorSupply', 'UnitedRentals', 'AveryDennison', 'UHS_Inc', 'MylanNews', 'WRBerkleyCorp', 'Textron', 'CruiseNorwegian', 'HIIndustries', 'NiSourceInc', 'MolsonCoors', 'WestRock', 'vornado', 'PerkinElmer', 'ApacheCorp', 'HenrySchein', 'regencycenters', 'IronMountain', 'CHRobinson', 'AdvanceAuto', 'AlbemarleCorp', 'CampbellSoupCo', 'GlobeLife', 'nrgenergy', 'packagingcorp', 'LKQCorp', 'FederalRealty', 'FBHS_News', 'DiscoveryIncTV', 'CFIndustries', 'jbhunt360', 'EastmanChemCo', 'Snapon_Tools', 'InterpublicIPG', 'WhirlpoolCorp', 'LiveNation', 'dish', 'DaVita', 'AimcoApts', 'Assurant', 'JuniperNetworks', 'PerrigoCompany', 'kimcorealty', 'F5Networks', 'abiomedimpella', 'CabotOG', 'SLGreen', 'ComericaBank', 'Pentair', 'nblenergy', 'PeoplesUnited', 'FTI_Global', 'ZionsBank', 'tapestryInc', 'NOVGlobal', 'Xerox', 'BorgWarner', 'AOSmithHotWater', 'CruiseNorwegian', 'RollinsPC', 'AlaskaAir', 'newell_brands', 'roberthalf', 'Kohls', 'nielsen', 'flir', 'Quanta_Services', 'RalphLauren', 'L_Brands', 'PVHCorp', 'InvescoUS', 'Sealed_Air', 'MosaicCompany', 'TechnipFMC', 'Flowserve', 'unumnews', 'MarathonOil', 'DevonEnergy', 'Macys', 'Nordstrom', 'GapInc', 'AllianceData', 'COTYInc', 'HelmerichPayne', 'UnderArmour']
    # for i in list:
    #     try:
    #         get_all_tweets(i)
    #     except:
    #         print(i)
    #         continue
