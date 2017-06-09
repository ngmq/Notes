Link: http://blog.echen.me/2012/03/20/infinite-mixture-models-with-nonparametric-bayes-and-the-dirichlet-process/

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

Polya Urn Model: 

```python
import numpy as np
# import matplotlib.pyplot as plt

def uniform_color_distribution():
    return 1.0 * np.random.randint(100) / 100.0
    
def polya_urn_model(color_distribution, no_balls, alpha):
    colors = list()
    
    for i in range(no_balls):
        x = np.random.rand()
        if x <= alpha / (alpha + len(colors)):
            new_color = color_distribution()
            colors.append(new_color)
        else:
            y = np.random.randint(len(colors))
            k = colors[y]
            colors.append(k)
        
    return colors
    
    
print( polya_urn_model(uniform_color_distribution, 10, 3.2) )

```
Để ý rằng sự khác biệt giữa Chinese Restaurant Process và Polya Urn Model là CRP chỉ quyết định distribution của clusters thôi (hàm random trả về index của colors), còn PUM thì quyết định cả distribution của cluster (uniform) và parameters của clusters (ở đây chính là các số 0.14, 0.55 random từ công thức randomint(0, 100) / 100.0).
