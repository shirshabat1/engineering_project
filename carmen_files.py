import numpy as np

START_TRAIN_FEATURES = 'train\\carmen\\features\\all\\'
START_TEST_FEATURES = 'test\\carmen\\features\\all\\'
START_VALID_FEATURES = 'validation\\carmen\\features\\all\\'

START_TRAIN_SIGNALS = 'train\\carmen\\signals'
START_TEST_SIGNALS = 'test\\carmen\\signals'
START_VALID_SIGNALS = 'validation\\carmen\\signals'



AREA_1_TRAIN = '\\area_1_carmen_train_5017_signals.npy'
AREA_2_TRAIN = '\\area_2_carmen_train_5017_signals.npy'
AREA_3_TRAIN = '\\area_3_carmen_train_5017_signals.npy'
AREA_4_TRAIN = '\\area_4_carmen_train_5017_signals.npy'

AREA_1_TEST = '\\area_1_carmen_test_1075_signals.npy'
AREA_2_TEST = '\\area_2_carmen_test_1075_signals.npy'
AREA_3_TEST = '\\area_3_carmen_test_1075_signals.npy'
AREA_4_TEST = '\\area_4_carmen_test_1075_signals.npy'

AREA_1_VALID = '\\area_1_carmen_validation_1076_signals.npy'
AREA_2_VALID = '\\area_2_carmen_validation_1076_signals.npy'
AREA_3_VALID = '\\area_3_carmen_validation_1076_signals.npy'
AREA_4_VALID = '\\area_4_carmen_validation_1076_signals.npy'


def load_data(area1, area2, area3, area4, path):
    data_area1 = np.load(path + area1, allow_pickle=True)
    data_area2 = np.load(path +area2, allow_pickle=True)
    data_area3 = np.load(path +area3, allow_pickle=True)
    data_area4 = np.load(path +area4, allow_pickle=True)
    return data_area1, data_area2, data_area3, data_area4


def load_files(start_path, monkey, type):
    files = []
    for i in range(1, 5):
        files.append(np.load(start_path + str(monkey) + '_area_' + str(i) + '_' + str(type) + '_features.npy',
                             allow_pickle=True))
    return files


carmen_validation_features = load_files(START_VALID_FEATURES, 'carmen', 'validation')
carmen_train_features = load_files(START_TRAIN_FEATURES, 'carmen', 'train')
carmen_test_features = load_files(START_TEST_FEATURES, 'carmen', 'test')

train1, train2, train3, train4 = load_data(AREA_1_TRAIN, AREA_2_TRAIN, AREA_3_TRAIN, AREA_4_TRAIN,START_TRAIN_SIGNALS)
test1, test2, test3, test4 = load_data(AREA_1_TEST, AREA_2_TEST, AREA_3_TEST, AREA_4_TEST, START_TEST_SIGNALS)
valid1, valid2, valid3, valid4 = load_data(AREA_1_VALID, AREA_2_VALID, AREA_3_VALID, AREA_4_VALID, START_VALID_SIGNALS)

#
# def load_test_feature(feature, small = 0):
#     start = START_TEST
#     area1, area2, area3, area4 = AREA_1_TEST, AREA_2_TEST, AREA_3_TEST, AREA_4_TEST
#     if small == 1:
#         start = 'small\\'+START_TEST
#         area1, area2, area3, area4 = AREA_1_SMALL_TEST, AREA_2_SMALL_TEST, AREA_3_SMALL_TEST, AREA_4_SMALL_TEST
#     test_1 = np.load(start + str(feature) + area1, allow_pickle=True)
#     test_2 = np.load(start + str(feature) + area2, allow_pickle=True)
#     test_3 = np.load(start + str(feature) + area3, allow_pickle=True)
#     test_4 = np.load(start + str(feature) + area4, allow_pickle=True)
#     return test_1, test_2, test_3, test_4
#
#
# def load_train_feature(feature, small = 0):
#     start = START_TRAIN
#     area1, area2, area3, area4 = AREA_1_TRAIN, AREA_2_TRAIN, AREA_3_TRAIN, AREA_4_TRAIN
#     if small == 1:
#         start = 'small\\'+START_TRAIN
#         area1, area2, area3, area4 = AREA_1_SMALL_TRAIN, AREA_2_SMALL_TRAIN, AREA_3_SMALL_TRAIN, AREA_4_SMALL_TRAIN
#     train_1 = np.load(start + str(feature) + area1, allow_pickle=True)
#     train_2 = np.load(start + str(feature) + area2, allow_pickle=True)
#     train_3 = np.load(start + str(feature) + area3, allow_pickle=True)
#     train_4 = np.load(start + str(feature) + area4, allow_pickle=True)
#     return train_1, train_2, train_3, train_4
#
#
# def load_valid_feature(feature, small = 0):
#     start = START_VALID
#     area1, area2, area3, area4 = AREA_1_VALID, AREA_2_VALID, AREA_3_VALID, AREA_4_VALID
#     if small == 1:
#         start = 'small\\'+START_VALID
#         area1, area2, area3, area4 = AREA_1_SMALL_VALID, AREA_2_SMALL_VALID, AREA_3_SMALL_VALID, AREA_4_SMALL_VALID
#     valid_1 = np.load(start + str(feature) +area1, allow_pickle=True)
#     valid_2 = np.load(start + str(feature) + area2, allow_pickle=True)
#     valid_3 = np.load(start + str(feature) +area3, allow_pickle=True)
#     valid_4 = np.load(start + str(feature) + area4, allow_pickle=True)
#     return valid_1, valid_2, valid_3, valid_4

