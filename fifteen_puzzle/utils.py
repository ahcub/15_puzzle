def exchange_collection_values(collection, id_1, id_2):
    collection[id_1], collection[id_2] = collection[id_2], collection[id_1]
