def study_schedule(permanence_period: list, target_time: int = -1) -> int:
    if verify_permanence_is_invalid(permanence_period):
        return None

    if type(target_time) is int and target_time > -1:
        count = 0
        for arrived, departure in permanence_period:
            if arrived <= target_time <= departure:
                count += 1
        return count
    return None


def verify_permanence_is_invalid(permanence_period: list) -> bool:
    for arrived, departure in permanence_period:
        if arrived is None or departure is None:
            return True
        if type(arrived) is not int:
            return True
        if type(departure) is not int:
            return True
    return False
