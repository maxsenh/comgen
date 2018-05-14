fw = open('new_47.txt.pfa', 'w')
with open("47.fa.txt.pfa") as db16:
    for line in db16:
        if ">" in line:
            fw.write("\n" + line)
        if line.strip("\n").isupper():
            fw.write(line.strip("\n"))