import numpy as np
# Removed unused import: math


class GridTopology:
    def get_selected_ids(self, node_id, config):

        """Selects and returns IDs based on the node_id and configuration.
        grid_size = int(config["num_users"] ** 0.5)

        Args:
            self: Instance of the class.
            node_id: The ID of the current node.
            config: Configuration parameters, including 'num_users'.

        Returns:
            A list of selected IDs.
        """
        grid_size = int(config["num_users"] ** 0.5)
        num_users = config["num_users"]
        # Additional logic to select and return IDs goes here
        selected_ids = []

        # Left
        if node_id % grid_size != 1:
            selected_ids.append(node_id - 1)

        # Right
        if node_id % grid_size != 0 and node_id < num_users:
            selected_ids.append(node_id + 1)

        # Top
        if node_id > grid_size:
            selected_ids.append(node_id - grid_size)

        # Bottom
        if node_id <= num_users - grid_size:
            selected_ids.append(node_id + grid_size)

        if(num_users == 1):
            selected_ids = [1]
        elif(num_users == 2):
            if(node_id == 1):
                selected_ids = [2]
            else:
                selected_ids = [1]
        elif(num_users == 3):
            if(node_id == 1):
                selected_ids = [2, 3]
            elif(node_id == 2):
                selected_ids = [1]
            else:
                selected_ids = [1]

        num_users_to_select = config["num_users_to_select"]
        # Force self node id to be selected, not removed before sampling to
        # keep sampling identic across nodes (if same seed)
        selected_collabs = np.random.choice(
            selected_ids,
            size=min(num_users_to_select, len(selected_ids)),
            replace=False,
        )
        selected_ids = list(selected_collabs) + [node_id]

        return selected_ids
