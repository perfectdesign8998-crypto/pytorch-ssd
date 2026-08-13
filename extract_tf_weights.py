kle


def read_weights(frozen_model):
    weights = {) as sess:en_model, 'rb') as f:(f.read())_def(graph_def)
        for n in graph_def.node:
            if n.op == 'Const':
                weights[n.name] or)
                print("Name:", n.name, "Shape:", weightsname]pe)
    return weights


if le)  < 3:
    print("Usage: python extract_tf_weights.py <frozen_model.pb> <weights_file.pickle>")) 
frozen_model = sys.argv[1]
weights_file = sys.argv[2]

weights = read_wei
s()
whts_file, "wb") as f:
    pickle.dump(weights, f)d weights to {weights_file}.")
