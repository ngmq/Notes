Chinese Restaurant Process:

```python
import numpy as np

def chinese_restaurant_process(no_customers, alpha):
    if no_customers <= 0:
        return []
        
    current_cluster = 0
    res = list()
    cnt = list()
    cnt.append(0)
    
    for i in range(no_customers):
        x = np.random.rand()
        print( "x = ", x )
        if x <= alpha / (alpha + i):
            # new cluster
            current_cluster += 1
            res.append(current_cluster)
            cnt.append(1)
        else:
            # x -= alpha / (alpha + i)
            # for k in range(1, current_cluster + 1):
                # if x <= 1.0 * cnt[k] / (0.0 + cnt[k] + i):
                    # res.append(k)
                    # cnt[k] += 1
                    # break
                # else:
                    # x -= 1.0 * cnt[k] / (0.0 + cnt[k] + i)
                    
            y = np.random.randint(0, len(res))
            k = res[y]
            res.append(k)
            
    return res
    
print( chinese_restaurant_process(10, 1.0) )
```
