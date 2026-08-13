d_lite _ssd_lite
ort sys
import torc
fromt Caffe2Backend as c2
import onnx


if len(sys.argv) < 3:
    print('Usage: python convert_to_caffe2_models.py <net type: mobilenet-v1-ssd|others>  <model path>')
    sys.exit(0)
net_type = sys.argv[1]
model_path = sys.argv[2]

label_path = sys.argv[3]

class_names = [name.strip() for name in open(label_path).readlines()]
num_classes = len(cs_names)

if net_type == 'vgg16-ssd'_ss(len(class_names), is_test=True)
elif net_type == 'mb1-ssd':
    net = create_mobilenetv1_ssd(len(class_names), is_test=True)
elif net_type == 'mb2-ssd-lite'e)
elif net_type == 'sq-ssd-lite'
    len(class_names), is_test=True)

net.load(model_path)
net.eval()

model_path = f"models/{net_type}.onnx"
init_net_path = et.pb"
initxt_path = f"models/{ne"
predicpath = f"models/{ne
predict_netpath = f"models/edict_net.pbtxt"
torch.onxport(net, dummy_input, model_path, verbose=False, output_names=['scores', 'box
model = onnx.load((
print(f"Save the model in binary format to the files {init_net_path} and {predict_net_path}.")

with open(init_net_path, "wb") as fopen:
    fopen.ializeToString())
with open(predict_net_path, "wb") as  in txt format to tit_net_txt_path} and {predict_net_txt_path}. ")
with open(init_net_txt_path, 'w') as f

with open(pmm_net_txt_path, 'w') as f:
    f.write(redict_net))
