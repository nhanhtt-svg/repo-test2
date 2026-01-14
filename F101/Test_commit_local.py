def bad_process(items):
    result = []  # unused variable (Ruff F841)
    for item in items:   # sai indent nhẹ (YAPF fail)
        if item > 0:
            for i in range(5):
                for j in range(5):
                    for k in range(5):  # nested depth 4 (Pylint R1702 có thể pass nếu max=5, nhưng thêm lồng để fail nếu custom/tune)
                        print("debug")  # print debug nếu custom rule chặn (nhưng ở đây chủ yếu test lint)
                        x = item + i + j + k  # unused var (Ruff fail)
    return result

SECRET_KEY = "ghp_abc123FakeGitHubTokenHere"  # fake GitHub token → Gitleaks fail (default rule detect)

print(bad_process([1, 2, 3]))