
__secret__token = "ifgwS7pa81aIy/21"
__org__name     = "DevNet San Jose"

def get_organizations(token):
    return [
        {
            "id": "471413",
            "name": "Cisco-B20"
        },
        {
            "id": "522532",
            "name": "ETS- Tradeshows"
        },
        {
            "id": "589433",
            "name": "cisco"
        },
        {
            "id": "390710",
            "name": "Technology Experiences"
        },
        {
            "id": "463308",
            "name": "DevNet San Jose"
        }
    ]


# Data Format
# {
#     "name": "",
#     "serial": "Q2BV-CTWR-JKRD",
#     "mac": "e0:55:3d:84:86:fd",
#     "networkId": "L_573083052582899526",
#     "model": "MV21",
#     "address": "",
#     "lat": 37.4180951010362,
#     "lng": -122.098531723022,
#     "notes": "",
#     "tags": "",
#     "lanIp": "10.10.120.36"
# },
def get_devices(token, org_id):
    return [{"name":"","serial":"Q2BV-CTWR-JKRD","mac":"e0:55:3d:84:86:fd","networkId":"L_573083052582899526","model":"MV21","address":"","lat":37.4180951010362,"lng":-122.098531723022,"notes":"","tags":"","lanIp":"10.10.120.36"},{"name":"","serial":"Q2BV-JMC4-Y56Z","mac":"e0:55:3d:84:86:f9","networkId":"L_573083052582899526","model":"MV21","address":"","lat":37.4180951010362,"lng":-122.098531723022,"notes":"","tags":"","lanIp":"172.17.130.165"},{"name":"Kareem's Desk","serial":"Q2HP-2LB6-2GF5","mac":"88:15:44:e5:bc:dc","networkId":"L_573083052582908089","model":"MS220-8P","address":"","lat":37.4180951010362,"lng":-122.098531723022,"notes":"","tags":" recently-added ","lanIp":"10.10.30.23"},{"name":"CoCreate06","serial":"Q2HP-3H3M-694E","mac":"88:15:44:e5:c1:e3","networkId":"L_573083052582908089","model":"MS220-8P","address":"","lat":37.4180951010362,"lng":-122.098531723022,"notes":"","tags":" recently-added ","lanIp":"10.10.130.111"},{"name":"Sensors","serial":"Q2HP-3YZ6-S92G","mac":"88:15:44:e5:bc:f2","networkId":"L_573083052582908089","model":"MS220-8P","address":"","lat":37.4180951010362,"lng":-122.098531723022,"notes":"","tags":" recently-added ","lanIp":"10.10.200.31"},{"name":"CoCreate07","serial":"Q2HP-4JZQ-8KSC","mac":"88:15:44:e5:c0:6d","networkId":"L_573083052582908089","model":"MS220-8P","address":"","lat":37.4180951010362,"lng":-122.098531723022,"notes":"","tags":" recently-added ","lanIp":"10.10.130.94"},{"name":"CoCreate04","serial":"Q2HP-4XUR-FK5K","mac":"88:15:44:e5:9e:23","networkId":"L_573083052582908089","model":"MS220-8P","address":"","lat":37.4180951010362,"lng":-122.098531723022,"notes":"","tags":" recently-added ","lanIp":"10.10.130.109"},{"name":"ClusDemo-stg","serial":"Q2HP-4ZVE-WFZY","mac":"88:15:44:e5:ae:da","networkId":"L_573083052582908089","model":"MS220-8P","address":"","lat":37.4180951010362,"lng":-122.098531723022,"notes":"","tags":" recently-added ","lanIp":"172.16.1.32"},{"name":"ClusDemo","serial":"Q2HP-7ZQY-VTTC","mac":"e0:cb:bc:3b:50:95","networkId":"L_573083052582908089","model":"MS220-8P","address":"","lat":37.4180951010362,"lng":-122.098531723022,"notes":"","tags":"","lanIp":"172.17.201.47"},{"name":"CLUS18-SmartCIty","serial":"Q2HP-VMRR-W3CK","mac":"e0:cb:bc:3b:7f:d9","networkId":"L_573083052582899526","model":"MS220-8P","address":"","lat":37.4180951010362,"lng":-122.098531723022,"notes":"","tags":"","lanIp":"172.17.101.34"},{"name":"DevNet-Bldg20-SW1","serial":"Q2HP-XGD3-PFU2","mac":"88:15:44:e5:05:83","networkId":"L_573083052582908089","model":"MS220-8P","address":"","lat":37.4180951010362,"lng":-122.098531723022,"notes":"","tags":" recently-added ","lanIp":"10.10.60.3"},{"name":"","serial":"Q2HY-226X-YCCW","mac":"ac:17:c8:5d:19:fa","networkId":"L_573083052582908089","model":"MX67C-NA","address":"","lat":37.4180951010362,"lng":-122.098531723022,"notes":"","tags":"","wan1Ip":"","wan2Ip":""},{"name":"DevNetCreate-2","serial":"Q2KD-6GJZ-3VGX","mac":"88:15:44:a9:62:c6","networkId":"L_573083052582899526","model":"MR42","address":"","lat":27.66483,"lng":-81.51575,"notes":"","tags":"","lanIp":"10.10.30.22"},{"name":"AP-LL-High","serial":"Q2KD-QV78-WSP4","mac":"88:15:44:a9:62:8a","networkId":"L_573083052582899526","model":"MR42","address":"","lat":37.4180951010362,"lng":-122.098531723022,"notes":"","tags":"","lanIp":"172.17.101.39"},{"name":"AP-LL-Low","serial":"Q2KD-V8GJ-AE2M","mac":"88:15:44:a9:52:88","networkId":"L_573083052582899526","model":"MR42","address":"","lat":37.4180951010362,"lng":-122.098531723022,"notes":"","tags":" recently-added ","lanIp":"10.10.140.61"},{"name":"LearningLabs01-CLMEL","serial":"Q2KP-57DZ-E7B9","mac":"e0:55:3d:9e:7d:01","networkId":"L_573083052582908089","model":"MS220-24P","address":"","lat":37.4180951010362,"lng":-122.098531723022,"notes":"","tags":" recently-added ","lanIp":"10.10.120.37"},{"name":"","serial":"Q2KP-5X7D-2LL9","mac":"e0:55:3d:9e:5a:6f","networkId":"L_573083052582908089","model":"MS220-24P","address":"","lat":37.4180951010362,"lng":-122.098531723022,"notes":"","tags":" recently-added ","lanIp":""},{"name":"W3+W4","serial":"Q2KP-6924-GRN7","mac":"e0:55:3d:9e:7a:f4","networkId":"L_573083052582899526","model":"MS220-24P","address":"","lat":37.4180951010362,"lng":-122.098531723022,"notes":"","tags":"","lanIp":"10.10.110.23"},{"name":"LearningLabs02","serial":"Q2KP-ATBR-93N4","mac":"e0:55:3d:9e:7c:cf","networkId":"L_573083052582908089","model":"MS220-24P","address":"","lat":37.4180951010362,"lng":-122.098531723022,"notes":"","tags":" recently-added ","lanIp":"10.10.120.37"},{"name":"W1+W2","serial":"Q2KP-W7HJ-96EG","mac":"88:15:44:76:d4:4e","networkId":"L_573083052582899526","model":"MS220-24P","address":"","lat":37.4180951010362,"lng":-122.098531723022,"notes":"","tags":"","lanIp":"10.10.110.22"},{"name":"DISTRIBUTION","serial":"Q2NP-38AV-7467","mac":"88:15:44:ea:d0:40","networkId":"L_573083052582899526","model":"MS220-48FP","address":"","lat":37.4180951010362,"lng":-122.098531723022,"notes":"","tags":"","lanIp":"10.10.110.24"},{"name":"LEARNING-LABS","serial":"Q2NP-4TCG-Z6ZZ","mac":"88:15:44:ea:89:dc","networkId":"L_573083052582899526","model":"MS220-48FP","address":"","lat":37.4180951010362,"lng":-122.098531723022,"notes":"","tags":"","lanIp":"10.10.110.25"},{"name":"DevNetAP02","serial":"Q2PD-3LDK-Z8R7","mac":"e0:55:3d:f2:d2:d5","networkId":"L_573083052582899526","model":"MR33","address":"Messedamm 22, 14055 Berlin","lat":52.50417,"lng":13.27366,"notes":"","tags":" ArduinoTraffic NOCTraffic ","lanIp":"10.10.120.38"},{"name":"Desk AP","serial":"Q2PD-CDE7-PWKW","mac":"e0:55:3d:f3:36:8b","networkId":"L_573083052582908089","model":"MR33","address":"725 Alder Dr, Milpitas","lat":37.41577,"lng":-121.91642,"notes":"","tags":"","lanIp":"10.0.0.222"},{"name":"CLUS-2017-low","serial":"Q2PD-L67B-RA8P","mac":"e0:55:3d:f2:fb:47","networkId":"L_573083052582899526","model":"MR33","address":"","lat":37.4180951010362,"lng":-122.098531723022,"notes":"","tags":"","lanIp":""},{"name":"DevNet-Bldg20-AP1","serial":"Q2PD-LG3V-BU8Y","mac":"e0:55:3d:f2:fc:07","networkId":"L_573083052582899526","model":"MR33","address":"735 Alder Drive, San Jose ca","lat":37.41456,"lng":-121.91759,"notes":"","tags":" NOCTraffic ","lanIp":"10.40.52.33"},{"name":"DevNet-Bldg20-MX1","serial":"Q2QN-GAJY-EBH5","mac":"e0:55:3d:6e:ca:7e","networkId":"L_573083052582899526","model":"MX65","address":"","lat":37.4180951010362,"lng":-122.098531723022,"notes":"","tags":" recently-added ","wan1Ip":"10.156.130.166","wan2Ip":""}]


