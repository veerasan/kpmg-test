from get_metadata import get_metadata

def gen_dict_extract(key, var):
    if hasattr(var, 'items'):
        for k, v in var.items():
            if k == key:
                yield v
            print("key , value -",k,v)
            if isinstance(v, dict):
                for result in gen_dict_extract(key, v):
                    print("key-1 , value-1,result-1 -->",result)
                    yield result
            elif isinstance(v, list):
                for d in v:
                    for result in gen_dict_extract(key, d):
                        print("key-2 , value-2,result-2 -->",k,v,result)
                        yield result


def find_key(key):
    metadata = get_metadata()
    return list(gen_dict_extract(key, metadata))


if __name__ == '__main__':
    key = input("Please enter the metadata key to extract?\n")
    print(find_key(key))
