def combinationSum(candidates: list[int], target: int) -> list[list[int]]:
    res = []
    # candidates.sort()  //uncomment for optimised 

    def backtrack(start, path, remaining):
        if remaining == 0:
            res.append(path[:])
            return
        if remaining < 0:
            return

        for i in range(start, len(candidates)):
            # if candidates[i] > remaining:
            #     break
            path.append(candidates[i])
            backtrack(i, path, remaining - candidates[i])
            path.pop()
        
    backtrack(0, [], target)

    return res