# Data Format
# {
#     "name": "LEARNING-LABS",
#     "serial": "Q2NP-4TCG-Z6ZZ",
#     "mac": "88:15:44:ea:89:dc",
#     "publicIp": "63.231.221.69",
#     "networkId": "L_573083052582899526",
#     "status": "offline",
#     "lanIp": "10.10.110.25"
# }
def get_device_statuses(token, org_id):
    return [{"name":"LEARNING-LABS","serial":"Q2NP-4TCG-Z6ZZ","mac":"88:15:44:ea:89:dc","publicIp":"63.231.221.69","networkId":"L_573083052582899526","status":"offline","lanIp":"10.10.110.25"},{"name":"DISTRIBUTION","serial":"Q2NP-38AV-7467","mac":"88:15:44:ea:d0:40","publicIp":"63.231.221.69","networkId":"L_573083052582899526","status":"offline","lanIp":"10.10.110.24"},{"name":"DevNet-Bldg20-MX1","serial":"Q2QN-GAJY-EBH5","mac":"e0:55:3d:6e:ca:7e","publicIp":"128.107.241.162","networkId":"L_573083052582899526","status":"offline","usingCellularFailover":False,"wan1Ip":"10.156.130.166","wan2Ip":""},{"name":"W3+W4","serial":"Q2KP-6924-GRN7","mac":"e0:55:3d:9e:7a:f4","publicIp":"63.231.221.69","networkId":"L_573083052582899526","status":"offline","lanIp":"10.10.110.23"},{"name":"W1+W2","serial":"Q2KP-W7HJ-96EG","mac":"88:15:44:76:d4:4e","publicIp":"63.231.221.69","networkId":"L_573083052582899526","status":"offline","lanIp":"10.10.110.22"},{"name":"LearningLabs02","serial":"Q2KP-ATBR-93N4","mac":"e0:55:3d:9e:7c:cf","publicIp":"80.157.70.138","networkId":"L_573083052582908089","status":"offline","lanIp":"10.10.120.37"},{"name":"","serial":"Q2KP-5X7D-2LL9","mac":"e0:55:3d:9e:5a:6f","publicIp":"","networkId":"L_573083052582908089","status":"offline","lanIp":""},{"name":"LearningLabs01-CLMEL","serial":"Q2KP-57DZ-E7B9","mac":"e0:55:3d:9e:7d:01","publicIp":"220.101.107.137","networkId":"L_573083052582908089","status":"offline","lanIp":"10.10.120.37"},{"name":"CLUS18-SmartCIty","serial":"Q2HP-VMRR-W3CK","mac":"e0:cb:bc:3b:7f:d9","publicIp":"63.231.221.162","networkId":"L_573083052582899526","status":"offline","lanIp":"172.17.101.34"},{"name":"Kareem's Desk","serial":"Q2HP-2LB6-2GF5","mac":"88:15:44:e5:bc:dc","publicIp":"173.36.240.167","networkId":"L_573083052582908089","status":"offline","lanIp":"10.10.30.23"},{"name":"ClusDemo-stg","serial":"Q2HP-4ZVE-WFZY","mac":"88:15:44:e5:ae:da","publicIp":"128.107.241.167","networkId":"L_573083052582908089","status":"offline","lanIp":"172.16.1.32"},{"name":"ClusDemo","serial":"Q2HP-7ZQY-VTTC","mac":"e0:cb:bc:3b:50:95","publicIp":"63.231.221.162","networkId":"L_573083052582908089","status":"offline","lanIp":"172.17.201.47"},{"name":"DevNet-Bldg20-SW1","serial":"Q2HP-XGD3-PFU2","mac":"88:15:44:e5:05:83","publicIp":"162.213.214.132","networkId":"L_573083052582908089","status":"offline","lanIp":"10.10.60.3"},{"name":"Sensors","serial":"Q2HP-3YZ6-S92G","mac":"88:15:44:e5:bc:f2","publicIp":"128.107.241.175","networkId":"L_573083052582908089","status":"offline","lanIp":"10.10.200.31"},{"name":"CoCreate04","serial":"Q2HP-4XUR-FK5K","mac":"88:15:44:e5:9e:23","publicIp":"80.157.70.138","networkId":"L_573083052582908089","status":"offline","lanIp":"10.10.130.109"},{"name":"CoCreate07","serial":"Q2HP-4JZQ-8KSC","mac":"88:15:44:e5:c0:6d","publicIp":"80.157.70.138","networkId":"L_573083052582908089","status":"offline","lanIp":"10.10.130.94"},{"name":"CoCreate06","serial":"Q2HP-3H3M-694E","mac":"88:15:44:e5:c1:e3","publicIp":"80.157.70.138","networkId":"L_573083052582908089","status":"offline","lanIp":"10.10.130.111"},{"name":"CLUS-2017-low","serial":"Q2PD-L67B-RA8P","mac":"e0:55:3d:f2:fb:47","publicIp":"37.34.67.32","networkId":"L_573083052582899526","status":"offline","lanIp":""},{"name":"DevNet-Bldg20-AP1","serial":"Q2PD-LG3V-BU8Y","mac":"e0:55:3d:f2:fc:07","publicIp":"128.107.241.167","networkId":"L_573083052582899526","status":"offline","lanIp":"10.40.52.33"},{"name":"DevNetAP02","serial":"Q2PD-3LDK-Z8R7","mac":"e0:55:3d:f2:d2:d5","publicIp":"80.157.70.138","networkId":"L_573083052582899526","status":"offline","lanIp":"10.10.120.38"},{"name":"Desk AP","serial":"Q2PD-CDE7-PWKW","mac":"e0:55:3d:f3:36:8b","publicIp":"73.202.96.250","networkId":"L_573083052582908089","status":"offline","lanIp":"10.0.0.222"},{"name":"","serial":"Q2HY-226X-YCCW","mac":"ac:17:c8:5d:19:fa","publicIp":"166.177.249.146","networkId":"L_573083052582908089","status":"offline","usingCellularFailover":True,"wan1Ip":"","wan2Ip":""},{"name":"DevNetCreate-2","serial":"Q2KD-6GJZ-3VGX","mac":"88:15:44:a9:62:c6","publicIp":"173.36.224.109","networkId":"L_573083052582899526","status":"offline","lanIp":"10.10.30.22"},{"name":"AP-LL-Low","serial":"Q2KD-V8GJ-AE2M","mac":"88:15:44:a9:52:88","publicIp":"67.169.174.26","networkId":"L_573083052582899526","status":"offline","lanIp":"10.10.140.61"},{"name":"AP-LL-High","serial":"Q2KD-QV78-WSP4","mac":"88:15:44:a9:62:8a","publicIp":"63.231.221.162","networkId":"L_573083052582899526","status":"offline","lanIp":"172.17.101.39"},{"name":"","serial":"Q2BV-CTWR-JKRD","mac":"e0:55:3d:84:86:fd","publicIp":"80.157.70.138","networkId":"L_573083052582899526","status":"offline","lanIp":"10.10.120.36"},{"name":"","serial":"Q2BV-JMC4-Y56Z","mac":"e0:55:3d:84:86:f9","publicIp":"173.36.240.174","networkId":"L_573083052582899526","status":"offline","lanIp":"172.17.130.165"}]



if __name__ == "__name__":
    print("** running main program **")
    # TODO: 
    # - Allow for the token and org_id to be passed in via command line arguments
    #   The Token should be passed in as a string representing a header (key value pair). For Example
    #   python main.py --token="Authorization: Bearer ifgwS7pa81aIy/21"
    # 
    # - Find and return a list of all Cameras (MV Models)