#
#
#
# def load_data(num, type, monkey, small):
#     data = ['', '', '', '']
#     type_small = type
#     if small == 1:
#         type_small = 'small\\' + str(type_small)
#     for i in range(1, 5):
#         data[i - 1] = np.load(
#             type_small + '\\' + monkey + '\\signals\\area_' + str(i) + '_' + monkey + '_' + type + '_' + str(
#                 num) + '_signals.npy', allow_pickle=True)
#     return data[0], data[1], data[2], data[3]


# monkey = 'carmen'
#
#
# sig_train1, sig_train2, sig_train3, sig_train4 = load_data(5017, 'train', monkey, 0)
# sig_test1, sig_test2, sig_test3, sig_test4 = load_data(1075, 'test', monkey, 0)
# sig_validation1, sig_validation2, sig_validation3, sig_validation4 = load_data(1076, 'validation', monkey, 0)
#
#
# train_1_psd_welch, train_2_psd_welch, train_3_psd_welch, train_4_psd_welch = load_train_feature('psd_welch')
# test_1_psd_welch, test_2_psd_welch, test_3_psd_welch, test_4_psd_welch = load_test_feature('psd_welch')
# valid_1_psd_welch, valid_2_psd_welch, valid_3_psd_welch, valid_4_psd_welch = load_valid_feature('psd_welch')
#
# train1, train2, train3, train4 = load_train_feature('regular')
# test1, test2, test3, test4 = load_test_feature('regular')
# valid1, valid2, valid3, valid4 = load_valid_feature('regular')
#
# train_1_psd_multitaper, train_2_psd_multitaper, train_3_psd_multitaper, train_4_psd_multitaper = load_train_feature('psd_multitapers')
# test_1_psd_multitaper, test_2_psd_multitaper, test_3_psd_multitaper, test_4_psd_multitaper = load_test_feature('psd_multitapers')
# valid_1_psd_multitaper, valid_2_psd_multitaper, valid_3_psd_multitaper, valid_4_psd_multitaper = load_valid_feature('psd_multitapers')
#
#
# train_1_welch, train_2_welch, train_3_welch, train_4_welch = load_train_feature('welch')
# test_1_welch, test_2_welch, test_3_welch, test_4_welch = load_test_feature('welch')
# valid_1_welch, valid_2_welch, valid_3_welch, valid_4_welch = load_valid_feature('welch')
#
#
#
#
# sig_small_train1, sig_small_train2, sig_small_train3, sig_small_train4 = load_data(1246, 'train', monkey, 1)
# sig_small_test1, sig_small_test2, sig_small_test3, sig_small_test4 = load_data(267, 'test', monkey, 1)
# sig_small_validation1, sig_small_validation2, sig_small_validation3, sig_small_validation4 = load_data(267,
#                                                                                                        'validation',
#                                                                                                        monkey, 1)
#
# train_small_1_psd_welch, train_small_2_psd_welch, train_small_3_psd_welch, train_small_4_psd_welch = load_train_feature('psd_welch',1)
# test_small_1_psd_welch, test_small_2_psd_welch, test_small_3_psd_welch, test_small_4_psd_welch = load_test_feature('psd_welch',1)
# valid_small_1_psd_welch, valid_small_2_psd_welch, valid_small_3_psd_welch, valid_small_4_psd_welch = load_valid_feature('psd_welch',1)
#
# train_small1, train_small2, train_small3, train_small4 = load_train_feature('regular',1)
# test_small1, test_small2, test_small3, test_small4 = load_test_feature('regular',1)
# valid_small1, valid_small2, valid_small3, valid_small4 = load_valid_feature('regular',1)
#
# train_small_1_psd_multitaper, train_small_2_psd_multitaper, train_small_3_psd_multitaper, train_small_4_psd_multitaper = load_train_feature('psd_multitapers',1)
# test_small_1_psd_multitaper, test_small_2_psd_multitaper, test_small_3_psd_multitaper, test_small_4_psd_multitaper = load_test_feature('psd_multitapers',1)
# valid_small_1_psd_multitaper, valid_small_2_psd_multitaper, valid_small_3_psd_multitaper, valid_small_4_psd_multitaper = load_valid_feature('psd_multitapers',1)
#
#
# train_small_1_welch, train_small_2_welch, train_small_3_welch, train_small_4_welch = load_train_feature('welch',1)
# test_small_1_welch, test_small_2_welch, test_small_3_welch, test_small_4_welch = load_test_feature('welch',1)
# valid_small_1_welch, valid_small_2_welch, valid_small_3_welch, valid_small_4_welch = load_valid_feature('welch',1)
#
