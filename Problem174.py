import collections

def flatten_dict(d, parent_key='', sep='.'):
    return { parent_key + sep + k if parent_key else k : v
             for kk, vv in d.items()
             for k, v in flatten_dict(vv, kk, sep).items()
            } if isinstance(d, dict) else {parent_key: d}

print(flatten_dict({
    "key": 3,
    "foo": {
        "a": 5,
        "bar": {
            "baz": 8
        },
        "": {
            "cc": 7
        }
    },
    "": {
        "a": 5,
        "bar": {
            "baz": 8
        },
        "": {
            "cc": 7
        }
    }
}))