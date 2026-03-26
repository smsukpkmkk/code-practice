import torch
from torch import nn




class ScaledDotProductAttention(nn.Module):
    def __init__(self):
        super().__init__()
        
    def forward(self, q: torch.Tensor, k : torch.Tensor, v : torch.Tensor):
        #q[n1, d] k[n2, d] v[n2, d]
        d = k.size(-1)
        # scores [n1, n2]，Q K相乘得到的矩阵
        scores = (q @ k.transpose(-1, -2)) / torch.sqrt(torch.tensor(d, dtype=torch.float32))
        # 对scores矩阵在列方向进行softmax·
        atten_weight = torch.softmax(scores,dim=-1)
        # out_put [n1, d] 
        out_put = atten_weight @ v
        return out_put
         
        

class MultiHeadAttention(nn.Module):
    def __init__(self, head:int, dim:int):
        super().__init__()
        # head是注意力头数 dim是隐藏维度
        self.head = head
        self.dim = dim
        self.head_dim = dim // head
        self.W_q = nn.Linear(self.dim,self.dim)
        self.W_k = nn.Linear(self.dim,self.dim)
        self.W_v = nn.Linear(self.dim,self.dim)
        self.W_o = nn.Linear(self.dim,self.dim)
        self.attention = ScaledDotProductAttention()
    def split_tensor(self, x:torch.Tensor):
        # tensor形状[n, d]
        seq, dim = x.size()
        # 对列进行分割以进行更好的划分，
        x = x.view(seq, self.head, self.head_dim).transpose(0, 1)
        return x
    def forward(self, q:torch.Tensor, k :torch.Tensor,v :torch.Tensor):
        
        seq, dim = q.size()
        Q = self.W_q(q)
        K = self.W_k(k)
        V = self.W_v(v)
        
        Q = self.split_tensor(Q)
        K = self.split_tensor(K)
        V = self.split_tensor(V)
        output : torch.Tensor
        # output输出的Tensor形状[head, n1, head_dim]
        output = self.attention(Q, K, V)
        # 交换把形状变成[n1, head, head_dim],然后contiguous变连续
        output = output.transpose(0,1).contiguous()
        # 拼接
        output = output.view(seq, dim)
        # 过最后一个线性层
        output = self.W_o(output)
        return output
         
      