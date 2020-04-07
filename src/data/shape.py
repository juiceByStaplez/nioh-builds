import pandas as pd

masterSkills = ['axe',
                'dual-swords',
                'hatchets',
                'kusarigama',
                'magic',
                'ninjutsu',
                'odachi',
                'samurai',
                'shiftling',
                'spear',
                'switchglaive',
                'sword',
                'tonfa', ]

masterFrame = pd.DataFrame(data=masterSkills, columns=['name'])
masterFrame['skill_tree'] = masterFrame.index
masterFrame.set_index('skill_tree')

skillFrame = None

for row,index in masterFrame.values:
    skill_tree_id = index + 1
    treeFrame = pd.read_json(f"{row}.json", orient='records').drop(columns='cost')
    treeFrame['skill_tree_id'] = skill_tree_id
    if skillFrame is None:
        skillFrame = treeFrame
    else:
        skillFrame = pd.concat([skillFrame, treeFrame])
    skill = ''



file = open(f"all_skills.csv", "w+")
file.write(skillFrame.to_csv())
file.close()