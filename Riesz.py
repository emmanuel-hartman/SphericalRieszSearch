import numpy as np
import matplotlib.pyplot as plt
import torch
from torch.autograd import grad

def proj(x):
    if torch.is_tensor(x):
        return x/torch.sqrt((x**2).sum(axis=0))
    return x/np.sqrt((x**2).sum(axis=0))


class RieszSearcher:
    
    def __init__(self, s):
        self.s=s


    def enr(self,x):
        dist=torch.zeros((x.shape[1],x.shape[1]))
        for i in range(0,dist.shape[0]):
            for j in range(i+1,dist.shape[0]):
                  dist[i,j]=(1/torch.sqrt(((x[:,i]-x[:,j])**2).sum()))**self.s

        dist=dist+dist.T
        return dist.sum()

    def plot(self,x, save=None):
        disp=x.detach().numpy()
        fig = plt.figure(figsize=(10,10))
        ax = fig.add_subplot(projection='3d')
        ax.scatter(disp[0,:], disp[1,:],disp[2,:])
        u, v = np.mgrid[0:2*np.pi:50j, 0:np.pi:50j]
        x1 = np.cos(u)*np.sin(v)
        y1 = np.sin(u)*np.sin(v)
        z1 = np.cos(v)
        # alpha controls opacity
        ax.plot_surface(x1, y1, z1, color="g", alpha=0.3)
        if save is not None:
            plt.savefig('out/out_{}.png'.format(save))
        else:
            plt.show()
        plt.close()


    def pgd(self,x,max_iter,epsilon,alpha, display=None):
        x.requires_grad_()
        ls=[x.detach().numpy()]
        enr_ls=[self.enr(x).item()]
        for i in range(0,max_iter):
            if display is not None:
                if i%display==0:
                    self.plot(x,save=i)
            x.requires_grad_()
            nabla=grad(self.enr(x), x, create_graph=True)[0]
            new_x=x-(alpha)*nabla
            new_x=proj(new_x)        
            enrx=self.enr(new_x)        
            re =(self.enr(x)-enrx)/enrx
            ls+=[x.detach().numpy()]
            enr_ls+=[enrx.item()]
            print(i,enrx.item(),re.item())
            if re> epsilon:
                x=new_x
            else:
                break
        return(x, self.enr(x), np.array(ls),np.array(enr_ls))