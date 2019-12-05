import os
omgevings_variabelen = os.environ

output_file = open("env_dump.txt", "w")

tellertje = 0
for key in omgevings_variabelen:
    tellertje += 1
    value = omgevings_variabelen[key]
    regel = "{},{}\n".format(key, value)
    output_file.write(regel)

output_file.close()
print("Ik ben klaar, {} resultaten".format(tellertje))
