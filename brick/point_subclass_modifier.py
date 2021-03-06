import json
import pdb

filename = 'point_subclass_dict.json'
with open(filename, 'r') as fp:
    d = json.load(fp)

new_d = dict()
postfixes = ['sensor', 'alarm', 'setpoint', 'status', 'command', 'meter']
for super_tagset, tagsets in d.items():
    if super_tagset.split('_')[-1] not in postfixes:
        continue
    new_tagsets = [ts for ts in tagsets if ts.split('_')[-1] in postfixes]
    new_d[super_tagset] = new_tagsets

with open(filename, 'w') as fp:
    json.dump(new_d, fp, indent=2)
