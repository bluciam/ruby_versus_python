def non_repeated(string):
    used_chars = {}
    
    for char in string:
        try:
            used_chars[ord(char)] += 1
        except:
            used_chars[ord(char)] = 1

    print
    print string

    for k,v in enumerate(used_chars):
#        print "k ", k
#        print "v ", v
        if used_chars[v] is 1:
            print chr(v) + " is not repeated"

    return used_chars


non_repeated("")
non_repeated("aab")
non_repeated("Hello")
non_repeated("a")
non_repeated("eloHHelo")
non_repeated(
"""Si vous n'avez pas encore remis vos partitions de Schubert (Messe
et Standchen) pourriez-vous les deposer a mon attention au secretariat du petit
College s'il vous plait ?

L'enregistrement du concert devrait me parvenir d'ici la fin de la semaine
prochaine. Jean-Paul Baty a une certaine quantite de montage a faire.

Vendredi 12 juin, vers 20h15, des retrouvailles sont prevues chez Angele et ses
parents apres la repetition qui se terminera a 20h. Angele, pourrais-tu nous
repreciser votre adresse s'il te plait ?
Merci Matthieu, Nathalie et Angele pour l'invitation !
Chacun apporte de quoi boire ou/et manger !
""")
