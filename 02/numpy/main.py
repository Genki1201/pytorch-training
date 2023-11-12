import numpy as np

data = np.array([
    [[85, 78], [67, 82], [92, 88], [75, 70], [60, 64]],
    [[70, 68], [77, 72], [85, 90], [60, 65], [78, 76]],
    [[80, 84], [88, 87], [66, 68], [72, 73], [64, 60]]])

print(f"1, {data.shape}")
print("2, ", np.mean(data, axis=1))
print("3, ", data[:,2,1].max())
print("4, ", np.array([[np.max(data[:,:,0]) - np.min(data[:,:,0])],[np.max(data[:,:,1]) - np.min(data[:,:,1])]]) )
print("5, ", np.count_nonzero((data[:,:,0]>=80), axis=1))
print("6, ", np.count_nonzero((data[:,:,0]+data[:,:,1])>=135))