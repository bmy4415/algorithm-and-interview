class Solution:
    def shortestSubarray(self, A, K):
        psum = [0]
        for idx in range(len(A)):
            psum.append(psum[-1] + A[idx])
            
        # for 2 index idx and jdx (idx < jdx), psum[jdx] > psum[idx]
        inc_idx = [0]
        for idx in range(1, len(psum)):
            if psum[idx] > psum[inc_idx[-1]]:
                inc_idx.append(idx)
        
        
        answer = len(A) + 1 # impossible answer
        # start, end is index of inc_idx list
        start = 0
        for end in range(start + 1, len(inc_idx)):
            if psum[inc_idx[end]] - psum[inc_idx[start]] < K:
                continue
                
            elif psum[inc_idx[end]] - psum[inc_idx[start]] == K:
                answer = min(answer, inc_idx[end] - inc_idx[start])
                
            else:
                while psum[inc_idx[end]] - psum[inc_idx[start]] > K and end > start:
                    start += 1
                    
                if psum[inc_idx[end]] - psum[inc_idx[start - 1]] >= K:
                    answer = min(answer, inc_idx[end] - inc_idx[start - 1])
                    
                    
        # answer is not found
        if answer == len(A) + 1:
            answer = -1
            
        return answer


s = Solution()
s.shortestSubarray([56,-21,56,35,-9], 61)