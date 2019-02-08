import os, sys, random
from shutil import copyfile

args = sys.argv

if(len(args) != 3):
    raise Exception("Provide source and destination path")
data_path = args[1]
split_path = args[2]
# create destination dir
os.makedirs(split_path, exist_ok=True)
# create train, valid, test
os.makedirs(split_path + "/train", exist_ok=True)
os.makedirs(split_path + "/valid", exist_ok=True)
os.makedirs(split_path + "/test", exist_ok=True)


def split_set(src_set, ratio):
    size = int(len(src_set) * ratio)
    set1 = []

    for i in range(size):
        rand_index = random.randint(0, len(src_set) - 1)
        set1.append(src_set[rand_index])
        del src_set[rand_index]

    return [set1, src_set]


def copy_files(src_dir, dest_dir, file_names):
    for file_name in file_names:
        copyfile(src_dir + "/" + file_name, dest_dir + "/" + file_name)


# for each category
for category_name in os.listdir(data_path):
    src_path = data_path + "/" + category_name
    train_dest = split_path + "/train/" + category_name
    valid_dest = split_path + "/valid/" + category_name
    test_dest = split_path + "/test/" + category_name
    # make dir for category
    os.makedirs(train_dest, exist_ok=True)
    os.makedirs(valid_dest, exist_ok=True)
    os.makedirs(test_dest, exist_ok=True)

    # list of categories
    cat_items = os.listdir(src_path)
    # split into train and test, make 80%, 20%
    [train_ls, test_ls] = split_set(cat_items, 0.8)
    # split from train to train and valid 80%, 20%
    [train_ls, valid_ls] = split_set(train_ls, 0.8)
    
    # copy files from original to spit dir 
    copy_files(src_path, train_dest, train_ls)
    copy_files(src_path, valid_dest, valid_ls)
    copy_files(src_path, test_dest, test_ls)