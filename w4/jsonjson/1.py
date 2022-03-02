import json
with open('sample_data.json ','r') as f:
    data=json.loads(f.read())
print("Interface status")
print("================================================================================")
print("DN                                                 Description           Speed    MTU  ")
print("-------------------------------------------------- --------------------  ------  ------")
for i in data["imdata"]:
    if (len(i["l1PhysIf"]["attributes"]["dn"])==42):
        print(i["l1PhysIf"]["attributes"]["dn"]+"                              "+i["l1PhysIf"]["attributes"]["speed"]+"   "+i["l1PhysIf"]["attributes"]["mtu"])
    else:
        print(i["l1PhysIf"]["attributes"]["dn"]+"                               "+i["l1PhysIf"]["attributes"]["speed"]+"   "+i["l1PhysIf"]["attributes"]["mtu"])