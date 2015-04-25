

def get_region_neighbors_as_text(region):
    neighbors = region.region_set.all()
    print neighbors
