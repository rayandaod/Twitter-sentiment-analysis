# Rather we want to run our algorithm on the whole dataset or not
FULL = False


# ----------------------------------------------------------------------------------------------------------------------
#                                                WORD EMBEDDINGS

CUT_VOCAB_N = 5

# GLOVE
GLOVE_K = 200
GLOVE_NMAX = 100
GLOVE_ETA = 0.001
GLOVE_ALPHA = 3/4
GLOVE_N_EPOCHS = 10

# STANFORD
STANFORD_K = 200  # Possible values: 25, 50, 100, 200
# ----------------------------------------------------------------------------------------------------------------------
#                                                   PREDICTION

TEST_SIZE = 0.1

# LOGISTIC REGRESSION
CV_FOLDS = 5

# NEURAL-NETWORK
NN_N_EPOCHS = 5
NN_BATCH_SIZE = 100
NN_PATIENCE = 2
NN_VERBOSE = True

NN_TRAIN_EMBEDDING_LAYER = True
MAX_SEQUENCE_LENGTH = 100
