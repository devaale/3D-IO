def test_ransac_execute_extract_one(test_cloud, test_ransac_algorithm):
    result_planes, _ = test_ransac_algorithm.execute(
        test_cloud, 3, 1000, 0.005, planes_to_extract=1
    )
    result_planes_count = len(result_planes)
    assert result_planes_count == 1


def test_ransac_execute_extract_two(test_cloud, test_ransac_algorithm):
    result_planes, _ = test_ransac_algorithm.execute(
        test_cloud, 3, 1000, 0.005, planes_to_extract=2
    )
    result_planes_count = len(result_planes)
    assert result_planes_count == 2
