
def to_pouring(capacities, bottles, from_id, to_id):
    for i in range(len(from_id)):
        f, t = from_id[i], to_id[i]
        volume = min(bottles[f],capacities[t]-capacities[f])
        bottles[f] -= volume
        bottles[t] += volume

    return bottles
