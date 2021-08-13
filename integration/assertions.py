def assert_if_desired_param_is_equal_to_objects_fields_in_list(list, field, value):
    for student_dict in list:
        assert student_dict[field] == value
