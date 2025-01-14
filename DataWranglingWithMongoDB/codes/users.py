import xml.etree.ElementTree as ET
import pprint

import os
#Set the proper current working directory
os.getcwd()
os.chdir('C:/Users/vaishnav/Desktop/DataWranglingWithMongoDB')

def process_map(filename):
    users = set()
    for _, element in ET.iterparse(filename):
        try:
            users.add(element.attrib['uid'])
        except KeyError:
            pass
        element.clear() #to clear memory
    return users

users = process_map('charlotte_north-carolina.osm')
pprint.pprint(users)
'''
The Result of my code is:
set(['1',
     '1007528',
     '1009527',
     '1012362',
     '103253',
     '10356',
     '103574',
     '1037396',
     '1041660',
     '104962',
     '1051550',
     '105255',
     '105454',
     '105839',
     '106510',
     '1067273',
     '107257',
     '10786',
     '1081635',
     '1087647',
     '11006',
     '110126',
     '1101758',
     '110639',
     '111209',
     '113450',
     '113918',
     '1149057',
     '11566',
     '115918',
     '116075',
     '1171221',
     '118134',
     '1188270',
     '1195005',
     '120146',
     '1201678',
     '1204209',
     '1209932',
     '121241',
     '123633',
     '1240670',
     '1240849',
     '12434',
     '12448',
     '1260280',
     '128017',
     '129614',
     '12992',
     '1299608',
     '130472',
     '1306',
     '131059',
     '1329572',
     '1330847',
     '134600',
     '135163',
     '1355899',
     '1355910',
     '1374718',
     '1376089',
     '1376118',
     '1408522',
     '1416503',
     '1424662',
     '1429212',
     '1429952',
     '1430450',
     '1443963',
     '1445406',
     '1451493',
     '145231',
     '146371',
     '1465903',
     '147510',
     '147876',
     '14850',
     '1494110',
     '1494432',
     '1494659',
     '1516961',
     '152289',
     '153669',
     '154164',
     '155066',
     '156133',
     '156157',
     '158231',
     '160138',
     '160651',
     '160949',
     '1611',
     '161269',
     '1617449',
     '163973',
     '165',
     '165061',
     '1651798',
     '165422',
     '165869',
     '16591',
     '166129',
     '167009',
     '1677922',
     '1679',
     '1679807',
     '168517',
     '169004',
     '1694880',
     '1699770',
     '170200',
     '170596',
     '1733690',
     '1735595',
     '1751737',
     '175600',
     '1781394',
     '1782960',
     '1783785',
     '179581',
     '1797607',
     '1802220',
     '1805170',
     '1806421',
     '181135',
     '1820886',
     '1824494',
     '1828630',
     '1829683',
     '1830867',
     '1832345',
     '1832883',
     '1836471',
     '1850730',
     '186167',
     '186281',
     '1872649',
     '1872875',
     '1874523',
     '1884215',
     '1888880',
     '1890412',
     '1900319',
     '190869',
     '1909453',
     '191112',
     '1911765',
     '191491',
     '1916073',
     '1924548',
     '19492',
     '1963041',
     '1963531',
     '1963548',
     '19735',
     '1978206',
     '1981443',
     '1981553',
     '1983446',
     '1995650',
     '200033',
     '200368',
     '200426',
     '2005436',
     '200922',
     '2012449',
     '2014205',
     '201789',
     '202615',
     '2027261',
     '2038907',
     '2049113',
     '204929',
     '2050395',
     '205051',
     '2053369',
     '2053563',
     '2057600',
     '2064896',
     '2072472',
     '207745',
     '2078284',
     '208225',
     '2082779',
     '2088234',
     '2102191',
     '2105413',
     '2110473',
     '2111876',
     '2115749',
     '2118267',
     '2118269',
     '2119363',
     '212111',
     '2130371',
     '2132468',
     '213831',
     '214969',
     '217070',
     '2180590',
     '2187964',
     '221363',
     '221878',
     '2219338',
     '2226712',
     '2228823',
     '223540',
     '2239939',
     '224440',
     '2246679',
     '2247878',
     '2253944',
     '225632',
     '2257331',
     '2284561',
     '2289315',
     '2291431',
     '2295049',
     '2302638',
     '2311536',
     '2311809',
     '231477',
     '231539',
     '2316249',
     '2318',
     '232126',
     '233180',
     '2338890',
     '2341900',
     '2349429',
     '2375384',
     '2377377',
     '2379679',
     '2386521',
     '23878',
     '2389178',
     '2389495',
     '2395258',
     '23999',
     '240041',
     '2417615',
     '2418101',
     '24247',
     '2432601',
     '2441939',
     '246',
     '2469567',
     '24942',
     '2497300',
     '2503288',
     '250487',
     '2504992',
     '2506901',
     '2511706',
     '2512300',
     '2527838',
     '252811',
     '2531909',
     '2549164',
     '2552192',
     '2554698',
     '255785',
     '2581869',
     '25867',
     '260703',
     '260982',
     '262151',
     '26299',
     '263635',
     '26365',
     '2675743',
     '26838',
     '2704165',
     '270512',
     '2722677',
     '2729735',
     '2748195',
     '2767782',
     '2776440',
     '2784255',
     '2812620',
     '28145',
     '2822257',
     '28237',
     '2826278',
     '2837854',
     '2854333',
     '28559',
     '286023',
     '286075',
     '28775',
     '289297',
     '290680',
     '292282',
     '292630',
     '29638',
     '297482',
     '303647',
     '30521',
     '30845',
     '310589',
     '31075',
     '31231',
     '314307',
     '322785',
     '32360',
     '329453',
     '32952',
     '330773',
     '331548',
     '332709',
     '334389',
     '336460',
     '336659',
     '339917',
     '345833',
     '346',
     '34829',
     '352368',
     '35243',
     '353357',
     '354358',
     '355242',
     '356',
     '3560',
     '3582',
     '36038',
     '360392',
     '360717',
     '36121',
     '364',
     '36443',
     '365944',
     '366682',
     '368827',
     '371121',
     '37137',
     '373434',
     '379381',
     '380000',
     '381909',
     '382725',
     '384562',
     '38487',
     '384894',
     '38784',
     '391126',
     '393155',
     '3962',
     '396764',
     '39688',
     '39774',
     '398086',
     '401102',
     '401490',
     '402624',
     '403175',
     '40397',
     '4054',
     '409326',
     '413047',
     '414318',
     '415732',
     '416346',
     '417785',
     '421055',
     '42191',
     '42429',
     '428712',
     '428722',
     '432209',
     '432464',
     '433196',
     '433198',
     '4363',
     '436419',
     '439947',
     '44200',
     '445671',
     '451067',
     '451693',
     '454589',
     '4697',
     '472067',
     '4732',
     '473471',
     '47544',
     '475877',
     '49031',
     '492876',
     '51045',
     '510836',
     '511032',
     '516407',
     '5193',
     '522859',
     '523394',
     '524797',
     '52898',
     '529645',
     '53050',
     '53127',
     '532118',
     '53445',
     '5359',
     '536243',
     '543467',
     '54759',
     '550560',
     '554234',
     '55916',
     '55945',
     '564585',
     '56597',
     '567139',
     '57158',
     '574637',
     '5748',
     '575547',
     '57884',
     '582811',
     '582855',
     '583054',
     '583870',
     '586574',
     '586964',
     '588035',
     '588575',
     '590907',
     '591947',
     '592819',
     '593205',
     '595221',
     '599711',
     '600768',
     '60244',
     '602466',
     '604945',
     '618377',
     '618879',
     '620387',
     '620540',
     '622468',
     '624042',
     '624084',
     '626974',
     '630540',
     '632073',
     '637742',
     '638291',
     '63969',
     '640351',
     '640563',
     '6424',
     '643236',
     '644905',
     '645244',
     '648351',
     '648509',
     '648834',
     '649103',
     '6513',
     '651369',
     '653666',
     '65442',
     '659418',
     '663559',
     '665694',
     '668014',
     '668354',
     '67862',
     '680121',
     '683562',
     '6871',
     '6879',
     '690989',
     '691602',
     '694737',
     '699397',
     '702653',
     '703517',
     '703657',
     '70696',
     '712866',
     '714898',
     '715952',
     '716156',
     '7168',
     '7203',
     '722137',
     '725620',
     '734072',
     '74277',
     '74937',
     '7591',
     '76002',
     '78656',
     '79933',
     '80285',
     '81423',
     '82317',
     '8287',
     '8339',
     '834053',
     '837066',
     '837425',
     '839970',
     '84054',
     '840635',
     '84263',
     '85673',
     '86504',
     '86703',
     '8703',
     '870861',
     '87586',
     '8764',
     '8909',
     '901515',
     '904289',
     '905056',
     '91499',
     '91568',
     '92274',
     '92286',
     '92387',
     '930338',
     '93788',
     '939079',
     '94578',
     '954647',
     '96974',
     '97431',
     '982168',
     '99207',
     '99476',
     '996997',
     '99985'])
'''     
