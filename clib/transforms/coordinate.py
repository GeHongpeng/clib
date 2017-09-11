import random


def jitter_position(bbox, size, step=(0, 0), random=False):
    def _new_position(value, step):
        pass
    while True:
        x_min_step = random.randint(-step[0], step[0])
        y_min_step = random.randint(-step[1], step[1])
        x_max_step = random.randint(-step[0], step[0])
        y_max_step = random.randint(-step[1], step[1])

        new_x_min = bbox[0] - x_min_step
        new_y_min = bbox[1] - y_min_step
        new_x_max = bbox[2] - x_max_step
        new_y_max = bbox[3] - y_max_step
        new_bbox = (new_x_min, new_y_min, new_x_max, new_y_max)

        if _check_position(new_bbox):
            break
    return new_bbox

def _check_position(bbox):
    if ((bbox[2] - bbox[0]) <= 0) or ((bbox[3] - bbox[1]) <= 0):
        return False
    else:
        return True
