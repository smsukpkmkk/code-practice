import torch

x = torch.tensor([])
print(torch.is_tensor(x))#torch.is_tensor(x)判断是否是张量
print('\n')
#—————————————————————————————————————————
print(torch.is_storage(x))#输出false
print(torch.is_storage(x.untyped_storage()))#返回tensor里面的纯数据部分输出true
print('\n')
#——————————————————————————————————————————
print(torch.is_complex(torch.tensor([1],dtype=torch.complex128)))#复杂类型输出true
print(torch.is_complex(torch.tensor([2],dtype=torch.float16)))#非复杂类型输出false
print('\n')
#——————————————————————————————————————————
