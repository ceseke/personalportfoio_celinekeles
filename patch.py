import re

with open('/Users/celinekeles/personalportfoio_celinekeles/index.html', 'r', encoding='utf-8') as f:
    content = f.read()

# The target block to wrap and duplicate is the `<div class="persona-grid">`...
start_str = '            <div class="persona-grid">'
end_str = '            <p class="audience-unique">'

start_idx = content.find(start_str)
end_idx = content.find(end_str)

if start_idx != -1 and end_idx != -1:
    grid_content = content[start_idx:end_idx]
    
    # We will replace the start_str up to end_str with the new split layout
    
    personas_grid = grid_content.replace('Participant', 'Persona')
    # Change the placeholder text a bit to show they are personas
    personas_grid = personas_grid.replace('A financially literate retiree', 'Description for Persona 1...')
    personas_grid = personas_grid.replace('A semi-retired professional', 'Description for Persona 2...')
    personas_grid = personas_grid.replace('Recently retired and new to reviewing', 'Description for Persona 3...')
    personas_grid = personas_grid.replace('Nearing retirement and relying on', 'Description for Persona 4...')
    
    new_html = f'''            <div class="audience-split">
              <div class="audience-participants">
                <h4 class="audience-section-title">Participants</h4>
{grid_content}              </div>
              
              <div class="audience-personas">
                <h4 class="audience-section-title">Personas</h4>
{personas_grid}              </div>
            </div>

'''
    
    new_content = content[:start_idx] + new_html + content[end_idx:]
    with open('/Users/celinekeles/personalportfoio_celinekeles/index.html', 'w', encoding='utf-8') as f:
        f.write(new_content)
    print("SUCCESS: HTML updated.")
else:
    print("ERROR: Could not find target strings.")
