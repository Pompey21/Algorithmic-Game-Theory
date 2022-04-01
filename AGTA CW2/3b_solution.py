from collections import Counter
from itertools import chain

graph = {
    's_v1'  : (7,3,9),
    's_v2'  : (2,4,4),
    's_v3'  : (5,7,5),
    'v1_t'  : (6,8,7),
    'v2_v1' : (1,7,3),
    'v2_t'  : (6,8,9),
    'v3_v2' : (2,9,8),
    'v3_t'  : (6,5,4)
}

paths = [
    [ 's_v3', 'v3_t'                    ],
    [ 's_v3', 'v3_v2', 'v2_t'           ],
    [ 's_v3', 'v3_v2', 'v2_v1', 'v1_t'  ],
    [ 's_v2', 'v2_t'                    ],
    [ 's_v2', 'v2_v1', 'v3_t'           ],
    [ 's_v1', 'v1_t'                    ],
]

collection = []

for i in range(len(paths)):
    for j in range(len(paths)):
        for k in range(len(paths)):
            profile = [paths[i],paths[j],paths[k]]
            collection.append(profile)

def get_congestion(profile):
  counts = Counter()
  flat_profile = list(chain.from_iterable(profile))

  flat_profile_counts = Counter(flat_profile).most_common()
  print(flat_profile_counts)
  return get_cost(flat_profile_counts)
      



def get_cost(congestion:list):
    sum_path = []
    for elem in congestion:
        cost_tripple = graph.get(elem[0])
        cost = cost_tripple[elem[1]-1]
        sum_path.append(cost)
    return [congestion,sum(sum_path)]

# result = get_cost(flat_profile_counts)
# print(result)

flat_profile_counts = get_congestion(collection[0])
print(flat_profile_counts)

