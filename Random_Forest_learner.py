import numpy as np

class RTLearner():
    def __init__(self, data_x, data_y):
        self.data_x = data_x
        self.data_y = data_y

    def initial_call(self, data_x, data_y):
        self.decision_tree = self.tree_create(data_x, data_y)
        return self.decision_tree

    def random_feature(self, data_x):
        size = data_x.shape[1]
        return np.random.choice(size)

    def tree_create(self, data_x, data_y):
        if data_x.shape[0] == 1: # only one row
            return np.array([-1, data_y[0], np.nan, np.nan])
        if np.all(data_y == data_y[0]):
            return np.array([-1, data_y[0], np.nan, np.nan])

        if data_x.shape[0] == 0:
            return np.array([])

        # if bases cases don't work, continue
        feature = self.random_feature(data_x)
        split_value = np.median(data_x[:,feature])

        # left and right halves
        left_half = data_x[:,feature] <= split_value
        right_half = data_x[:,feature] > split_value

        # construct trees
        left_tree = self.tree_create(data_x[left_half], data_y[left_half])
        right_tree = self.tree_create(data_x[right_half], data_y[right_half])

        root_node = np.array([feature, split_value, 1, left_tree.shape[0] + 1])

        return np.vstack((root_node, left_tree, right_tree))

    def predict(self, data):

        def traverse_tree(points, node):
            node = self.decision_tree[node]
            if node[0] == -1: #if it is a leaf node, return the predicted value
                return node[1]

            node_index = int(node[0])
            split_value = node[1]

            if points[node_index] <= split_value:
                return traverse_tree(points, node_index + int(node[2]))
            else:
                return traverse_tree(points, node_index + int(node[3]))

        def initiate_prediction(points):
            return traverse_tree(points, 0)

        predictions = np.apply_along_axis(initiate_prediction, 1, data)
        return predictions

if __name__ == '__main__':
    x_train = np.array(
        [[0.37454012, 0.95071431, 0.73199394],
         [0.59865848, 0.15601864, 0.15599452],
         [0.05808361, 0.86617615, 0.60111501],
         [0.70807258, 0.02058449, 0.96990985],
         [0.83244264, 0.21233911, 0.18182497]]
    )

    y_train = np.array(
        [3.60578034, 1.60021285, 2.92909007, 1.54129054, 2.09938835]
    )

    tester = RTLearner(x_train, y_train)
    print(tester.initial_call(x_train, y_train))

    x_test = np.array(
        [[0.9600173, 0.69951205, 0.99986729],
         [0.2200673, 0.16105635, 0.73984099],
         [0.99645573, 0.31634698, 0.13654458],
         [0.38398001, 0.32051928, 0.36641475],
         [0.70965156, 0.90014243, 0.53411544]]

    )

    y_test = np.array([4.15785624, 1.51697086, 2.95411922, 1.85027812, 4.1195264])

    print(tester.predict(x_test))